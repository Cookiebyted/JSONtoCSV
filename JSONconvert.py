import json
import pandas as pd

def flattenJSON(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenJSON(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]
    return val

with open('airlines.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    #print(len(data)) # number of airline delay instances

combinedDF = pd.DataFrame()

for i in range(len(data)):
    flattened = flattenJSON(data[i], '_')
    df = pd.json_normalize(flattened)
    combinedDF = pd.concat([combinedDF, df])

combinedDF.to_csv('airlines.csv', mode='w', header=True)
