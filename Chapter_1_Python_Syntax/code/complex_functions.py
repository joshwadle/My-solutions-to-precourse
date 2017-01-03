def conjugate(complex_1):
  '''
  the complex conjugate of the number z = a + bi is defined to be a - bi.

  parameters
  ----------
  complex_1: tuple (r_1, i_1) to represent r_1 + i_1 i

  return
  ------
  (r,i) the real and imaginary part of the complex conjugate of complex_1

  >>> complex_1 = (3, 4)
  >>> conjugate(complex_1)
  (3, -4)
  '''
  pass

def add(complex_1, complex_2):
  '''
  add two complexes together
  parameters
  ----------
  complex_1: tuple (r_1, i_1) to represent r_1 + i_1 i
  complex_2: tuple (r_2, i_2) to represent r_2 + i_2 i

  return
  ------
  (r,i) the real and imaginary part of the complex obtained by adding
  complex_1 and complex_2

  >>> complex_1 = (3, 4)
  >>> complex_2 = (1, 2)
  >>> add(complex_1, complex_2)
  (4, 6)
  '''
  pass

def substract(complex_1, complex_2):
  '''
  substract complex_2 from complex_1
  parameters
  ----------
  complex_1: tuple (r_1, i_1) to represent r_1 + i_1 i
  complex_2: tuple (r_2, i_2) to represent r_2 + i_2 i

  return
  ------
  (r,i) the real and imaginary part of the complex obtained by substracting
  complex_2 from complex_1

  >>> complex_1 = (3, 4)
  >>> complex_2 = (1, 2)
  >>> substract(complex_1, complex_2)
  (2, 2)
  '''
  pass

def multiply(complex_1, complex_2):
  '''
  multiply two complexes together
  parameters
  ----------
  complex_1: tuple (r_1, i_1) to represent r_1 + i_1 i
  complex_2: tuple (r_2, i_2) to represent r_2 + i_2 i

  return
  ------
  (r,i) the real and imaginary part of the complex obtained by multiplying
  complex_1 and complex_2

  >>> complex_1 = (3, 4)
  >>> complex_2 = (1, 2)
  >>> multiply(complex_1, complex_2)
  (2, 2)
  '''
  pass

def print_complex(complex_1):
    '''
    prints the complex in a standard format 'a + bi'
    with 'a' the real part and 'b' the imaginary one

    >>> complex_1 = (3, 4)
    >>> print_complex(complex_1)
    3 + 4i
    '''
    pass
