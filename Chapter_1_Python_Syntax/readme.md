# Chapter 1:  Python Best Practices

### This is an chapter to practice python, where we look at built-in functions and data structures.

## Learning Objectives

These will vary depending on your background.

#### Confirmed coder
Breeze through the exercises!

#### Confident coder
Practice makes perfect. Maybe you come from another language or have used Python sporadically, these assignments will get you up to speed with Python quickly (both in terms of syntax
and style).

#### On the road to confident coder
The course will heavily use Python for most of its analyses/projects.  It is not
necessary to be an expert in Python coming into the course (that is part of what we will
teach you!) but it is helpful to be familiar with its syntax.

## Main Resources

Lecture notes:
* Take a look at these [notes](resources/python.md) that go over python topics you should become familiar with:
  - Python Termimal (ipython)
  - Advanced Python (Generators, Looping tools, List comprehensions, Lambda functions, Sets and Dictionaries, Mutable vs Immutable, Permutations and Combinations, File I/O, Exception Handling)
  - Python Style

Go to the [extra resources section](#going-further:-more-resources) for books, exercises and videos we recommend.

## Assignments

#### Installation
You should have the Anaconda distribution installed (see Chapter_0). If you do not (and you should!), follow the installation instructions directly below to get setup. Then continue on to the assignments.

- Install the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python 2.7
(not Python 3) distribution
- Use [conda](http://www.continuum.io/blog/conda) to install any additional packages.

#### Instructions

Read all instructions below, then fill in the functions provided for you in each file located in the [assignements folder](assignments). You will work with strings, numbers, lists, dictionaries, sets and even generators.

You should then check your work by running the following command in the Terminal:

```
$ python -m doctest assignment_1x.py
```

Make sure you are in the right directory (the one containing `assignment_1x.py`).

We are using the `doctest` module, which is included in standard library, to test that the functions' output are as expected. The `doctest` module looks prompts `>>>` in a docstring to generate automatic tests.

```python
def my_function(argument1, argument2):
  '''
  this is a docstring, it describes what the function does and what the
  parameters are. This is were the prompt is placed, as follows:
  >>> my_function(value1, value2)
  expected_output
  '''
```

### 1. Practice with built-ins functions

- Practice using the `map` function and list comprehensions with [assignment_1a](assignments/assignment_1a.py). With `map` functions you will be using the lambda operator/function, which is an easy way to create a quick, anonymous functions that will not need to be re-used. List comprehensions will allow you to achieve the same result without lambda operators. There are 7 functions to fill.

- Practice writing `lambda x: f(x)` functions with `filter` and `reduce`. There are 5 functions to complete in [assignment_1b](assignments/assignment_1b.py).

- Practice some more using indices and slicing in 4 functions with [assignment_1c](assignments/assignment_1c.py)

- Practice some useful functions `enumerate` and `zip` as well as the methods `join` and `sort` with [assignment_1d](assignments/assignment_1d.py). There are 6 functions for you to complete.

- Practice using `itertools` module, in particular `combinations` and `permutations`. There are only 2 functions to fill in for this [assignment_1e](assignments/assignment_1e.py). Take the time to understand how `generators` and `iterators` work.


### 2. Generating text

Fill in the functions `word_counts`, `associated_words` and `make_random_story`
in [2_words.py](code/2_words.py). These will give you practice with reading files, strings and dictionaries.

Take a look at the [Collections module](https://docs.python.org/2/library/collections.html).
You may be able to use `DefaultDict` and `Counter` to simplify your code.

### 3. Fizz Buzz fun with Python

FizzBuzz is infamous for being a simple programming problem that [a lot of software
engineers struggle with](http://blog.codinghorror.com/why-cant-programmers-program/).

* Implement the function `fizzbuzz` in [3_fizzbuzz.py](code/3_fizzbuzz.py). Don't worry, this is not the main point of this question.

* Modify the function definition so that the following calls all work. You should have 3 and 5 be the default parameters.
([documentation](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values))

        fizzbuzz(15)                  # "FizzBuzz"
        fizzbuzz(15, fizz=4)          # "Buzz"
        fizzbuzz(15, buzz=4)          # "Fizz"
        fizzbuzz(15, fizz=6, buzz=7)  # ""

    Now in the main block you should be able to remove the 2nd and 3rd parameters.

* Look at how the main function uses `sys.argv`. You can run your program with this
command in the command line:

        python 3_fizzbuzz.py 20

    Modify `words.py` so that you can run your program like this:

        python 2_words.py alice.txt 200

    You'll have to import the `sys` module and use `sys.argv` ([documentation](https://docs.python.org/2/library/sys.html))

## Recap

Can you answer these questions:

 1. What's the difference between a list and a generator? And the advantages of either?
 2. What is the advantage of storing a word list in a set rather than a list?

You should be comfortable with everything below.

- Basic data structures and associated methods
  * int, float
  * string
  * list
  * dict
  * set
  * range
- Control structures
  * if, elif, else
  * while
  * for
  * break, continue, pass
- Enumerations
  * for loops
  * list comprehensions
  * enumerate
  * zip
- Functions
  * Declaration
  * Calling
  * Keyword arguments
- Object orientation
  * Classes
  * Methods
  * Properties (instance variables)
  * self
- Modules
  * import
  * aliasing (`import pandas as pd`)
  * global import (`from pandas import *`)
- IO
  * Read a file
  * Write to a file

## Going Further: More resources

If you still feel new to Python, you might benefit from looking at one of these resources (books with snippets of codes or exercises):
* [Learn Python the Hard Way](http://learnpythonthehardway.org/), with the [free version](https://learnpythonthehardway.org/book/). Work your way through the exercises 0 to 39, it offers a great combination of explanations and exercises to apply the concepts.
* [Dive Into Python](http://www.diveintopython.net/): Chapters 1 through 6 are particularly relevant to make sure you are familiar with dictionaries, lists, tuples and have some exposure to classes.
* [Effective Python](http://www.effectivepython.com/) and its associated [GitHub account](https://github.com/bslatkin/effectivepython)

If you like to follow along videos, Coursera offers some courses on programming in Python as well:
* [Learn to Program: The Fundamentals](https://www.coursera.org/course/programming1)
* [Learn to Program: Crafting Quality Code](https://www.coursera.org/course/programming2)

Python also has great documentation which is helpful if you need to look up how something is done in Python:
* [Python tutorial](https://docs.python.org/2/tutorial/)
* [Python library](https://docs.python.org/2/library/)
