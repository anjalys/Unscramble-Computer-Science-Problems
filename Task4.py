"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('/Applications/Udacity/P0/Unscramble-Computer-Science-Problems/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('/Applications/Udacity/P0/Unscramble-Computer-Science-Problems/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def numbersCouldBeTeleMarketers():

    #declare sets for outgoing calls and other calls and texts 
    callers=set()
    calltextSenderReceiver=set()

    ##loop through calls data
    for call in calls:
        caller=call[0]
        receiver=call[1]
        callers.add(caller)
        calltextSenderReceiver.add(receiver)

    #loop through texts data
    for text in texts:
        textSender=text[0]
        textReceiver=text[1]
        calltextSenderReceiver.add(textSender)
        calltextSenderReceiver.add(textReceiver)

    callers=callers.difference(calltextSenderReceiver)
    telemarketers=list(callers)

    print("These numbers could be telemarketers:")
    print(*(sorted(telemarketers)), sep='\n')

numbersCouldBeTeleMarketers()

