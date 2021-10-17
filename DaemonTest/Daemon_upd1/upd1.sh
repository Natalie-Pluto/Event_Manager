#!/bin/bash

# Use calendar.py to write to pipe file
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 Birthday Pluto
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 Event Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 Birthday BirthdayParty Natalie
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-10-2005 Event NewEvent


num=$(ps | grep 'Daemon_upd1' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1