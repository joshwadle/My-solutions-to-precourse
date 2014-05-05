# SQL

Structured Query Language (SQL) is used to interact with data stored in
relational databases.

There are many relational databases (PostgreSQL, MySQL, etc.) but they all share
SQL as a query language. We'll be using SQLite.

## Install SQLite
If you are running Mac or GNU/Linux, you probably already have SQLite3 installed.
Try running it in the terminal.

    sqlite3

If it's not installed, check your package manager; it might be called "sqlite" or "sqlite3".

If you're on Windows, download the Windows binaries from [here](http://www.sqlite.org/download.html).

More directions are [here](http://mislav.uniqpath.com/rails/install-sqlite3/).

## Basic commands

```sh
$ sqlite3 beds.sqlite
```

Display headers

    >> .header on

A single SQLite3 database can contain many tables. List the tables.

    >> .tables

Show a table schema

    >> .schema beds

Get the whole table. (This will take a while.)

```sql
SELECT * FROM beds;
```

Get the first ten records.

```sql
SELECT * FROM beds LIMIT 10;
```

Count how many records there are.

```sql
SELECT count(*) FROM beds;
```

Count how many rows are XXX

```sql
SELECT count(*) FROM beds WHERE Facility_ID = 28321;
```

Order

```sql
SELECT * FROM beds ORDER BY Bed_Census_Date;
```

## Assignment
* [SQL Zoo](http://sqlzoo.net/wiki/Main_Page): tutorials 1-7 

## Additonal Resources
* [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/).
