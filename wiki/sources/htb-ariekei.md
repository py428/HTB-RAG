---
type: source
title: "HTB Ariekei writeup"
raw: raw/htb-ariekei.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[ariekei]]
---
# Source: HTB Ariekei writeup
> Insane-difficulty box walkthrough covering Docker container exploitation, Shellshock and ImageTragick attacks, and privilege escalation chains.

## Key facts extracted
- Ariekei uses Docker with multiple containers: bastion, waf, blog (beehive), convert (calvin)
- WAF blocks Shellshock exploitation from external, but internal access bypasses protection
- calvin container vulnerable to ImageTragick via image upload functionality
- /common directory mounted across containers provides network diagrams and SSH keys
- bastion container SSH key (root@arieka) provides internal network access
- Shellshock exploitation on beehive container requires SSH tunneling for reverse shell
- Spanishdancer user encrypted SSH key cracked with password "purple1"
- Docker group membership allows mounting host filesystem for privilege escalation
- Multiple SSH service versions suggest different container base images

## Filed into
[[ariekei]], [[imagetragick]], [[shellshock]], [[docker-escape]], [[ssh-key-reuse]], [[container-pivoting]]
