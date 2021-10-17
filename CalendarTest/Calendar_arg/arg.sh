#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPP 19-11-1986 BakeDay 2>> error.csv


num=$(ps | grep 'Calendar_arg' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1