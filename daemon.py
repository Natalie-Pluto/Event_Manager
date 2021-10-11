#!/bin/python
import signal
import os
import sys
import datetime

# Use this variable for your loop
daemon_quit = False
# pipe file
Pipe_Name = "/tmp/cald_pipe"
# Error log file
error_file = "/tmp/cald_err.log"
# Where the path of the database stored
cal_link = "/tmp/calendar_link"


# Do not modify or remove this handler
# Handler for quitting the program
def quit_gracefully(signum, frame):
    global daemon_quit
    daemon_quit = True


# For ADD command
def add(db_path, date, event, description):
    is_event_exists = False
    # File for recording errors produced.
    err_file = open(error_file, 'a')
    check_db = open(db_path, 'r')
    with open(db_path, 'a') as db:
        try:
            # Check if the database path is valid
            if not os.path.isfile(db_path):
                err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
                return 0
            # Check if the event existed already
            for line in check_db.readlines():
                e_date = line.split(",")[0].strip()
                e_event = line.split(",")[1].strip()
                if date == e_date and e_event == event:
                    err_file.write("Warning: Event already exist -- " + str(datetime.datetime.now()) + "\n")
                    is_event_exists = True
            # If event not exist in db
            if not is_event_exists:
                if description == "":
                    db.write(date + "," + event + "\n")
                else:
                    db.write(date + "," + event + "," + description + "\n")
        except OSError:
            err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    db.close()
    err_file.close()
    check_db.close()


# For UPD command
def upd(db_path, date, old_event, new_event, new_des):
    # File for recording errors produced.
    err_file = open(error_file, 'a')
    with open(db_path, 'r') as file:
        lines = file.readlines()
    with open(db_path, 'w') as file:
        try:
            # Check if the database path is valid
            if not os.path.isfile(db_path):
                err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
                return 0
            # Check if the event existed already
            for line in lines:
                e_date = line.split(",")[0].strip()
                e_event = line.split(",")[1].strip()
                # Find the target event
                if date == e_date and e_event == old_event:
                    if new_des == "":
                        file.write(date + "," + new_event + "\n")
                    else:
                        file.write(date + "," + new_event + "," + new_des + "\n")
                else:
                    file.write(line)

        except OSError:
            err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    err_file.close()
    file.close()


# For DEL command
def dele(db_path, date, event):
    # File for recording errors produced.
    err_file = open(error_file, 'a')
    with open(db_path, 'r') as file:
        lines = file.readlines()
    with open(db_path, 'w') as file:
        try:
            # Check if the database path is valid
            if not os.path.isfile(db_path):
                err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
                return 0
            # Check if the event existed already
            for line in lines:
                e_date = line.split(",")[0].strip()
                e_event = line.split(",")[1].strip()
                if not (date == e_date and e_event == event):
                    file.write(line)

        except OSError:
            err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    err_file.close()
    file.close()


def run():
    # store the valid database path
    vaild_db_path = " "
    # Create named pipe
    if not os.path.exists(Pipe_Name):
        os.mkfifo(Pipe_Name)

    # The path of the database should be stored in the temporary index file named /tmp/calendar_link.
    path_file = open(cal_link, "w")

    # File for recording errors produced.
    err_file = open(error_file, "a")

    # Get the path for the database
    # If the path for the database is specified:
    try:
        if len(sys.argv) != 1:
            db_path = sys.argv[1]
            # If the path provided does not specified the database file,
            # use the default file name 'cald_db.csv'
            if db_path[-1] == "/":
                default_dbfile = db_path + "/cald_db.csv"
                vaild_db_path = default_dbfile
                # write to calendar link
                path_file.write(default_dbfile)
            else:
                # When the database file name is specified
                vaild_db_path = db_path
                # write to calendar link
                path_file.write(db_path)
        # No database path specified, use the current directory
        else:
            db_path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/cald_db.csv"
            vaild_db_path = db_path
            # write to calendar link
            path_file.write(db_path)
    except OSError:
        err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")

    path_file.close()
    # create database
    db = open(vaild_db_path, "a")
    db.close()
    pipe = ""
    # Start the loop
    while not daemon_quit:
        pipe = open(Pipe_Name, "r")
        try:
            # Read commands from the pipe file
            commands = pipe.readline()
            if len(commands.split("|")) >= 4:
                command_type = commands.split("|")[0]
                date_str = commands.split("|")[1]
                event_str = commands.split("|")[2]
                des_str = ""
                dess_str = ""
                if len(commands.split("|")) >= 4:
                    des_str = commands.split("|")[3]
                if len(commands.split("|")) >= 5:
                    dess_str = commands.split("|")[4]

                # Distinguish the command type and conduct the command
                if command_type == "ADD":
                    add(vaild_db_path, date_str, event_str, des_str)
                if command_type == "UPD":
                    upd(vaild_db_path, date_str, event_str, des_str, dess_str)
                if command_type == "DEL":
                    dele(vaild_db_path, date_str, event_str)
                if command_type == "GET":
                    pass
                else:
                    err_file.write("Warning: Not a valid command! -- " + str(datetime.datetime.now()) + "\n")
            else:
                err_file.write("Warning: Not enough arguments -- " + str(datetime.datetime.now()) + "\n")

        except OSError:
            err_file.write("Warning: Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    # Close the file
    pipe.close()
    err_file.close()

    # Do not modify or remove this function call
    signal.signal(signal.SIGINT, quit_gracefully)


if __name__ == '__main__':
    run()
