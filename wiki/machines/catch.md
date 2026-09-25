---
type: machine
title: Catch
platform: htb
os: linux
difficulty: medium
tags: [android, web, docker, php, redis, privesc]
solved: 2026-07-09
sources: [[htb-catch]]
related: []
---
# Catch
> Catch Global Systems requires finding an API token in an Android application, and using that to leak credentials from a chat server. Those credentials provide access to multiple CVEs in a Cachet instance, providing several different paths to a shell. The intended path injects into a configuration file to set a malicious Redis server and store a serialized PHP object to get execution. To escalate to root, abuse a command injection vulnerability in a Bash script checking APK files by giving an application a malicious name field.

## Attack path
1. Extract [[api-token-leak]] from Android APK using [[apk-reversal]]
2. Use chat API to leak Cachet credentials
3. Exploit [[cachet-cve-2021-39172]] via [[redis-abuse]] for [[php-deserialization]] to get shell in container
4. Extract database credentials from container
5. SSH to host
6. Exploit [[command-injection]] in APK verification script for root

## Techniques used
- [[apk-reversal]] — Analyze Android APK with Jadx and MobSF to find hardcoded API token
- [[api-token-leak]] — Extract Let's Chat token from application strings
- [[sqli]] — Alternative path via CVE-2021-39165 SQL injection in Cachet API
- [[ssti]] — Alternative path via server-side template injection in Cachet
- [[cachet-cve-2021-39172]] — Laravel configuration injection to set Redis as cache driver
- [[php-deserialization]] — Use phpggc to create Laravel/RCE4 payload stored in Redis
- [[redis-abuse]] — Host malicious Redis server to serve serialized PHP payload
- [[command-injection]] — Inject malicious APK name field ($(...)) into verify.sh script

## Tools used
- [[nmap]]
- [[feroxbuster]]
- jadx
- mobsf
- [[curl]]
- redis-cli
- phpggc
- apktool
- sqlmap
- [[pspy]]

## Services / ports
- [[ssh]] (22)
- [[http]] (80, 8000)
- gitea (3000)
- lets-chat (5000)
- cachet (8000)

## Lessons / notes
- Multiple CVE paths to RCE in Cachet (CVE-2021-39165, CVE-2021-39172, CVE-2021-39173, CVE-2021-39174)
- Docker container environment (hostname 70e4165dab0b)
- Database credentials leaked in .env file (will/s2#4Fg0_%3!)
- Cron job cleanup resets modified config files
- APK name field unsanitized in app_check() function
- SetUID binary copy of bash gives euid=0 root shell
