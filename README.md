# GME Data

Data on 2021 Activity in Gamestop Stock
  (NYSE: [$GME](https://finance.yahoo.com/quote/GME?p=GME), XFRA: [$GS2C](https://finance.yahoo.com/quote/GS2C.DE?p=GS2C.DE)).

## Manifest

path | description
---- | -----------
`gme/shortvol.txt` | consolidated daily short volume data for GME
`gme/ftd.txt` | daily failure to deliver data, limited to GME and containing ETFs
`gme/ibkr/borrowable/*` | number of borrowable shares (of GME, GS2C, various ETFS)
`gme/options/*/*` | options chain data from webull (1 file per 5 minute snapshot)
`raw/sec/ftd/*.txt` | raw total-market [failure to deliver data](https://www.sec.gov/data/foiadocsfailsdatahtm) from the SEC.
`raw/finra/*/*.txt` | raw cross-exchange short volume reports from [FINRA](http://regsho.finra.org/regsho-Index.html).
`fetch_data.py` | python file to fetch/generate the short volume data
`borrowable.py` | python script to fetch borrowable shares from interactive brokers
`ftd.sh` | shell script to extract failure-to-deliver data
`wb-opts.py` | python script to fetch option chain from webull


## Want to help?

See the [reddit post on /r/GME](https://www.reddit.com/r/GME/comments/m6a4zj/gmedata_repository_on_github/)
