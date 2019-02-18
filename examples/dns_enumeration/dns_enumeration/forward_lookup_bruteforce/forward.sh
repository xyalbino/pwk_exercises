#!/bin/bash

# for each name in the "list.txt" file, run a forward DNS lookup
# then grep and cut the output, using " " as the delimiter, specifying the
# first and fourth fields

for name in $(cat list.txt)
do
	host $name.megacorpone.com | grep "has address" | cut -d " " -f 1,4
done
