#!/bin/bash

# This test will test on the add commands which contains double quotation marks:

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add2/add2.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff add2.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi
