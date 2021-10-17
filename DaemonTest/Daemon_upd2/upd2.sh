#!/bin/bash

# Use calendar.py to write to pipe file
# All possible format with double quotation marks are tested
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
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 "School Day" "Summer Holiday" "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-10-2005 "Pizza Day" "Cake Day" Yes
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-10-2005 "Tea Day" "Study Day"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 SchoolDay "Christmas Holiday" "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 BakeDay "Bake Day" Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 GoodDay "Winter Holiday"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 "Tutor Day" Holiday "Hell Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 "Cat Day" DogDay Yes!
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 "Cooking class" Monday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 SunDay Friday "Ha Ha"

num=$(ps | grep 'Daemon_upd2' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1