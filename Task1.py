"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_numbers(files):
    set_log=set()
    for index in files:
        set_log.add(index[0])
        set_log.add(index[1])
    return set_log

#Function call for texts and calls
call_set=unique_numbers(calls) 
text_set=unique_numbers(texts)

#Update one set to another set
call_set.update(text_set)

#Records in texts
print("There are {} different telephone numbers in the records.".format(len(call_set)))

