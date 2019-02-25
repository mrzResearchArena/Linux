# Linux Handling

&nbsp;

## 1. How to reduce terminal text / Customizing BASH Prompt 
```console
rafsanjani@mrz:~$ PS1='[\u@\h \W]\$ '           (Small)
rafsanjani@mrz:~$ PS1='[@ \W]\$ '               (Extra Small)
```
&nbsp;

## x. Regular Expression

#### Step 1: Search a keyword from a file
```console
rafsanjani@mrz:~$ cat fileName.txt | grep 'keyword'
```

#### Step 2: Count the number of fasta sequence from a file (.fasta)
```console
rafsanjani@mrz:~$ grep '>' fileName.fasta | wc -l
```


&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
