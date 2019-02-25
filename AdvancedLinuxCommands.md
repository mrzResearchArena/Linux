# Linux Handling

&nbsp;

## 1. How to reduce terminal text? / Customizing BASH Prompt Text
```console
rafsanjani@mrz:~$ PS1='[\u@\h \W]\$ '       (Small)
rafsanjani@mrz:~$ PS1='[@ \W]\$ '           (Extra Small)
```
&nbsp;

## 2. Regular Expression
#### Step 1: Search a keyword from a file
```console
rafsanjani@mrz:~$ grep 'keyword' fileName.txt
rafsanjani@mrz:~$ cat fileName.txt | grep 'keyword'
```

#### Step 2: Count the number of fasta sequence from a file (.fasta)
```console
rafsanjani@mrz:~$ grep '>' fileName.fasta | wc -l
```

#### Step 3: Show all .fasta file in current dicrectory
```console
rafsanjani@mrz:~$ ls | grep '.fasta'
rafsanjani@mrz:~$ ls | egrep '.fasta$'
```

#### Step 4: Find all files that ends with .fasta and .fa in current dicrectory
```console
rafsanjani@mrz:~$ ls | egrep '*.fa$|*.fasta$'
```

&nbsp;

## 3. Shell Programming

#### Step 1: Assigning Variable
```sh
v=`ls | egrep '*.fa$|*.fasta$'`          # using ` `
v=$(ls | egrep '*.fa$|*.fasta$')         # using $( )
echo $v
```

#### Step 2: Loop
```sh
v=`ls | egrep '*.fa$|*.fasta$'`

for i in $v ; do
    echo $i
done
```


&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
