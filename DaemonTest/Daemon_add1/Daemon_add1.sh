#!/bin/bash

# This test will test on the add commands which does not contain double quotation marks:

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add1/add1.csv

# The event '19-11-1986,SchoolDay,No' should be stored in the test.csv.
# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff add1.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm add1.csv
