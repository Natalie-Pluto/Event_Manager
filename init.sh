#!/sbin/openrc-run

command=/usr/bin/daemon

depend() {
  need localmount
}

start() {
  if [ "${RC_CMD}" = "restart" ];
  then
    ebegin"Restarting daemon"
    start-stop-daemon --start --exec /usr/bin/daemon \
      --pidfile /usr/bin/daemon.pid --name daemon
    eend $?
  fi

  ebegin"Starting daemon"
  start-stop-daemon --start --exec /usr/bin/daemon \
    --pidfile /usr/bin/daemon.pid --name daemon
  eend $?
}


stop() {
  ebegin"Stopping daemon"
  start-stop-daemon --stop --exec /usr/bin/daemon \
    --pidfile /usr/bin/daemon.pid --name daemon
  eend $?
}
