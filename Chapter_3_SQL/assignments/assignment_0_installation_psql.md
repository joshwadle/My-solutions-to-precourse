# Assignment: SQL on simple tables

## Objectives

Setting up PostgreSQL. You should follow the instructions below to install. There are no answers to return, just make sure you have PostgreSQL ready to go!

_______________________________________

## Resources

Here's the [postgres docs](http://www.postgresql.org/docs/9.3/interactive/).

_______________________________________

## Install PostgreSQL

### Homebrew installation
Homebrew is a package management software on Apple's macOS.
 
1. Install brew cask.

    * Install brew (you should already have it installed -- see Chapter 0). Instructions [here](http://brew.sh/)
    * Install brew cask with: `brew install caskroom/cask/brew-cask`

    If you already have them, update: `brew update && brew upgrade brew-cask`

2. Install your Postgres database. The easiest way to to install the pre-build application (with an adorable icon) using the following command:

    ```
    brew cask install postgres
    ```

3. After the installation is complete, use Spotlight to search for `postgres` and open the Application. It will ask you if you want to move it to the Applications folder, say "Move it"


### Setting up psql on a Mac

You will often be following the following steps, they are explained more in details in the Chapter 0 - Workflow.

1. Go to the home directory by running `cd` in the terminal

2. Open terminal configurations by typing `atom ~/.bash_profile`

3. Insert the following line at the end of the file and save the file.

   ```export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH```

   Make sure to copy paste this line exactly.

4. Open a new terminal and run `psql`. You should not have any error message.
