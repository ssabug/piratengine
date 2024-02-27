# Network Traffic

The players/computers with EngineDJ software uses IGMPv3, HTTP and mDNS protocols .

## IGMPv3

All EngineDJ hardware devices join group on address 224.0.0.22. Computer with EngineDJ Software does not seem to use it.

## mDNS

All EngineDJ hardware / software send packets to address 224.0.0.251.

## HTTP

There are SSDP messages from EngineDJ software to 239.255.255.250 those contain M-SEARCH * HTTP/1.1 .

These are triggered after loading EngineDJ software as a source from a hardware player.

We can connect via http to computer ip address on port 50010, and got the following output:
���������?яя��?яя��� �ю�����������?��

While running Engine DJ on a computer and sharing a playlist, we have TCP stream between the player requesting the playlist content and the computer.

This kind of output is seen :
[output_1](output1.txt)