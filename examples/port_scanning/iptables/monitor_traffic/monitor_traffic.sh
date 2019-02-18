#!/bin/bash
# script title: monitor_traffic.sh
# usage: monitor_traffic.sh [target_ip_address]

# check args and print description if no args or too many args are given
if [ $# -gt 1 ] || [ $# -lt 1 ]
then
	echo "[!] This script uses iptables to monitor incoming and outgoing"
	echo "[!] traffic for a specified target ip address..."
	echo ""
	echo "[*] Usage: $0 [target_ip_address]"
	echo ""
	echo "[!] Use iptables -vn -L to view results..."
	echo "[!] Use iptables -Z to zero all counters..."
else
	# reset all counters and iptables rules
	iptables -Z && iptables -F
	
	# measure incoming traffic TO $1
	iptables -I INPUT 1 -s $1 -j ACCEPT

	#measure outgoing traffic FROM $1
	iptables -I OUTPUT 1 -d $1 -j ACCEPT
fi
	
