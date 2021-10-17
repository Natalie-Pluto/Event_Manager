#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "School Day" "I hate it!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 30-01-2020 "Pizza Day" Yes
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 29-12-2009 "Travel to Aus"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SchoolDay "I hate it!"

num=$(ps | grep 'Daemon_add2' | grep -v 'grep' | cut -c 1-6 )

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1