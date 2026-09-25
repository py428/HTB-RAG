---
type: tool
title: ExifTool
category: recon
tags: [metadata, osint]
updated: 2026-07-09
---

# ExifTool

## What it does
Reads and writes file metadata (EXIF/IPTC/XMP) for images, documents, etc. A quiet goldmine for usernames, software versions, GPS, and author names.

## Common usage
```
exiftool image.jpg                         # dump all metadata
exiftool *.jpg | grep -i author             # hunt for names
```

## Used on
- [[absolute]] — `Author`/`Artist` tags on website hero images gave the full names that seeded [[kerberos-username-enumeration]].
