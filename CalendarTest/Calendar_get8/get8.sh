#!/bin/bash

# Use calendar.py to write to pipe file
# Use calendar.py to write to pipe file (all possible format)
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 20-01-1986 "School Day" "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 "Pizza Day" Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 20-02-1976 "Tutor Day"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 22-03-2007 "Drink Day" "sad, cancelled"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-12-1988 SchoolDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 23-06-2006 BakeDay Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 18-11-1996 GoodDay "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 28-12-1996 Birthday "Hell, Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1886 "Cat, Dog Day" Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 13-05-1996 "Cake Day, cancelled" "so sad"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 17-11-2016 "Cooking class, started"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 06-10-2020 "Tea Day, Monday"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 09-10-2020 "Yoga Day, Monday" "tired, fun"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py GET NAME "Nat's Birthday" 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py GET NAME 2>> error.csv
rm db.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py GET NAME "Pizza Day" 2>> error.csv

num=$(ps | grep 'Calendar_get8' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1