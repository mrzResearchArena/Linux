# Linux Server Handling

&nbsp;

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
rafsanjani@mrz:~$ screen -S anySocketName -X quit
```

&nbsp;

## 2. How to copy a file/directory from local machine to remote machine?

```console
rafsanjani@mrz:~$ scp  <source>  <destination>
```
***Note:*** `150.78.20.89` and `learning` are the IP address and user name of remote machine respectively.

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

&nbsp;

## 4. How to check GPU configuration?

#### Step 1: Ensure GPU Existence
```console
rafsanjani@mrz:~$ nvidia-smi
```
#### Step 2: Ensure CUDA Existence
```console
rafsanjani@mrz:~$ nvcc --version
```
#### Step 3: Ensure by run a simple programme (PyTorch)
```console
rafsanjani@mrz:~$ python
>>> import torch
>>> torch.cuda.is_available()
Output: True (available) / False (NOT available)
```

&nbsp;

## 5. How to create an anaconda virtual environment?

#### Step 1: Create a virtual environment ####
```console
rafsanjani@mrz:~$ conda create -n anyName python=3.x anaconda
```

#### Step 2: Entering the virtual environment ####
```console
rafsanjani@mrz:~$ source activate anyName
```

#### Step 3: Detach from the virtual environment ####
```console
rafsanjani@mrz:~$ source deactivate
```

&nbsp;

## 6. Tricks for anaconda virtual environment?

#### Step 1: Remove an user from virtual environment ####
```console
rafsanjani@mrz:~$ conda env remove --name anyName
```
&nbsp;

## 7. Space Optimization!

#### Step 1: Uninstall all unused packages from virtual environment ####
```console
rafsanjani@mrz:~$ conda clean --yes --all
```

#### Step 2: Clean Trash ####
```console
rafsanjani@mrz:~$ rm -rf ~/.local/share/Trash/* 
```

#### Step 3: OS Auto Clean ####
```console
rafsanjani@mrz:~$ sudo apt autoremove

rafsanjani@mrz:~$ sudo apt autoclean
```


&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
