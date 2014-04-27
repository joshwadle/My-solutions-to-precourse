SQL
===

## Install SQLite
If you are running Mac or GNU/Linux, you probably already have SQLite3 installed.
Try running it in the terminal.

    sqlite3

If it's not installed, check your package manager; it might be called "sqlite" or "sqlite3".

If you're on Windows, download the Windows binaries from [here](http://www.sqlite.org/download.html).

More directions are [here](http://mislav.uniqpath.com/rails/install-sqlite3/).

## Basic commands
Then run it.

```sh
sqlite3 beds.sqlite
```

Display headers

    .header on

A single SQLite3 database can contain many tables. List the tables.

    .tables

Show a table schema

    .schema beds

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

## More
Do exercises 1 to 12 of [Learn SQL the Hard way](http://sql.learncodethehardway.org/book/).
