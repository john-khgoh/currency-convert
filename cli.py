import urllib3
import json
import argparse
from os import getcwd, name

path = getcwd()
http = urllib3.PoolManager()
os = name
#website = '127.0.0.1:8008' #localhost
website = 'https://currency-convert-1.herokuapp.com'
currency = 'usd'
target_currency = 'usd'
cnt = 0
value = 0
separator = '\\'

#Get arguments required to run
parser = argparse.ArgumentParser(description='Currency converter')
parser.add_argument('--file', dest='file',help='Name of the input file.',required=True)
parser.add_argument('--target-currency', dest='target_currency',help='Specify the target currency e.g. usd, eur, without inverted commas',required=True)
args = vars(parser.parse_args())

target_currency = args['target_currency']
file = args['file']

#Different separator for Windows, *nix and MacOS
if(os=='nt'):
    separator='\\'
else:
    separator='/'

filepath = path + separator + file

#Test the connection to the URL to ensure connectivity
try:
    r = http.request('GET',website)
except:
    raise Exception("Unable to access URL")

#Reads one line at a time without storing it in memory. It should be able to handle very large JSON files.
with open(filepath) as f:
    for line in f:
        cnt += 1

        try:
            data = json.loads(line)
            value = data['value']
            currency = data['currency']
            url = website + '/' + 'convert' + '/' + currency + '/' + target_currency + '/' + str(value)
            r = http.request('GET',url)
            output = r.data.decode('ascii')
            output = json.loads(output)
            print(output)
        except:
            print("Error reading %s at line %d" %(file,cnt)) #Notifies if there are errors with the input file, but continues with other lines
