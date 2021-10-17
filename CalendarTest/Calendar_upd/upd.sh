#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "School Day" "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 "Pizza Day" Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SchoolDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 BakeDay Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 GoodDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "Tutor Day" No
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "Cat Day" Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SunDay "Ha Ha"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "Cooking class"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 "Tea Day" Go!
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 "School Holiday" "Summer Holiday" "Hell Yes!" 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-105-20055 "Pizza Day" "Cake Day" Yes 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-10-2005 "Tea Day" "Pizza Day" 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-110-1986 SchoolDay 2>> error.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 BakeDay 2>> error.csv
# Delete the database file
rm upd.csv
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 SunDay Friday "Ha Ha" 2>> error.csv


num=$(ps | grep 'Calendar_upd' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $1
sleep 1