"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#Function to get the max duration of calls
dict_call={}
for index in calls:
    #Outgoing calls
    if index[0] not in dict_call:
        dict_call[index[0]]=int(index[3])
    else:
        dict_call[index[0]]+=int(index[3])
        
    #receiving calls 
    if index[1] not in dict_call:
        dict_call[index[1]]=int(index[3])
    else:
        dict_call[index[1]]+=int(index[3])

max_value = max(dict_call.values()) #max value in dict call_duration
max_key = [key for key, value in dict_call.items() if value == max_value]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key[0], max_value))

