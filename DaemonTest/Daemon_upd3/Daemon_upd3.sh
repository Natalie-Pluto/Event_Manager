#!/bin/bash

# This test will test on the update command which contains commas

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_upd3/upd3.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff upd3.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm upd3.csv