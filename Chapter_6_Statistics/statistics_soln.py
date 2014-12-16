import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)

# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A list of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The list containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A list that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    return np.random.choice(population, size=n)


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The list of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    return np.sum(lst) / len(lst)

def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [The list of numbers, either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    lst_mean = get_mean(lst)
    if sample:
        lst_variance = np.sum(np.square(lst - lst_mean)) / (len(lst) - 1)
    else:
        lst_variance = np.sum(np.square(lst - lst_mean)) / len(lst)

    return lst_variance

def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    var = get_variance(sample)
    sem = np.sqrt(var / len(sample))
    return sem

def get_confidence_interval(sample, confidence=.95):
    """INPUT:
    - sample(NUMPY ARRAY)
    - confidence(FLOAT) [The confidence of the ci from 0 to 1, usually .95]

    OUTPUT:
    - (tuple) [mean, mean - half_rng, mean + half_rng]
    """
    sem = get_sem(sample)
    mean = get_mean(sample)
    half_rng = sem * scs.t.ppf((1 + confidence) / 2., len(sample)-1)
    return mean, mean - half_rng, mean + half_rng


def get_interquartile_range(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - iqr(FLOAT) [Interquartile range]
    """
    q1, q3 = np.percentile(population, [25., 75.])
    return q3 - q1


def get_outlier(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - outliers(NUMPY ARRAY) [List of outliers]
    """
    q1, q3 = np.percentile(population, [25., 75.])
    print q1, q3
    rng_val = get_interquartile_range(population) * 3
    return population[(population < (q1 - rng_val)) | (population > (q3 + rng_val))]


if __name__ == '__main__':
    population = load_pickle('population.pkl')
    print 'First 10 element of the population: ', population[:5]
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)


    print get_mean(sample_100)
    print get_mean(sample_1000)
    print '--------'
    print get_variance(sample_100)
    print get_variance(sample_1000)
    print 'SEM  --------------------'
    print get_sem(sample_100)
    print get_sem(sample_1000)
    print '---------------------'
    print get_confidence_interval(sample_100)
    a,b,c = get_confidence_interval(sample_1000, confidence=0.95)
    print '95 CI:', c - b
    a2,b2,c2 = get_confidence_interval(sample_1000, confidence=0.7)
    print '70 CI:', c2 - b2
    print '--------'
    print get_outlier(population)

