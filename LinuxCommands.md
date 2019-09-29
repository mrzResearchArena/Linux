# Linux Handling
&nbsp;

### 1. System Update and Upgrade
```console
user@machine:~$ sudo apt update                           # Update
user@machine:~$ sudo apt upgrade                          # Upgrade
user@machine:~$ sudo apt update && sudo apt upgrade       # Update and Upgrade Together
```

&nbsp;

### 2. How to reduce terminal text? / Customizing BASH Prompt Text
```console
user@mrz:~$ PS1='[\u@\h \W]\$ '                       # Small
user@mrz:~$ PS1='[@ \W]\$ '                           # Extra Small
```

&nbsp;

### 3. Program Killing Procedure
#### Step 1: Show the Running Program
```console
user@mrz:~$ top           
# Example: PID (3288), USER (rafsanjani), and COMMAND (firefox)
```

#### Step 2: Kill Program
```console
user@mrz:~$ kill 3288             # Kill a particular program
# Example: Here, 3288 is the process identity (PID), Then the program (3288) will halt.

rafsanjani@mrz:~$ kill -9 -1            # Kill all the program
```
&nbsp;

### 4. Display Files and Directories

#### Step 1: Display all file names
```console
user@mrz:~$ ls  <!-- -->        # View all visible file and directory
user@mrz:~$ ls -1               # View in a single-line
user@mrz:~$ ls -a               # View everyting includes ( ., .., .anyName )
user@mrz:~$ ls -A               # View everyting except ( ., .. )
user@mrz:~$ ls -l               # View all visible with their details and long list formating ( l ) 
user@mrz:~$ ls -lh              # View all visible with their details and human readable file size ( h ) 
user@mrz:~$ ls -d */            # View only directories
user@mrz:~$ ls  anyDirectory    # View all visible file and directory for anyDirectory
```

#### Step 2: Display last five modified files with their details
```console
user@mrz:~$ ls -tlh | head -6        # sort by last modification of time ( t )
```

#### Step 3: Display particular file in current dicrectory (`without grep and egrep`)
```console
user@mrz:~$ ls *.fasta               # View all .fasta extension files
user@mrz:~$ ls *.fasta | wc -l       # View the total number of .fasta extension files
```

#### Step 4: Display particular file in current dicrectory
```console
user@mrz:~$ ls | grep '.fasta'               # View all files that ends with .fasta extension  
user@mrz:~$ ls | egrep '.fasta$'             # View all files that ends with .fasta extension  
user@mrz:~$ ls | egrep '*.fa$|*.fasta$'      # View all files that ends with both .fasta and .fa extension  
```

&nbsp;

### 5. String Handling
#### Step 1: Replace text segment (using sed)
```console
user@mrz:~$ sed 's/oldText/newText/' fileName.txt        # Change the text segment without replacement) 
user@mrz:~$ sed -i 's/oldText/newText/' fileName.txt     # Change the text segment with replacement) 
```
#### Step 2: Replace text segment (using [tr](https://www.youtube.com/watch?v=i0Q8LRSiUZ4))
```console
user@mrz:~$ cat fileName.txt | tr '!' '.'                # tr must use as a pipeline
```

&nbsp;

### 6. Regular Expression
#### Step 1: Search a keyword from a file
```console
user@mrz:~$ grep 'keyword' fileName.txt
user@mrz:~$ cat fileName.txt | grep 'keyword'
```

#### Step 2: Count the number of fasta sequence from a file (.fasta)
```console
user@mrz:~$ grep '>' fileName.fasta | wc -l              # Number of lines denotes by ( l )
```

#### Step 3: Gmail Pattern
```console
user@machine:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | tr '-d' '.' | egrep '[a-zA-Z0-9]{7,29}' 

user@machine:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | egrep '[a-zA-Z0-9.]{7,29}' 
```

&nbsp;

### 7. TTY Mode
```console
user@mrz:~$ sudo chvt 7                        # Try 1, 2, 3, ... 7

or, we can use shortcut key: control + alter + F7    # Try F1, F2, F3, ... F7
```


&nbsp;
&nbsp;



**Note:** The step doesn't mean you have to follow one by one.
