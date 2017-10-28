# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import sys

if len(sys.argv) != 3:
    print 'usage: $python define.py <app_id> <app_key>'
    sys.exit()

app_id = sys.argv[1]
app_key = sys.argv[2]

language = 'en'
inputfile = open('words.txt', 'r')
word_ids = inputfile.readlines()
output = open('definitions.txt', 'w')

def getDefinition(data):
    return data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

for word in word_ids:
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    if r.status_code == 200:
        try:
            definition = getDefinition(r.json())
        except:
            definition = 'no definition'
    else:
        definition = r.status_code
    output.write(word.rstrip()+' '+json.dumps(definition)+'\n')

inputfile.close()
output.close()
