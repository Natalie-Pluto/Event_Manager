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
def add(db_path, data, event, description):
    # File for recording errors produced.
    err_file = open(error_file, "a")
    # If database does not exist anymore
    db = open(db_path, "w")
    try:
        # If no description
        if len(description) == 0:
            db.write(data + "," + event + "\n")
        else:
            # If there's description
            db.write(data + "," + event + "," + description + "\n")
    except OSError:
        err_file.write("Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    db.close()

    err_file.close()


# For UPD command
def upd(db_path):
    pass


# For DEL command
def dele(db_path):
    pass


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
    # The program will only take the first argument.
    try:
        if len(sys.argv) != 1:
            db_path = sys.argv[1]
            # If the path provided does not specified the database file,
            # use the default file name 'cald_db.csv'
            if db_path[-1] == "/":
                default_dbFile = db_path + "/cald_db.csv"
                vaild_db_path = default_dbFile
                print("haha")
                # write to calendar link
                path_file.write(default_dbFile)
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
        err_file.write("Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")

    path_file.close()
    # create database
    db = open(vaild_db_path, "w")
    db.close()
    # Start the loop
    while not daemon_quit:
        pipe = open(Pipe_Name, "r")
        try:
            # Read from the pipe file
            commands = pipe.readline()
            print(commands)
            if not len(commands) == 0:
                # Get the command type
                command_type = commands.split(" ")[0]
                date_str = commands.split(" ")[1]
                event_str = commands.split(" ")[2]
                if len(commands.split(" ")) > 3:
                    des_str = commands.split(" ")[3]
                else:
                    des_str = ""
                # Distinguish the command type and conduct the command
                if command_type == "ADD":
                    add(vaild_db_path, date_str, event_str, des_str)
                if command_type == "UPD":
                    upd(vaild_db_path)
                if command_type == "DEL":
                    dele(vaild_db_path)
                if command_type == "GET":
                    pass
                else:
                    err_file.write("Not a valid command! -- " + str(datetime.datetime.now()) + "\n")
        except OSError:
            err_file.write("Unable to process calendar database -- " + str(datetime.datetime.now()) + "\n")
    # Close the file
    pipe.close()
    err_file.close()

    # Do not modify or remove this function call
    signal.signal(signal.SIGINT, quit_gracefully)



if __name__ == '__main__':
    run()
