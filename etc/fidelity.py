"""
Top owned stocks at fidelity:

https://eresearch.fidelity.com/eresearch/gotoBL/fidelityTopOrders.jhtml

(this only shows one day, but the thought was to parse what's there
and then maybe collect historical data from archive.org)
"""
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd


def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    dom = etree.HTML(str(soup))

    df = pd.DataFrame()
    df['sym'] = dom.xpath("//td[@class='second']/span/text()")
    df['buy'] = [int(x) for x in dom.xpath("//td[@class='fifth']/span/text()")]
    df['sell'] = [int(x) for x in dom.xpath("//td[@class='seventh']/span/text()")]
    df['ratio'] = df.buy / (df.buy + df.sell)
    return df


