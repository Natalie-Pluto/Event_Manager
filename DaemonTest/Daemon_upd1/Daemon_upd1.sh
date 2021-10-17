#!/bin/bash

# This test will test on the update command which does not contain double quotation marks
# This test will also test on the case when the event to be updated has a description in database but the update command
# does not provide the description (Therefore the description should be removed after update)

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_upd1/upd1.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff upd1.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi