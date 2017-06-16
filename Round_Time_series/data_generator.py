import random
import json

fulldata = []
i = 1
while i <= 30:
    hours = []
    j = 1
    while j <= 24:
        hours.append({"hour":j,"value":random.random()})
        j += 1
    fulldata.append({"day":i, "hours":hours})
    i +=1

with open("data.json", "w") as file:
    json.dump(fulldata, file)
