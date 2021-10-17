#!/bin/bash

# This test will test on the error msg produced by delete commands
# * Date error
# * Event name missing
# * Multiple error
# * Unable to process calendar database

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/CalendarTest/Calendar_del/del.csv

DIFF=$(diff error.csv testError.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm error.csv
