
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

## 1. Kill Process/Programme
#### Step 1: Show the running process/programme
```console
rafsanjani@mrz:~$ top
[Example: PID (3288), USER (mrz), COMMAND (firefox)]
```
#### Step 2: Kill a process/programme
```console
rafsanjani@mrz:~$ kill <PID> (kill 3288; the the firefox programme will stop.)
```
#### Step 3: Kill all the process/programme
```console
rafsanjani@mrz:~$ kill -9 -1
```

&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
