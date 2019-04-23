# Linux Handling
&nbsp;

## 1. System Update and Upgrade
#### Step 1: 
```console
rafsanjani@mrz:~$ sudo apt update                           # Update
rafsanjani@mrz:~$ sudo apt upgrade                          # Upgrade
rafsanjani@mrz:~$ sudo apt update && sudo apt upgrade       # Update and Upgrade Together
```
&nbsp;

## 2. Kill Program Procedure
#### Step 1: Show the Running Program
```console
rafsanjani@mrz:~$ top           
# Example: PID (3288), USER (rafsanjani), and COMMAND (firefox)
```

#### Step 2: Kill Program
```console
rafsanjani@mrz:~$ kill 3288             # Kill a particular program
# Example: Here, 3288 is the process identity (PID), Then the program (3288) will halt.

rafsanjani@mrz:~$ kill -9 -1            # Kill all the program
```

&nbsp;
## 3. Display Files
#### Step 1: Display all file names
```console
rafsanjani@mrz:~$ ls 
rafsanjani@mrz:~$ ls -1              # View in a single-line
rafsanjani@mrz:~$ ls -a              # View everyting includes ( ., .., .git )
rafsanjani@mrz:~$ ls -A              # View everyting except ( ., .. )
rafsanjani@mrz:~$ ls -l              # View all visible with their details and long list formating ( l ) 
rafsanjani@mrz:~$ ls -lh             # View all visible with their details and human readable file size ( h ) 
rafsanjani@mrz:~$ ls -d */           # View only directories
```
#### Step 2: Display last (5) modified files with their details
```console
rafsanjani@mrz:~$ ls -tlh | head -6        # t (sort by last modification time)
```

&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
