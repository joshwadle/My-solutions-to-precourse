# Chapter 5 Pandas
<br>
## Chapter 5 Instructions
In this chapter you will be answering  **the same exact questions you answered in the SQL chapter, but by using Pandas instead of SQL.**  <br>
*Fill in your answers in the functions provided  `assignment.py` file. *


## The Data To Use
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
Choose a nursing home ("Facility"), and subset the data by that nursing home.  Answer the following using **Pandas**.  

**Fill your answers in the provided assignment.py file.**

* The count of how many censuses were reported
* The earliest census date
* The latest census date
* The ten census dates with the highest number of available beds for that nursing home
* The ten census dates with the lowest number of available beds for that nursing home

<br>

## Getting started with Pandas
Pandas main workhorse is the Pandas DataFrame. A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.).

*The DataFrame has both a row and column index;* it can be thought of kind of like collection of dictionaries that have BOTH vertical and horizontal keys.  The vertical key is the like the column, all the horizontal key is like the index.  
## A simple starterfile.

```python
import pandas as pd
import numpy as np

df = pd.read_csv('example.csv', delimiter='|' )
print df.head()
```
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>Date</th>
<th>Outlook</th>
<th>Temperature</th>
<th>Humidity</th>
<th>Windy</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td> 07-01-2014</td>
<td>    sunny</td>
<td> 85</td>
<td> 85</td>
<td> False</td>
<td> Don't Play</td>
</tr>
<tr>
<th>1</th>
<td> 07-02-2014</td>
<td>    sunny</td>
<td> 80</td>
<td> 90</td>
<td>  True</td>
<td> Don't Play</td>
</tr>
<tr>
<th>2</th>
<td> 07-03-2014</td>
<td> overcast</td>
<td> 83</td>
<td> 78</td>
<td> False</td>
<td>       Play</td>
</tr>
<tr>
<th>3</th>
<td> 07-04-2014</td>
<td>     rain</td>
<td> 70</td>
<td> 96</td>
<td> False</td>
<td>       Play</td>
</tr>
<tr>
<th>4</th>
<td> 07-05-2014</td>
<td>     rain</td>
<td> 68</td>
<td> 80</td>
<td> False</td>
<td>       Play</td>
</tr>
</tbody>
</table>
</div>


## Loading data using Pandas
`df = pd.read_csv('filename.csv')`
Load delimited data from a file, URL, or file-like object. Use comma as default delimiter.

`df = pd.read_table()`
Load delimited data from a file, URL, or file-like object. Use tab ('\t') as default delimiter

`pd. read_fwf()` Read data in fixed-width column format (that is, no delimiters)

`pd.read_clipboard()` Create a dataframe from your own damn cliboard!!! _wtf! im seriously_


`df.to_csv('output.csv', sep='|', index=False, header=False )` Using DataFrame’s to_csv method, we can write the data out to a comma-separated file:

# DataFrame Essentials
Below is a collection of panda things I use  like 80% of the time.  In addition, is also a list of those annyoing things I kept on having to look up now all in one place. Please, together we can make data cleaning as  easy as sunday morning, if we all contribute just _one_ entry today, this resource will be 22 times better.  

I get the best use of this page just by hitting  `command+F` on my keyboard, and typing the name of the thing I am looking for.
## Functions I use all the time.
<table border="1" class="dataframe" style="overflow:visible";>
<thead>
<tr style="text-align: right;">
<th></th>
<th>Pandas function</th>
<th>WHAT IT DOES</th>
</tr>
</thead>
<tbody>
<tr>
<th>0 </th>
<td>                               import pandas as pd</td>
<td>                              imports pandas as pd</td>
</tr>
<tr>
<th>1 </th>
<td>              df = pd.read_csv('path-to-file.csv')</td>
<td>                             load data into pandas</td>
</tr>
<tr>
<th>2 </th>
<td>                                      df.head( 5 )</td>
<td>    prints the first n lines. in this case 5 lines</td>
</tr>
<tr>
<th>3 </th>
<td>                                          df.index</td>
<td>               prints the index of your dataframe </td>
</tr>
<tr>
<th>4 </th>
<td>                                        df.columns</td>
<td>              prints the columns of your dataframe</td>
</tr>
<tr>
<th>5 </th>
<td>                               df.set_index('col')</td>
<td> make the index (aka row names) the values of a...</td>
</tr>
<tr>
<th>6 </th>
<td>                                  df.reset_index()</td>
<td>                                       reset index</td>
</tr>
<tr>
<th>7 </th>
<td>           df.columns = ['new name1', 'new name2']</td>
<td>                                       rename cols</td>
</tr>
<tr>
<th>8 </th>
<td> df = df.rename(columns={'old name 1': 'new nam...</td>
<td>                               rename specific col</td>
</tr>
<tr>
<th>9 </th>
<td>                                         df['col']</td>
<td>                                selects one column</td>
</tr>
<tr>
<th>10</th>
<td>                            df[ ['col1', 'col2'] ]</td>
<td>                          select more than one col</td>
</tr>
<tr>
<th>11</th>
<td>                                     df['col'] = 1</td>
<td>                     set the entire col to equal 1</td>
</tr>
<tr>
<th>12</th>
<td>                          df['empty col'] = np.nan</td>
<td>                              make an empty column</td>
</tr>
<tr>
<th>13</th>
<td>              df['col3'] = df['col1'] + df['col2']</td>
<td> create a new col, equal the the sum of other cols</td>
</tr>
<tr>
<th>14</th>
<td>                                          df.ix[0]</td>
<td>                                      select row 0</td>
</tr>
<tr>
<th>15</th>
<td>                                      df.ix[5:100]</td>
<td>                         select rows 5 through 100</td>
</tr>
<tr>
<th>16</th>
<td>                                    df.ix[[1,2,3,4]]</td>
<td>                           select rows 1,2,3 and 4</td>
</tr>
<tr>
<th>17</th>
<td>                                   df.ix[0]['col']</td>
<td>        select row and column, reterive cell value</td>
</tr>
<tr>
<th>18</th>
<td>                                     del df['col']</td>
<td>                 delete or drop or remove a column</td>
</tr>
<tr>
<th>19</th>
<td>                            df.drop('col', axis=1)</td>
<td>                 delete or drop or remove a column</td>
</tr>
<tr>
<th>20</th>
<td>                                    df.drop('row')</td>
<td>                    delete or drop or remove a row</td>
</tr>
<tr>
<th>21</th>
<td>            df = df.sort('col', ascending=False)\n</td>
<td>                    sort data frame on this column</td>
</tr>
<tr>
<th>22</th>
<td>         df.sort(['col', 'col2'], ascending=False)</td>
<td>                   sort data by col1, then by col2</td>
</tr>
<tr>
<th>23</th>
<td>                              solo_col = df['col']</td>
<td>             make a variable that is equal the col</td>
</tr>
<tr>
<th>24</th>
<td>                    just_values = df['col'].values</td>
<td>   returns an array with just the values, NO INDEX</td>
</tr>
<tr>
<th>25</th>
<td>                  df[ (df['col'] == 'condition') ]</td>
<td>          return df when col is equal to condition</td>
</tr>
<tr>
<th>26</th>
<td> df[ (df['col 1'] == 'boobies') &amp; (df['col 2'] ...</td>
<td> return df when one col meets this condition AN...</td>
</tr>
<tr>
<th>27</th>
<td> df['col'][ (df['col1'] == 'this') &amp; (df['col2'...</td>
<td> set col1 to new value when col1 == this, and c...</td>
</tr>
<tr>
<th>29</th>
<td>                           df.groupby('col').sum()</td>
<td> group by groupby a column and SUM all other (t...</td>
</tr>
<tr>
<th>30</th>
<td> df.plot(kind='bar')  **kind= 'bar' or 'line' o...</td>
<td>                                   make a bar plot</td>
</tr>
<tr>
<th>32</th>
<td>                         alist = df['cols'].values</td>
<td> extract just the values of a column into a lis...</td>
</tr>
<tr>
<th>33</th>
<td>                         a_matrix = df.as_matrix()</td>
<td> extract just the values of a whole dataframe a...</td>
</tr>
<tr>
<th>34</th>
<td>                                   df.sort(axis=1)</td>
<td> sort by column names ie; if your df columns we...</td>
</tr>
<tr>
<th>35</th>
<td>                           df.sort('col' , axis=0)</td>
<td> will sort by the 'col' column with lowest vals...</td>
</tr>
<tr>
<th>36</th>
<td>           df.sort('col' , axis=0, ascending=True)</td>
<td> will sort by the 'col' column with highest val...</td>
</tr>
<tr>
<th>37</th>
<td>           df.sort( ['col-a', 'col-b'], axis = 0) </td>
<td>                      sort by more than one column</td>
</tr>
<tr>
<th>38</th>
<td>                                   df.sort_index()</td>
<td>              this will sort the index, your index</td>
</tr>
<tr>
<th>39</th>
<td>                         df.sort_index(by='col-a')</td>
<td> this is the same thing as just doing df.sort('...</td>
</tr>
<tr>
<th>40</th>
<td>                                         df.rank()</td>
<td> it keeps your df in order, but ranks them in w...</td>
</tr>
<tr>
<th>41</th>
<td> df = pd.DataFrame( {'col-a': alist, 'col-b': o...</td>
<td> how to put or how to insert a list into a data...</td>
</tr>
<tr>
<th>42</th>
<td>                                         df.dtypes</td>
<td> will print out the type of value that is in ea...</td>
</tr>
<tr>
<th>43</th>
<td>                    df['float-col'].astype(np.int)</td>
<td> will change columns data type.  np.int stands ...</td>
</tr>
<tr>
<th>44</th>
<td>                        joined = dfone.join(dftwo)</td>
<td>  join two dataframes if the keys are in the index</td>
</tr>
<tr>
<th>45</th>
<td>     merged = pd.merge(dfone, dftwo, on='key col')</td>
<td> merge two dataframes on a similar column or a ...</td>
</tr>
<tr>
<th>46</th>
<td>                pd.concat([dfone, dftwo, series3])</td>
<td> like, append data to the end of a dataframe, t...</td>
</tr>
<tr>
<th>47</th>
<td>        pd.concat([dfone, dftwo, series3], axis=1)</td>
<td> append data but as columns, like, this will ma...</td>
</tr>
</tbody>
</table>


    ## Navigating the df

    *  ```df['colname']  ``` <br>
    Select single column or sequence of columns from the DataFrame.

    *  ```df.ix[val]```  <br> Selects single row of subset of rows from the DataFrame.

    * ```df.ix[:, val]``` <br>
    Selects single column of subset of columns.


    * df.ix[val1, val2] <br>
    Select both rows and columns.

    * df.reset_index() <br>
    Conform one or more axes to new indexes.

    * df.xs() <br>
    Select single row or column as a Series by label.

    * df.icol() , df.irow() <br>
    Select single column or row, respectively, as a Series by integer location.

    * df.get_value(), df.set_value() <br>
    Select single value by row and column label.
    ___
    <br>

    ## Unique Values, Value Counts, and Conditional Selecting are so handy all the time

    ```
    In [217]: obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

    In [218]: uniques = obj.unique()
    In [219]: print uniques
    Out[219]:
    array([c, a, d, b], dtype=object)

    In [220]: print obj.value_counts()
    Out[220]:
    c 3
    a 3
    b 2
    d 1

    In [222]: mask = obj.isin(['b', 'c'])
    In [223]: print mask
    0 False
    1 False
    2 False  
    3 False
    4 False
    5 True
    6 True


    In [224]: print obj[mask]
    Out[224]:
    0 c
    5 b
    6 b
    7 c
    8 c

    ```
    ---

    <br>





    ## Applying a function to a column
    Function application and mapping p132
    ```python
    texts['Weight'] = texts['msg'].apply(lambda x: len(str(x)))
    texts['Weight'] = texts['Weight'].astype(int)
    ```

    <br>
    ## How to convert a column to a datetime object
    ```python
    texts['dt'] = pd.to_datetime(texts['dt'])
    texts['hr'] = texts['dt'].apply(lambda x: x.strftime('%H'))

    ```

    ## Sorting and ranking p133

    ## Computing Descriptive Statistics p137
    Just look at all these rad math things you can do with the columns in your dataframe...
    > ![alt text](images/summary-stats.png "Page p139 yo")

    ___


    ## Filtering Out Missing Data p144

    > ![alt text](images/dropNA.png "Yooo, this is all on Chapter 5: Getting Started with pandas   p144")
    ```
    In [234]: from numpy import nan as NA
    In [235]: data = pd.Series([1, NA, 3.5, NA, 7])
    In [236]: data.dropna()
    Out[236]:
    0 1.0
    2 3.5
    4 7.0
    ```

    <br>
    <br>

## Loading in data files, and saving / exporting data in pandas.  
    `pd.read_csv('filename.csv')`
    Load delimited data from a file, URL, or file-like object. Use comma as default delimiter.

    `pd.read_table()` Load delimited data from a file, URL, or file-like object. Use tab ('\t') as default delimiter

    `pd. read_fwf()` Read data in fixed-width column format (that is, no delimiters)

    `pd.read_clipboard()` Create a dataframe from your own damn cliboard!!! _wtf! im seriously_


    `df.to_csv('output.csv', sep='|', index=False, header=False )` Using DataFrame’s to_csv method, we can write the data out to a comma-separated file:

    > > ![alt text](images/reading-csvs.png "Yooo, this is all on Chapter 5: Getting Started with pandas   p144")




    <br>
    ___

    <br>
    ## A simple starterfile.  

    ```python
    import pandas as pd
    import numpy as np

    df = pd.read_csv('data/playgolf.csv', delimiter='|' )
    print df.head()
    ```




    > <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: right;">
    <th></th>
    <th>Date</th>
    <th>Outlook</th>
    <th>Temperature</th>
    <th>Humidity</th>
    <th>Windy</th>
    <th>Result</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>0</th>
    <td> 07-01-2014</td>
    <td>    sunny</td>
    <td> 85</td>
    <td> 85</td>
    <td> False</td>
    <td> Don't Play</td>
    </tr>
    <tr>
    <th>1</th>
    <td> 07-02-2014</td>
    <td>    sunny</td>
    <td> 80</td>
    <td> 90</td>
    <td>  True</td>
    <td> Don't Play</td>
    </tr>
    <tr>
    <th>2</th>
    <td> 07-03-2014</td>
    <td> overcast</td>
    <td> 83</td>
    <td> 78</td>
    <td> False</td>
    <td>       Play</td>
    </tr>
    <tr>
    <th>3</th>
    <td> 07-04-2014</td>
    <td>     rain</td>
    <td> 70</td>
    <td> 96</td>
    <td> False</td>
    <td>       Play</td>
    </tr>
    <tr>
    <th>4</th>
    <td> 07-05-2014</td>
    <td>     rain</td>
    <td> 68</td>
    <td> 80</td>
    <td> False</td>
    <td>       Play</td>
    </tr>
    </tbody>
    </table>
    </div>
    ___

    <br>
    <br>
    ## Visually what grouping does

    ![alt text](images/pandas_groupby_visual.jpg "The apples.csv file is located in the data folder if you care to see for yourself")
    ___

    # What you can do to a groupby object!
    ```python
    In [22]: gb = df.groupby('gender')
    In [23]: gb.<TAB>
    gb.agg        gb.boxplot    gb.cummin     gb.describe   gb.filter     gb.get_group  gb.height     gb.last       gb.median     gb.ngroups    gb.plot       gb.rank       gb.std        gb.transform
    gb.aggregate  gb.count      gb.cumprod    gb.dtype      gb.first      gb.groups     gb.hist       gb.max        gb.min        gb.nth        gb.prod       gb.resample   gb.sum        gb.var
    gb.apply      gb.cummax     gb.cumsum     gb.fillna     gb.gender     gb.head       gb.indices    gb.mean       gb.name       gb.ohlc       gb.quantile   gb.size       gb.tail       gb.weight
    ```

    <br>
    ```
    Put a list of list into a pandas dataframe

    import pandas as pd
    main_list = [ [1,2,3,4, 'cheese'], [99,23,33,44, 'rubber']]

    df = pd.DataFrame()
    for i, row in enumerate(main_list):
    df[i] = main_list[i]
    df.T

    '''

    0	1	2	3	4
    0	1	2	3	4	cheese
    1	99	23	33	44	rubber
    '''
    ```

    <br>

    ## Pandas Replace values in columns

    ```python
    In [25]: df = DataFrame({1: [2,3,4], 2: [3,4,5]})

    In [26]: df
    Out[26]:
    1  2
    0  2  3
    1  3  4
    2  4  5

    In [27]: df[2]
    Out[27]:
    0    3
    1    4
    2    5
    Name: 2

    In [28]: df[2].replace(4, 17)
    Out[28]:
    0     3
    1    17
    2     5
    Name: 2

    In [29]: df[2].replace(4, 17, inplace=True)
    Out[29]:
    0     3
    1    17
    2     5
    Name: 2

    In [30]: df
    Out[30]:
    1   2
    0  2   3
    1  3  17
    2  4   5
    ```



    ## PANDAS HOW TO MERGE ON INDEX
    ```python

    #dataframes must have shared values in the index
    test = pd.merge(dfLeft, dfRight, left_index=True, right_index=True)
    ```
    <br>
    ## A hack to making your graphs look pretty
    >```python
    pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
    plt.rcParams['figure.figsize'] = (15, 5)
    ```
    ___

    <br>
    # Student contributions

    Sonaliii says:  How to get dataframe dimensions

    > How to get dataframe dimensions
    ```python
    In [44]: print dfBatting.shape
    Out[44]: (97889, 24)
    ```
    ___

    <br>
    Nhan Nguyen aka Nhan Bread says: Replacing NaN with 0

    > adding .fillna(0) will replace NaN values with 0 or whatever you specify in the brackets.
    ```python
    dfBatting = dfBatting.fillna(0)
    ```
    ___

    <br>
    Homeboy Roy says: Selecting names that start with z (or values that match some criterion)
    >An often useful thing to do is select values from a data frame that meet some arbitrary condition. One student asked how we could select just the players whose names start with z. You can do that like this:
    ```python
    dfBatting[dfBatting['playerID'].apply(lambda x: x[0] == 'z')]
    ```
    The expression inside the outer brackets creates a Boolean array of True/False, and only selects the rows that are True.
    ___

    <br>

    Zen Ben & Appalling Paul The Apple Snapper tell us how How to expand table output to include all columns w/o [...]:
    >You set options for pandas, there are a number of options you can change, general format is:
    pd.set_option('option',new value)
    to change number of columns in output:
    ```python
    pd.set_option('display.max_columns',50)
    ```
    Here's a link that explains the different options: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html
    ___

    <br>
    Slogan Logan tells us how to count:  
    >To see the counts of all distinct value within a column you can use the format dataframe.column.value_counts().
    ```python
    dfBatting.playerID.value_counts()
    ```
    ___

    <br>
    KatherineYu aka KatherineYu: merging without repeating columns:

    >```python
    colsToUse_fromSals = list(dfSals.columns - dfB.columns)+['yearID','playerID']
    dfBatSals = pd.merge(dfB, dfSals[colsToUse_fromSals], how = 'inner', on = ['yearID', 'playerID'])
    cols_to_use = df2.columns - df.columns
    dfNew = merge(df, df2[cols_to_use.tolist()], left_index=True, right_index=True, how='outer')
    ```
    http://stackoverflow.com/questions/19125091/pandas-merge-how-to-avoid-duplicating-columns
    ___

    <br>
    Jlippi & Tony Tony Tony say reading HTML tables:
    > we were trying to pull statistics off the interwebs.. I found if it's in a table format, I could right click-> inspect element (in chrome), 'copy as HTML' and paste the table into a file. then I could do:
    ```python
    salaries = pd.read_html('data/salaries.html')
    salaries[0]
    ```
    ___

    <br>
    Router Wouter says casting column to list:
    > You can create a list of column entries using this:
    ```python
    col_list = list( all2001['playerID'] )
    ```


    ___
    <br>
    Zack Says
    > how to load multiple files into one dataframe

    ```python
    import pandas as pd
    import os
    import sys

    files = os.listdir(os.curdir + '/extra_data/')  #since the data in located in a folder called extra_data.
    lst_of_dfs = []

    for f in files:
    tmp = pd.read_csv( ('extra_data/%s'% f) )
    num_rows += len(tmp)
    lst_of_dfs.append(tmp)

    df = pd.concat(lst_of_dfs, keys=['Clev', 'Hungry', 'LongB', 'Siwss'])
    print len(df)  # should be the same length of of num_rows
    ```

    <br>
    ___
    <br>
    ### How to group time data
    groupby time data, resample, dealing with dates, datetime

    ```python
    import pandas as pd
    df = pd.read_csv('data/nasa_log_july.tsv', delimiter='\t')

    #CONVERT STRING TO DATETIME OBJECT
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])  

    #SET THE DATETIME OBJECT TO YOUR BE YOUR INDEX
    # VERY IMPORT THAT YOUR DATETIME OBJECT IS YOUR INDEX
    df = df.set_index('Timestamp')

    # df.resample() == df.groupby()       (not excatly, but close enough)
    # YOU CAN THINK OF LIKE  df.groupby()
    # RUEL CAN BE   rule='D'<for day> , rule='Y', rule='M' for month, or rule='5min' <for 5 min chunks>
    grouped_dataframe = df.resample(rule='1min', how='count')

    ```
