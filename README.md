Finance related utilities in Python


# parsestock

Parse stock price to calculate objective price according to past and current EPS

*05/24/2016 Removed historical EPS data because https://tw.finance.yahoo.com/ seems to block urllib API now

This script is for Taiwan Stock Exchange. It uses Google finance for current EPS data.

Usage:

Put the stock code number into the list.txt

Execute:

Python stock.py list.txt
