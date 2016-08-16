import sys

### Fill in each function below.

### Run "python -m doctest 3_fizzbuzz.py" at the command line to test your work.

def fizzbuzz(num, fizz, buzz):
    '''
    INPUT: int, int, int
    OUTPUT: string

    Return "Fizz" if num is divisible by fizz,
           "Buzz" if num is divisible by buzz,
           "FizzBuzz" if num is dibisible by both fizz and buzz, and
           "" otherwise

    Example:
    >>> fizzbuzz(15, 3, 5)
    'FizzBuzz'
    >>> fizzbuzz(10, 3, 5)
    'Buzz'
    >>> fizzbuzz(40, 20, 33)
    'Fizz'
    >>> fizzbuzz(15, 7, 13)
    '''

    pass

if __name__ == '__main__':
    if len(sys.argv) >= 2 and isnumeric(sys.argv[1]):
        print fizzbuzz(int(sys.argv[1]), 3, 5)
