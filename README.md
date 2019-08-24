Finance related utilities in Python 3

# rounding

Round a float x to nth digits after decimal points with base m.

Usage:

python3 rounding.py  x  n  m

Example:

python3 rounding.py  1.645332  5  5

It will output 1.64535

# parsestock

Parse stock price to calculate price according target dividend yield.

This script is for Taiwan Stock Exchange.

It uses Yahoo API for current price, and Yahoo TW finance for dividend data.

Usage:

Put the stock code number into the list.txt

Execute:

Python3 stock.py list.txt
