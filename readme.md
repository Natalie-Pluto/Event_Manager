# **Calendar**

This readme file will give explanations and instructions on the tests and scripts.

## **Test**

-------------

### **Daemon Test**

Inside the DaemonTest directory, there are directories for different tests. Inside each one of these directories, 
there are two bash scripts and one csv file. One bash script is for running the daemon.py in the background
and the other one is for writing commands into pipe file. The csv file is for testing which contents the expected data. 
Once Daemon.py is terminated,the bash script will compare the csv files created by Daemon.py with the test csv file, 
printing 'PASSED' for passing this test or 'FAILED' for failing this test.

Brief explanations of individual tests (Detailed explanations are made as comments in the script file):

1. `Daemon_add1` 

This test will test on the add commands which does not contain double quotation marks.

2. `Daemon_add2`

This test will test on the add commands which contains double quotation marks

3. ` Daemon_add3`

This test will test on the add commands which contains commas in the description/ event string

4. `Daemon_add4`

This test will test on the error cases for add commands:

*  Date provided not valid

*  No event name provided

*  Duplicate event

5. `Daemon_upd1`

This test will test on the update command which does not contain double quotation marks.
This test will also test on the case when the event to be updated has a description in 
database, but the update command does not provide the description (Therefore the description should be removed after update)

6. `Daemon_upd2`

This test will test on the update command which contains double quotation marks.
All possible format with double quotation marks are tested

7. `Daemon_upd3`

This test will test on the update command which contains commas

8. `Daemon_upd4`

This test will test on the error cases for add commands:

*  Date provided not valid

*  Not enough argument

*  Event not exist

*  Duplicate event

9. `Daemon_del1`

This test will test on the delete command which does not contain double quotation marks

10. `Daemon_del2`

This test will test on the delete command which contains double quotation marks and/or comma

11. `Daemon_del3`

This test will test on the error cases for delete command:

*  Date provided not valid

*  Not enough argument

*  Event not exist (No output)

12. `Daemon_Path`

This test will test on the command line argument - provide name and path of the database

13. `Daemon_defaultPath`

This test will test on the command line argument - provide path of the database but not provide the name. 
The default csv file name will be used -> cald_db.csv

14. `Daemon_noArg`

This test will test on the command line argument - No command line argument provided.
The default csv file name be used -> cald_db.csv and the path will be as the same as the daemon.py



### **Calendar Test**

Inside the CalendarTest directory, there are directories for different tests. Inside each one of these directories, 
there are two bash scripts and one csv file. One bash script is for running the daemon.py in the background
and the other one is for writing commands into pipe file via calendar.py. The csv file is for testing which contents the expected data. 
Once Daemon.py is terminated,the bash script will compare the csv file created by the test with this csv file, 
printing 'PASSED' for passing this test or 'FAILED' for failing this test.

Brief explanations of individual tests (Detailed explanations are made as comments in the script file):

1. `Calendar_arg`

This test will test on the if no arg or wrong command type provided.

2. `Calendar_add`

This test will test on the error msg produced by add commands
* Date error
* Event name not provided
* Multiple error
* Unable to process calendar database

3. `Calendar_del`

This test will test on the error msg produced by delete commands
* Date error
* Event name missing
* Multiple error
* Unable to process calendar database

4. `Calendar_upd`

This test will test on the error msg produced by update commands
* Date error
* Event not exist
* Multiple error
* Unable to process calendar database
* Event exist
* Not enough argument

5. `Calendar_get1`

This test will test on the get command - date action option

6. `Calendar_get2`

This test will test on the get command - date action option with multiple args

7. `Calendar_get3`

This test will test on the error msg produced by GET DATE commands
* Date error
* Unable to process calendar database

8. `Calendar_get4`

This test will test on the get command - interval action option

9. `Calendar_get5`

This test will test on the error msg produced by GET INTERVAL commands
* Date error
* Start date is after End date
* Unable to process calendar database
* Not enough arguments given

10. `Calendar_get6`

This test will test on the get command - NAME action option

11. `Calendar_get7`

This test will test on the get command - NAME action option - multiple args

12. `Calendar_get8`

This test will test on the error msg produced by GET NAME commands
* Unable to process calendar database
* Missing arguments 
* Not exist event name (no output)


### **How to Execute Tests**

1. Change access permission:

`chmod +rwx <script_file>`

2. Run the scripts:

Run the script which run the Daemon.py first in background (It is the one which has the same name with the
directory name):

`./<script_file> &`

then run the script which write commands to pipe file:

`./<script_file>`

Output:

If passed:
```
./Daemon_add1.sh: line 6: 79430 Terminated: 15          python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add1/add1.csv
PASSED
[1]+  Done                    ./Daemon_add1.sh`
```

If failed:
```
./Daemon_add1.sh: line 6: 79506 Terminated: 15          python3 /Users/natalielu/Desktop/INFO1112/Asm2/cald/daemon.py /Users/natalielu/Desktop/INFO1112/Asm2/cald/DaemonTest/Daemon_add1/add1.csv
FAILED
[1]+  Done                    ./Daemon_add1.sh
```
