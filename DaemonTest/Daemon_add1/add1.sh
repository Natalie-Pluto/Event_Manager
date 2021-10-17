#!/bin/bash
echo "ADD 19-11-1986 SchoolDay No" >> /tmp/cald_pipe

num=$(ps | grep 'Daemon_add1' | grep -v 'grep' | cut -c 1-6)

# Get the pid of the Daemon.py and kill it
set -- $num
kill $2
sleep 1