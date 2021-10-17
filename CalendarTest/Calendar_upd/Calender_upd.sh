#!/bin/bash

# This test will test on the error msg produced by update commands
# * Date error
# * Event not exist
# * Multiple error
# * Unable to process calendar database
# * Event exist
# * Not enough argument

# Start Daemon.py
python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/CalendarTest/Calendar_upd/upd.csv

DIFF=$(diff error.csv testError.csv)
if [ "$DIFF" != "" ]
then
  echo FAILED
else
  echo PASSED
fi

rm error.csv

