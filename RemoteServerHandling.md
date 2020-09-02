# Linux Server Handling

&nbsp;

### 1. How to check machine configuration?

- #### Step 1: Information about OS
```console
user@machine:~$ uname -a              # All informatics about OS
# Output: Linux rafsanjani 4.15.0-65-generic #74~16.04.1-Ubuntu SMP Wed Sep 18 09:51:44 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

user@machine:~$ uname -r              # Kernel Release      --> 4.15.0-65-generic
user@machine:~$ uname -v              # Kernel Version      --> #74~16.04.1-Ubuntu
user@machine:~$ arch                  # Kernel Architecture --> x86_64 (64 bits)
user@machine:~$ lsb_release -a        # Distributor ID: Ubuntu, Description: Ubuntu 18.04.3 LTS, Release: 18.04, Codename: bionic
user@machine:~$ cat /etc/os-release   # Another way!
```

- #### Step 2: Processor Model:
```console
user@machine:~$ lscpu | grep 'Model name'              # Output: Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz
user@machine:~$ cat /proc/cpuinfo | grep 'model name'  # Output: Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz
```

- #### Step 3: RAM Status
```console
user@machine:~$ free -h                        # RAM capacity
user@machine:~$ sudo dmidecode --type 17       # RAM information
user@machine:~$ nproc                          # RAM Core
```

- #### Step 4: HDD (Hard Disk Drive) Status

  - ##### Step 4.1: Working Drive (Dual Boot Mode OS)
  ```console
  user@machine:~$ df -h                            # Show disk usage

  user@machine:~$ du -h --max-depth=1 /home/user   # Show the directory space usage for the particular location.
  user@machine:~$ du -h -s /home/user              # -s, is for the summarizing the given location size.
  ```

  - ##### Step 4.2: Whole HDD Information (Identifying the Partition Type)
  ```console
  user@machine:~$ sudo fdisk -l
  ```

&nbsp;

### 2. Ubuntu Installation for Deep Learning 
- #### Step 1: Fulll Setup [ [by clicking here!](https://lambdalabs.com/lambda-stack-deep-learning-software) ]
- #### Seep 2: GPU Setup [ [by clicking here!](https://github.com/mrzResearchArena/Linux-Documentation/blob/master/installGPU.sh) ]

&nbsp;

### 3. How to check GPU configuration?

- #### Step 1: Ensure GPU Existence
```console
rafsanjani@mrz:~$ nvidia-smi
```
- #### Step 2: Ensure CUDA Existence
```console
rafsanjani@mrz:~$ nvcc --version
```
- #### Step 3: Ensure by run a simple programme (PyTorch/Tensorflow):
  - [PyTorch](https://github.com/mrzResearchArena/Linux/blob/master/check-PyTorch-GPU-existance.py)
  - [Tensorflow-2.x](https://github.com/mrzResearchArena/Linux/blob/master/check-TF-GPU-existance.py)

- #### Step 4: GPU Memory Allocation:
  - [Allocate GPU Memory](https://github.com/mrzResearchArena/Linux/blob/master/allocateGPU.py)



&nbsp;

### 4. How does the screen work?

- #### Step 1: Current Status of the Running Socket(s)
```console
rafsanjani@mrz:~$ screen -list   # screen -ls
```

- #### Step 2: Generate a Socket
```console
rafsanjani@mrz:~$ screen -S anySocketName
```

- #### Step 3: Detach Screen without Killing the Socket
```console
rafsanjani@mrz:~$ control + A + D        # The shortcut for the logout.
```

- #### Step 4: Resume the Socket after Detach
```console
rafsanjani@mrz:~$ screen -r anySocketName
```

- #### Step 5: Kill a Socket
```console
rafsanjani@mrz:~$ screen -S anySocketName -X quit
```

- #### Step 6: Kill All Screen
```console
rafsanjani@mrz:~$ killall screen
```

- #### Step 7: Remove Dead Screen
```console
rafsanjani@mrz:~$ screen -wipe
```

- #### Step 8: Know the Current Socket Name
```console
rafsanjani@mrz:~$ echo $STY
```

&nbsp;

### 5. How to copy a file/directory from local machine to remote machine?

```console
rafsanjani@mrz:~$ scp  <source>  <destination>
```
***Note:*** `150.78.20.89` and `learning` are the IP address and user name of remote machine respectively.

- #### Step 1: Copy a file 
```console
rafsanjani@mrz:~$ scp /home/rafsanjani/anyFile.csv learning@150.78.20.89:/home/learning/mrzResearchArena
```

- #### Step 2: Copy a directory
```console
rafsanjani@mrz:~$ scp -r /home/rafsanjani/anyDirectory learning@150.78.20.89:/home/learning/mrzResearchArena
```
- #### Step 3: How to copy all files to HDD?
```console
user@machine:~$ cp -rf /home/user/ /media/user/BACKUP
```
&nbsp;

### 6. How to access jupyter notebook remotely?

- #### Step 1: Run on a remote machine ####
```console
learning@150.78.20.89:~$ jupyter-notebook --no-browser --port=8889 
```
***Note:*** By running, you will recieve a token from remote machine (or, server). 

Exmaple: http://localhost:8889/?token=05f9832e3a503c9cab5f89b28e8c6e25b74ce61e2fc8ddzz

&nbsp;

- #### Step 2: Run on a local machine ####
```console
rafsanjani@mrz:~$ ssh -N -f -L localhost:8888:localhost:8889 learning@150.78.20.89
```
***Note:*** `150.78.20.89` and `learning` are the IP address and user name of remote machine respectively.

&nbsp;

- #### Step 3: Go to the local machine's web browser and type the below URL! ####
```console
localhost:8888/tree
```

- #### Step 4: Graphical Interface ####

&nbsp;

![Jupyter Remotely](https://github.com/mrzResearchArena/Linux-Documentation/blob/master/jupyternotebook.png)

***Figure:*** A simple three-step process for running a remote Jupyter notebook.

##### Learning Resource-1 [ [by clicking here!](https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/) ]
##### Learning Resource-2 [ [by clicking here!](https://amber-md.github.io/pytraj/latest/tutorials/remote_jupyter_notebook/) ]

&nbsp;

### 7. Space Optimization:

- #### Step 1: Uninstall all unused packages from virtual environment ####
```console
rafsanjani@mrz:~$ conda clean --yes --all
```

- #### Step 2: Clean Trash ####
```console
rafsanjani@mrz:~$ rm -rf ~/.local/share/Trash/* 
```

- #### Step 3: Auto Remove and Auto Clean ####
```console
rafsanjani@mrz:~$ sudo apt autoremove && sudo apt autoclean 
```

&nbsp;

### 8. Keep Remote SSH Alive / Increase SSH Connection Timeout / Prevent Remote SSH Disconnect:

- #### Step 1: Configure
```console
user@machine:~$ sudo vi /etc/ssh/sshd_config
```

- #### Step 2: Set the Value
```
ClientAliveInterval  21600   # 6h --> (3600 x 6) seconds.
```

- #### Step 3: Reload the SSH
```console
user@machine:~$ sudo systemctl reload sshd
```

- **References:** https://www.tecmint.com/increase-ssh-connection-timeout/
