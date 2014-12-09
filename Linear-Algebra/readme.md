Linear Algebra
===================================
In this exercise, we will be doing a numpy focused linear algebra overview.

This will cover all of the basic operations you can do with matrices, as well as some properties of linear algebra with relevant machine learning.

Overview
==============================
1. Matrix vs Vectors
2. Scalar Operations
3. Matrix Vector Multiplication
4. Matrix Matrix Multiplication
5. Elementwise Matrix Operations
6. Axis wise operations
7. Rank
8. Extra Credit


Resources
====================
* [Linear dependence](http://www.math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/lindep/lindep.html)
* [Rank](http://www.cliffsnotes.com/math/algebra/linear-algebra/real-euclidean-vector-spaces/the-rank-of-a-matrix)
* [Rank in numpy](http://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.linalg.matrix_rank.html)
* [Determinant in numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)
* [Broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
* [Matrix overview](http://cs229.stanford.edu/section/cs229-linalg.pdf)
* [Nd arrays](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)

```python
# This is a preview of the Linear_Algebra_Assignment.py
# ======================================================
# Fill your answer directly into the Linear_Algebra_Assignment.py

import numpy as np

# Part One:  Matrix vs Vectors
#==============================

def one():
    '''
    INPUT: NONE
    OUTPUT: A numpy row vector of 100 random integers all between the values of 0 and 10. (matrix)

    Create a row vector with numpy (1 x 100).

    Example:
    >>>
    >>> rv = one()
    >>> print rv
    >>> [1, 1, 1, 6, ..., 9]
    '''
    return answer


def two():
    '''
    INPUT: NONE
    OUTPUT: A column vector of 100 sequential floats all between 0 and 50. (matrix)

    Create a column vector with numpy (100 x 1).

    Example:
    >>>
    >>> cv = two()
    >>> print cv
    >>> [[  0.        ]
    [  0.50505051]
    [  1.01010101]
    ...
    [ 50.        ]]
    '''
    return answer


def three():
    '''
    INPUT: NONE
    OUTPUT: A 6x6 numpy matrix

    Create a square 6 by 6 matrix.

    Example:
    >>>
    >>> M = three()
    >>> print M
    >>> [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]
    [24 25 26 27 28 29]
    [30 31 32 33 34 35]]
    '''

    return answer


def four():
    '''
    INPUT: NONE
    OUTPUT: A random 2 x 3 numpy matrix

    Create a random 2 x 3 matrix.
    You should be able to do this with one command  (look at the numpy random module).

    Example:
    >>>
    >>> M = four()
    >>> print M
    >>> [[7 8 2]
    [9 4 3]]
    '''
    return answer


def five():
    '''
    Create a 6 x 6 identity matrix.

    INPUT: NONE
    OUTPUT: 6x6 identity matrix

    Example:
    >>> I = five()
    >>> print I
    >>> [[ 1.  0.  0.  0.  0.  0.]
    [ 0.  1.  0.  0.  0.  0.]
    [ 0.  0.  1.  0.  0.  0.]
    [ 0.  0.  0.  1.  0.  0.]
    [ 0.  0.  0.  0.  1.  0.]
    [ 0.  0.  0.  0.  0.  1.]]
    '''

    return answer

def six():
    '''
    Create a (4 x 9) matrix with sequential ints 1 through 36.

    Example:
    >>> print answer
    >>>> [[ 1  2  3  4  5  6  7  8  9]
    [10 11 12 13 14 15 16 17 18]
    [19 20 21 22 23 24 25 26 27]
    [28 29 30 31 32 33 34 35 36]]
    '''
    return answer


def seven(M):
    '''
    INPUT: Matrix output from function six.
    OUTPUT:  First three columns of Matrix from function six.

    Call function six() and save it as M,
    Return just the first 3 columns of M

    Example:
    >>> M = six()
    >>> print seven(M)
    >>> [[ 1  2  3]
    [10 11 12]
    [19 20 21]
    [28 29 30]]

    '''
    return answer



def eight(M):
    '''
    INPUT: Matrix output from function six.
    OUTPUT:  Last two ROWS of Matrix from function six.

    Example:
    >>> M = six()
    >>> print eight(M)
    >>> [[19 20 21 22 23 24 25 26 27]
    [28 29 30 31 32 33 34 35 36]]
    '''

    return answer


            # PART 2: SCALAR OPERATIONS
            # =========================

def nine():
    '''  
    INPUT: None
    OUTPUT: A numpy array with values [2 3 5 8 9]

    Create this numpy array (called V): [2 3 5 8 9]
    '''
    return V

def ten():
    '''
    INPUT: V (matrix from nine() )
    OUTPUT: [ 2.5  3.5  5.5  8.5  9.5]

    Do a scalar addition by 0.5 to V.
    '''
    return answer



def eleven():
    '''
    INPUT: V (matrix from nine() )
    Do a scalar multiple by -2.

    '''
    return answer



def twelve():
    '''
    INPUT: V (matrix from nine() )

    Create a 1 by 5 vector 'b'
    so that the following would get the same result as you did in #2:
    v + b (called broadcasting).
    '''
    return answer


            # PART 3: MATRIX / VECTOR Multiplication
            # ======================================
def thirteen():
    '''
    Create column vector with 3 ints, called as column_vector.
    Create a row vector with 3 ints, called as row_vector.
    Create 3 x 3 square matrix called and square_matrix:
    Return as column_vector, row_vector, square_matrix
    '''

    return column_vector, row_vector, square_matrix


def fourteen(column_vector, row_vector):
    '''
    INPUT: Using column_vector and row_vector from thirteen() as the inputs
    OUTPUT:  n x m shaped vector where n is number of rows in row_vector and m is number of cols in col_vec

    Perform a vector vector multiply on column_vector and row_vector.
    This should output a n x m matrix where n is the number of rows in row_vector and m is the number of columns in column_vector.
    Say column_vector is a 2 x 1 and row_vector is a 1 x 3, output will be a 2 x 3 matrix.

    '''
    return answer

def fifteen(column_vector, row_vector, square_matrix):
    '''
    INPUT: Using column_vector and row_vector from thirteen() as the inputs
    OUTPUT:  return c_answer, r_answer

    c_answer is the matrix multiplication of column_vector and square_matrix
    r_answer is the matrix multiplication of row_vector and square_matrix


    For both column_vector and row_vector, matrix multiply by square_matrix.
    One will have to go on the left and one will have to go on the right.
    If it lets you do both directions,
    you probably are doing elementwise multiplication instead of matrix multiplication!
    '''
    return c_answer, r_answer


def sixteen(column_vector, row_vector):
    '''
    Compute the dot product of row_vector and column_vector.
    '''
    return answer




# PART 4: MATRIX MATRIX MULTIPLICATION
#====================================
def seventeen():
    '''
    question one:  If A is a 3 x 2 and B is a 4 x 3, can you matrix multiply them (AB)?
    If question_one is true, set variable 'answer_one' equal to True, if false, set 'answer_one' equal to False

    question two: If so, what is the shape?
    If answer_one is True, set variable 'answer_two' equal to the shape of the matrix, if False, set 'answer_two' equal to None

    question three:  Can you matrix multiply them in the other direction (BA)?
    If true, set variable 'answer_three' equal to True, if false, set 'answer_three' equal to False

    four:  If so, what's the shape of that?
    If answer_three is True, set variable 'answer_four' to be the shape of the matrix in answer_three, if False set 'answer_four' equal to None

    OUTPUT: answer_one BOOLEAN,
    answer_two Tuple or None,
    answer_three BOOLEAN,
    answer_four Tuple or None
    '''
    return answer_one, answer_two, answer_three, answer_four


def eighteen():
    '''
    Create a random 3 x 6 matrix as 'rand_matrix'.

    Matrix multiply rand_matrix and the transpose of rand_matrix as 'answer_one'

    Reshape rand_matrix so that it can be multiplied by the original as 'answer_two'. (hint np.reshape() )

    Return Matrix multiply 'rand_matrix' and 'answer_two' as 'answer_three'

    INPUT: None
    OUTPUT: answer_one  NUMPY MATRIX
    answer_two  NUMPY MATRIX
    answer_three NUMPY MATRIX

    '''

    return answer_one, answer_two, answer_three


# PART 5: Elementwise Matrix Operations
#======================================

def nineteen():
    '''
    Create 2 random 6 x 2 matrices as A and B.
    Square A (this will be the same shape).
    Add, subtract, multiply and divide A and B (This will be the same shape).

    INPUT: None
    OUTPUT: answer_square, answer_add, answer_subtract, answer_multiply, answer_divide
    '''
    return answer_square, answer_add, answer_subtract, answer_multiply, answer_divide


def twenty():
    '''
    Create two matricies, A and B.
    Make Matrix 'A' a 4x1 shaped matrix with values 1 through 4.
    A = [ [1], [2], [3], [4] ]

    Make matrix B a 1x3 matrix that look like this:
    B = [[ 100.  200.  300.]]

    answer = add Matrix A to Matrix B
    return answer
    '''

    return answer


def twenty_one():
    '''
    Create a 10x10 matrix that looks just like this
    M = [[ 0  1  2  3  4  5  6  7  8  9]
    [10 11 12 13 14 15 16 17 18 19]
    [20 21 22 23 24 25 26 27 28 29]
    [30 31 32 33 34 35 36 37 38 39]
    [40 41 42 43 44 45 46 47 48 49]
    [50 51 52 53 54 55 56 57 58 59]
    [60 61 62 63 64 65 66 67 68 69]
    [70 71 72 73 74 75 76 77 78 79]
    [80 81 82 83 84 85 86 87 88 89]
    [90 91 92 93 94 95 96 97 98 99]]
    '''
    return M


def twenty_two(M):
    '''
    Calculate the sums, mean and standard deviation of the values in the matrix from function twenty_one.
    INPUT: M is matrix from function twenty_one
    OUTPUT:  answer_sum, answer_mean, answer_std
    '''
    return answer_sum, answer_mean, answer_std


def twenty_three(M):
    '''
    Calculate the column wise sums, mean and standard deviation of the matrix.

    INPUT: M is matrix from function twenty_one
    OUTPUT:  col_sum, col_mean, col_std
    '''
    return col_sum, col_mean, col_std


def twenty_four(M):
    '''
    Calculate the row wise sums, mean and standard deviation of the matrix.

    INPUT: M is matrix from function twenty_one
    OUTPUT:  row_sum, row_mean, row_std
    '''
    return row_sum, row_mean, row_std


```
Extra Credit 1:
===========================
These are to practice linear algebra and programming. You shouldn't use any numpy magic and you *should* (gasp!) use for loops in your solutions. You should write a function for each of these.

1. Implement matrix multiply given two 2-dimensional lists of numbers. Test it out with a 6 x 3 matrix and a 3 x 5 matrix. (This is the hardest of these four questions)
2. Implement transpose without using the numpy method.
3. Implement the reshape function.
4. Implement elementwise multiply given two 2d lists.


Extra Credit (> 2 dimensional data, yes this is used! Look into tensors)
===========================
1. Create a random 3d tensor with 2 slices, 3 rows and 4 columns (you should create it just like you create a matrix except there's an extra dimension!)
2. Sum the 2 slices of the tensor.
