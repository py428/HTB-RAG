---
type: machine
title: Reset
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc, r-commands]
solved: 2026-07-09
sources: [[htb-reset]]
related: []
---
# Reset
> A Linux machine with a vulnerable password reset feature that leaks credentials in the response. The attack path involves log poisoning for RCE, abusing Berkeley r-commands for horizontal movement, and sudo nano escape for root access.

## Attack path
1. [[nmap]] scan reveals [[http]] and Berkeley r-commands ports
2. [[password-reset-bypass]] via API response that returns new password
3. Authenticate to web dashboard as admin user
4. [[log-poisoning]] in Apache access.log using User-Agent header
5. RCE via PHP include() of poisoned log file
6. [[rlogin-abuse]] using .rhosts and /etc/hosts.equiv configuration
7. [[tmux-session-recovery]] to obtain sadm credentials
8. [[sudo-nano-escape]] to get root shell

## Techniques used
- [[password-reset-bypass]] — API returns new password in response without email verification
- [[log-poisoning]] — Inject PHP code into Apache access.log for execution via include()
- [[rlogin-abuse]] — Trust-based authentication using /etc/hosts.equiv and .rhosts
- [[tmux-session-recovery]] — Attach to existing tmux session to find credentials
- [[sudo-nano-escape]] — Execute shell commands from nano editor via Ctrl+R

## Tools used
[[nmap]] | [[feroxbuster]] | [[netcat]] | [[evil-winrm]]

## Services / ports
[[http]] (80) | [[ssh]] (22) | rlogin (513) | rsh (514)

## Lessons / notes
- Password reset APIs should never return credentials in responses
- PHP include() on log files can lead to RCE via log poisoning
- Berkeley r-commands rely on hostname-based trust relationships
- tmux sessions may contain sensitive information or credentials
- nano editor allows command execution when run with sudo
- Berkeley r-commands are deprecated due to serious security vulnerabilities
