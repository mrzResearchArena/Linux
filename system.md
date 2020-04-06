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
