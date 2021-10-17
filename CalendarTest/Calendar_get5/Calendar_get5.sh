#!/bin/bash

# This test will test on the error msg produced by GET INTERVAL commands
# * Date error
# * Start date is after End date
# * Unable to process calendar database
# * Not enough arguments given

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/CalendarTest/Calendar_get5/db.csv

DIFF=$(diff error.csv testError.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm error.csv