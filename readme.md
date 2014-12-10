# Zipfian Academy Precourse Curriculum

__Goal: to get you ready to jump into our curriculum on day 1.__

Please read this entire document before getting started on the following
sections.

You'll be going through several readings and tutorials and ultimately submitting a couple assignments, the most important of which is a short project to be done in Python and SQL.

Progress through the following sections in any order you'd like. Make sure
you complete the work in the "Assignment" section of each document.

Try to get into good habits of development early, since we will be pair programming in the class we will be standardizing on a [development workflow](workflow.md).  Please try to follow this as you complete the precourse curriculum.

1. [shell](assignment/shell.md)
1. [git](assignment/git.md)
1. [Python](assignment/python)
1. [SQL](assignment/sql.md)
1. [Project](project/readme.md)
1. [markdown tutorial](http://markdowntutorial.com/)
1. [Theory (math/stats/prob)](assignment/theory.md)
1. [Intro to Machine Learning (with sklearn)](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section6_1-Scikit-Learn.ipynb)

**Python** is probably the most important of these. **shell**, **git** and **SQL** will also be very important in week 1. The **Theory** and **machine learning** will be important for week 2.

You will all be keeping a blog throughout the course. You may want to set that
up now so that you can blog about your prepration. Here are some [blogging
options](extra/blog/readme.md).

## What to submit

You should submit the following:

1. [problems.py](assignment/python/problems.py), [words.py](assignment/python/words.py), and [fizzbuzz.py](assignment/python/fizzbuzz.py) solutions
2. Solution to project in Python
3. Solution to project in SQL
4. A readme.md file (written in Markdown) describing your approach/process to completing the project.

### How to submit

You will submit your solutions with a git [pull request](https://help.github.com/articles/using-pull-requests). Here are step by step instructions of how to do this:

1. Fork this repository (go to https://github.com/zipfian/precourse and click "Fork")
1. [Install git](https://help.github.com/articles/set-up-git) on your computer
if you haven't already
1. Clone the repository on your computer: `git clone https://github.com/<your username>/precourse`
1. Create a directory called "solutions" and add your files to the solutions folder
1. Add your files to the repository: `git add solutions`
1. Commit your changes: `git commit -m "My solutions to precourse"`
1. Push your changes to your fork: `git push origin master`
1. Make a pull request by going to https://github.com/zipfian/precourse and clicking "Pull Requests" and then "New Pull Request"

It's good workflow to commit and push to your fork often, even when you're not done. Then you have older versions of your work in case you screw something up or lose something. We will get a notification of your submission once you submit a pull request.

If we've made changes to the repository after you forked it and you want to update your repository to reflect them, you can run this command: `git pull https://github.com/zipfian/precourse master`

## The Project

In order for you to get familiar with a few different languages, we'd like you
to conduct a very basic analysis in Python and SQL.  __This the best guide/test
of your knowledge for the first day of class.__

Follow the directions in the [project directory](project/readme.md), and
repeat the analysis in Python and SQL.

__NOTE: We will no longer be using R in the curriculum and you are not expected to know it__

## Getting help
Feel free to contact us whenever you could use some help with anything in the precourse work.

Consult the [list of additional references and resources](extra/references.md) if you'd
like to further cover anything. The `extra` directory also contains some
additional references on operating systems and text editors as well as
HTML/CSS/JavaScript.
