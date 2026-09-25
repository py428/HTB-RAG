---
type: machine
title: Delivery
platform: htb
os: linux
difficulty: easy
tags: [linux, web, email, mattermost, database, privesc]
solved: 2026-07-09
sources: [[htb-delivery]]
related: []
---

# Delivery

> Beginner-friendly Linux box featuring an osTicket helpdesk integrated with Mattermost, where email verification bypass leads to internal chat access and credential harvesting.

## Attack path

1. Create support ticket via [[http]] helpdesk to get @delivery.htb email address
2. Use ticket email to verify Mattermost account registration
3. Access internal Mattermost chats to find SSH credentials
4. Login via SSH and enumerate Mattermost database configuration
5. Extract root password hash from database and crack using hashcat rules
6. Use cracked password to su to root

## Techniques used

- [[email-manipulation]] — Abuse helpdesk ticket system to generate domain email for verification
- [[credential-harvesting]] — Extract credentials from internal Mattermost conversations
- [[database-dump]] — Access MySQL database to extract password hashes
- [[password-cracking]] — Use hashcat rules to crack password variants

## Tools used

- [[nmap]] — Port enumeration and service identification
- [[smbclient]] — Access helpdesk file shares (if needed)
- [[ssh]] — Shell access and privilege escalation
- [[mysql]] — Database access and hash extraction
- [[hashcat]] — Password cracking with rules

## Services / ports

- [[ssh]] (22) — Shell access
- [[http]] (80) — Helpdesk web interface
- [[http]] (8065) — Mattermost chat server

## Lessons / notes

- Helpdesk systems with ticket creation can be abused to generate domain emails for verification bypass
- Internal chat platforms often contain credential leaks in conversations
- Mattermost stores configuration including database credentials in `config.json`
- Database access can reveal password hashes for offline cracking
- Hashcat rules (like best64.rule) are effective against password variants
- Easy box good for practicing web application manipulation and social engineering workflows