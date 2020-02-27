#!/bin/sh
#########################
clear() {
printf "Start cleaning...\n"
sleep 2
#find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm -r temp
rm -r data
sleep 2
printf "End cleaning\n"
}
clear
