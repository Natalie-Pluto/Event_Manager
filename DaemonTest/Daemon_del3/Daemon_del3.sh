#!/bin/bash

# This test will test on the error cases for delete command:
# Date provided not valid
# Not enough argument
# Event not exist (No output)

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_del3/del3.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff del3.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi