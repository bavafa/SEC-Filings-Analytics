#!/usr/bin/env python
# coding: utf-8

# ### BAIT 508 Project 1: SEC Filings Analytics
# 
# 
# - In this assignment, you will use your Python skills (`pandas`, `matplotlib`, `for` loop, `if` condition, ...) to analyze SEC filings.
# - There are short-answer questions and visualization questions. 

# ### Import the appropriate library you need to solve the questions.

from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Please assign the variables `first_name`, `last_name`, `student_id`, and `email` with your first name, last name, student ID, and email address.


first_name = str("Meysam")
last_name = str("Bavafa")
student_id = int("########")
email = str("meysam.bavafa@gmail.com")


# ##### Question 1: Find the number of characters in this file and assign it to the `ans1` variable.
# - Download `feed_header_2017-2019.tsv` file into the same directory, where `hw1_starter.ipynb` is located. (If not, there will be an extra deduction on your grade)
# - Open `feed_header_2017-2019.tsv` file with `read-only` file mode.

ans = []

file = open("feed_header_2017-2019.tsv", "r")

ans3 = 0    # Number of lines in the file
ans2 = 0    # Number of words in the file
ans1 = 0    # Number of characters in the file
for line in file:
    line = line.strip('\t')    # Omitting tabs
    words = line.split()
    ans3 += 1
    ans2 += len(words)
    ans1 += len(line)

file.close()

# We generated ans1 above
ans.append(ans1)

# ##### Question 2: Find the number of words in the file and assign it to the `ans2` variable.
# - We consider <b>word</b> as all numbers, special characters, and text separated by white space.


# We generated ans2 above
ans.append(ans2)


# ##### Question 3: Find the number of lines in the file and assign it to the `ans3` variable.


# We generated ans3 above
ans.append(ans3)

# ### From now on, you will decide which industry area you will analyze to investigate the trend of that industry. 
# ### To do so, you will select the first digit of `SIC` code.
# 
# ##### Question 4: Divide the `student_id` by 7, and add 1 to the `remainder`. <br> $\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;$ Use `int` function to drop the decimal point. Assign its value to the `ans4` variable.

ans4 = int((student_id % 7) + 1)

ans.append(ans4)

# ### Now, you have the first digit of `SIC` that you will analyze.
# ### Please extract the rows of the following condition. 
# - Read the `tsv` using `pandas` function. 
# - Save the dataframe name as `df`.
# 
# 
# ##### Question 5: Find the shape of `df` and assign it to the `ans5` variable.
# - You need to read the file using pandas first and save it as `df`.
# - Next, filter the row based on your `ans4` value and save this filtered dataframe as `df`.
# - When you do sorting, please make `ASSIGNED-SIC` as `float` first.
# - We need rows with an `ASSIGNED-SIC` column value ranging in `[ans4*1000,(ans4+1)*1000)`.
# - Next, please sort the values that come in this range.
# - Therefore, the filtered dataframe will be `df`!
# - `ans5` value type should be `tuple`.


df = pd.read_csv('feed_header_2017-2019.tsv', sep='\t')

df = df.loc[(df['ASSIGNED-SIC'] >= ans4 * 1000) & (df['ASSIGNED-SIC'] < (ans4+1) * 1000)]

# Using astype method: https://datatofish.com/convert-string-to-float-dataframe/
df['ASSIGNED-SIC'] = df['ASSIGNED-SIC'].astype(float)

df = df.sort_values('ASSIGNED-SIC')
ans5 = df.shape
#print(ans5)
type(ans5)

ans.append(ans5)


# ##### Question 6: Please find the third most appeared `FORM-TYPE` in dataframe `df` and assign its value to the `ans6`.
# - You can find the form type information in the `FORM-TYPE` column.


# Set up an empty dict.
count_formt = {}

for i in range (len(df)):
    formt = df.iloc[i]['FORM-TYPE']
    
    # If formtype is in count_formt, increment by 1 
    if formt in count_formt.keys():
        count_formt[formt] += 1
    # O/W Add formtype to count_formt dict. with intial value 1
    else:
        count_formt[formt] = 1

ans6 = sorted(count_formt, key = count_formt.get, reverse = True)[2]

ans.append(ans6)

# ##### Question 7: How many rows are there which `CITY` value is `SEATTLE` in dataframe `df`?
# - You can find the city information in the `CITY` column.


ans7 = df['CITY'].to_list().count('SEATTLE')
# print(ans7)
ans.append(ans7)

# ##### Question 8: How many cases are the same as the first 10 digits of `ACCESSION-NUMBER` and the `CIK` column value? <br> $\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;$Please assign the total number of cases to the `ans8`.
# - `ACCESSION-NUMBER` stands for the unique Document ID.
# - Here is the example of `ACCESSION-NUMBER` : `0001193125-19-230866` 
# - The first 10 digits (`0001193125`) comprise the Central Index Key (CIK) of the entity submitting the filing.
# - This filing could be submitted by either the company or a third-party filer agent.
# - If the company submit the file, then first 10 digits will be the same as its CIK value.
# - For comparison, please convert both `CIK` value and first 10 digts of `ACESSION-NUMBER` as `integer`. 
# - For example, we do not need first three zero in the case of `0001193125`. So the number should be `1193125`.


comp_num = [uid for uid in df['ACCESSION-NUMBER']]
comp_list = []
for i in comp_num:
    comp_first = i.split('-')[0]
    comp_list.append(int(comp_first))     

df['CIK-COMPARE']=comp_list
df['ans8']= np.where(df['CIK-COMPARE'] == df['CIK'], 1, 0)
ans8 = df['ans8'].to_list().count(1)

ans.append(ans8)

# ### From questions 9 to 12, you will analyze the feature of the company name.
# ### To solve questions 9~ 12, you need to use the `CONFORMED-NAME` column value from the dataframe `df`.

# ##### Question 9: Find the longest company name and assign it to the `ans9`.
# 
# - You do not need to split the value to extract the company name. 
# - Here are company name examples : `Apple, inc.`, `Amazon, inc.`


name = ''
#row_num = 0

for i in range (len(df)):
    if len(df.iloc[i]['CONFORMED-NAME']) > len(name):
        name = df.iloc[i]['CONFORMED-NAME']
        #row_num = i

ans9 = name

ans.append(ans9)

# ##### Question 10: Find the most common `word` among company names and assign it to the `ans10`.
# 
# - We consider <b>word</b> as all numbers, special characters, and text separated by white space.
# - You will get the <b>word</b> using the `split` method.
# - For Question 10, each <b>word</b> is case-sensitive.
# - Also, please do not remove the special characters and punctuation. (e.g., co., inc.)


# Set up an empty dict.
word_list = {}

for i in range (len(df)):
    words = df.iloc[i]['CONFORMED-NAME'].split()
    
    for w in words:
        
        # If w is in word_list dict., increment by 1 
        if w in word_list.keys():
            word_list[w] += 1
        
        # O/W Add w to word_list with intial value 1
        else:
            word_list[w] = 1

ans10 = sorted(word_list, key = word_list.get, reverse = True)[0]

ans.append(ans10)

# ### What was the answer to `ans10`? 
# - Inc.
# ### Do you think the answer is informative?
# - No
# ### If not, the reason is that the value is not well preprocessed.
# ### For better interpretation, we need to take a preprocessing step.
# ### Data preprocessing can be defined as manipulating or extracting the data to enhance data analytic performance.
# ### Data preprocessing is an important step in the data mining process.

# ##### Question 11: Find the most common word among company names after `preprocessing` the data and assign it to the `ans11`.
# 
# [Please follow the below preprocessing step]
# - Please lowercase the company name value. -> `Inc.` should be `inc.`
# - Please remove all special characters and punctuation from a string. -> `inc.` should be `inc`
# - To remove all special characters and punctuation, please use the following syntax : `'[^0-9a-zA-Z]+'`
# - The value should consist of letters and numbers. -> `inc`
# - Also, filter the value which length is less than 1. -> if there is a value `i`, then `i` should be removed


# REF: https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
import re

names = {}

for i in range (len(df)):
    words = df.iloc[i]['CONFORMED-NAME'].split()
    
    for w in words:
        w = (re.sub('[^A-Za-z0-9]+', '', w)).lower()
        if len(w) > 1:
            
            # If w is in names dict., increment by 1 
            if w in names.keys():
                names[w] += 1
        
            # O/W Add w to names with intial value 1
            else:
                names[w] = 1

ans11 = sorted(names, key = names.get, reverse = True)[0]

ans.append(ans11)

# ### Last step of  preprocessing the data is to get rid of the  `stopword`.
# ### `Stopwords` are generally the most common words in a language and may not be meaningful such as `the`, `a`, `of` and `or`.
# ### In the industry section, the following words can be stopwords (`inc`, `co`, `se`, `ltd`, ... ).
# ### Therefore, you need to delete the `stopwords` to get the most precise result.
# 
# ##### Question 12: Find the most common word among company names after removing stopwords and assign it to the `ans12`.
# - We consider <b>word</b> as all numbers and text separated by white space.
# - Filter the word if the word includes any items among the provided `stopwords` list.
# - `stopwords` list : `['inc','corp','co','ltd','de','llc','group','holdings','lp','plc','cf','sa','nv','gt','as','rr']`

import re

stopwords = ['inc','corp','co','ltd','de','llc','group','holdings','lp','plc','cf','sa','nv','gt','as','rr']
names = {}

for i in range (len(df)):
    words = df.iloc[i]['CONFORMED-NAME'].split()
    
    for w in words:
        w = (re.sub('[^A-Za-z0-9]+', '', w)).lower()
        
        # Omiting stopwords and 1 char words
        if w not in stopwords and len(w) > 1:
            
            # If w is in names dict., increment by 1 
            if w in names.keys():
                names[w] += 1
        
            # O/W Add w to names with intial value 1
            else:
                names[w] = 1

ans12 = sorted(names, key = names.get, reverse = True)[0]

ans.append(ans12)

# ### Question 13 ~ 15: You want to see the trend of  `STATE` where the companies submit the `10-K` report in `2018` or `2019` from the `df` dataframe.
# - The first step is to make the new column, `year`, which includes the year value from `FILING-DATE` column.
# - Please convert the `year` column datatype as `int`.
# - Next, filter the dataframe which <b>1)</b> `Form-Type` is `10-K` and <b>2)</b> `Year` is `2018` or `2019` and assign the filtered result as the
# `df_10K`.

# ##### Question 13: Please find the unique number of states from the dataframe `df_10K` and assign it to the `ans13`.


df['year'] = [int(item[0]) for item in df['FILING-DATE'].str.split('-')]

df_10K = df.loc[(df['FORM-TYPE'] == '10-K') & (df['year'].isin([2018, 2019]))]

ans13 = df_10K["STATE"].nunique()

ans.append(ans13)

# ### You are provided `states` information in `us_states.csv`.
# ### If comparing `states` list from  `df_10K`  with `us_states.csv`, you will notice that some state names are invalid. 
# ### Therefore, you need to preprocess the `State` value in `df_10K` dataframe. 
# ### Download `us_state.csv` file into the same directory, where `hw1_starter.ipynb` is located. (If not, there will be an extra deduction on your grade)
# ### Read the `us_states.csv` file and remove rows with invalid states from `df_10K` dataframe.
# 
# ##### Question 14: Please find the unique number of valid states from the dataframe `df_10K_state` and assign its value to the `ans14`.
# - Use the `pandas` library to open the `us_states.csv` file as a dataframe `usa_states`.
# - Get rid of rows which `STATE` column value is not the same as `State` column value from dataframe `usa_states`.
# - Save the preprocessed dataframe name as `df_10K_state`.

states = pd.read_csv('us_states.csv')

# REF: https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value?noredirect=1&lq=1
df_10K_state = df_10K[df_10K['STATE'].isin(states['State'])]

ans14 = df_10K_state["STATE"].nunique()

ans.append(ans14)

# ##### Question 15: Find the number of `10-K` reports from the state of `NY` from the  `df_10K_state` dataframe.

ans15 = len(df_10K_state[df_10K_state['STATE'] == 'NY'])

ans.append(ans15)

# ##### Question 16: Make the `bar` graph based on the following instructions.
# - You want to know the top <b>7</b> states where the `10-K` reports were most reported.
# - To make a <b>bar</b> graph, please use the `df_10K_state` dataframe.
# - Before drawing the graph, make the `state_count` dictionary which contains the state and the number of 10-K reports for that state.<br/>
#   (e.g.) <b>{'NY': 166, 'CA':  ... }</b>
# - Set all labels' font size as font size <b>15</b>. 
# - Set the xlabel as "`STATE`" (please use `STATE` column).
# - Set the ylabel as "`Number of 10-K reports`" (please use `state_count` dictionary).
# - Set the title as "`Number of 10-K reports in 2018 and 2019`".
# - Save the graph named "`hw1_ans16_{student_id}.png`".<br/>
#   (e.g.) <b>hw1_ans16_37510930.png</b>


state_count = {}

for i in range (len(df_10K_state)):
    st = df_10K_state.iloc[i]['STATE']

    if st in state_count.keys():
        state_count[st] += 1
        
    else:
        state_count[st] = 1

tops = sorted(state_count, key = state_count.get, reverse = True)[:7]

#print(tops)
#print(state_count)

x = []
y = []

for k, v in state_count.items():
    if k in tops:
        x.append(k) 
        y.append(v)

# REF: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
s = dict(zip(x, y))
sorted_states = dict(sorted(s.items(), key=lambda item: item[1], reverse = True))
rev_sorted_states = dict(sorted(s.items(), key=lambda item: item[1]))


# REF:https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot?rq=1
# Set Label sizes to 15
plt.rcParams.update({'font.size': 15})

plt.bar(sorted_states.keys(), sorted_states.values())

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.xlabel('STATE')
plt.ylabel('Number of 10-K reports')
plt.title('Number of 10-K reports in 2018 and 2019', fontsize=15)
plt.savefig('hw1_ans16_31222086.png')
plt.show()


# ##### Question 17: Continue to make the `Horizontal bar` graph using the same dataset in Q16. Assign different colors to each bar and arrange the bars in descending order (Large to small from top to bottom).
# - Use the `state_count` dictionary you just generated.
# - Assign different colors to each bar (You can choose any colors you want).
# - Arrange the bars in descending order.
# - Set all labels' font size as font size <b>15</b>. 
# - Set the ylabel as "`STATE`".
# - Set the xlabel as "`Number of 10-K reports`".
# - Set the title as "`Number of 10-K reports in 2018 and 2019`".
# - Save the graph named "`hw1_ans17_{student_id}.png`".<br/>
#   (e.g.) <b>hw1_ans17_37510930.png</b>


plt.rcParams.update({'font.size': 15})

plt.barh(list(rev_sorted_states.keys()), list(rev_sorted_states.values()), color = ['yellow', 'red', 'green', 'blue', 'cyan', 'orange', 'purple'])
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

plt.ylabel('STATE')
plt.xlabel('Number of 10-K reports')
plt.title('Number of 10-K reports in 2018 and 2019', fontsize=15)
plt.savefig('hw1_ans17_31222086.png')
plt.show()


# ##### Question 18: Make a `Line Plot` to show the number of 10-K reports in state `NY` and `MA` by month in 2018.
# - Use the `df_10K_state` dataframe for analysis. 
# - Filter out all the 10-K reports in `NY` and `MA` in 2018 and store them as `df_10K_2018`.
# - Generate a new column `FILING-MONTH` from column `FILING-DATE`, which records the month of `FILING-DATE`.(eg. `2018-09-01` -> `09`).
# - Calculate the number of reports in each month for `NY` and `MA`. Store them separately in two dictionaries: `dict_ny` and `dict_ma`. 
# - Sort the dictionary by the key(`month`).
# - Make the plot based on the dictionaries.
# - Set all labels' font size as font size <b>15</b>. 
# - Set the ylabel as "`Number of 10-K reports`" .
# - Set the xlabel as "`Months`".
# - Set the title as "`The Number of 10-k reports by Months in 2018`".
# - Add legend to the plot.
# - Save the graph named "`hw1_ans18_{student_id}.png`".<br/>
#   (e.g.) <b>hw1_ans18_37510930.png</b>


df_line = df_10K_state.loc[(df_10K_state['year'] == 2018) & (df_10K_state['STATE'].isin(['NY', 'MA']))]

df_line['FILING-MONTH'] = [item[1] for item in df_line['FILING-DATE'].str.split('-')]

dict_ny = {'01': 0, '02': 0, '03': 0,'04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0,'10': 0, '11': 0, '12': 0}
dict_ma = {'01': 0, '02': 0, '03': 0,'04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0,'10': 0, '11': 0, '12': 0}

for i, r in df_line.iterrows():

    if df_line['STATE'][i] == 'NY':
        dict_ny[df_line['FILING-MONTH'][i]] += 1
    else:
        dict_ma[df_line['FILING-MONTH'][i]] += 1

#print(dict_ny)
#print(dict_ma)

# Plot
plt.rcParams.update({'font.size': 15})

plt.plot(dict_ny.keys(), dict_ny.values(), "-b", label='Months', alpha=0.6)
plt.plot(dict_ma.keys(), dict_ma.values(), "-r", label='Number of 10-K reports', alpha=0.6)

plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

# REF: https://www.kite.com/python/answers/how-to-change-the-font-size-of-a-matplotlib-legend-in-python
plt.title('The Number of 10-k reports by Months in 2018', fontsize=15)
plt.legend(['Months', 'Number of 10-K reports'], prop={"size":10})
plt.savefig('hw1_ans18_31222086.png')
plt.show()


# ##### Question 19: How many 10-K reports are generated in each city between 2018 and 2019? Please draw a `histogram` showing the distribution of 10-K report numbers for all cities. Set the bin numbers to `20` 
# - Use the `df_10K_state` dataframe for analysis.
# - Utilize the `CITY` column to calculate the number of 10-K reports for each city. You may use for-loop, Counter, or groupby.
# - Make the histogram and set the number of bins to `20`.
# - Set all labels' font size as font size <b>15</b>. 
# - Set the xlabel as "`The Number of 10-k reports`".
# - Set the title as "`Distribution of the number of 10-k reports for each city`".
# - Save the graph named "`hw1_ans19_{student_id}.png`".<br/>
#   (e.g.) <b>hw1_ans19_37510930.png</b>


cities = list(dict(Counter(list(df_10K_state['CITY']))).values())

from collections import Counter

c = Counter(cities)
hic = c.most_common()

# Histogram
plt.rcParams.update({'font.size': 15})

plt.hist(hic, bins = 20)

# REF: https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html
plt.xticks(fontsize = 15, rotation = 'vertical')
plt.yticks(fontsize = 15)

plt.xlabel('The Number of 10-k reports')
plt.title('Distribution of the number of 10-k reports for each city', fontsize=15)
plt.savefig('hw1_ans19_31222086.png')
plt.show()


# ##### Question 20: Make outfile name format as `hw1_answers_{student_id}.txt` and save it to `txt` file                
# - when you write the answer, please keep format(please refer to word doc example).
# - The total line number should be 17.
# - The first line should be your last name, first name, email.
# - From the second to before the last line, these lines should be starting with `answer{number}=your_own_answer`. <br>
#  (ex) `answer7=hello` (there will be no whitespace)
# - The last line should be `HW 1 is done!!!`
# - file name should be like this : <b>hw1_answers_37510930.txt</b>


file = last_name + ', ' + first_name + ', ' + email + '\n'
for i in range(len(ans)):
    file = file + 'answer' + str(i+1) + '=' + str(ans[i]) +'\n'

file = file + 'Project 1 is done!!!'
print(file)

filename = 'hP1_' + str(student_id) + '.txt'

with open(filename, 'w') as outfile:
    outfile.write(file)

