Project: New York State Nursing Home Weekly Bed Census
===

## Data
This directory contains New York State's
[nursing home weekly bed census](https://health.data.ny.gov/Health/Nursing-Home-Weekly-Bed-Census-Beginning-2009/uhyy-xp9s?)
in a few different formats.

* `beds.csv` is a comma-delimited file
* `beds.json` is JSON
* `beds.tsv` is tab-delimeted
* `beds.sqlite` is a SQLite3 database.

(The first two of these came directly from the data portal,
and we converted the CSV to the other two formats.)

## Assignment
Choose a nursing home ("Facility"), and subset the data by that nursing home.
Find the following in Python then SQL.

* The count of how many censuses were reported
* The earliest census date
* The latest census date
* The ten census dates with the highest number of available beds for that nursing home
* The ten census dates with the lowest number of available beds for that nursing home

## Extra credit

* Do the project exclusively with UNIX shell commands
* Use Python to make plots, fit models, or do other analyses
