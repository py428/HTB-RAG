---
type: technique
title: Adminer file read
tags: [web, linux, mysql, credential-access, file-read]
platforms: [linux]
updated: 2026-07-09
---

# Adminer file read

## What it is
Adminer is a single-file PHP database management tool (a lighter phpMyAdmin). When an instance is exposed on a web server, it can be turned into an arbitrary local file reader — often without ever needing valid database credentials. The primitive is MySQL's `LOAD DATA LOCAL INFILE`: the client (Adminer, running on the target) reads a file from its own filesystem and ships the contents to the server over the DB protocol. By pointing the Adminer login form at an attacker-controlled rogue MySQL server, the operator makes Adminer read sensitive local files (web-app configs, SSH keys, `/etc/passwd`) and exfiltrate them, turning a benign DB UI into a file-disclosure oracle.

## When it works
- Adminer (or a similar web DB admin like phpMyAdmin) is reachable on the target.
- The web app's MySQL client library allows `LOCAL INFILE` transfers (PHP `mysqli` with `mysqlnd` typically does by default).
- You can either log in with recovered DB credentials to a local DB and issue `LOAD DATA LOCAL INFILE` yourself, or — more usefully — point Adminer's "server" field at a rogue MySQL server you control, which forces the file read on connect.

## How it's done
The credential-less path uses a rogue MySQL server. Stand one up (e.g. a `LOAD DATA LOCAL INFILE` rogue-MySQL listener such as `gl-infra-server` / Rogue-MySql-Server), then in the exposed Adminer login form set the server to your listener's IP/port and connect. On the client handshake the rogue replies with a `LOAD DATA LOCAL INFILE` packet naming the target file you want (`/var/www/html/config.php`, `~/.ssh/id_rsa`, etc.); Adminer reads it and transmits the contents to you, which you capture server-side.

If you already have DB credentials (recovered from a backup or source leak), simply log Adminer into the local [[mysql]] instance and run:
```
CREATE TEMPORARY TABLE foo (c TEXT);
LOAD DATA LOCAL INFILE '/home/waldo/.ssh/id_rsa' INTO TABLE foo;
SELECT * FROM foo;
```
Any file the web-user can read comes back as a row.

## Observed on
- [[admirer]] — LOAD DATA LOCAL INFILE for local file read through database interface

## See also
[[ldap-description-credential]], [[gpp-cpassword]]
