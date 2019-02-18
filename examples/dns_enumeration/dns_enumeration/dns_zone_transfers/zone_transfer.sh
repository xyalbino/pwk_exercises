#!/bin/bash

# Simple Zone Transfer Bash Script
# $1 is the first argument given after the bash script


# Check if argument was given, if not, print usage....
if [ $# -lt 1 || $# -gt 1 ]
then
	echo "[*] Usage: zone_transfer.sh [domain]"
	echo "[*] Exiting..."
	exit 1
else

	# If argument was given, identify the DNS servers for the domain
	# For each of these servers, attmept a zone transfer
	for server in $(host -t ns $1 | cut -d " " -f4)
	do 
		host -l $1 ${server}
	done
fi

exit 0
