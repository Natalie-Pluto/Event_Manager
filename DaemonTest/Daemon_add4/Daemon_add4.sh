#!/bin/bash

# This test will test on the the error cases for add commands:
# 1. Date provided not valid
# 2. No event name provided
# 3. Duplicate event

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add4/add4.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff add4.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  # Test if there's content in error log file
  if [ -s /tmp/cald_err.log ]
  then
    echo PASSED
  else
    echo FAILED
  fi
fi



