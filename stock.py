import urllib
import re
import sys


def get_quote(symbol):
	base_url = 'http://www.bloomberg.com/quote/'
	content = urllib.urlopen(base_url + symbol +':TT' ).read()
	m = re.search('<div class="price">(.*?)</div>', content)
	if m:
		quote = m.group(1)
	else:
		quote = 'no quote available for: ' + symbol
	return quote

def get_estimate(symbol):
	base_url = 'https://www.google.com/finance?q=TPE:'
	content = urllib.urlopen(base_url + symbol).read()
	m = re.findall('<td class="val">(.*?)\s', content)
	dif=0
	if m:
		print ' P/E ratio is ',m[5]
		print ' estimate EPS is ',m[7]
	      	r=float(m[7])*20;
		print 'current reasonable price for 5% retrun might be ',r
		r=float(m[7])*25;
		print 'current reasonable price for 4% retrun might be ',r
		r=float(m[7])*50;
		print 'current reasonable price for 2% retrun might be ',r
	else:
		print ' get estimate EPS failure ' + symbol

def p_price(symbol):
	print symbol+' current price is ',get_quote(symbol)
	get_estimate(symbol);


if __name__ == "__main__":
	try:
		stocklist = open(sys.argv[1]).read().splitlines()
		print '\n'
		for line in stocklist:
			p_price(line)
			print '\n'
    	except KeyboardInterrupt:
        	print "\n\nUser Press Ctrl+C,Exit"
