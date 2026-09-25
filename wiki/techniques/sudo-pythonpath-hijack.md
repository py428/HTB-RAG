---
type: technique
title: sudo PYTHONPATH hijack
tags: [linux, privesc, sudo, python]
platforms: [linux]
updated: 2026-07-09
---
# sudo PYTHONPATH hijack

## What it is
A Linux privilege-escalation technique that abuses a `sudo` rule configured with the `SETENV`
tag. `SETENV` lets the invoking user override environment variables — including `PYTHONPATH` —
even though `sudo` normally scrubs them. When the allowed command is a Python script run by
root, an attacker preloads a malicious module of the same name as one the script imports: Python
honors the attacker-controlled `PYTHONPATH` first, loads the hostile module with root privileges,
and the code inside executes as root — yielding a shell or other privileged action.

## When it works
- A `sudoers` entry grants the user the right to run a Python interpreter (or a `.py` script)
  as root, AND
- That entry carries the `SETENV:` tag (visible as `SETENV:` in `sudo -l`), AND
- The target script imports a module the attacker can shadow with a hand-crafted file of the
  same name.

## How it's done
1. Enumerate with `sudo -l` and confirm a root-owned Python script (e.g. `backup.py`) runnable
   via `sudo`, with the `SETENV:` tag on the rule.
2. Inspect the script's imports and pick a standard/top-level module to shadow.
3. Write a replacement module that runs your payload at import time, e.g.
   ```python
   # shutil.py — placed in the attacker's writable dir
   import os
   os.system("/bin/bash")
   ```
4. Run the script with `PYTHONPATH` pointing at your dir, using `-E`-free execution so the env
   is honored:
   ```bash
   sudo PYTHONPATH=/tmp/evil /opt/scripts/backup.py
   ```
   Python loads your `shutil.py` before the real one, and the payload fires as root.

Cite the enumeration and scripting tooling as [[sudo-enumeration]] where relevant.

## Observed on
- [[admirer]] — SETENV tag allowing PYTHONPATH manipulation to hijack Python libraries in backup.py

## See also
