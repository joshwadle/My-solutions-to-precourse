# Programming with Python (we will be using version 2.x)

The course will heavily use Python for most of its analyses/projects.  It is not necessary to be an expert in Python coming into the course (that is what we will teach you!) but it is helpful to be familiar with it's syntax.

Not everyone knows Python (or what parts to focus on it in the classroom).  We have provided resources here to get any student familiar with another programming language up to speed with Python quickly (both in terms of syntax and style).  __At Zipfian we teach Python 2.x (specifically 2.7)__

## Installing

We use the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python 2.7 (not Python 3) distribution and use [conda](http://www.continuum.io/blog/conda) to install any additional packages.

## Assignment
Run `python` from a terminal, and you'll get to a Python
terminal where you can test out Python interactively.
You can exit with control-D or `exit`.

There's a better terminal called IPython. Run `ipython` to enter it.

Within the IPython terminal, you can type "`%run <filename>`"
to effectively copy the contents of a file into the terminal.

    In [1]: %run example.py
    
    In [2]: example()
    Hi
    
    In [3]: 

You can do something quite similar from an ordinary shell. If you write 
some Python code in a file, then run `python` on the file, the same thing
happens, except that the Python session ends right after the file is run;
that is, it's as if you copied the contents of the file into the terminal
and then closed the terminal.

### Python language
You can load the contents of a file with `open(<filename>).read()`. For example,
this prints the current file

```python
readme = open('readme.md').read()
print readme
```

Split a string into a list of strings with `.split`.

```python
readme = open('readme.md').read()
print readme.split('\n')
```

You can use the `.replace` method replace text within a string variable.

```python
dawg = 'Yo dawg, I heard u like NNS so we put a NN in yur NN so u can VB while you VB.'
print dawg.replace('NNS', 'cars').replace('NN', 'car').replace('VB', 'drive')
```

You load other python files with `import`.
You can use this to load other files.

    In [1]: import example
    
    In [2]: example.example()
    Hi
    
    In [3]: 

You can also use this to load system-wide libraries.

    In [1]: import string
    
    In [2]: print string.ascii_letters
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    In [3]: 

### Berkeley Bootcamp

Please follow along and complete the exercises/assignments from the Berkeley Python [bootcamp](http://www.pythonbootcamp.info/schedule).  This will get you up to speed on all of the scientific libraries we will be using.  

Also complete the scikit-learn [tutorial](https://github.com/jakevdp/sklearn_pycon2014) and pandas [workshop](http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb) ([video](https://vimeo.com/79835526))

## References
No need to Read these -- use them to look up anything the exercise covers that you do not know

* [Python introduction](http://docs.python.org/2/tutorial/introduction.html)
* [Intro to Python notebook](http://nbviewer.ipython.org/urls/bitbucket.org/amjoconn/watpy-learning-to-code-with-python/raw/3441274a54c7ff6ff3e37285aafcbbd8cb4774f0/notebook/Learn%20to%20Code%20with%20Python.ipynb)
* [Python Docs](http://docs.python.org/2/)
* [IPython docs](http://ipython.org/ipython-doc/rel-0.13.1/index.html)
* [Think Python](http://www.greenteapress.com/thinkpython/thinkpython.pdf)
* [Scipy Lectures](http://scipy-lectures.github.io/)
