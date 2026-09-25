---
type: source
title: "HTB Dyplesher writeup"
raw: raw/htb-dyplesher.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[dyplesher]]
---
# Source: HTB Dyplesher writeup
> Insane difficulty box with memcache, Git bundles, Minecraft servers, and RabbitMQ. Complex chain involving authentication bypass, custom plugin development, network sniffing, and AMQP message publishing. Writeup covers memcache binary protocol, Bukkit plugin creation, and Cuberite exploitation.

## Key facts extracted
- Exposed .git directory on test subdomain leaked memcache credentials
- Memcache required binary protocol with SASL authentication
- Git bundles contained custom code with SQLite user database
- Bukkit plugins ran as server user allowing file system writes
- RabbitMQ AMQP traffic contained credentials for queue publishing
- Cuberite plugins in Lua executed with system permissions

## Filed into
[[dyplesher]], [[git-exposure]], [[memcache-authentication]], [[password-cracking]], [[git-bundle-analysis]], [[plugin-development]], [[network-sniffing]], [[amqp-injection]]
