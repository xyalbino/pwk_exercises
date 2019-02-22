#!/bin/bash

hosts=$(cat ./smb_hosts)

for host in $hosts
do
	enum4linux -a $host > "host_"$host $
done


