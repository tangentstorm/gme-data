"""
fetch GME data from various websites
"""
import datetime
import os
import requests
import csv

START_DATE = datetime.date(2021, 1, 4)  # first trading day of new year
MARKET_CLOSED = {datetime.date(*a) for a in [
  (2021, 1, 18),  # MLK day
  (2021, 2, 15),  # presidents day
]}

RAW_SHORTVOL_PATH = 'raw/finra/%s-shortvol'
GME_SHORTVOL_PATH = 'gme/shortvol.txt'


# codes used in the 'market' column for finra daily short volume
# http://regsho.finra.org/DailyShortSaleVolumeFileLayout.pdf
FINRA_MARKETS = {
  'N': 'FNYX',   # N = NYSE TRF
  'Q': 'FNSQ',   # Q = NASDAQ TRF Carteret
  'B': 'FNQC',   # B = NASDAQ TRF Chicago
  'D': 'FNRA',   # D = ADF  (almost always 0 data)
  'O': 'FORF',   # O = ORF (not actually listed in the spec, but available for download)
}



def market_days():
    """generate date objects for each trading day since START_DATE"""
    one = datetime.timedelta(days=1)
    end = datetime.date.today() - one
    day = START_DATE
    while day < end:
        if day.weekday() < 5 and day not in MARKET_CLOSED:
            yield day
        day += one
    yield day


def fetch_raw_shortvol():
    """fetch consolidated short volume data from FINRA website"""
    for market in ['CNMS'] + list(FINRA_MARKETS.values()):
        for day in market_days():
            date = '{0:d}{1:02d}{2:02d}'.format(day.year, day.month, day.day)
            name = market + 'shvol' + date + '.txt'
            path = os.path.join(RAW_SHORTVOL_PATH % market.lower(), name)
            if not os.path.exists(path):
                url = 'http://regsho.finra.org/' + name
                res = requests.get(url)
                txt = '\n'.join(res.content.decode('utf8').split('\r\n'))
                open(path, 'w').write(txt)
                print("{} -> {}".format(url, path))


def gen_gme_shortvol():
    """generate gme rows from the raw short volume files"""
    for market in ['CNMS'] + list(FINRA_MARKETS.values()):
        root = RAW_SHORTVOL_PATH % market.lower()
        for path in os.listdir(root):
            for row in csv.DictReader(open(os.path.join(root, path)), delimiter='|'):
                # columns:
                if row["Symbol"] == "GME":
                    yield row


def write_gme_shortvol():
    c = 'Date | Symbol | ShortVolume | ShortExemptVolume | TotalVolume | Market'.split(' | ')
    w = csv.DictWriter(open(GME_SHORTVOL_PATH, 'w', newline=''), fieldnames=c, delimiter='|', lineterminator='\n')
    w.writeheader()
    for row in sorted(gen_gme_shortvol(), key=lambda x: (x['Date'], -len(x['Market']), x['Market'])):
        w.writerow(row)


if __name__ == "__main__":
    fetch_raw_shortvol()
    write_gme_shortvol()
