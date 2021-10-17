# Use calendar.py to write to pipe file

python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-11-1986 Holiday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 07-10-2005 PizzaDay Nat
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py ADD 19-04-2020 SchoolDay Monday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 19-11-1986 Holiday
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/calendar.py DEL 07-10-2005 PizzaDay Nat


num=$(ps | grep 'Daemon_del1' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1