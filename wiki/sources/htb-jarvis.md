---
type: source
title: "HTB Jarvis writeup"
raw: raw/htb-jarvis.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jarvis]]
---
# Source: HTB Jarvis writeup
> Medium Linux machine with three stages: SQL injection behind IronWAF, PHPMyAdmin LFI to RCE, Python command injection, and systemctl privilege escalation.

## Key facts extracted
- IronWAF 2.0.3 protects room.php, bans for 90 seconds after 5+ suspicious requests
- SQL injection UNION with 7 columns: cod=-1250 UNION ALL SELECT 1,2,3,4,5,6,7-- -
- MySQL credentials: DBadmin / imissyou (hash *2D2B7A5E4E637B8FBA1D17F40318F277D29964D0)
- PHPMyAdmin 4.8.0 on port 64999 (banned IPs redirect here)
- CVE-2018-12613: LFI via target=db_sql.php%3f/../../../../etc/passwd
- Python simpler.py has command injection in ping function
- Forbidden chars: `['&', ';', '-', '\`', '||', '|']` but `$()` works
- SUID /bin/systemctl owned by root:pepper allows service creation
- WAF Python script monitors /var/log/apache2/access.log in real-time

## Filed into
[[jarvis]], [[sqli]], [[waf-bypass]], [[phpmyadmin-lfi]], [[command-injection]], [[systemctl-abuse]]
