#!/usr/bin/env python

import urllib
import re
from googlefinance import getQuotes
import json
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2 :
        print 'USAGE : python stock.py [stock_symbol]'
        exit(0)
    else:
        stock_symbol = sys.argv[1]
        try:
            print json.dumps(getQuotes(stock_symbol), indent=2)
        except:
            print stock_symbol, " is not a valid stock symbol"

