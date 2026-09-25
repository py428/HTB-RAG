---
type: source
title: "HTB Cypher writeup"
raw: raw/htb-cypher.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cypher]]
---
# Source: HTB Cypher writeup

> Complete walkthrough of Cypher, a medium-difficulty HTB box featuring a Neo4J graph database application vulnerable to Cypher injection and command injection through custom extensions, with privilege escalation via sudo abuse of the bbot tool.

## Key facts extracted

- Running Neo4J graph database on Ubuntu 24.04 with nginx reverse proxy
- Custom APOC extension contains command injection in `getUrlStatusCode` function
- Neo4j service credentials reused by graphasm user
- User `graphasm` can run bbot as root with NOPASSWD
- bbot allows loading custom Python modules from arbitrary directories

## Filed into

[[cypher]], [[cypher-injection]], [[command-injection]], [[sudo-abuse]], [[neo4j]], [[docker]]