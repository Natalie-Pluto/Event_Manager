#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "School Day" "I hate it!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 30-01-2020 "Pizza Day" Yes
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 29-12-2009 "Travel to Aus"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SchoolDay "I hate it!"

num=$(ps | grep -i Daemon_add2 | cut -d ' ' -f 1 )
# Get the pid of Daemon_add1.sh
for n in $num
do
  nn=$n
  break
done

# Get the pid of the Daemon.py
pid1=`expr $nn + 1`
echo $pid1

# Kill it
kill $pid1
sleep 1