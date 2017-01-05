# Assignment: Recap and solve without the mouse

## Objectives
We will be using some of the notions we have learned in this chapter to follow a typical Galvanize git workflow. Please do not use the mouse, rely on keyboard shortcuts.

_______________________________________

## Questions

Below is a script that you should follow. In the [Answers](#answers) section, type out the commands you needed to run to achieve the goals described in the script
<ol>
  <li> Open an iTerm2 window. Use spotlight!
  </li>
  <li> Make a directory 'Assignment6' on your Desktop. Inside this directory, create a 'data' directory, a 'code' directory.
  </li>
  <li> Make 'Assignment6' a git repository.
  </li>
  <li> Use Atom to create a 'my_script.py' in the 'code' directory.
  </li>
</ol>
```python
#my_script
def my_function(first_name, mood_today):
  '''
  parameters
  ----------
  first_name: as STR
  mood_today: as STR
  '''
  return "Hello, my name is {}, and I'm feeling {}.".format(first_name, mood_today)

print my_function('John', 'happy')
```
<ol start="5">
  <li> Commit the changes to the repository.
  </li>
  <li> Run the script in the terminal.
  </li>
  <li> This script is not ideal. there should really be a if " __name__ == '__main__' " " block. Add that block.
  </li>
  <li> Run the script again. Once it works, commit the changes.
  </li>
  <li> Let's use the repl approach and open ipython. We will then import my_script as a module.
  </li>
  <li> Let's test 'my_function' with your own arguments.
  </li>
  <li> Let's be polite, go back to your Atom file and modify the function.
  </li>
</ol>
```python
def my_function(first_name, mood_today):
  '''
  parameters
  ----------
  first_name: as STR
  mood_today: as STR
  '''
  return "Hello, my name is {}, and I'm feeling {}. Thank you for asking!".format(first_name, mood_today)
```
<ol start="12">
  <li>. Check that the autoreload magic happened by calling `my_function` again. Exit out of iPython.
  </li>
  <li> Make a new markdown 'readme.md' file in the Assignment6 directory.
  </li>
</ol>
```
# Practice with keyboard shortcuts

## Goal
I will not rely on my mouse.

## Assessment
So far, so good!
```
<ol start="14">
  <li> Create a new script 'my_numpy_script.py' in the 'code directory'.
  </li>
</ol>
```python
#my_numpy_script
import numpy

def summing_lists(list1, list2):
  return list1 + list2

def summing_arrays(array1, array2):
  return array1 + array2

if __name__ == '__main__':
  list_A = [1,2,3]
  list_B = [4,5,6]

  array_A = numpy.array(list_A)
  array_B = numpy.array(list_B)

  print 'Summing lists'
  print summing_lists(list_A, list_B)

  print '\n' + 'Summing arrays'
  print summing_arrays(array_A, array_B)
```
<ol start="15">
  <li> We are going to be using a module, numpy. Let's make sure the package is installed. (Do you remember what to do if it is not installed? What if it is not available in the Anaconda distribution?)
  </li>
  <li> Run the script. We'll get into numpy in later chapters!
  </li>
  <li> Look at the content of the 'code' directory.
  </li>
  <li> Commit changes to the scripts, but do not commit the readme.md.
  </li>
  <li> Let's delete the readme.md file.
  </li>
  <li> Look at the log of your commits to make sure your commit messages are meaningful..
  </li>  
</ol>
_______________________________________

## Answers
YOUR ANSWER
