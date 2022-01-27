import json

f1 = open("States.json","r")
data = json.load(f1)
#print(data)
for s in data['states']:
    if len(s['area_codes']) > 2:
        print(s['name'],"....",s['abbreviation'],"....",s['area_codes'])

#display names of the states who are having more than two area codes or display name of the state and number of area codes for every state
