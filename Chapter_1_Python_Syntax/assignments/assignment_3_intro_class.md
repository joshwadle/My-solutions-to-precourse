# Assignment: Introduction to python classes

## Objectives

This assignment is designed to be a progressive construction of a `Complex` class.

- Moving from functions to methods.
- Defining a class and the `__init__` method.
- Creating an instance of the class.
- Writing methods and calling them via the `.` notation.
- Writing and calling key 'magic' methods.
- Importing a class as a module in iPython.

#### Instructions
Follow along the script, it will guide you in the creation of a class called Complex. You will need to apply the knowledge gained in so called CHALLENGE items.

## Define functions

Let us first think about setting up functions that would allow us to manipulate complexes. If you are not familiar with complexes, you can check out this [Wikipedia article](https://en.wikipedia.org/wiki/Complex_number) and in particular the [elementary operations section](https://en.wikipedia.org/wiki/Complex_number#Elementary_operations).

CHALLENGE: We want to be able to take the conjugate of a complex number and we want add, subtract and multiply complex numbers together.

YOUR ANSWER: Fill in the functions [complex_functions.py](../code/complex_functions.py).

Note: Filling in the functions [complex_functions.py](../code/complex_functions.py) is good coding practice, but not the main aim of this section, so a [solution file](../code/solns_complex_functions.py) is provided.

## Setting up a class

The aim of setting up a class is to regroup objects that have similar attributes, here complexes that have a real part and an imaginary part. Let's make a `complex_class.py` script.

### 1. Defining a class

This is very straightforward. Copy paste the following lines in `complex_class.py`.

```python
class Complex(object):
  pass
```

First notice the use the reserved word `class`, and followed by the class name. By convention, class names are capitalized. Everything in a class is indented (here just the `pass`.)

In the terminal, run `ipython` and import the class as you would a module.

```
# ipython
In [1]: from complex_class import Complex
```

### 2. Initializing the Class:

In the `complex_class.py`, replace the previous lines by

```python
class Complex(object):
    def __init__(self, real, imaginary):
      self.type = 'a complex number'
      self.real = real
      self.imaginary = imaginary
```

Within classes, we use the term 'methods' instead of 'functions'. The first method to call is the `__init__` method. We will spend more time looking at methods in the following 2 sections. The point of the `__init__` method is to allow us to create instances of a class. An instance of a class is an individual object of the class.

To create an instance of a class (instantiation):

```
# ipython
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_1
Out[3]: <complex_class.Complex at 0x102518a10>
```

NB: Make sure you have the `autoreload` set up as described in Chapter_0. If you do not, start a new ipython session everytime. This ensures that you have access to the latest version of the Complex class.

Within classes, we can define instance variable: these are variables that are used within the class. In this example, we can have access to `real` and `imaginary`, the real part and imaginary part of the complex number of interest. They belong only to the current instance of a class

To access the attributes of an instance like `complex_1`:

```
# ipython
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_1.real
Out[3]: 3

In [4]: complex_1.imaginary
Out[4]: 4

In [5]: complex_1.real = 5

In [6]: complex_1.real
Out[6]: 5

In [7]: complex_1.type
Out[7]: 'a complex number'
```

Note that input `In [5]` and `In [6]` shows how to modify the 'real' attribute. Input `In [7]` shows that it is possible to access instance variables not entered as arguments of the class, but present in the `__init__` method.

CHALLENGE: Let us use the [complex_class.py](../code/complex_class.py). Open iPython in the terminal and import the `Complex` class. Create an instance of the class Complex, `complex_2`, for the complex number 1 + 3i. Change its imaginary part to 2. Access its real part, then its imaginary part.

YOUR ANSWER: Copy paste the inputs and outputs obtained in iPython.

## Defining more methods

Remember `join` and `sort` methods vs the `enumerate()` function from the `assignment_1.md`? `join` and `sort` are methods from the String class, already implemented in python. Methods are available through the `.` notation.

### 1. Methods relying on the class instance

A very useful aspect of methods in a class is `self`, as it bounds the object’s data to the object. Let's add the following method to the class Complex (don't forget the indentation)

```python
  def print_complex(self):
      '''
      prints the complex in a standard format 'a + bi'
      with 'a' the real part and 'b' the imaginary one
      if b = 0: 'a'
      if a = 0: 'b'
      else: 'a + bi'
      a and b: rounded to 2 decimal
      '''
      (r_1, i_1) = self.real, self.imaginary
      if i_1 == 0:
          complex_number = "{:.2f}".format(r_1)
      elif r_1 == 0:
          if i_1 >= 0:
              complex_number = "{:.2f}i".format(i_1)
          else:
              complex_number = "-{:.2f}i".format(abs(i_1))
      elif i_1 > 0:
          complex_number = "{:.2f} + {:.2f}i".format(r_1, i_1)
      else:
          complex_number = "{:.2f} - {:.2f}i".format(r_1, abs(i_1))
      return complex_number
```

Notice that the complex number does not need to be passed in as an argument.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_1.print_complex()
3 + 4i
```

CHALLENGE: Implement the `conjugate` method in `complex_class.py`. Open an iPython session, import the `Complex` class as a module and create the instance `complex_1` as shown above. Apply the `conjugate` method to obtain `conjugate_complex_1`, a class instance, and print it out.

YOUR ANSWER: Copy paste the inputs and outputs obtained in iPython.

### 2. Methods using several instances of a class

Let's add the following method to the class Complex (don't forget the indentation)

```python
  def add(self, other_complex):
      '''
      add two complexes together

      return
      ------
      the complex obtained by adding the other complex
      '''
      (r_1, i_1) = self.real, self.imaginary
      (r_2, i_2) = other_complex.real, other_complex.imaginary
      return Complex(r_1 + r_2, i_1 + i_2)
```

Let's see how to use this `add` method.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_2 = Complex(1,2)

In [4]: complex_3 = complex_1.add(complex_2)

In [5]: complex_3.print_complex()
Out[5]: '4.00 + 6.00i'
```

CHALLENGE: Implement the `subtract` and the `multiply` methods to create the resulting class instance. Open an iPython session, import the class, create instances `complex_1` and `complex_2` before finally subtracting `complex_2` to `complex_1` and printing the result. Multiply `complex_1` and `complex_2` and print the result.

YOUR ANSWER: Copy paste the inputs and outputs obtained in iPython.

## Defining key magic methods

It would be great to just be able to use the operand `+` to add 2 complex numbers together. Or to be able to `print` the instance and see the complex number in human compatible format 'a + bi'. This is not possible yet.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_2 = Complex(1,2)

In [4]: print complex_2
<solns_complex_class.Complex object at 0x102519c50>

In [5]: complex_3 = complex_1 + complex_2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-6a2bc4fd790a> in <module>()
----> 1 complex_3 = complex_1 + complex_2

TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
```

To achieve our aims, let's use so-called python 'key magic methods', with `__xxxx__` methods. This include:
- `__str__`: print statement to compute the "informal" string representation of an object.
- `__add__`, `__sub__`, `__mul__`, `__div__`, `__len__`: use operand `+`, `-`, `*`, `/`, `len()` ...

Note that you do not need to call these double underscore methods directly, python knows to use them when you call functions (`print`, `len()`, ...) or operands (`+`, `-`, `*`, `/`, ...)

Replace the `print_complex` function by:
```python
  def __str__(self):
      if self.imaginary == 0:
          complex_number = "{:.2f}".format(self.real)
      elif self.real == 0:
          if self.imaginary >= 0:
              complex_number = "{:.2f}i".format(self.imaginary)
          else:
              complex_number = "-{:.2f}i".format(abs(self.imaginary))
      elif self.imaginary > 0:
          complex_number = \
                  "{:.2f} + {:.2f}i".format(self.real, self.imaginary)
      else:
          complex_number = \
                  "{:.2f} - {:.2f}i".format(self.real, abs(self.imaginary))
      return complex_number
```

You can now print the Complex instance in a human friendly format. Check it in iPython.

```
#ipython
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: print complex_1
3.00 + 4.00i
```

Now replace the `add` method by the following code:

```python
  def __add__(self, other_complex):
      '''
      add two complexes together

      return
      ------
      (r,i) the real and imaginary part of the complex obtained by adding the
      other complex

      '''
      (r_1, i_1) = self.real, self.imaginary
      (r_2, i_2) = other_complex.real, other_complex.imaginary
      return Complex(r_1 + r_2, i_1 + i_2)
```

The error we had in the beginning of this section, when we use `+`, should disappear. Try it out in iPython.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_2 = Complex(1,2)

In [4]: print complex_1 + complex_2
4.00 + 6.00i
```

CHALLENGE: Replace `substract` by  `__sub__` and `multiply` by `__mul__` in your `complex_class.py`. Check that your implementation is correct by opening iPython, creating `complex_1` and `complex_2`, and printing the result of `complex_1 - complex_2` and `complex_1 * complex_2`.

YOUR ANSWER: Copy paste the inputs and outputs obtained in iPython.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_2 = Complex(1,2)

In [4]: print complex_1 - complex_2

In [5]: print complex_1 * complex_2
```
If you want to check your result, you should get `2.00 + 2.00i` for the subtraction and `-5.00 + 10.00i` for the multiplication.
