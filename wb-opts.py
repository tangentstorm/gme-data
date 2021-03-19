#!/usr/bin/python3
"""
fetch option chain for $GME from webull
"""
# pip3 install paho-mqtt
import os
import json
from webull import webull
from datetime import datetime

OP_KEYS = [
    # basics about the option
    'symbol', #'GME210319P00001000',

    # redundant fields:
    # 'exchangeId', #189,
    # 'unSymbol',         # 'GME' -- underlying symbol
    # 'expireDate',       # '2021-03-19',
    # 'weekly',           # 0      -- bit flag?
    # 'direction',        # 'put',
    # 'strikePrice',      # '1',
    # 'quoteLotSize',     # 100,
    # 'quoteMultiplier',  # 100,
    # 'currencyId',       # 247,
    # 'regionId',         # 6,
    # 'tickerId',         # 1018810794,
    # 'belongTickerId',   # 913255341    -- ticker for underlying stock??
    # 'derivativeStatus', # 0,  ?? redundant?

    # current candle:
    'open',             # '0.01',
    'high',             # '0.01',
    'low',              # '0.01',
    'preClose',         # '0.01',  ??
    'close',            # '0.01',

    # current market
    # 'askList', # [{'price', '0.01', 'volume', '10303'}],
    # 'bidList', #[{'price', '0.00', 'volume', '0'}],

    # today's trading info
    'activeLevel',      # 50,
    'change',           # '0.00',
    'changeRatio',      # '0.0000',
    'openIntChange',    # 51,
    'openInterest',     # 61537,
    'latestPriceVol',   # '1',
    'volume',           # '4', today's volume?

    # greeks:
    'delta',            # '0.0000',
    'gamma',            # '0.0000',
    'rho',              # '0.0000',
    'theta',            # '0.0000',
    'vega',             # '0.0000',

    'tradeStamp'        # 1616166891361,   # is this a compact tradetime?
    'tradeTime',        # '2021-03-19T13,52,22.079+0000',
]

def print_op(f, op):
    row = [op.get(k,'') for k in OP_KEYS]
    row.extend([
        op['askList'][0]['price'],
        op['askList'][0]['volume'],
        op['bidList'][0]['price'],
        op['bidList'][0]['volume'] ])
    f.write('|'.join(str(x) for x in row)+'\n')


ROOT = "gme/options"

def main(sym="GME"):
    now = datetime.now()
    ym  = now.strftime('%Y%m')
    day = now.strftime('%d')
    hms = now.strftime('%H%M%S')

    wb = webull()
    wb.login(*json.load(open('.wb-creds.json')))

    os.makedirs(f'{ROOT}/{ym}', exist_ok=True)
    f = open(f'{ROOT}/{ym}/{sym}-opchain-{ym}{day}{hms}.txt', 'w')
    f.write('|'.join(OP_KEYS + ['ask','avol','bid','bvol'])+'\n')
    for exp in wb.get_options_expiration_dates(stock=sym):
        ops = wb.get_options(stock=sym, expireDate=exp['date'])
        for op in ops:
            call = op['call']
            put  = op['put']
            exp = call['expireDate']
            strike = call['strikePrice']
            print_op(f, call)
            print_op(f, put)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__))) # for cron
    main()
