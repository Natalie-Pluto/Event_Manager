import os
import sys

# Named pipe within /tmp named cald_pipe
Pipe_Name = "/tmp/cald_pipe"
# Where the path of the database stored
cal_link = "/tmp/calendar_link"

def get():
    db_file = open(cal_link, "r")
    try:
        # Get the path of the database
        db_link = db_file.readline()
        # Test if an index file or the database file exist
        if not os.path.isfile(db_link):
            print(db_link)
            # Print error msg to stderr
            sys.stderr.write("Unable to process calendar database\n")
            # Terminate
            sys.exit()
    except OSError:
        # Print error msg to stderr
        sys.stderr.write("Unable to process calendar database\n")
    db_file.close()


def run():
    pipe = open(Pipe_Name, "a")
    # Write commands into the pipe file
    try:
        # To store the command
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] == "GET":
                get()
            if " " in sys.argv[i]:
                pipe.write('"' + sys.argv[i] + '" ')
            else:
                pipe.write(sys.argv[i] + "  ")
            i = i + 1
    except OSError:
        sys.stderr.write("Unable to process calendar database\n")

    # Close the file
    pipe.close()


if __name__ == '__main__':
    run()

