#!/bin/bash

# This test will test on the command line argument - provide name and path of the database

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_path/path.csv

# Test if the data base file exist
if [ -s /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_path/path.csv ]
  then
    echo PASSED
  else
    echo FAILED
fi

rm /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_path/path.csv