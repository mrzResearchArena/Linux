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


## 3. String Handling
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
```

&nbsp;

## 4. Shell Programming

#### Step 1: Assigning Variable
```sh
v=`ls | egrep '*.fa$|*.fasta$'`          # using ` `
v=$(ls | egrep '*.fa$|*.fasta$')         # using $( )

echo $v
```
###### Note: There will be `no space` before and after `equal sign`.

#### Step 2: Loop

##### Step 1: Simple Print Number
```sh
for i in {1..9..2}; do
    echo $i
done
```

##### Step 2: Simple Print (Itemized)
```sh
for i in 1 9 2; do
    echo $i
done
```

##### Step 3: Show file name one-by-one
```sh
v=`ls | egrep '*.fa$|*.fasta$'`

for i in $v; do
    echo $i
done
```

##### Step 4: Check whether it is file or directory
```sh
v=`ls`

for i in $v; do
    if [ -d $i ]; then
        echo $i '->' 'is a directory.'
    else
        echo $i '->' 'is a file.'
    fi
done
```

#### Step 3: Array

##### Step 1: Array indexing
```sh
v=(`ls | egrep '*.fa$|*.fasta$'`)        # Convert into array 

echo ${v[0]}                             # First-index of array
echo ${v[1]}                             # Second-index of array
echo ${v[2]}                             # Third-index of array
echo ${v[3]}                             # Fourth-index of array
echo ${v[4]}                             # Fifth-index of array

echo ${#v[*]}                            # length of the array; alternatively ${#v[@]} 
```

##### Step 2: Array with for-index-loop
```sh
v=(`ls | egrep '*.fa$|*.fasta$'`)           # Convert into array

for (( i = 0; i < ${#v[*]}; i++ )); do      # length of array is ${#v[*]} or ${#v[@]} 
    echo ${v[$i]}                           # Access each element of the array
done
```

##### Step 3: Array with for-each-loop
```sh
v=(`ls | egrep '*.fa$|*.fasta$'`)

for i in ${v[*]}; do
    echo $i
done
```


&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
