#!/bin/bash
echo "ADD 19-11-1986 SchoolDay No" >> /tmp/cald_pipe

num=$(ps | grep -i Daemon_add1 | cut -d ' ' -f 1 )
# Get the pid of Daemon_add1.sh
for n in $num
do
  nn=$n
  break
done

# Get the pid of the Daemon.py
pid1=`expr $nn + 1`
echo $pid1

# Kill it
kill $pid1
sleep 1
