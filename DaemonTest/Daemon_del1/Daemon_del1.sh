#!/bin/bash

# This test will test on the delete command which does not contain double quotation marks

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_del1/del1.csv

# Compare the content in test.csv with the expected content in add1.csv
DIFF=$(diff del1.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi