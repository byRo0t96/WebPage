#!/bin/sh
#########################
stop() {
printf "Stoping php server...\n"
sleep 2
checkphp=$(ps aux | grep -o "php" | head -n1)
checkssh=$(ps aux | grep -o "ssh" | head -n1)
pkill -f -2 php > /dev/null 2>&1
killall -2 php > /dev/null 2>&1
pkill -f -2 ssh > /dev/null 2>&1
killall ssh > /dev/null 2>&1
sleep 2
printf "php server is stoped\n"
}
stop
