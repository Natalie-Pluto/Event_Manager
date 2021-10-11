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

I'm really worry that the private testcase will only print "Multiple errors occur!" without other individual error msgs.
If it is the case... HELP! ;-;
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

'''
def date_compare(date1, date2) -> str:
    # Return "B" for date1 bigger than date2, "S" for date1 smaller than date2, "E" for equal
    day1 = date1.split("-")[0].strip()
    month1 = date1.split("-")[1].strip()
    year1 = date1.split("-")[2].strip()
    day2 = date2.split("-")[0].strip()
    month2 = date2.split("-")[1].strip()
    year2 = date2.split("-")[2].strip()
    if year1 > year2:
        return "B"
    elif year1 < year2:
        return "S"
    else:
        if month1 > month2:
            return "B"
        elif month1 < month2:
            return "S"
        else:
            if day1 > day2:
                return "B"
            elif day1 < day2:
                return "S"
            else:
                return "E"


def date_opt(event_date, event_name, event_description):
    # If no date provided
    if len(sys.argv) < 4:
        sys.stderr.write("Unable to parse date\n")
        sys.exit()
    # Get date
    i = 3
    while i < len(sys.argv):
        date = sys.argv[i].strip()
        # Check if the date is valid
        if not date_format_check(date):
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
        else:
            # Check if the event is on this day
            if date == event_date:
                print(event_date + " : " + event_name + " : " + event_description)
        i += 1


def interval_opt(event_date, event_name, event_description) -> str:
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    # Check date
    if not date_format_check(sys.argv[3]) or not date_format_check(sys.argv[4]):
        sys.stderr.write("Unable to parse date\n")
        sys.exit()
    # Check start & end date order
    if date_compare(start_date, end_date) == "B":
        sys.stderr.write("Unable to Process, Start date is after End date\n")
        sys.exit()
    # Store date of events
    if date_compare(start_date, event_date) == "S" and date_compare(end_date, event_date) == "B":
        return event_date + " : " + event_name + " : " + event_description
    elif date_compare(start_date, event_date) == "E" and date_compare(end_date, event_date) == "B":
        return event_date + " : " + event_name + " : " + event_description
    elif date_compare(start_date, event_date) == "S" and date_compare(end_date, event_date) == "E":
        return event_date + " : " + event_name + " : " + event_description


def date_list_sort(date_list1, date_list2):
    j = 0
    while j < len(date_list1):
        i = j + 1
        while i < len(date_list2):
            if date_list1[j] is not None and date_list2[i] is not None:
                if date_compare(date_list1[j].split(":")[0].strip(), date_list2[i].split(":")[0].strip()) == "B":
                    tmp = date_list1[j]
                    tmp2 = date_list2[i]
                    date_list1[j] = tmp2
                    date_list1[i] = tmp
                    date_list2[j] = tmp2
                    date_list2[i] = tmp
            i += 1
        j += 1
    for line in date_list1:
        print(line)


def action_opt(event_date, event_name, event_description):
    # Check enough argument
    if len(sys.argv) < 4:
        sys.stderr.write("Please specify an argument\n")
        sys.exit()
    i = 3
    while i < len(sys.argv):
        name = sys.argv[i].strip()
        # Check if the event is on this day
        if event_name.startswith(name):
            print(event_date + " : " + event_name + " : " + event_description)
        i += 1


def get():
    error_counter = 0
    db = ""
    # Check the file path
    if path_valid() == "NA":
        error_counter += 1
    else:
        db = path_valid().strip()
    # open and read the database
    db_file = open(db, 'r')
    # Get action option
    action_option = sys.argv[2]
    date_list = []
    date_list2 = []
    try:
        for line in db_file.readlines():
            event_date = line.split(",")[0].strip()
            event_name = line.split(",")[1].strip()
            event_description = ""
            if len(line.split(",")) >= 3:
                event_description = line.split(",")[2].strip()
            if action_option == "DATE":
                date_opt(event_date, event_name, event_description)
            elif action_option == "INTERVAL":
                date_list.append(interval_opt(event_date, event_name, event_description))
                date_list2.append(interval_opt(event_date, event_name, event_description))
            elif action_option == "NAME":
                action_opt(event_date, event_name, event_description)
            else:
                sys.stderr.write("Invalid action option.\n")
        if action_option == "INTERVAL":
            date_list_sort(date_list, date_list2)
    except OSError:
        sys.stderr.write("Unable to process calendar database\n")
    db_file.close()
'''

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
    else:
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
        db = path_valid().strip()
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
    # Check the file path
    if path_valid() == "NA":
        sys.exit()
    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
    else:
        sys.stderr.write("Unable to parse date\n")
        sys.exit()
    # Check enough argument
    if len(sys.argv) < 4:
        sys.stderr.write("Missing event name\n")
        sys.exit()


def run():
    pipe = open(Pipe_Name, "a")
    # Write commands into the pipe file
    # To store the command
    if sys.argv[1].strip() == "GET":
        get()
    elif sys.argv[1].strip() == "ADD":
        add_error_check()
    elif sys.argv[1].strip() == "UPD":
        upd_error_check()
    elif sys.argv[1].strip() == "DEL":
        del_error_check()
    else:
        # Invalid command
        sys.stderr.write("Multiple errors occur!\n")
        # Terminate
        sys.exit()
    i = 1
    while i < len(sys.argv):
        try:
            pipe.write(sys.argv[i].strip() + " ")
            if " " in sys.argv[i]:
                pipe.write('"' + sys.argv[i] + '" ')
            else:
                pipe.write(sys.argv[i] + " ")
        except OSError:
            sys.stderr.write("Unable to process calendar database\n")
        i = i + 1

    # Close the file
    pipe.close()


if __name__ == '__main__':
    run()
