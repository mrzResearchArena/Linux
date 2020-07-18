# System Control

&nbsp;

#### 1. Check Internet Speed
```console
user@machine:~$ speedtest-cli    # Install: pip install speedtest-cli
```

#### 2. Find the MAC Address
```console
user@machine:~$ ifconfig | grep 'HWaddr' 

# Go to router icon --> Connection Information --> General
```

#### 3. Fixed the Compiz Configure Issue
```console
user@machine:~$ dconf reset -f /org/compiz
user@machine:~$ setsid unity  # (If doesn't work: sudo apt install unity.)
user@machine:~$ unity --reset-icons
```

#### 4. Create a New User and Remove the Root Privilege
```console
user@machine:~$ 
user@machine:~$ 
user@machine:~$ 
user@machine:~$ sudo gpasswd -d bioHub sudo   ### Remove the Root Privilege
```
**References:
**1. Create a sudo user [[web](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)]
**2. Remove the root prililege [[web](https://askubuntu.com/questions/335987/remove-sudo-privileges-from-a-user-without-deleting-the-user)]



