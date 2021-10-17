#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "School Day" "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 "Pizza Day" Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SchoolDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 BakeDay Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 GoodDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 07-100-20005 "Pizza Day" Nat 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 19-11-1986 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 19-110-1986 2>> error.csv

# Delete the database file
rm del.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 07-10-2005 "Pizza Day" 2>> error.csv


num=$(ps | grep 'Calendar_del' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1