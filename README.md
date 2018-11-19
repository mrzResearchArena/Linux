## Access Remote Server

## 1. How does screen work?

#### Step 1: Current status of the running socket(s)
```console
rafsanjani@mrz:~$ screen -list
```

#### Step 2: Generate a socket
```console
rafsanjani@mrz:~$ screen -S anySocketName
```

#### Step 3: Detach screen without killing the socket
```console
rafsanjani@mrz:~$ control + A + D 
```

#### Step 4: Resume the socket after detach
```console
rafsanjani@mrz:~$ screen -r anySocketName
```

#### Step 5: Kill a socket
```console
rafsanjani@mrz:~$ screen -S anySocketName  `-X quit`
```

&nbsp;

## 2. How to copy a file/directory from local machine to remote machine?

```console
rafsanjani@mrz:~$ scp  <source>  <destination>
```
***Note:*** `15.78.20.89` and `learning` are the IP address and user name of remote machine respectively.

#### Step 1: Copy a file 
```console
rafsanjani@mrz:~$ scp /home/rafsanjani/anyFile.csv learning@150.78.20.89:/home/learning/mrzResearchArena
```

#### Step 2: Copy a directory
```console
rafsanjani@mrz:~$ scp -r /home/rafsanjani/anyDirectory learning@150.78.20.89:/home/learning/mrzResearchArena
```
&nbsp;

## 3. How to check machine configuration?

#### Step 1: RAM Status
```console
rafsanjani@mrz:~$ free -h
```

#### Step 2: Processor Model
```console
rafsanjani@mrz:~$ cat /proc/cpuinfo | grep 'model name'
```

#### Step 3: Information about OS
```console
rafsanjani@mrz:~$ uname -a
```

**Note:** The step doesn't mean you have to follow one by one.
