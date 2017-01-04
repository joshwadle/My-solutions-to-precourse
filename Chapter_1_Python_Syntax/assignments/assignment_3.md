# Assignment: Object Oriented Programming

## Objectives

- Moving from functions to methods.
- Defining a class and the `__init__` method.
- Creating an instance of the class.
- Writing methods and calling them via the `.` notation.
- Writing and calling key 'magic' methods.
- Importing a class as a module in iPython.

If you are completely new to classes in Python, or want to practice, you can first complete an [introductory assignment](assignment_3_intro_class.md) that will walk through the creation of a `Complex` class.
_______________________________________

## Questions & Answers

Implement a `RandomStory` class to generate a random story in a file called `assignment_3a.py`. It should accept as parameters:
- `<filename>`: the path to the file used to generate the random stories (for instance `alice.txt`)
- `n_gram`: the number of words - 1, 2 or 3- used to choose the new word.
This class should have a `train` method that creates the instance variable `dict_word` (keys are tuples of 1 to 3 words depending on the value of `n_gram`, values are lit of words that follow these words in the reference text). It should also have a `generate` method, with `num_words` as a parameter, that generates a random story `num_words` long.

Go back to the functions developed to [generate random text](assignment_2a.py) and adapt them to create this class.

You should be able to run the following code in ipython once you implemented the `RandomStory` class.

```
#ipython
In [1]: from assignment_3a import RandomStory

In [2]: story_1 = RandomStory('alice.txt', 1)

In [3]: story_2 = RandomStory('alice.txt', 2)

In [4]: story_3 = RandomStory('alice.txt', 3)

In [5]: story_1.train()

In [6]: story_1.dict_word

In [7]: story_1.generate(100)

In [8]: story_2.train()

In [9]: story_2.generate(200)

In [10]: story_3.train()

In [11]: story_3.generate(100)
```
