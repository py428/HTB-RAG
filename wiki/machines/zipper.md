---
type: machine
title: Zipper
platform: htb
os: linux
difficulty: hard
tags: [monitoring, linux, privesc, zabbix]
solved: 2026-07-09
sources: [[htb-zipper]]
related: []
---
# Zipper
> Zipper is a monitoring server running Zabbix. The attack path involves Zabbix API abuse for command execution, multiple paths to shells via API and agent communication, and privilege escalation through path hijacking and systemd service manipulation.

## Attack path
1. [[zabbix-api-abuse]] for [[zabbix-script-execute]] on monitored hosts
2. [[zabbix-agent-communication]] via agent from Zabbix server to Zipper
3. [[path-hijacking]] for SUID binary zabbix-service
4. [[systemd-service-hijack]] via writable purge-backups.service file

## Techniques used
- [[zabbix-api-abuse]] — API script.create and script.execute for command execution
- [[zabbix-script-execute]] — execute_on parameter controls server vs agent execution
- [[zabbix-agent-communication]] — RCE via agent communication from Zabbix server
- [[path-hijacking]] — SUID binary calls system() without absolute path
- [[systemd-service-hijack]] — Writable ExecStart= in systemd service file for root execution

## Tools used
[[nmap]], [[curl]], [[nc]], [[ssh]], [[ltrace]], [[strings]], [[openssl]], [[journalctl]], [[python]]

## Services / ports
[[ssh]] (22), [[http]] (80), [[zabbix-agent]] (10050)

## Lessons / notes
- Zabbix API allows command execution on monitored hosts via scripts
- execute_on=0 runs on agent, execute_on=1 runs on server
- SUID binaries calling system() without absolute path vulnerable to PATH hijacking
- systemd service files writable by users can be modified for privilege escalation
- Multiple paths to same goal (shell) demonstrate flexibility in exploitation