# Zipfian Academy Precourse Curriculum

__Goal: to get you ready to jump into our curriculum on day 1.__

Please read this entire document before getting started on the following
sections.

You'll be going through several readings and tutorials and ultimately submitting
several assigments, the most important of which is a short project to be done in
Python and SQL.

Progress through the following sections in any order you'd like. Make sure
you complete the work in the "Assignment" section of each document.

1. [shell](assignment/shell.md)
1. [Python](assignment/python.md)
1. [git](assignment/git.md)
1. [SQL](assignment/sql.md)
1. [Project](project/readme.md)
1. [Theory (math/stats/prob)](assignment/theory.md)

The most important sections for day 1 are **shell** and **Python**.

You will all be keeping a blog throughout the course. You may want to set that
up now so that you can blog about your prepration. Here are some [blogging
options]('extra/blog/readme.md').

## The Project

In order for you to get familiar with a few different languages, we'd like you
to conduct a very basic analysis in Python and SQL.  __This the best guide/test
of your knowledge for the first day of class.__

Follow the directions in the [project directory](project/readme.md), and
repeat the analysis in Python and SQL.

__NOTE: We will no longer be using R in the curriculum and you are not expected to know it__

## Submitting Assigments

You should submit the following:

1. Python code for [UNIX/Python tutorial](http://inst.eecs.berkeley.edu/~cs188/sp12/projects/tutorial/tutorial.html). There's two problems for you to submit buried in the file. You should submit `buyLotsOfFruit.py` and `shopSmart.py`
2. Solution to project in Python
3. Solution to project in SQL

### How to submit

You will submit your solutions with a git [pull request](https://help.github.com/articles/using-pull-requests). Here are step by step instructions of how to do this:

1. Fork this repository (go to https://github.com/zipfian/precourse and click "Fork")
1. [Install git](https://help.github.com/articles/set-up-git) on your computer
if you haven't already
1. Clone the repository on your computer: `git clone https://github.com/<your username>/precourse`
1. Create a directory called "solutions" and add your files to the solutions folder
1. Add your files to the repository: `git add solutions`
1. Commit your changes: `git commit -M "My solutions to precourse"`
1. Push your changes to your fork: `git push origin master`
1. Make a pull request by going to https://github.com/zipfian/precourse and clicking "Pull Requests" and then "New Pull Request"

It's good workflow to commit and push to your fork often, even when you're not done. Then you have older versions of your work in case you screw something up or lose something. We will get a notification of your submission once you submit a pull request.

If we've made changes to the repository after you forked it and you want to update your repository to reflect them, you can run this command: `git pull https://github.com/zipfian/precourse master`

## Key Tutorials

It's best to go through each of the sections above. However, at minimum, go
through these tutorials.

* [UNIX data manipulation](http://planspace.org/2013/05/21/command-line-data-manipulation/)
* [Git Immersion](http://gitimmersion.com/) (extra: Github [Pages](http://dannguyen.github.io/github-for-portfolios/))
* [Berkeley bootcamp](http://www.pythonbootcamp.info/schedule): this will get you up to speed on all of the scientific libraries we will be using.
* [pandas workshop](http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb) (with [video](https://vimeo.com/79835526))
* [SQL Zoo (with SQLite)](http://sqlzoo.net/wiki/Main_Page)
* [scikit-learn tutorial](https://github.com/jakevdp/sklearn_pycon2014) 
* [Stats/Probability](http://courses.washington.edu/css490/2012.Winter/lecture_slides/02_math_essentials.pdf)

## Extra

The `extra` directory has some references on operating systems and text editors that you might consider installing and learning. It also references some tutorials on HTML, CSS, and javascript basics.

This is the least important part of the precourse work, so skip it if you don't have time.

## Getting help
Feel free to contact us whenever you could use some help with anything in the precourse work.

Consult the [list of additional references and resources][references] if you'd
like to further cover anything.

[references]: './extra/references.md'

