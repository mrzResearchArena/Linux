# System Control

&nbsp;

### 1. Check Internet Speed
```console
user@machine:~$ speedtest-cli    # Install: pip install speedtest-cli
```

&nbsp;

### 2. How to reduce terminal text? / Customizing BASH Prompt Text
```console
user@machine:~$ PS1='[\u@\h \W]\$ '                       # Small
user@machine:~$ PS1='[@ \W]\$ '                           # Extra Small
```

&nbsp;

### 3. Find the MAC Address
```console
user@machine:~$ ifconfig | grep 'HWaddr' 

# Go to router icon --> Connection Information --> General
```

&nbsp;

### 4. Fixed the Compiz Configure Issue
```console
user@machine:~$ dconf reset -f /org/compiz
user@machine:~$ setsid unity  # (If doesn't work: sudo apt install unity.)
user@machine:~$ unity --reset-icons
```

&nbsp;

### 5. TTY Mode
```console
user@machine:~$ sudo chvt 7                            # Try 1, 2, 3, ... 7 

# or, we can use shortcut key: control + alter + F7    # Try F1, F2, F3, ... F7 
```

&nbsp;

### 6. Create a New User and Remove the Root Privilege
```console
user@machine:~$ sudo adduser anyName           ### Add a New User
user@machine:~$ sudo usermod -aG sudo anyName  ### Add the Root Privilege
user@machine:~$ sudo gpasswd -d anyName sudo   ### Remove the Root Privilege
```

- #### References:
1. Create a SUDO User ([web](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart))
2. Remove the Root Privilege-1 ([web](https://askubuntu.com/questions/335987/remove-sudo-privileges-from-a-user-without-deleting-the-user))
3. Remove the Root Privilege-2 ([web](https://www.liquidweb.com/kb/remove-delete-user-ubuntu-16-04/))
4. Create User and Remove the Root Privilege ([web](https://www.ostechnix.com/how-to-grant-and-remove-sudo-privileges-to-users-on-ubuntu/))
5. Restore the Root Privilege ([web](https://www.ostechnix.com/how-to-restore-sudo-privileges-to-a-user/))
