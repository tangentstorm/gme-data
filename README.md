# GME Data

Data on 2021 Activity in Gamestop Stock
  (NYSE: [$GME](https://finance.yahoo.com/quote/GME?p=GME), XFRA: [$GS2C](https://finance.yahoo.com/quote/GS2C.DE?p=GS2C.DE)). 

## Manifest

path | description
---- | -----------
`raw/finra/*/*.txt` | daily NYSE short volume reports from [FINRA](http://regsho.finra.org/regsho-Index.html).
`gme/shortvol.txt` | consolidated daily short volume data for GME 
`fetch_data.py` | python file to fetch/generate all of the above
`raw/ibkr/borrowable/*` | number of borrowable shares (of GME, GS2C, various ETFS)
`borrowable.py` | python script to fetch borrowable shares from interactive brokers

## Want to help?

See the reddit post here: https://www.reddit.com/r/GME/comments/m6a4zj/gmedata_repository_on_github/
