# GME Data

Data on 2021 Activity in Gamestop Stock (NYSE: [$GME](https://finance.yahoo.com/quote/GME?p=GME)). 

## Manifest

path | description
---- | -----------
`raw/finra/*/*.txt` | daily NYSE short volume reports from [FINRA](http://regsho.finra.org/regsho-Index.html).
`gme/shortvol.txt` | consolidated daily short volume data for GME 
`fetch_data.py` | python file to fetch/generate all of the above
