import os
import sys
import datetime
# Named pipe within /tmp named cald_pipe
Pipe_Name = "/tmp/cald_pipe"
# Where the path of the database stored
cal_link = "/tmp/calendar_link"

'''
JUSTIFICATION:
Multiple Errors ->
1. If there is error not specified in the spec, print "Multiple errors occur!"
2. There are multiple errors occurred -> Print individual error first, in the end print "Multiple errors occur!"

For 2, I can't find any confirmation on Ed, there are some posts about it but they all got no reply. I will assume that 
we need to print individual error first, then in the end print "Multiple errors occur!". 
'''


# Check if the date is valid
def date_format_check(date) -> bool:
    if len(date.split("-")) != 3:
        return False
    day = date.split("-")[0]
    month = date.split("-")[1]
    year = date.split("-")[2]
    is_date_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_date_valid = False

    return is_date_valid


def path_valid() -> str:
    db_file = open(cal_link, "r")
    try:
        # Get the path of the database
        db_link = db_file.readline()
        # Test if an index file or the database file exist
        if not os.path.isfile(db_link):
            # Print error msg to stderr
            sys.stderr.write("Unable to process calendar database\n")
            return "NA"
    except OSError:
        # Print error msg to stderr
        sys.stderr.write("Unable to process calendar database\n")
        return "NA"
    db_file.close()
    return db_link


def get():
    error_counter = 0
    # Check the file path
    if path_valid() == "NA":
        error_counter += 1
    else:
        db = path_valid()


def add_error_check():
    error_counter = 0
    # Check the file path
    if path_valid() == "NA":
        error_counter += 1
    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            sys.stderr.write("Unable to parse date\n")
            error_counter += 1
    # Check enough argument
    if len(sys.argv) < 4:
        sys.stderr.write("Missing event name\n")
        error_counter += 1
    # Check if there are multiple errors happened
    if error_counter > 1:
        sys.stderr.write("Multiple errors occur!\n")
    if error_counter > 0:
        sys.exit()


def upd_error_check():
    db = ""
    error_counter = 0
    if_event_exist = False
    # Check the file path
    if path_valid() == "NA":
        error_counter += 1
    else:
        db = path_valid()
    # Check if the event exists
    lines = open(db, 'r')
    for line in lines.readlines():
        if line.split(",")[1].strip() == sys.argv[3] and line.split(",")[0].strip() == sys.argv[2]:
            if_event_exist = True
    if not if_event_exist:
        sys.stderr.write("Unable to update, event does not exist\n")
        error_counter += 1
    lines.close()
    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            sys.stderr.write("Unable to parse date\n")
            error_counter += 1
    # Check enough argument
    if len(sys.argv) < 5:
        sys.stderr.write("Not enough arguments given\n")
        error_counter += 1
    # Check if there are multiple errors happened
    if error_counter > 1:
        sys.stderr.write("Multiple errors occur!\n")
    if error_counter > 0:
        sys.exit()


def del_error_check():
    error_counter = 0
    # Check the file path
    if path_valid() == "NA":
        error_counter += 1
    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            sys.stderr.write("Unable to parse date\n")
            error_counter += 1
    # Check enough argument
    if len(sys.argv) < 4:
        sys.stderr.write("Missing event name\n")
        error_counter += 1
    # Check if there are multiple errors happened
    if error_counter > 1:
        sys.stderr.write("Multiple errors occur!\n")
    if error_counter > 0:
        sys.exit()


def errors(error_type):
    if error_type == "DATE":
        sys.stderr.write("Unable to parse date\n")
    elif error_type == "EVENT":
        sys.stderr.write("Missing event name\n")
    elif error_type == "ARG":
        sys.stderr.write("Not enough arguments given\n")
    elif error_type == "DB":
        sys.stderr.write("Unable to process calendar database\n")
    # Not valid command type (NV)
    elif error_type == "NV":
        sys.stderr.write("Multiple errors occur!\n")
    elif error_type == "MUL":
        sys.stderr.write("Multiple errors occur!\n")


def run():
    pipe = open(Pipe_Name, "a")
    # Write commands into the pipe file
    try:
        # To store the command
        i = 1
        while i < len(sys.argv):
            if sys.argv[1] == "GET":
                get()
            elif sys.argv[1] == "ADD":
                add_error_check()
            elif sys.argv[1] == "UPD":
                upd_error_check()
            elif sys.argv[1] == "DEL":
                del_error_check()
            else:
                # Invalid command
                sys.stderr.write("Multiple errors occur!\n")
                # Terminate
                sys.exit()
            pipe.write(sys.argv[i] + " ")
            '''
            if " " in sys.argv[i]:
                pipe.write('"' + sys.argv[i] + '" ')
            else:
                pipe.write(sys.argv[i] + " ")
            '''
            i = i + 1
    except OSError:
        sys.stderr.write("Unable to process calendar database\n")

    # Close the file
    pipe.close()


if __name__ == '__main__':
    run()

