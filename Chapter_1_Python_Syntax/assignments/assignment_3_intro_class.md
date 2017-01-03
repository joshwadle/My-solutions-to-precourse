# Assignment: Introduction to python classes

## Objectives

- Moving from functions to methods.
- Defining a class and the `__init__` method.
- Creating an instance of the class.
- Writing methods and calling them via the `.` notation.
- Writing and calling key 'magic' methods.
- Importing a class as a module in iPython.

#### Instructions
Follow along the script, it will guide you in the creation of a class called Complex. You will need to apply the knowledge gain in so called ACTION items.

## Define functions

Let us first think about setting up functions that would allow us to manipulate complexes. If you are not familiar with complexes, you can check out this [Wikipedia article](https://en.wikipedia.org/wiki/Complex_number) and in particular the [elementary operations section](https://en.wikipedia.org/wiki/Complex_number#Elementary_operations). In particular, we want to be able to add, subtract and multiply complex numbers together.

ACTION: Fill in the functions [complex_functions.py](../code/complex_functions.py).

Filling in the functions [complex_functions.py](../code/complex_functions.py) is good programming practice, but not the main aim of this section, so a [solution file](../code/solns_complex_functions.py) is provided.

## Setting up a class

The aim of setting up a class is to regroup objects that have similar attributes, here complexes that have a real part and an imaginary part.

### 1. Defining a class

This is very straightforward.

```python
class Complex(object):
  pass
```

First use the reserved word `class`, and then indicate the class name. By convention, class names are usually capitalized. Everything in a class is indented

In the terminal, run `ipython` and import the class as you would a module.

```
# ipython
In [1]: from complex_class import Complex
```

### 2. Initializing the Class:

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

ACTION: Use the [complex_class.py](../code/complex_class.py). Create an instance of the class Complex, `complex_2`, for the complex number 1 + 3i. Change its imaginary part to 2.

## Defining more methods

Remember `join` and `sort` methods vs the `enumerate()` function from the `assignment_1.md`? `join` and `sort` are methods from the String class, already implemented in python. Methods are available through the `.` notation.

### 1. Methods for relying on the class instance

A very useful aspect of methods in a class is `self`, as it bounds the object’s data to the object. Let's add the following method to the class Complex (don't forget the indentation)

```python
  def print_complex(self):
      '''
      prints the complex in a standard format 'a + bi'
      with 'a' the real part and 'b' the imaginary one
      '''
      print '{0} + {1}i'.format(self.real, self.imaginary)
```

Notice that the complex number does not need to be passed in as an argument.

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_1.print_complex()
3 + 4i
```

ACTION: Implement the `conjugate` method, create instance `complex_1` and apply the `conjugate` method to it.

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
4 + 6i
```

ACTION: Implement the `subtract` and the `multiply` method, create instances `complex_1` and `complex_2` before finally subtracting `complex_2` to `complex_1` and multiplying `complex_1` and `complex_2`.

## Defining key magic methods

It would be great to just be able to use the operand `+` to add 2 complex numbers together. Or to be able to `print` the instance and see the complex number. This is not possible yet.

```
In [6]: complex_1 + complex_2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-df4ca884b615> in <module>()
----> 1 complex_1 + complex_2

TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
```

Let's use so-called python 'magic methods', with `__xxxx__` methods. This include:
- `__str__`: print statement to compute the "informal" string representation of an object.
- `__add__`, `__sub__`, `__mul__`, `__div__`, `__len__`: operand `+`, `-`, `*`, `/`, `len()` ...

You do not need to call these double underscore methods directly, python knows to use them when you call functions (`print`, `len()`, ...) or operands (`+`, `-`, `*`, `/`, ...)

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

ACTION: Replace `substract` by  `__sub__` and `multiply` by `__mul__`. Check that your implementation is correct. Give the output obtained for `In [4]` and `In [5]`

```
In [1]: from complex_class import Complex

In [2]: complex_1 = Complex(3,4)

In [3]: complex_2 = Complex(1,2)

In [4]: print complex_1 - complex_2

In [5]: print complex_1 * complex_2
```
