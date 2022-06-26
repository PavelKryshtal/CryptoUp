import requests
import json
import time

url_all = "https://api.bittrex.com/api/v1.1/public/getcurrencies"

INTERVAL = 1

j = requests.get(url_all)
data = json.loads(j.text)
allc = [d['Currency'] for d in data['result']]
print(allc)

cryptos = input('cryptos to monitor, for ex. btc,bat,eth?')
cryptos = [c.upper() for c in cryptos.strip().split(',')]

notfound = [c for c in cryptos if c not in allc]

if notfound:
  print(f'неизвестная крипта {notfound}')
  import sys
  sys.exit()


def get_price(crypto):
  url = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-{crypto}"
  print(url)
  j = requests.get(url)
  data = json.loads(j.text)
  price = data['result']['Ask']
  return price

while True:
  data = [(c,get_price(c)) for c in cryptos]
  print(data)
  time.sleep(INTERVAL)