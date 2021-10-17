import os
import sys
import datetime


# Named pipe within /tmp named cald_pipe
Pipe_Name = "/tmp/cald_pipe"
# Where the path of the database stored
cal_link = "/tmp/calendar_link"


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
            return "NA"
    except OSError:
        return "NA"
    db_file.close()
    return db_link


'''
This is a method to compare time,
I wrote this because I thought we can't use datetime module at first.
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

'''
If more than one arg:
The output will be order by the order of args: 
(calendar GET DATE 09-01-2020 09-01-1999)
09-01-2020 : School Day : NO
09-01-2020 : Party : Yay!
09-01-2020 : Dentist : NO!
09-01-1999 : Exam : NO
09-01-1999 : Holiday : YES
09-01-1999 : Birthday : Yay!
'''
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
        # Program will terminate immediately once an invalid date is determined.
        # If there are more dates provided after, these dates will be ignored
        if not date_format_check(date):
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
        else:
            # Check if the event is on this day
            if date == event_date:
                if event_description != "":
                    print(event_date + " : " + event_name + " : " + event_description)
                else:
                    print(event_date + " : " + event_name + " :")
        i += 1


def interval_opt(event_date, event_name, event_description) -> str:
    # Check enough argument
    if len(sys.argv) < 5:
        sys.stderr.write("Not enough arguments given\n")
        sys.exit()
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
        if event_description != "":
            return event_date + " : " + event_name + " : " + event_description
        else:
            return event_date + " : " + event_name + " :"
    elif date_compare(start_date, event_date) == "E" and date_compare(end_date, event_date) == "B":
        if event_description != "":
            return event_date + " : " + event_name + " : " + event_description
        else:
            return event_date + " : " + event_name + " :"
    elif date_compare(start_date, event_date) == "S" and date_compare(end_date, event_date) == "E":
        if event_description != "":
            return event_date + " : " + event_name + " : " + event_description
        else:
            return event_date + " : " + event_name + " :"


'''
This is a method to sort the result list by date.
'''
def date_list_sort(date_list1, date_list2):
    j = 0
    while j < len(date_list1):
        i = j + 1
        while i < len(date_list2):
            if date_list1[j] and date_list2[i]:
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
        if line is not None:
            print(line)

'''
If only one arg:
The output will be ordered by date.
If more than one arg:
The output will be order by event name (as the order of args) and then order by date:
(calendar GET NAME "School Day" Exam)
09-01-2020 : School Day : NO
09-01-2021 : School Day : NO
09-01-2022 : School Day : NO
09-01-2020 : Exam : NO
09-01-2021 : Exam : NO
09-01-2022 : Exam : NO
'''
def name_opt1(db):
    date_list1 = []
    date_list2 = []

    # Check enough argument
    if len(sys.argv) < 4:
        sys.stderr.write("Please specify an argument\n")
        sys.exit()

    # open and read the
    # database
    i = 3
    while i < len(sys.argv):
        name = sys.argv[i].strip()
        db_file = open(db, 'r')
        try:
            for line in db_file.readlines():
                # If line is not empty
                if not line == '\n':
                    # Get date, event and description
                    # Note: According what I mentioned in the daemon.py
                    '''
                    If the event or description string contains comma, it will be stored with double quotes in the database.
                    19-11-1920,"Pizza Day, cancelled",sad
                    19-11-1920,SummerHoliday,"sleeping, working"
                    '''
                    # Event and description string may contains comma therefore has quotes around them
                    event_date = line.split(",")[0].strip()
                    event_name = line.split(",")[1].strip()
                    event_description = ""
                    if '"' in line:
                        if len(line.split('"')) > 3:
                            event_name = line.split('"')[1].strip()
                            event_description = line.split('"')[3].strip()
                        elif len(line.split('"')) == 3 and '"' in line.split(",")[1]:
                            event_name = line.split('"')[1].strip()
                            if line.split('"')[2].strip():
                                event_description = line.split('",')[1].strip()
                        elif len(line.split('"')) == 3 and '"' not in line.split(",")[1]:
                            event_description = line.split('"')[1].strip()
                    else:
                        if len(line.split(",")) >= 3:
                            event_description = line.split(",")[2].strip()
                    # Check if the event is on this day
                    if event_name.startswith(name):
                        if event_description != "":
                            date_list1.append(event_date + " : " + event_name + " : " + event_description)
                            date_list2.append(event_date + " : " + event_name + " : " + event_description)
                        else:
                            date_list1.append(event_date + " : " + event_name + " :")
                            date_list2.append(event_date + " : " + event_name + " :")
            # Sort the list and print out
            date_list_sort(date_list1, date_list2)
            date_list1.clear()
            date_list2.clear()
            i += 1
        except OSError:
            sys.stderr.write("Unable to process calendar database\n")
            sys.exit()
        db_file.close()


def get():
    # Check the file path
    if path_valid() == "NA":
        sys.stderr.write("Unable to process calendar database\n")
        sys.exit()
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
            # If line is not empty
            if not line == '\n':
                # Get date, event and description
                # Note: According what I mentioned in the daemon.py
                '''
                If the event or description string contains comma, it will be stored with double quotes in the database.
                19-11-1920,"Pizza Day, cancelled",sad
                19-11-1920,SummerHoliday,"sleeping, working"
                '''
                # Event and description string may contains comma therefore has quotes around them
                event_date = line.split(",")[0].strip()
                event_name = line.split(",")[1].strip()
                event_description = ""
                if '"' in line:
                    if len(line.split('"')) > 3:
                        event_name = line.split('"')[1].strip()
                        event_description = line.split('"')[3].strip()
                    elif len(line.split('"')) == 3 and '"' in line.split(",")[1]:
                        event_name = line.split('"')[1].strip()
                        if line.split('"')[2].strip():
                            event_description = line.split('",')[1].strip()
                    elif len(line.split('"')) == 3 and '"' not in line.split(",")[1]:
                        event_description = line.split('"')[1].strip()
                else:
                    if len(line.split(",")) >= 3:
                        event_description = line.split(",")[2].strip()

                if action_option == "DATE":
                    date_opt(event_date, event_name, event_description)
                elif action_option == "INTERVAL":
                    date_list.append(interval_opt(event_date, event_name, event_description))
                    date_list2.append(interval_opt(event_date, event_name, event_description))
                elif action_option == "NAME":
                    pass
                else:
                    sys.stderr.write("Invalid action option.\n")
                    sys.exit()

        # The output of his action need to be sorted in a way so it needs to be implement in a different way
        if action_option == "NAME":
            name_opt1(db)
        # Sort and return the result
        if action_option == "INTERVAL":
            date_list_sort(date_list, date_list2)

    except OSError:
        sys.stderr.write("Unable to process calendar database\n")
        sys.exit()
    db_file.close()


def add_error_check():
    error_counter = 0
    date_error = False
    name_error = False
    path_error = False
    # Check the file path
    if path_valid() == "NA":
        path_error = True
        error_counter += 1

    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            date_error = True
            error_counter += 1
    # Date is not given
    else:
        date_error = True
        error_counter += 1

    # Check enough argument
    if len(sys.argv) == 3:
        name_error = True
        error_counter += 1

    # Check if there are multiple errors happened
    if error_counter == 1:
        if date_error:
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
        elif name_error:
            sys.stderr.write("Missing event name\n")
            sys.exit()
        elif path_error:
            sys.stderr.write("Unable to process calendar database\n")
            sys.exit()
    elif error_counter > 1:
        sys.stderr.write("Multiple errors occur!\n")
        sys.exit()


def upd_error_check():
    db = ""
    error_counter = 0
    if_event_exist = False
    if_updated_exist = False
    path_error = False
    event_error = False
    updated_error = False
    date_error = False
    arg_error = False

    # Check the file path
    if path_valid() == "NA":
        path_error = True
        error_counter += 1
    else:
        db = path_valid()

    # Check if the event exists
    if not path_error:
        lines = open(db, 'r')
        try:
            if len(sys.argv) > 4:
                # Check if the event to be update exist
                for line in lines.readlines():
                    if not line == '\n':
                        if '"' in line.split(",")[1].strip():
                            if line.split('"')[1].strip() == sys.argv[3] and line.split(",")[0].strip() == sys.argv[2]:
                                if_event_exist = True
                        else:
                            if line.split(",")[1].strip() == sys.argv[3] and line.split(",")[0].strip() == sys.argv[2]:
                                if_event_exist = True
                        '''
                        [This is not addressed in the assignment spec but I feel like it is an error case]
                        Check if the updated event existed in the database to avoid duplicate. 
                        '''
                        if '"' in line.split(",")[1].strip():
                            if line.split('"')[1].strip() == sys.argv[4] and line.split(",")[0].strip() == sys.argv[2]:
                                if_updated_exist = True
                        else:
                            if line.split(",")[1].strip() == sys.argv[4] and line.split(",")[0].strip() == sys.argv[2]:
                                if_updated_exist = True

            # Event to be updated does not exist
            if not if_event_exist and len(sys.argv) > 4:
                event_error = True
                error_counter += 1

            # Update event existed already
            if if_updated_exist:
                updated_error = True
                error_counter += 1

        except OSError:
            path_error = True
        lines.close()

    # Check the date
    '''
    Justification:
    I think this error will never be printed to stderr because an invalid date  leads to event not exist. Hence,
    the output will always be "Multiple errors occur!"
    '''
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            date_error = True
            error_counter += 1

    # Check enough argument
    if len(sys.argv) < 5:
        arg_error = True
        error_counter += 1

    # Check if there are multiple errors happened
    if error_counter == 1:
        if path_error:
            sys.stderr.write("Unable to process calendar database\n")
            sys.exit()
        elif date_error:
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
        elif event_error:
            sys.stderr.write("Unable to update, event does not exist\n")
            sys.exit()
        # This error is when the updated event already existed in the database therefore will create duplicate
        # Print "Multiple errors occur!" because according to the asm spec,
        # error which is not addressed should be printed as "Multiple errors occur!"
        elif updated_error:
            sys.stderr.write("Multiple errors occur!\n")
            sys.exit()
        elif arg_error:
            sys.stderr.write("Not enough arguments given\n")
            sys.exit()
    elif error_counter > 1:
        sys.stderr.write("Multiple errors occur!\n")
        sys.exit()


def del_error_check():
    errorCounter = 0
    path_error = False
    date_error = False
    event_error = False

    # Check the file path
    if path_valid() == "NA":
        path_error = True
        errorCounter += 1

    # Check the date
    if len(sys.argv) >= 3:
        if not date_format_check(sys.argv[2]):
            date_error = True
            errorCounter += 1
    # No date is given
    else:
        date_error = True
        errorCounter += 1

    # Check enough argument
    if len(sys.argv) < 4:
        event_error = True
        errorCounter += 1

    if errorCounter == 1:
        if path_error:
            sys.stderr.write("Unable to process calendar database\n")
            sys.exit()
        elif date_error:
            sys.stderr.write("Unable to parse date\n")
            sys.exit()
        elif event_error:
            sys.stderr.write("Missing event name\n")
            sys.exit()
    elif errorCounter > 1:
        sys.stderr.write("Multiple errors occur!\n")
        sys.exit()


def run():
    if len(sys.argv) < 2:
        # No command type provided
        sys.stderr.write("Multiple errors occur!\n")
        # Terminate
        sys.exit()
    if sys.argv[1].strip() == "GET":
        get()
        sys.exit()
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
    pipe = open(Pipe_Name, "w")

    # Write commands into the pipe file
    try:
        # To store the command
        i = 1
        while i < len(sys.argv):
            if " " in sys.argv[i]:
                pipe.write('"' + sys.argv[i] + '" ')
            else:
                pipe.write(sys.argv[i] + " ")
            i = i + 1
    except OSError:
        sys.stderr.write("Unable to process calendar database\n")

    # Close the file
    pipe.close()


if __name__ == '__main__':
    run()
