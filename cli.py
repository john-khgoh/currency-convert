import urllib3
import json
import argparse
from os import getcwd, name

path = getcwd()
http = urllib3.PoolManager()
os = name
#website = '127.0.0.1:8008'
#port = 8008
currency = 'usd'
target_currency = 'usd'
value = 0
separator = '\\'

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

#Reads one line at a time, so should be able to handle very large json files
with open(filepath) as f:
    for line in f:
        data = json.loads(line)
        value = data['value']
        currency = data['currency']
        url = website + '/' + 'convert' + '/' + currency + '/' + target_currency + '/' + str(value)
        r = http.request('GET',url)
        output = r.data.decode('ascii')
        output = json.loads(output)
        print(output)   
        
'''
url = website + ':' + str(port) + '/' + 'convert' + '/' + currency + '/' + target_currency + '/' + str(value)

http = urllib3.PoolManager()
#r = http.request('GET', '127.0.0.1:8008/convert/usd/usd/1.0')
r = http.request('GET',url)
output = r.data.decode('ascii')
output = json.loads(output)
print(output)
'''
