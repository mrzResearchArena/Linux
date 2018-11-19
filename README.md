# Access Remote Server

### Step #1: Current status of the running socket(s)
```console
rafsanjani@mrz:~$ screen -list
```

### Step #2: Generate a socket
```console
rafsanjani@mrz:~$ screen -S socketName
```


### Step #3: Detach screen (without killing the socket)
```console
rafsanjani@mrz:~$ control + A + D 
```

### Step #4: Resume the socket after detach
```console
rafsanjani@mrz:~$ screen -r socketName
```

### Step #5: Remove a socket
```console
rafsanjani@mrz:~$ screen -X -S socketName quit
```


