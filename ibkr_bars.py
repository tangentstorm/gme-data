"""
fetch 5-minute price bars for recent dates

https://interactivebrokers.github.io/cpwebapi/
"""

# TODO: 5-minute bars (only seems to work for period<=1m)
# TODO: run this through a sqlite database on each update (for de-duping + just to have it in sql)
# TODO: normalize dates/times (??)
# TODO: fetch ETFs

import requests

GATEWAY = 'https://localhost:5000/v1/portal/iserver'


def write_head(f):
    f.write('time|open|high|low|close|volume\n')


sym = "GME"
cid = 36285627
period = '1y'
bar = '1h'


url = f'{GATEWAY}/marketdata/history?conid={cid}&period={period}&bar={bar}'


bars = requests.get(url, verify=False).json()['data']
f = open(f'gme/bars/{bar}/{sym.lower()}-{bar}.txt', 'w', newline='\n')
write_head(f)
for bar in bars:
    f.write('{t}|{o}|{h}|{l}|{c}|{v}\n'.format(**bar))
f.close()
