# Assignment: Working with Command Lines

## Objectives
You will be using commands to create, move and rename files and directories.

If you have never used a Terminal before, follow the guided steps in [assignment_2_command_line_sample.md](assignment_2_command_line_sample.md). This will show you the commands you need to type to create directory, move them, copy files and delete them.

If you are somewhat familiar with a Terminal, figure out the right command lines to achieve the action items described below. The command lines, in the order you typed them, should be placed in the YOUR ANSWER placeholder.

A [cheatsheet](../resources/command_line_basics.md) is available to help you.

_______________________________________

## Questions

Do not use finder, just stay in the Terminal

1. Make a `testing_directory` on your Desktop.
2. Inside this directory, make a `code` directory, a `data` directory, a `raw_data` directory and a `test` directory.
3. Enter the `testing_directory` and create a `readme.md` file and a `do_not_readme.md` file with Atom.
4. Create a `simple_script.py` in the `test` directory with Atom, add the following text: `print('Hello World!')`.
5. Place the `raw_data` directory inside the `data` directory.
6. Get the new path to the `raw_data` directory.
7. Move the `simple_script.py` inside the `code` directory.
8. Rename the python script `hello_world.py`.
9. Delete the `do_not_readme.md` file.

To check your work, you can run `$ tree` in the `testing_directory`. Your output should look like this.

```
├── code
│   └── hello_word.py
├── data
│   └── raw_data
├── readme.md
└── test
```
_______________________________________

## Answers
Please indicate the commands necessary to execute steps 1-9.

YOUR ANSWER:Joshs-Air:Desktop joshwadle$ mkdir testing_directory
Joshs-Air:Desktop joshwadle$ cd testing_directory
Joshs-Air:testing_directory joshwadle$ mkdir code
Joshs-Air:testing_directory joshwadle$ mkdir data
Joshs-Air:testing_directory joshwadle$ mkdir raw_data
Joshs-Air:testing_directory joshwadle$ mkdir test
Joshs-Air:testing_directory joshwadle$ atom readme.md
Joshs-Air:testing_directory joshwadle$ atom do_not_readme.md
Joshs-Air:testing_directory joshwadle$ cd test
Joshs-Air:test joshwadle$ atom simple_script.py
Joshs-Air:test joshwadle$ cd ..
Joshs-Air:testing_directory joshwadle$ mv raw_data data/raw_data
Joshs-Air:testing_directory joshwadle$ cd data
Joshs-Air:data joshwadle$ cd raw_data
Joshs-Air:raw_data joshwadle$ pwd
/Users/joshwadle/Desktop/testing_directory/data/raw_data
Joshs-Air:raw_data joshwadle$ mv simple_script.py code/simple_script.py
mv: rename simple_script.py to code/simple_script.py: No such file or directory
Joshs-Air:raw_data joshwadle$ cd..
-bash: cd..: command not found
Joshs-Air:raw_data joshwadle$ cd ..
Joshs-Air:data joshwadle$ cd ..
Joshs-Air:testing_directory joshwadle$ mv test/simple_script.py code/simple_script.py
Joshs-Air:testing_directory joshwadle$ cd code
Joshs-Air:code joshwadle$ mv simple_script.py hello_world.py
Joshs-Air:code joshwadle$ cd ..
Joshs-Air:testing_directory joshwadle$ rm do_not_readme.md
