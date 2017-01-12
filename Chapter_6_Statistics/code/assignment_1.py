import numpy as np
import scipy.stats as scs

def get_mean(lst):
    """INPUT:
    - lst as list of int/float

    OUTPUT:
    - mean value of the input list (FLOAT)

    Hint: Don't use np.mean().
    """
    pass

def get_median(lst):
    """INPUT:
    - lst as list

    OUTPUT:
    - median value of the input list (FLOAT)

    Hint: Don't use np.median().
    """
    pass

def get_mode(lst):
    """INPUT:
    - lst as list

    OUTPUT:
    - mode value of the input list (FLOAT)

    Hint: Don't use scs.mode().
    """
    pass

def get_range(lst):
    """INPUT:
    - lst as list

    OUTPUT:
    - range of the input list (FLOAT)
    """
    pass

def get_IQR(lst):
    """INPUT:
    - lst as list

    OUTPUT:
    - the interquartile range of the input list (FLOAT)

    Hint: you may use np.percentile
    """
    pass

def remove_outliers(lst):
    """INPUT:
    - lst as list

    OUTPUT:
    - sorted lst with any data points 3 interquartile range below Q1
    (25th percentile) or 3 interquartile range above Q3 (75th percentile)
    """
    pass

def run_check(lst):
    print('Mean: ', get_mean(lst) == np.mean(lst))
    print('Median: ', get_median(lst) == np.median(lst))
    print('Mode: ', get_mode(lst) == scs.mode(lst).mode[0])

def print_summary_metrics(lst):
    print('*' * 50)
    print(' '*16 + 'Summary statistics')
    print('*' * 50)
    print('mean: {} | median: {} | mode: {}'.format(get_mean(lst),
                                                    get_median(lst),
                                                    get_mode(lst)))
    print('range: {} | IQR: {}'.format(get_range(list_nums),get_IQR(list_nums)))
    print('\n')
    print('original list: \n          {}'.format(lst))
    print('sorted list: \n          {}'.format(sorted(lst)))
    print('List without outliers: \n          {}'.format(\
                                                    remove_outliers(list_nums)))

if __name__ == '__main__':
    list_nums = [100, 9, 4, 7, 22, 37, 44, 22, 79, 88, 200, 37, 22, 1000]
    run_check(list_nums)
    print_summary_metrics(list_nums)
