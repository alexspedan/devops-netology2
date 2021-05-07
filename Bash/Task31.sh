#!/bin/bash

for ip in "87.250.250.242" "13.107.6.156" "8.8.8.8"
do
  for ((i=1;i<=5;i++))
  do
  curl -s http://$ip > /dev/null
  (($?)) && echo "$ip:80 is NOK as of `date`"  || break & echo "$ip:80 is OK as of `date`"
done
done
