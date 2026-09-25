---
type: technique
title: Fail2ban RCE
tags: [linux, privesc, rce, fail2ban, command-injection]
platforms: [linux]
updated: 2026-07-09
---

# Fail2ban RCE

## What it is
Fail2ban versions before 0.11 / 2.0 ran their ban and mail actions through a shell, and several default action templates interpolated the output of `whois` against the offending IP straight into the command line (CVE-2021-32749). Because that output was never sanitized, anyone who can influence the whois response can inject shell metacharacters that execute as **root** when fail2ban fires the action — turning a self-inflicted ban into code execution.

## When it works
- Fail2ban is installed, runs as **root**, and an active jail uses a mail/action template that calls `whois <ip>` with shell expansion (CVE-2021-32749, fail2ban < 0.11 / 2.0).
- You can **control the whois reply** for the IP fail2ban will look up: either by running a rogue whois server the target queries, or by writing a malicious `/etc/whois.conf` (or system whois config) that redirects lookups to your host.
- You can **trigger a ban** against a chosen IP (e.g., failed SSH auth against an sshd jail) so fail2ban executes the action and runs the poisoned `whois`.

## How it's done
1. Stand up a responder that returns a payload instead of a normal whois record. Plant it in the target's whois path (write `/etc/whois.conf` pointing at your host) or point fail2ban at a host you control.
2. Embed shell injection in the reply — the action template concatenates the raw `whois` output into a shell command run as root, so a newline/backtick/`$(...)` sequence becomes live.
3. Trip the jail (e.g., a handful of bad SSH logins) so fail2ban bans your IP and runs the mail action. The `whois` lookup returns your payload and it executes as root.
```
# minimal rogue whois responder (listens, prints payload, closes)
while true; do
  printf '$(cp /bin/bash /tmp/rootbash && chmod u+s /tmp/rootbash)\n' | ncat -lvp 43
done
```
Tools: a custom whois responder (e.g., [[ncat]]/python), and a write primitive to plant `whois.conf`. On [[admirertoo]] the write came from OpenCats (CVE-2021-25294) via phpggc.

## Observed on
- [[admirertoo]] — CVE-2021-32749 whois command injection via mail action payload

## See also
