# Chapter 7: Hypothesis Testing

### This is a short foray into hypotesis testing.

## Learning Objectives

- hypothesis testing concepts: significance level, p-value, type I erro, type II errors
- variants of the t-tests (one sample t-test, Inference for two means)
- python `scipy.stats` module, and in particular functions such as `scs.ttest_1samp` `scs.ttest_ind` or `scs.ttest_rel`

## Main Resources

- [basics of hypothesis testing](http://stattrek.com/hypothesis-test/hypothesis-testing.aspx?tutorial=ap)
- [One sample t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/one-sample-t-test), [Two sample unpaired t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/two-sample-t-test-for-comparing-two-means), [Two sample paired t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/paired-difference-t-test):

NB. Answers to some of the assignments' questions can be found in these pages.

## Assignments

#### Introduction
[Chapter 6](../Chapter_6_Statistics) covered the concept of population and sampling, we move on to use hypothesis testing to test assumptions about population parameters based on a sample from the population.

### 1. General considerations in hypothesis testing

[Assignment 1:](assignments/assignment_1_general_ht.md) Take this opportunity to go back to basics:
  - define terms used in hypothesis testing,
  - layout the 4 steps in setting up in hypothesis testing (choice of the test statistics, one vs two tailed),
  - think about the errors that you could make and make relevant choices.
Answer the questions in [assignment_1_general_ht.md](assignments/assignment_1_general_ht.md).

### 2. One sample t-tests

[Assignement 2:](assignments/assignment_2_one_sample_ttest.md) One sample t-tests are useful to investigate if a population mean is equal to the a hypothesized value. They are used for samples of continuous data (e.g. height as oppose to color). We will implement a t-test in [assignment_2.py](code/assignment_2.py) and compare it to `scipy.stats`'s `scs.ttest_1samp`.

### 3. Inference for two means

[Assignement 3:](assignments/assignment_3_two_sample_ttest.md):
- Two sample unpaired t-test: Test if 2 populations have the same mean value

- Two sample paired t-test: Test if 2 populations have the same mean value when
there is a one-to-one mapping between the 2 populations, i.e. blood pressure before
treatment and after treatment


Hint:
  - The unpaired two sample t-test function is ```scs.ttest_ind()```.
  - The paired two sample t-test function is `scs.ttest_rel()`

- PART 2.4:  
    If I told you ```sample_1``` is the hours people have worked daily before we brought in a new blend of coffee, and ```sample_2``` is after the new coffee, use the correct function to tell if we should get the new coffee. Include in your answer of how sure you are of your conclusion

- PART 2.5:  
If I told you ```sample_1``` is the hours people have worked daily at company A and ```sample_2``` is hours for people at company B, use the correct function to determine if company A or company B is more productive. Include in your answer of how sure you are of your conclusion



## Recap

## Going Further: More resources

- All the statistical test docs for `scipy` can be found [**here**](http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html)

- For more statistical `numpy` functions, see [**this**](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
