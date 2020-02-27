#!/bin/sh
#########################start
start() {
printf "Starting php server...\n"
sleep 2
server="server"
cd $server && php -S 127.0.0.1:3333 > /dev/null 2>&1 & 
sleep 2
printf "php server is working\n"
}
start
