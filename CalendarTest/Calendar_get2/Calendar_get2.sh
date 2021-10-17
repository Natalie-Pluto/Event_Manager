#!/bin/bash

# This test will test on the get command - date action option with multiple args

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/CalendarTest/Calendar_get2/db.csv

DIFF=$(diff get2.csv test.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm db.csv
rm get2.csv