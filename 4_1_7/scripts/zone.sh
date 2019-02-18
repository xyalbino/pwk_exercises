#!/bin/bash

#Simple Zone Transfer Bash Script
# $1 is the first argument given after the bash script
# Chck if argument was given, if not, print usage

if [ $@ < 2 ]
then
	echo "Simple zone transfer script..."
	echo "Usage: zone.sh [domain name]"
	exit 0
else
	# if argument was given, identify the DNS servers for the domain
	for server in $(host -t ns $1 | cut -d " " -f 4)
	do
		#for each of these servers, attempt a zone transfer
		host -l $1 $server | grep "has address"
	done
fi
