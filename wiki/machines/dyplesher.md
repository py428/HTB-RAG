---
type: machine
title: Dyplesher
platform: htb
os: linux
difficulty: insane
tags: [linux, web, memcache, git, minecraft, rabbitmq, amqp]
solved: 2026-07-09
sources: [[htb-dyplesher]]
related: []
---
# Dyplesher
> Complex multi-stage box requiring memcache authentication, Git bundle analysis, Bukkit plugin development, and RabbitMQ message publishing. Attack chain: leak memcache creds from .git repo, dump hashes, crack passwords, access Gogs, analyze git bundles, write malicious Bukkit plugin for shell, sniff network for RabbitMQ creds, publish malicious Cuberite plugin for root.

## Attack path
1. [[git-exposure]] — Exposed .git directory contains memcache authentication credentials
2. [[memcache-authentication]] — Use binary memcache protocol with SASL auth to dump username/password hashes
3. [[password-cracking]] — Crack bcrypt hashes to get database and user passwords
4. [[git-bundle-analysis]] — Extract git bundles from Gogs release, find custom code with SQLite database
5. [[plugin-development]] — Write malicious Bukkit plugin to drop webshell and SSH key
6. [[network-sniffing]] — Use dumpcap with wireshark group to capture RabbitMQ traffic containing credentials
7. [[amqp-injection]] — Publish malicious Cuberite plugin URL to RabbitMQ queue for root execution

## Techniques used
- [[git-exposure]] — .git directory on test subdomain exposed memcache credentials in index.php source
- [[memcache-authentication]] — Binary memcache protocol required SASL authentication with username/password
- [[password-cracking]] — Bcrypt hashes from memcache and SQLite database cracked with rockyou.txt
- [[git-bundle-analysis]] — Git bundles contained custom Minecraft server code with user database
- [[plugin-development]] — Crafted Bukkit plugin in Java to write webshell and SSH keys to target locations
- [[network-sniffing]] — Used dumpcap binary with capabilities to capture RabbitMQ AMQP traffic
- [[amqp-injection]] — Used amqp-publish tool to submit malicious plugin URL to RabbitMQ exchange

## Tools used
[[nmap]], [[gobuster]], [[git]], memcached-cli, memccat, [[hashcat]], [[ssh]], dumpcap, Wireshark, amqp-publish

## Services / ports
[[ssh]] (22), [[http]] (80), [[dns]] (53), [[amqp]] (5672), memcache (11211), minecraft (25565)

## Lessons / notes
- Memcache SASL auth only works with binary protocol, not ASCII/text protocol
- Bukkit plugins run as server user, allowing file writes to web directories and SSH authorized_keys
- RabbitMQ credentials leaked in packet capture due to unencrypted AMQP traffic
- Cuberite plugins written in Lua can execute system commands via os.execute()
- Firewall restrictions limited outbound connections to specific ports (5672, 11211)
