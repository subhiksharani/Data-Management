import requests
from firebase import firebase
import json
import sys

def inverted_index(input_file):
    file1 = input_file[0]
    inv_address = {}
    with open(file1) as f:
        data = [json.loads(line) for line in f]
    for i in range(len(data)):
        for key,value in data[i].items():
            if key=="address":
                for word in value.split():
                    if word in inv_address:
                        inv_address[str(word)].insert(len(inv_address),str(data[i]['account_number']))
                    else:
                        inv_address[str(word)]=[str(data[i]['account_number'])]
    json_data = json.dumps(inv_address).encode()
    loader = requests.put('https://inf551-88232.firebaseio.com/index.json', data=json_data)    

if __name__=="__main__":
    inverted_index(sys.argv[1:])
