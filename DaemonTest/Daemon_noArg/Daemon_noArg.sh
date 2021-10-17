#!/bin/bash

# This test will test on the command line argument - No command line argument provided
# The default csv file name be used -> cald_db.csv and the path will be as the same as the daemon.py

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py

# Test if the data base file exist
if [ -s /Users/natalielu/Desktop/INFO1112/Asm2/cald/cald_db.csv ]
  then
    echo PASSED
  else
    echo FAILED
fi

rm /Users/natalielu/Desktop/INFO1112/Asm2/cald/cald_db.csv