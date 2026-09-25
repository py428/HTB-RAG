---
type: technique
title: Audio SQL injection
tags: [web, linux, sql-injection, audio, speech-recognition]
platforms: [linux]
updated: 2026-07-09
---

# Audio SQL injection

## What it is
Audio SQL injection is a SQL injection variant where the payload is delivered as a spoken audio clip rather than typed text. The target application accepts an audio file upload, runs it through a speech-to-text (ASR / voice recognition) pipeline, and then uses the transcribed string unsanitized inside a SQL query. Because the attacker controls the waveform that the recognizer turns into text, they control the SQL that the backend ultimately executes — single quotes, `UNION`, `OR 1=1`, and the rest — exactly as in classic string-based SQL injection, just spoken aloud. The interesting wrinkle is the mapping layer: each speech engine renders spoken words or phonemes into specific characters and symbols, so crafting the payload means understanding how that particular engine vocalizes SQL metacharacters (e.g. "single quote", "union", "semicolon") and producing audio that transcribes cleanly into valid injection syntax.

## When it works
- The web application exposes an **audio upload / "ask the assistant" interface** whose transcripts reach a SQL backend.
- Uploaded audio is handed to a **speech-to-text engine** whose output is concatenated into a query without parameterization.
- You can **generate or manipulate audio** (text-to-speech tools, spliced WAV/MP3 segments) so the recognizer reliably emits the exact SQL symbols you want.
- The SQL query runs against a backend you care about (e.g. `mysql.user`) for credential or data extraction.

## How it's done
Build the payload as spoken text and feed it to the recognizer. Generate a WAV/MP3 that voices the injection string — for example, a phrase that transcribes to `' UNION SELECT user,host,authentication_string FROM mysql.user --` — using a TTS engine such as `flite` (or a hosted voice service), then upload it through the audio interface:
```
# synthesize spoken SQL injection payload with flite
flite -t "single quote union select user host authentication string from mysql dot user" -o payload.wav
curl -s -X POST http://target/upload -F "audio=@payload.wav"
```
If the engine mis-transcribes symbols, iterate on phrasing (spell out punctuation, adjust pacing/word choice) until the transcript forms valid SQL. Once the transcript hits the query, treat it like any other injection: dump credentials from `mysql.user`, read rows, and pivot with recovered passwords via [[ssh]]. Tools: `flite`, `curl`, [[mysql]], `sqlmap` (if you can replay the transcribed payload against an HTTP endpoint).

## Observed on
- [[ai]] — SQL injection through speech recognition using audio file manipulation

## See also
[[database-credential-exposure]]
