---
type: source
title: "HTB Pollution writeup"
raw: raw/htb-pollution.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[pollution]]
---
# Source: HTB Pollution writeup
> Hard HackTheBox Linux box demonstrating advanced web exploitation chain: XXE for file disclosure, Redis session hijacking for auth bypass, PHP filter chain LFI-to-RCE, PHP-FPM abuse for user privsep, and prototype pollution in NodeJS API for root.
## Key facts extracted
- Forum contains Burp history export with admin token for `/set/role/admin` endpoint
- XXE injection in XML upload allows reading any file (demonstrated on `/etc/hostname`, `/etc/passwd`, Apache configs)
- Developers site protected by HTTP auth; credentials in `/var/www/developers/public/.htpasswd` (username: developers_group, hash: $apr1$)
- Bootstrap.php stores Redis session credentials: `tcp://localhost:6379/?auth=COLLECTR3D1SPASS`
- Developers site vulnerable to PHP filter injection via `include($_GET['page'] . ".php")`
- Victors PHP-FPM pool listens on 127.0.0.1:9000, writable via FastCGI
- Victors NodeJS API runs on localhost:3000 as root with lodash prototype pollution vulnerability in `/admin/messages/send`
- JWT secret in `functions/jwt.js`: `JWT_COLLECT_124_SECRET_KEY`
## Filed into
[[pollution]], [[xxe]], [[redis-session-manipulation]], [[php-filter-injection]], [[php-fpm-abuse]], [[prototype-pollution]], [[htpasswd-cracking]], [[password-cracking]]
