![Scrambled](https://0xdfimages.gitlab.io/img/scrambled-cover.webp)

Scrambled presented a purely Windows-based path. There are some hints on a webpage, and from there the exploitation is all Windows. NTLM authentication is disabled for the box, so a lot of the tools I’m used to using won’t work, or at least work differently. I’ll find user creds with hints from the page, and get some more hints from a file share. I’ll kerberoast and get a challenge/response for a service account, and use that to generate a silver ticket, getting access to the MSSQL instance. From there, I’ll get some more creds, and use those to get access to a share with some custom dot net executables. I’ll reverse those to find a deserialization vulnerability, and exploit that to get a shell as SYSTEM. Because the tooling for this box is so different I’ll show it from both Linux and Windows attack systems. In Beyond Root, two other ways to abuse the MSSQL access, via file read and JuicyPotatoNG.

## Box Info

[![Scrambled](/icons/box-scrambled.webp)](https://hackthebox.com/machines/scrambled)

[Scrambled](https://hackthebox.com/machines/scrambled)

Medium

Retire Date 01 Oct 2022

OS ![Windows](/icons/Windows.webp)

Rated Difficulty ![Rated difficulty for Scrambled](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/scrambled-diff.webp)

Radar Graph ![Radar chart for Scrambled](https://pub-4caceed5c57c4466b559b0834d2806c9.r2.dev/img/scrambled-radar.webp)

User

01:06:15 Root

01:05:01 Creator ## Fork

Scrambled was all about core Windows concepts. There are many tools in Linux to interact with these, but they almost all differ from the native tools in Windows used for the same purpose. For this machine, almost every step was different on Linux and Windows, so I’m going to show both! Select either one here, or navigate via the menu on the left side.

| [![windows](/icons/Windows-large.png)](/2022/10/01/htb-scrambled-win.html) | [![linux](/icons/Linux-large.png)](/2022/10/01/htb-scrambled-linux.html) |
| --- | --- |
|  |  |
