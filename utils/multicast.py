#!/usr/bin/env python
import time
from datetime import datetime
import socket
import sys
import struct
import argparse
import pickle

group = '232.8.8.8'
mport = 1900
mttl = 10
message = 'multicast test tool'

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Multicast Send/Receive Test Tool')
parser.add_argument("-send", metavar="string", help="Send a Message",
                    type=str)
parser.add_argument("-receive", help="Receive Messages from Group",
                    action="store_true")
parser.add_argument("-group", metavar="Multicast Group (default: 232.8.8.8)", type=str)
parser.add_argument("-port", metavar="UDP Port", help="UDP Port to receive on (default 1900)",type=int)
parser.add_argument('-ttl', metavar='int', help="Multicast TTL (default 10)", type=int)
parser.add_argument("-v", help="Verbose Output", action="store_true")
parser.add_argument("-bind", metavar="IP Address to bind", type=str)
args = parser.parse_args()

def receiver(mgroup):
    'Receive on a multicast group'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Windows workaround
    try:
        sock.bind((mgroup, mport))
    except socket.error:
        sock.bind(('', mport))

    if bind == "0.0.0.0":
        mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
    else:
        mreq = struct.pack("4s4s", socket.inet_aton(group), socket.inet_aton(bind))

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print('Listing on ' + mgroup + ' port ' + str(mport) + ' Local address ' + bind)

    while True:
        (data, address) = sock.recvfrom(12000)

        # Try to unpickle log record from a DatagramHandler
        #if str(address[0]) == '192.168.0.27':
        try:
            #lrtxt = pickle.loads(data)
            print ( str(address[0]) + ': ' + str(data, encoding='utf-8') )

        # Print message normally
        except Exception as e:
            #print('Exception', str(e))
            msg='';
            for b in data:msg+=chr(b)
            print (str(address[0]) + ': ' + str(msg))
        #print('Received on ' + mgroup + ' from ' + address[0] + ' from port ' + str(address[1]))


def sender(mgroup):
    'Send to a multicast group'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    ttl_bin = struct.pack('@i', mttl)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bin)
    if bind != "0.0.0.0":
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(bind))
    while 1:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mcast_msg = [message, time_now]
        data = pickle.dump(mcast_msg)
        print('Sending to ' + mgroup + ' (TTL ' + str(mttl) + '): ' + mcast_msg)
        sock.sendto(data, (mgroup, mport))
        time.sleep(1)

if args.group:
    group = args.group
if args.ttl:
    mttl = int(args.ttl)
if args.port:
    mport = args.port
if args.bind:
    bind = args.bind
else:
    bind = "0.0.0.0"

if args.send:
    message = args.send
    sender(group)
elif args.receive:
    receiver(group)
else:
    parser.print_help()
