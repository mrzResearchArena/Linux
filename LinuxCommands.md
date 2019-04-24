# Linux Handling
&nbsp;

## 1. System Update and Upgrade
```console
rafsanjani@mrz:~$ sudo apt update                           # Update
rafsanjani@mrz:~$ sudo apt upgrade                          # Upgrade
rafsanjani@mrz:~$ sudo apt update && sudo apt upgrade       # Update and Upgrade Together
```
&nbsp;


## 2. Kill Program Procedure
#### Step 1: Show the Running Program
```console
rafsanjani@mrz:~$ top           
# Example: PID (3288), USER (rafsanjani), and COMMAND (firefox)
```

#### Step 2: Kill Program
```console
rafsanjani@mrz:~$ kill 3288             # Kill a particular program
# Example: Here, 3288 is the process identity (PID), Then the program (3288) will halt.

rafsanjani@mrz:~$ kill -9 -1            # Kill all the program
```

&nbsp;
## 3. Display Files and Directories

#### Step 1: Display all file names
```console
rafsanjani@mrz:~$ ls  <!-- -->        # View all visible file and directory
rafsanjani@mrz:~$ ls -1               # View in a single-line
rafsanjani@mrz:~$ ls -a               # View everyting includes ( ., .., .anyName )
rafsanjani@mrz:~$ ls -A               # View everyting except ( ., .. )
rafsanjani@mrz:~$ ls -l               # View all visible with their details and long list formating ( l ) 
rafsanjani@mrz:~$ ls -lh              # View all visible with their details and human readable file size ( h ) 
rafsanjani@mrz:~$ ls -d */            # View only directories
rafsanjani@mrz:~$ ls  anyDirectory    # View all visible file and directory for anyDirectory
```

#### Step 2: Display last (5) modified files with their details
```console
rafsanjani@mrz:~$ ls -tlh | head -6        # sort by last modification of time ( t )
```

#### Step 3: Display particular file in current dicrectory (`without grep and egrep`)
```console
rafsanjani@mrz:~$ ls *.fasta              # View all .fasta extension files
```

#### Step 4: Display particular file in current dicrectory
```console
rafsanjani@mrz:~$ ls | grep '.fasta'               # View all files that ends with .fasta extension  
rafsanjani@mrz:~$ ls | egrep '.fasta$'             # View all files that ends with .fasta extension  
rafsanjani@mrz:~$ ls | egrep '*.fa$|*.fasta$'      # View all files that ends with both .fasta and .fa extension  
```


&nbsp;


## 5. String Handling
#### Step 1: Replace text segment (using sed)
```console
rafsanjani@mrz:~$ sed 's/oldText/newText/' fileName.txt        (Change the text segment without replacement)
rafsanjani@mrz:~$ sed -i 's/oldText/newText/' fileName.txt     (Change the text segment with replacement)
```
#### Step 2: Replace text segment (using [tr](https://www.youtube.com/watch?v=i0Q8LRSiUZ4))
```console
rafsanjani@mrz:~$ cat fileName.txt | tr '!' '.'                (Must use as a pipeline)
```

#### Step 3: Gmail Pattern
```console
rafsanjani@mrz:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | tr '-d' '.' | egrep '[a-zA-Z0-9]{7,29}' 

rafsanjani@mrz:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | egrep '[a-zA-Z0-9.]{7,29}' 

```

&nbsp;



## 4. Regular Expression
#### Step 1: Search a keyword from a file
```console
rafsanjani@mrz:~$ grep 'keyword' fileName.txt
rafsanjani@mrz:~$ cat fileName.txt | grep 'keyword'
```

#### Step 2: Count the number of fasta sequence from a file (.fasta)
```console
rafsanjani@mrz:~$ grep '>' fileName.fasta | wc -l 
```

&nbsp;


&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
