# Shell Programming

&nbsp;

#### Step 1: Assigning Variable
```sh
v=`ls | grep -E '*.fa$|*.fasta$'`          # using ` `
v=$(ls | grep -E '*.fa$|*.fasta$')         # using $( )

echo $v
```
***Note:*** There will be `no space` before and after `equal sign`.

&nbsp;
&nbsp;

#### Step 2: Conditional Operation (if-else)

- ##### Step 1: Check Numbers
  ```sh
  if [ 2 -lt 3 ]; then # 2 < 3
      echo 'action, if works.'
  else
      echo 'action, else works.'
  fi
  ```

  ***Note-1:*** We can't use [2 -lt 3]; use proper `space`.

  ***Note-2:*** [Documentation](https://www.linuxtechi.com/compare-numbers-strings-files-in-bash-script/).

&nbsp;
&nbsp;

#### Step 3: Iteration (Loop)

- ##### Step 1: Simple Print Number
  ```sh
  for i in {1..9..2}; do
      echo $i
  done

  # Output (Like): 1, 3, 5, 7, 9
  ```

- ##### Step 2: Simple Print (Itemized)
  ```sh
  for i in 1 9 2; do
      echo $i
  done

  # Output (Like): 1, 9, 2
  ```

- ##### Step 3: Show file name one-by-one
  ```sh
  v=`ls | grep -E '*.fa$|*.fasta$'`

  for i in $v; do
      echo $i
  done
  ```

- ##### Step 4: Check whether it is file or directory
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

&nbsp;
&nbsp;

#### Step 3: Array

- ##### Step 1: Array indexing
  ```sh
  v=(`ls | egrep '*.fa$|*.fasta$'`)        # Convert into array 

  echo ${v[0]}                             # First-index of array
  echo ${v[1]}                             # Second-index of array
  echo ${v[2]}                             # Third-index of array
  echo ${v[3]}                             # Fourth-index of array
  echo ${v[4]}                             # Fifth-index of array

  echo ${#v[*]}                            # length of the array; alternatively ${#v[@]} 
  ```

- ##### Step 2: Array with for-index-loop
  ```sh
  v=(`ls | egrep '*.fa$|*.fasta$'`)           # Convert into array

  for (( i = 0; i < ${#v[*]}; i++ )); do      # length of array is ${#v[*]} or ${#v[@]} 
      echo ${v[$i]}                           # Access each element of the array
  done
  ```

- ##### Step 3: Array with for-each-loop
  ```sh
  v=(`ls | egrep '*.fa$|*.fasta$'`)

  for i in ${v[*]}; do
      echo $i
  done
  ```

&nbsp;
&nbsp;

**Note:** The step doesn't mean you have to follow one by one.
