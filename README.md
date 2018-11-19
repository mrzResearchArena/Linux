## Access Remote Server

### How does screen work?

#### Step #1: Current status of the running socket(s)
```console
rafsanjani@mrz:~$ screen -list
```
&nbsp;
![None](1.png)

&nbsp;
![Running](2.png)



#### Step #2: Generate a socket
```console
rafsanjani@mrz:~$ screen -S socketName
```


#### Step #3: Detach screen (without killing the socket)
```console
rafsanjani@mrz:~$ control + A + D 
```

#### Step 4: Resume the socket after detach
```console
rafsanjani@mrz:~$ screen -r socketName
```

#### Step 5: Remove a socket
```console
rafsanjani@mrz:~$ screen -X -S socketName quit
```

**Note:** The step doesn't mean you have to follow one by one.


### Cory a file/directory from local machine to remote machine

```console
rafsanjani@mrz:~$ scp <source> <destination>
```

#### Example 1:
```console
rafsanjani@mrz:~$ scp /home/rafsanjani/fileName.csv learning@150.78.20.89:/home/learning/mrzResearchArena
```


