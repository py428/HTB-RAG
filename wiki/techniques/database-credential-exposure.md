---
type: technique
title: Database credential exposure
tags: [web, linux, credential-access, database, config]
platforms: [linux]
updated: 2026-07-09
---

# Database credential exposure

## What it is
Applications almost always store the credentials they use to reach their database somewhere on disk — a PHP `config.php`, a JSON `config_prod.json`, a `.env`, or `wp-config.php` — usually in plaintext. The same credentials are also frequently reused as the operating-system user's password, so reading one config file can pivot directly into a shell. The database itself is a second source: the MySQL `mysql.user` table holds every database account and its authentication hash, and once you have SQL injection or a console, dumping it can recover passwords (or crackable hashes) for users that exist on the box.

## When it works
- You have **any file-read primitive** on the host: directory traversal/LFI in the web app, a post-exploitation shell, or a world-readable config left by a lazy deploy.
- Or you have **SQL injection / direct DB access** that lets you query `mysql.user`.
- The recovered DB password is **reused** by a system user (common on dev boxes where the app user and the OS user share credentials), or the hash can be cracked.

## How it's done
```
# config files — grep the web root for connection strings
grep -riE 'password|passwd|db_pass|mysql://' /var/www/html 2>/dev/null
cat /var/www/html/config.php
cat /opt/app/config_prod.json

# inside the database — dump MySQL accounts and hashes
mysql -u <user> -p<pw> -e "SELECT user,host,authentication_string FROM mysql.user;"
```
Typical targets: `config.php` / `db.php` (PHP), `config_prod.json` / `settings.py` (web frameworks), `.env`, `wp-config.php` (WordPress). Once you have a credential, try it against [[ssh]] and `su` before assuming it is DB-only. Tools: [[mysql]], `grep`, `find`.

## Observed on
- [[admirertoo]] — credentials stored in PHP config files for jennifer user
- [[agile]] — MySQL credentials stored in config_prod.json
- [[ai]] — Password extraction from MySQL users table

## See also
[[ldap-description-credential]], [[gpp-cpassword]]
