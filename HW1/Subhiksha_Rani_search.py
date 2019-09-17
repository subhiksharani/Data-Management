import requests
import json, ast
import sys
from firebase import firebase

def loaddata():
    url = 'https://inf551-88232.firebaseio.com/index.json'
    response = requests.get(url)
    data = response.json()
    cleandata = ast.literal_eval(json.dumps(data))
    return cleandata

def search(term, data):
    words=term.lower().split()
    output=[]
    for word in words:
        for key,value in data.items():
            if key.lower()==word.lower():
                if value not in output:
                    output.append(value)                
    temp = reduce(lambda x,y :x+y , output)
    result = []
    for item in temp:
        if item not in result:
            result.append(item)
    print("The Account Numbers associated with <",term,"> is ", result)

if __name__=="__main__":    
    data1 = loaddata()
    search(sys.argv[1], data1)
