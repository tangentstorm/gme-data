"""
Fetch available shares to borrow from interactive brokers.

These are country-specific files with snapshots for the whole market,
and downloading an entire copy of the file would waste a ton of space,
so I'm just going to save the data for individual tickers.
"""
import os
import ftplib
from io import BytesIO

# list of etfs containing GME.
#    taken from https://docs.google.com/spreadsheets/d/1PZ2-hnCtDNRnbE8Wm5ByudBcg26T3lGjsec9bSE9x9I/edit#gid=0
#    by way of https://www.reddit.com/r/GME/comments/m63jfb/ftd_of_62_etfs_that_contained_gme/
# TODO: fetch updated data from https://etfdb.com/stock/GME/ periodically (it says there are now 81)
ETFS = (('GAMR XRT RETL XSVM VIOV RWJ VIOO PSCD VIOG VTWV IUSS VCR VTWO SFYF IWC EWSC SYLD PRF RALS FNDX '
         'FNDB VBR IJS XJR NUSC SLYV IJR SPSM SLY FLQS IJT GSSC SLYG VXF NVQ IWN ESML VB SAA DMRS BBSC '
         'OMFS FDIS STSB SSLY IWM SCHA PBSM UWM VTHR URTY VTI TILT VLU HDG AVUS MMTM DSI SPTM IWV SCHB ITOT DFAU')
        .split(' '))

# the country data to retrieve
WANTED = [
    ('us', 'usa.txt', set(['GME'] + ETFS)),
    ('de', 'germany.txt', {'GS2C'})]


def add_to_index(country, *etc):
    path = f'raw/ibkr/borrowable/index.{country}.txt'
    init = not os.path.exists(path)
    with open(path, 'a+') as f:
        if init: f.write('SYM|CUR|NAME|CON|ISIN\n')
        f.write('|'.join(etc))


def main():
    """collect the borrowable shares for the tickers we care about"""
    ftp = ftplib.FTP('ftp3.interactivebrokers.com')
    ftp.login('shortstock')

    for country, remote, tickers in WANTED:
        bio = BytesIO()
        ftp.retrbinary('RETR ' + remote, bio.write)

        lines = bio.getvalue().decode('utf8').split('\r\n')

        # strip the padding lines:
        assert lines.pop() == ''
        assert lines.pop().startswith('#EOF')  # followed by '|' + row count
        bof = lines.pop(0)
        head = lines.pop(0)
        assert head == '#SYM|CUR|NAME|CON|ISIN|REBATERATE|FEERATE|AVAILABLE|'

        _, dt, ts = bof.split('|')

        for row in lines:
            sym, cur, name, con, isin, rebate, fee, avail, _ = row.split('|')
            if sym in tickers:
                path = f'raw/ibkr/borrowable/{country}/{sym}.txt'
                init = not os.path.exists(path)
                with open(path, 'a+', newline='\n') as f:
                    if init:
                        f.write('DT|TM|REBATE|FEE|AVAIL\n')
                        add_to_index(country, sym, cur, name, con, isin)
                    # now add the actual data:
                    f.write('|'.join([dt, ts, rebate, fee, avail])+'\n')


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__))) # for cron
    main()
