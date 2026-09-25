---
type: source
title: "HTB Europa writeup"
raw: raw/htb-eureka.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[europa]]
---
# Source: HTB Europa writeup

> Complete walkthrough of Europa Linux box covering SQL injection authentication bypass, PHP preg_replace code execution, and cron job hijacking for root access.

## Key facts extracted
- SSL certificate reveals domain: europacorp.htb with subdomain admin-portal.europacorp.htb
- Login form vulnerable to SQL injection: admin@europacorp.htb';-- -
- sqlmap extracts admin password hash: 2b6d315337f18617ba18922c0b9597ff → SuperSecretPassword!
- Tools.php uses preg_replace with /e modifier for RCE
- Cron job runs /var/www/cronjobs/clearlogs every minute as root
- clearlogs calls /var/www/cmd/logcleared.sh which doesn't exist by default

## Filed into
[[europa]], [[sqli-auth-bypass]], [[preg-replace-rce]], [[cronjob-hijack]]
