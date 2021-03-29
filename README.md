# GME Data

Data on 2021 Activity in Gamestop Stock
  (NYSE: [$GME](https://finance.yahoo.com/quote/GME?p=GME), XFRA: [$GS2C](https://finance.yahoo.com/quote/GS2C.DE?p=GS2C.DE)).

## Manifest

The `gme` directory contains cleaned-up data specific to GameStop and ETFs that cointain it.

path | update cycle | description
---- | -----------  | ------------
`gme/shortvol.txt`      | 1d  | consolidated daily short volume data for GME
`gme/ftd.txt`           | 2w  | daily failure to deliver data, limited to GME and containing ETFs
`gme/ibkr/borrowable/*` | 15m | number of borrowable shares (of GME, GS2C, various ETFS)
`gme/options/*/*`       | 5m  | options chain data from webull (1 file per 5 minute snapshot)
`gme/bars/*/*`          | n/a | open/high/low/close/volume bars for various timeframes (currently 1h bars for 1year)


The `raw` directory contains the raw files used to generate (some of) the GME-specific data.

path | update cycle | description
---- | ------------ | -----------
`raw/sec/ftd/*.txt` | 2w | raw total-market [failure to deliver data](https://www.sec.gov/data/foiadocsfailsdatahtm) from the SEC.
`raw/finra/*/*.txt` | 1d | raw cross-exchange short volume reports from [FINRA](http://regsho.finra.org/regsho-Index.html).

The top level directory contains the scripts used to fetch and generate this data.

path | description
---- | -----------
`finra_shortvol.py` | python file to fetch/generate the short volume data
`borrowable.py`     | python script to fetch borrowable shares from interactive brokers
`ftd.sh`            | shell script to extract failure-to-deliver data
`wb-opts.py`        | python script to fetch option chain from webull
`ibkr_bars.py`      | python script to fetch candlestick+volume data from interactive brokers
`publish.sh`        | shell script to publish this data to github.
`crontab.txt`       | the `crontab` schedule for running the above programs

## Want to help?

See the [reddit post on /r/GME](https://www.reddit.com/r/GME/comments/m6a4zj/gmedata_repository_on_github/)
or the [discord server](https://discord.gg/sy3ye2tD).
