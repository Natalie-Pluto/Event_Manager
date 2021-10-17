#!/bin/bash

# This test will test on the command line argument - provide path of the database but not provide the name
# The default csv file name will be used -> cald_db.csv

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_defaultPath/

# Test if the data base file exist
if [ -s /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_defaultPath/cald_db.csv ]
  then
    echo PASSED
  else
    echo FAILED
fi