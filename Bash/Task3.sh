#!/bin/bash

hosts=("192.168.1.1" "173.194.222.113" "87.250.250.242")
port=80
for h in ${hosts[@]}; do
    for ((i=1;i<=5;i++))
    do
result=$(nmap $h -p$port | grep open)
pattern="open";
  if [[ $result =~ $pattern ]]; then
    echo "$h on port $port is up"
    echo $result
    echo "$(date)" >> curl.log
  else
    echo "$h on port $port is down"
    echo $result
    echo "$(date)" "!!!ERROR!!!""$h on port $port is down" >> curl.log
    break
  fi
done
done
