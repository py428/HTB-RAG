---
type: source
title: "HTB Schooled writeup"
raw: raw/htb-schooled.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[schooled]]
---
# Source: HTB Schooled writeup
> FreeBSD Moodle exploitation guide covering stored XSS for cookie theft, CVE-2021-14321 privilege escalation, malicious plugin upload for RCE, database credential extraction, and FreeBSD package manager abuse for root access through custom package hosting.

## Key facts extracted
- Moodle 3.9 installation on moodle.schooled.htb with student registration
- Stored XSS in MoodleNet profile (CVE-2020-25627) steals manager session
- CVE-2021-14321: Course enrollment allows teacher to manager privilege escalation
- Manager role impersonation via "Log in as" feature
- Plugin installation after permissions modification enables RCE
- Database credentials: moodle/PlaybookMaster2020, admin hash cracks to !QAZ2wsx
- jamie user has sudo rights: /usr/sbin/pkg update and /usr/sbin/pkg install *
- pkg.conf points to devops.htb for package repository
- wheel group can write /etc/hosts for repository redirection

## Filed into
[[schooled]], [[stored-xss]], [[moodle-privilege-escalation]], [[plugin-upload]], [[package-manager-abuse]], [[hosts-file-modification]]
