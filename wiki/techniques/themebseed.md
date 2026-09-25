---
type: technique
title: ThemeBleed
tags: []
platforms: []
updated: 2026-07-09
---

# ThemeBleed

## What it is
ThemeBleed (CVE-2023-38146) is a remote code execution vulnerability in how Windows loads theme
files (`.theme` / `.msstyles`). When a user opens a `.theme` file whose referenced `.msstyles`
payload lives on a remote SMB/UNC path, Windows validates the Authenticode signature of that
payload — but a time-of-check / time-of-use (TOCTOU) race condition lets the attacker-controlled
SMB server serve a legitimately *signed* file during signature verification, then swap it for a
malicious, unsigned DLL in the brief window before the file is mapped. Because the signature was
already accepted, the unsigned replacement is loaded into the theme-host process as if it were
trusted, yielding code execution as the victim user.

## When it works
- The victim opens an attacker-supplied `.theme` file (delivered via phishing, a malicious
  document/shortcut, or a protocol handler), AND
- The victim's host can reach an attacker-controlled SMB server — the `.theme` points its
  `MSStyles` file at a UNC path you serve, AND
- The target runs an unpatched, vulnerable Windows build (pre-October 2023 cumulative update).

## How it's done
Stand up an SMB share holding two payloads: a legitimately signed `.msstyles` and a malicious
replacement (a DLL exporting the style entry points Windows expects). Craft a `.theme` file whose
`[VisualStyles]` `Path=` points at a UNC path on your server. When the victim opens it, win the
race: serve the signed file the instant Windows checks the signature, then swap in your malicious
DLL before it is loaded. Serve the share with [[smb]] (e.g. Impacket `smbserver.py` with the
response manipulated by a PoC driver). Public ThemeBleed PoCs exist that automate the swap.

## Observed on
- [[aero]] — CVE-2023-38146 race condition in Windows theme signature verification

## See also
