
# Linux Handling

&nbsp;

## 1. System Update and Upgrade
#### Step 1: Update
```console
rafsanjani@mrz:~$ sudo apt update 
```

#### Step 2: Upgrade
```console
rafsanjani@mrz:~$ sudo apt upgrade 
```

#### Step 3: Update and Upgrade Together
```console
rafsanjani@mrz:~$ sudo apt update && sudo apt upgrade 
```

&nbsp;

## 2. Kill Process (Programme)
#### Step 1: Show the Running Process
```console
rafsanjani@mrz:~$ top
[Example: PID (3288), USER (rafsanjani), COMMAND (firefox)]
```
#### Step 2: Kill a Process
```console
rafsanjani@mrz:~$ kill <PID> 
[kill 3288; The firefox programme will stop.]
```
#### Step 3: Kill All the Process
```console
rafsanjani@mrz:~$ kill -9 -1 
```
&nbsp;

## 3. Display Files
#### Step 1: Display all file names
```console
rafsanjani@mrz:~$ ls 
rafsanjani@mrz:~$ ls -1     # View in a single-line
rafsanjani@mrz:~$ ls -a     # View everyting includes ( ., .., .git )
rafsanjani@mrz:~$ ls -A     # View everyting except ( ., .. )
```
#### Step 2: Display all file names with details
```console
rafsanjani@mrz:~$ ls -ltrh 
```
#### Step 3: Display last (5) modified files with their details
```console
rafsanjani@mrz:~$ ls -tlh | head -6        # t (sort by last modification time), l (long list), and h (human readable)
```

&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
