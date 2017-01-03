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
    (r_1, i_1) = complex_1
    return (r_1, -i_1)

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
    (r_1, i_1) = complex_1
    (r_2, i_2) = complex_2
    return (r_1 + r_2, i_1 + i_2)

def subtract(complex_1, complex_2):
    '''
    subtract complex_2 from complex_1
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
    >>> subtract(complex_1, complex_2)
    (2, 2)
    '''
    (r_1, i_1) = complex_1
    (r_2, i_2) = complex_2
    return (r_1 - r_2, i_1 - i_2)

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
    (-5, 10)
    '''
    (r_1, i_1) = complex_1
    (r_2, i_2) = complex_2
    return (r_1 * r_2 - i_1 * i_2, r_1 * i_2 + r_2 * i_1)

def print_complex(complex_1):
    '''
    prints the complex in a standard format 'a + bi'
    with 'a' the real part and 'b' the imaginary one
    if b = 0: 'a'
    if a = 0: 'b'
    else: 'a + bi'
    a and b: rounded to 2 decimal

    >>> complex_1 = (3, 4)
    >>> print_complex(complex_1)
    3.00 + 4.00i
    '''
    (r_1, i_1) = complex_1
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
