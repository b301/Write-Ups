zzzzzzzzzzzzzzzzzzzzz boot up already
[anonymous is very cool]

IP=10.10.112.57

<h1>enumeration</h1>

```
└─$ nmap -sV -sC 10.10.112.57
Starting Nmap 7.92 ( https://nmap.org ) at 2022-02-24 23:42 IST
Nmap scan report for 10.10.112.57
Host is up (0.12s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.50.80
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) 
| ssh-hostkey:
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)
|_  256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.68 seconds

```

bruh... just ftp and ssh?

ftp credentials:

```
username: anonymous
password:
```

huh, it worked?
anyhow, that scan cannot be everything there is ...

```
└─$ nmap -A -sV -sC 10.10.112.57 -vv -T4
Starting Nmap 7.92 ( https://nmap.org ) at 2022-02-24 23:52 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
Initiating Ping Scan at 23:52
Scanning 10.10.112.57 [2 ports]
Completed Ping Scan at 23:52, 0.08s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 23:52
Completed Parallel DNS resolution of 1 host. at 23:52, 1.13s elapsed
Initiating Connect Scan at 23:52
Scanning 10.10.112.57 [1000 ports]
Discovered open port 21/tcp on 10.10.112.57
Discovered open port 22/tcp on 10.10.112.57
Discovered open port 139/tcp on 10.10.112.57
Discovered open port 445/tcp on 10.10.112.57
Completed Connect Scan at 23:52, 3.62s elapsed (1000 total ports)
Initiating Service scan at 23:52
Scanning 4 services on 10.10.112.57
Completed Service scan at 23:52, 11.33s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.112.57.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:52
NSE: [ftp-bounce 10.10.112.57:21] PORT response: 500 Illegal PORT command.
Completed NSE at 23:52, 2.61s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.57s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
Nmap scan report for 10.10.112.57
Host is up, received conn-refused (0.081s latency).
Scanned at 2022-02-24 23:52:27 IST for 19s
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE    SERVICE     REASON      VERSION
21/tcp   open     ftp         syn-ack     vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.50.80
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open     ssh         syn-ack     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCi47ePYjDctfwgAphABwT1jpPkKajXoLvf3bb/zvpvDvXwWKnm6nZuzL2HA1veSQa90ydSSpg8S+B8SLpkFycv7iSy2/Jmf7qY+8oQxWThH1fwBMIO5g/TTtRRta6IPoKaMCle8hnp5pSP5D4saCpSW3E5rKd8qj3oAj6S8TWgE9cBNJbMRtVu1+sKjUy/7ymikcPGAjRSSaFDroF9fmGDQtd61oU5waKqurhZpre70UfOkZGWt6954rwbXthTeEjf+4J5+gIPDLcKzVO7BxkuJgTqk4lE9ZU/5INBXGpgI5r4mZknbEPJKS47XaOvkqm9QWveoOSQgkqdhIPjnhD
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPjHnAlR7sBuoSM2X5sATLllsFrcUNpTS87qXzhMD99aGGzyOlnWmjHGNmm34cWSzOohxhoK2fv9NWwcIQ5A/ng=
|   256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDHIuFL9AdcmaAIY7u+aJil1covB44FA632BSQ7sUqap
139/tcp  open     netbios-ssn syn-ack     Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open     netbios-ssn syn-ack     Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
2251/tcp filtered dif-port    no-response
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 41538/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 53869/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 42594/udp): CLEAN (Failed to receive data)
|   Check 4 (port 38792/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   ANONYMOUS<00>        Flags: <unique><active>
|   ANONYMOUS<03>        Flags: <unique><active>
|   ANONYMOUS<20>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-02-24T21:52:43
|_  start_date: N/A
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2022-02-24T21:52:43+00:00

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:52
Completed NSE at 23:52, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.82 seconds

```

that seems more like it!

<h1>enum4linux</h1>

```
└─$ enum4linux 10.10.112.57
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Fri Feb 25 00:02:57 2022

 ==========================
|    Target Information    |
 ==========================
Target ........... 10.10.112.57
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ====================================================
|    Enumerating Workgroup/Domain on 10.10.112.57    |
 ====================================================
[+] Got domain/workgroup name: WORKGROUP

 ============================================
|    Nbtstat Information for 10.10.112.57    |
 ============================================
Looking up status of 10.10.112.57
        ANONYMOUS       <00> -         B <ACTIVE>  Workstation Service
        ANONYMOUS       <03> -         B <ACTIVE>  Messenger Service
        ANONYMOUS       <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

        MAC Address = 00-00-00-00-00-00

 =====================================
|    Session Check on 10.10.112.57    |
 =====================================
[+] Server 10.10.112.57 allows sessions using username '', password ''

 ===========================================
|    Getting domain SID for 10.10.112.57    |
 ===========================================
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ====================================== 
|    OS information on 10.10.112.57    |
 ======================================
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 10.10.112.57 from smbclient:
[+] Got OS info for 10.10.112.57 from srvinfo:
        ANONYMOUS      Wk Sv PrQ Unx NT SNT anonymous server (Samba, Ubuntu)
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03

 =============================
|    Users on 10.10.112.57    |
 =============================
index: 0x1 RID: 0x3eb acb: 0x00000010 Account: namelessone      Name: namelessone       Desc: 

user:[namelessone] rid:[0x3eb]

 =========================================
|    Share Enumeration on 10.10.112.57    |
 =========================================

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        pics            Disk      My SMB Share Directory for Pics
        IPC$            IPC       IPC Service (anonymous server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            ANONYMOUS

[+] Attempting to map shares on 10.10.112.57
//10.10.112.57/print$   Mapping: DENIED, Listing: N/A
//10.10.112.57/pics     Mapping: OK, Listing: OK
//10.10.112.57/IPC$     [E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ====================================================
|    Password Policy Information for 10.10.112.57    |
 ====================================================


[+] Attaching to 10.10.112.57 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] ANONYMOUS
        [+] Builtin

[+] Password Info for Domain: ANONYMOUS

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 37 days 6 hours 21 minutes
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes
        [+] Locked Account Duration: 30 minutes
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 37 days 6 hours 21 minutes


[+] Retieved partial password policy with rpcclient:

Password Complexity: Disabled
Minimum Password Length: 5


 ==============================
|    Groups on 10.10.112.57    |
 ==============================

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 =======================================================================
|    Users on 10.10.112.57 via RID cycling (RIDS: 500-550,1000-1050)    |
 =======================================================================
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-2144577014-3591677122-2188425437
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-21-2144577014-3591677122-2188425437 and logon username '', password ''
S-1-5-21-2144577014-3591677122-2188425437-500 *unknown*\*unknown* (8)
S-1-5-21-2144577014-3591677122-2188425437-501 ANONYMOUS\nobody (Local User)
S-1-5-21-2144577014-3591677122-2188425437-502 *unknown*\*unknown* (8)
.
.
.
S-1-5-21-2144577014-3591677122-2188425437-512 *unknown*\*unknown* (8)
S-1-5-21-2144577014-3591677122-2188425437-513 ANONYMOUS\None (Domain Group)
S-1-5-21-2144577014-3591677122-2188425437-514 *unknown*\*unknown* (8)
.
.
.
S-1-5-21-2144577014-3591677122-2188425437-1002 *unknown*\*unknown* (8)
S-1-5-21-2144577014-3591677122-2188425437-1003 ANONYMOUS\namelessone (Local User)
S-1-5-21-2144577014-3591677122-2188425437-1004 *unknown*\*unknown* (8)
.
.
.
S-1-5-21-2144577014-3591677122-2188425437-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
S-1-5-32-500 *unknown*\*unknown* (8)
.
.
.
S-1-5-32-543 *unknown*\*unknown* (8)
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
S-1-5-32-1000 *unknown*\*unknown* (8)
.
.
.
S-1-5-32-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\namelessone (Local User)

 =============================================
|    Getting printer info for 10.10.112.57    |
 =============================================
No printers returned.


enum4linux complete on Fri Feb 25 00:09:55 2022
```

after a little messing around i figured out how tf smbclient works

```
smbclient //10.10.112.57/pics
```

the smb files turn out to be a deadend ... read some writeups (yes im that weak) and figure i need to write into
the clean.sh file a remote shell and i got a reverse shell yay...

user.txt >> 90d6f992585815ff991e68748c414740

ok no more cheats! 

so find / -perm /4000 (or 6000? whatever) 2>/dev/null (because fuck errors)

try pkexec doesnt work
try env works

gg.ez

root.txt >> 4d930091c31a622a7ed10f27999af363
