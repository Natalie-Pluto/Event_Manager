# Use calendar.py to write to pipe file

python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 "School, Day" "Hell, Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 "Pizza Day" Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 SchoolDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 BakeDay Yay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 07-10-2005 "School, Day" "Pizza Day" "Hell, Yes!"
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-110-1086 SchoolDay Holiday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-10-2000 Birthday Holiday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986 BakeDay
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py UPD 19-11-1986


num=$(ps | grep 'Daemon_upd4' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1