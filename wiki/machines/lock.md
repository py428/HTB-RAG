---
type: machine
title: Lock
platform: htb
os: windows
difficulty: easy
tags: [windows, web, ad, git, rdp, privesc, cve]
solved: 2026-07-09
sources: [[htb-lock]]
related: []
---

# Lock
> Windows box with Gitea instance where leaked API token leads to private repo access, CI/CD webshell upload, mRemoteNG credential decryption, and CVE-2023-49147 PDF24 repair exploit for SYSTEM.

## Attack path
1. [[git-leak]] — hardcoded API token in Gitea commit history
2. [[api-token-leak]] — use token to enumerate private repos via Gitea API
3. [[ci-cd-abuse]] — commit ASPX webshell to website repo with auto-deploy
4. [[mremoteng-decrypt]] — decrypt mRemoteNG config.xml to get Gale Dekarios password
5. [[cve-2023-49147]] — oplock on faxPrnInst.log during PDF24 repair to get SYSTEM shell

## Techniques used
- [[git-leak]] — sensitive API token in Git commit history on Gitea
- [[api-token-leak]] — Gitea personal access token exposed in repos.py diff
- [[ci-cd-abuse]] — Git push triggers immediate deployment to IIS webroot
- [[web-shell-upload]] — ASPX webshell uploaded via Git to get foothold
- [[mremoteng-decrypt]] — decrypt mRemoteNG AES encrypted passwords from config.xml
- [[cve-2023-49147]] — PDF24 Creator repair function opens SYSTEM cmd.exe via oplock
- [[oplock]] — opportunistic lock on log file to hang installer process

## Tools used
[[nmap]], feroxbuster, [[curl]], git, python3, mremoteng-decrypt, [[xfreerdp]], netexec, SetOpLock

## Services / ports
- [[http]] (80) — IIS hosting static site
- [[http]] (3000) — Gitea instance
- [[smb]] (445)
- [[rdp]] (3389) — Terminal Services

## Lessons / notes
- Git commit history can leak credentials even after removal from current files
- Gitea personal access tokens provide full repo access via API
- CI/CD pipelines can be abused for instant webshell deployment
- mRemoteNG stores passwords in AES encrypted XML config files decryptable with public tools
- PDF24 Creator v11.15.1 vulnerable to CVE-2023-49147 — oplock on log file during repair exposes SYSTEM cmd.exe
- netexec supports command execution over RDP protocol for flag retrieval
