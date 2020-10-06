#! /bin/bash

rm output.txt
rm data.csv

exec 3>output.txt
exec 4>data.csv

echo "Last Alive,Index" >&4

for i in {1..1000}
do
	output=$(./josephus $i)
	o1="${output}, Size of Circle: ${i}"
	o2="${output},${i}"
	echo $o1 >&3
	echo $o2 >&4
done
