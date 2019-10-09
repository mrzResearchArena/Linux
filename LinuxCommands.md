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
user@machine:~$ PS1='[\u@\h \W]\$ '                       # Small
user@machine:~$ PS1='[@ \W]\$ '                           # Extra Small
```

&nbsp;

### 3. Program Killing Procedure
#### Step 1: Show the all running program
```console
user@machine:~$ top
# Example: PID (3288), USER (rafsanjani), and COMMAND (firefox)
```

#### Step 2: Kill program(s)
```console
user@machine:~$ kill 3288             # Kill a particular program
# Example: Here, 3288 is the process identity (PID), Then the program (3288) will halt.

user@machine:~$ kill -9 -1            # Kill all the program
```
&nbsp;

### 4. Display Files and Directories

#### Step 1: Display all file names
```console
user@machine:~$ ls  <!-- -->        # View all visible file and directory
user@machine:~$ ls -1               # View in a single-line
user@machine:~$ ls -a               # View everyting includes ( ., .., .anyName )
user@machine:~$ ls -A               # View everyting except ( ., .. )
user@machine:~$ ls -l               # View all visible with their details and long list formating ( l ) 
user@machine:~$ ls -lh              # View all visible with their details and human readable file size ( h ) 
user@machine:~$ ls -d */            # View only directories
user@machine:~$ ls  anyDirectory    # View all visible file and directory for anyDirectory
```

#### Step 2: Display last five modified files with their details
```console
user@machine:~$ ls -tlh | head -6        # sort by last modification of time ( t )
```

#### Step 3: Display particular file in current dicrectory (`without grep and grep -E`)
```console
user@machine:~$ ls *.fasta                 # View all .fasta extension files
user@machine:~$ ls *.fasta | wc -l         # View the total number of .fasta extension files
user@machine:~$ ls -1 *.fasta | sort -n   # View all .fasta extension files in increasing order
```

#### Step 4: Display particular file in current dicrectory
```console
user@machine:~$ ls | grep '.fasta'                   # View all files that ends with .fasta extension  
user@machine:~$ ls | grep -E '\.fasta$'              # View all files that ends with .fasta extension  
user@machine:~$ ls | grep -E '*\.fa$|*\.fasta$'      # View all files that ends with both .fasta and .fa extension
user@machine:~$ ls -1 | grep -E '*\.fasta$'| wc -l   # Find all .fasta files from a location

# -E, is for the regular expression.
```

#### Step 5: Find the expected files
```console
user@machine:~$ find /home/mrz/Desktop/Bk/MakeDB -name '*.pssm'  # View all files that ends with .fasta extension  
```


&nbsp;

### 5. String Handling
#### Step 1: Replace text segment (using sed)
```console
user@machine:~$ sed 's/oldText/newText/' fileName.txt        # Change the text segment without replacement) 
user@machine:~$ sed -i 's/oldText/newText/' fileName.txt     # Change the text segment with replacement) 
```
#### Step 2: Replace text segment (using [tr](https://www.youtube.com/watch?v=i0Q8LRSiUZ4))
```console
user@machine:~$ cat fileName.txt | tr '!' '.'                # tr must use as a pipeline
```

&nbsp;

### 6. Regular Expression
#### Step 1: Search a keyword from a file
```console
user@machine:~$ grep 'keyword' fileName.txt
user@machine:~$ cat fileName.txt | grep 'keyword'
```

#### Step 2: Count the number of fasta sequence from a file (.fasta)
```console
user@machine:~$ grep '>' fileName.fasta | wc -l              # Number of lines denotes by ( l )
```

#### Step 3: Gmail Pattern
```console
user@machine:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | tr '-d' '.' | egrep '[a-zA-Z0-9]{7,29}' 
user@machine:~$ echo '1hj..bjb....bjh..b@gmail.com'| egrep '@gmail.com$' | egrep '^[a-zA-Z]' | sed 's/@gmail.com//' | egrep '[a-zA-Z0-9.]{7,29}' 
```

&nbsp;

### 7. Download file from the website 
#### 7.1 Download Files from the FTP Server 
```console
user@machine:~$ wget 'ftp://ftp.ncbi.nlm.nih.gov/blast/db/nr.*.tar.gz'   # Download `nr` dataset from the NCBI website   
```

&nbsp;

### 8. TTY Mode
```console
user@machine:~$ sudo chvt 7                            # Try 1, 2, 3, ... 7 

# or, we can use shortcut key: control + alter + F7    # Try F1, F2, F3, ... F7 
```

&nbsp;

### 8. Compress/Uncompress the File and Directory
#### 8.1 Compress/Uncompress file using `gzip`
```console
user@machine:~$ gzip   anyName.fasta                   # anyName.fasta    --> anyName.fasta.gz
user@machine:~$ gunzip anyName.fasta.gz                # anyName.fasta.gz --> anyName.fasta      # gzip -d anyName.fasta.gz

user@machine:~$ gzip   *.fasta                         # *.fasta          --> *.fasta.gz
user@machine:~$ gunzip *.fasta.gz                      # *.fasta.gz       --> *.fasta            # gzip -d *.fasta.gz
```

#### 8.2 Compress/Uncompress file using `bzip2`
```console
user@machine:~$ bzip2   anyName.fasta                  # anyName.fasta      --> anyName.fasta.bz2
user@machine:~$ bunzip2 anyName.fasta.bz2              # anyName.fasta.bz2  --> anyName.fasta     # bzip2 -d anyName.fasta.bz2

user@machine:~$ bzip2   *.fasta                        # *.fasta            --> *.fasta.bz2
user@machine:~$ bunzip2 *.fasta.bz2                    # *.fasta.bz2        --> *.fasta           # bzip2 -d *.fasta.bz2
```

#### 8.3 Compress/Uncompress Directory
##### 8.3.1 Compress Directory
```console
user@machine:~$ tar -cvf anyName.tar *.fasta           # -c, is for create a .tar file
user@machine:~$ gzip anyName.tar                       # Or, bzip2 anyName.tar
```

##### 8.3.2 Uncompress Directory
```console
user@machine:~$ gunzip anyName.tar.gz                   # Or, bunzip2 anyName.tar.bz2
user@machine:~$ tar -xvf anyName.tar                    # -x, is for extract the .tar file

# Suggestion: Use graphical mode for the directory uncompression, if the directory is small-sized.
```

**Note:** gunzip, is also gzip -d, and bzip2, is als

&nbsp;
&nbsp;


**Note:** The step doesn't mean you have to follow one by one.
