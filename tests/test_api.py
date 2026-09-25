import unittest
from unittest.mock import Mock, patch

import requests

from api.index import (
    EMBEDDING_DIMENSIONS,
    HF_INFERENCE_URL,
    _extract_embedding,
    _search_terms,
    get_hf_embedding,
    get_relevant_chunks,
)


class EmbeddingTests(unittest.TestCase):
    def test_current_hugging_face_router_is_used(self):
        self.assertEqual(
            HF_INFERENCE_URL,
            "https://router.huggingface.co/hf-inference/models/"
            "sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction",
        )

    @patch("api.index.requests.post")
    def test_embedding_response_is_unwrapped_and_validated(self, post):
        vector = [0.1] * EMBEDDING_DIMENSIONS
        response = Mock()
        response.json.return_value = [vector]
        post.return_value = response

        self.assertEqual(get_hf_embedding("test question", "token"), vector)
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(post.call_args.args[0], HF_INFERENCE_URL)

    def test_invalid_embedding_shape_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unexpected shape"):
            _extract_embedding([0.1, 0.2])

    def test_lexical_fallback_keeps_distinctive_query_terms(self):
        terms = _search_terms(
            "Which machine has no modifiable services identified by winPEAS?"
        )

        self.assertIn("modifiable", terms)
        self.assertIn("services", terms)
        self.assertIn("winpeas", terms)
        self.assertNotIn("which", terms)
        self.assertNotIn("machine", terms)

    @patch("api.index.get_lexical_chunks")
    @patch("api.index.get_hf_embedding")
    def test_network_failure_uses_lexical_fallback(self, embed, lexical):
        embed.side_effect = requests.ConnectionError("provider unavailable")
        lexical.return_value = [{"id": "control"}]
        supabase = Mock()

        with self.assertLogs("api.index", level="ERROR"):
            result = get_relevant_chunks(
                supabase, "Which machine has no modifiable services?", "token"
            )

        self.assertEqual(result, [{"id": "control"}])
        lexical.assert_called_once_with(
            supabase, "Which machine has no modifiable services?", 10
        )


if __name__ == "__main__":
    unittest.main()
