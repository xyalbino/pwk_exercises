#!/bin/bash

# reset all counters and iptables rules
iptables -Z && iptables -F

# measure incoming traffic TO 10.11.21.97
iptables -I INPUT 1 -s 10.11.21.97 -j ACCEPT

# measure outgoing traffic FROM 10.11.21.97
iptables -I OUTPUT 1 -d 10.11.21.97 -j ACCEPT

# swtiches:
#
#	-Z: zero all counters
#	-F: reset all rules
#	-I: insertion - will insert a new rule and apply it first
#					to the chain
#	-s: source
#	-d: destination
#
# Viewing the output:
#
#	iptables -vn -L
#		-v: view
#		-n: numerica addresses only
#		-L: List format
#
# Zeroing all counters:
#
#	iptables -Z
#
