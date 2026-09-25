---
type: source
title: "HTB Toby writeup"
raw: raw/htb-toby.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[toby]]
---
# Source: HTB Toby writeup
> Complete analysis of HackTheBox Toby machine covering WordPress backdoor exploitation, container escape, database password cracking, SSH key capture, and custom PAM module brute-forcing.
## Key facts extracted
- WordPress 5.7.2 with heavily obfuscated backdoor in wp-includes/comment.php
- XOR-based C2 communication with session-based single-byte keys
- Docker environment with WordPress, MySQL, and Gogs containers
- Time-seeded password generation in Flask application
- Custom PAM module with 0.1s delay per correct character for password brute-forcing
- Automated MySQL database backups with SSH key transfer
## Filed into
[[toby]], [[webshell-backdoor]], [[xor-encoding]], [[container-escape]], [[password-generation]], [[ssh-capture]], [[pam-backdoor]]
