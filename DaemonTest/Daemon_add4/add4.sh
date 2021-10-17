#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "Happy Birthday" Pluto
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "Happy Birthday" Pluto
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 303-01-99999 "Invalid Date"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 29-12-2009

num=$(ps | grep 'Daemon_add4' | grep -v 'grep' | cut -c 1-6 )

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1