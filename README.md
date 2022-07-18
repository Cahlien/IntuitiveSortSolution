# Intuitive Sort Solution

## Description
This application sorts a list of strings lexicographically with 
the following rules:

- Strings are sorted alphabetically.
- Numbers are sorted numerically.
- Adjacent numbers and a decimal followed by a number are collected together 
  and sorted as a single number.
- All other punctuation is considered alphabetical.

## Hypothesis
Python's performance is only impressive when compared to Ruby, so
it is ideal to utilize the built-in implementations, which are written
in C, whenever possible.  Implementing the interpreter pattern to 
tokenize a string and a custom comparator to compare the resulting tokens, 
along with a function to orchestrate the process, will produce 
the most efficient solution with the minimum of drag on performance.

## Running Natively
The following command will run the application, if all the dependencies are installed:

```bash
$ pip install -r requirements.txt
$ python intuitive_sort.py ./instructions/sort_me.txt
```

## Running in Docker
### Building and Running the Python2 Container with the Default Arguments
```bash
$ docker build -t intuitive-sort-p2:latest .
$ docker run --name intuitive-sort-p2 intuitive-sort-p2:latest 
```

### Building and Running the Python3 Container with the Default Arguments
```bash
$ docker build -t intuitive-sort-p3:latest .
$ docker run --name intuitive-sort-p3 intuitive-sort-p3:latest 
```

### Running the Python2 Container Interactively
```bash
$ docker run -it intuitive-sort-p2:latest bash
$ /app/IntuitiveSortSolution.py /app/instructions/sort_me.txt
```

### Running the Python3 Container Interactively
```bash
$ docker run -it intuitive-sort-p3:latest bash
$ /app/IntuitiveSortSolution.py /app/instructions/sort_me.txt
```

## Application Guidelines
Lexicographic sorting compares numbers as text, using their ASCII value, but
this creates a sort order that is not intuitive for a human user. Create
a sorting algorithm that treats all adjacent digits as a single number. Treat
a period that is surrounded by digits as a decimal.

Create a python script that reads a single file name from the command line. The
file contains one word per line. Print the words using this intuitive sort
order. A test word list can be found in sort_me.txt.

Your script needs to run with both python2 and python3.

The correct sort order is:
2.718splice
3sure8termed
3sure37termed
3sure210termed
19splice
151splice
aztec
bees-4knees
bees-5.9.knees
bees-11.knees
bees-42.knees
extols
haydn2.37jaunt
haydn2.4jaunt
haydn6.4jaunt
haydn10.9
haydn42.14
honour
keeper
laws1
laws2
laws3
laws4
laws9
laws10
laws11
laws12
laws13
laws13.234
laws13.73
laws74
laws100
laws101
laws102
laws103
laws1000
laws1001
laws1002
laws1003
posed1
posed13
posed27
posed202
shorty
supper
