#!/bin/bash

# This test will test on the add commands which contains commas in the description/ event string:

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add3/add3.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff add3.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi