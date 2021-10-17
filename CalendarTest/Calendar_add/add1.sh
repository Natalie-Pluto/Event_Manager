#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 190-11-196 "Happy, Sad Day" 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 190-11-1966  2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 190-11-196 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 2>> error.csv
# Delete the database file
rm add1.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1960 "Happy Birthday" 2>> error.csv


num=$(ps | grep 'Calendar_add' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1