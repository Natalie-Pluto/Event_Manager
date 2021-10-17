#!/bin/bash

# This test will test on the update command which contains double quotation marks

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_upd2/upd2.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff upd2.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm upd2.csv