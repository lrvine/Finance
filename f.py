import urllib
import re
import sys



def get_quote(symbol):
    base_url = 'https://tw.finance.yahoo.com/q/q?s='
    content = urllib.urlopen(base_url + symbol ).read()
    m = re.search('<td align="center" bgcolor="#FFFfff" nowrap><b>(.*?)<', content)
    if m:
        quote = m.group(1)
    else:
        quote = 'no quote available for: ' + symbol
    return quote

def get_avgdividend(symbol):
    base_url = 'https://tw.finance.yahoo.com/d/s/dividend_'
    content = urllib.urlopen(base_url + symbol +'.html' ).read()
    m = re.findall('<td align="center">(.*?)</td>', content)
    dit=0;
    dif=0;
    count=0;
    if m:
        for i in range(len(m)):
          if ((i+1)%5) == 0:
            #print m[i]
            dit=dit+float(m[i])
            if count == 4 :
              dif=dit
            count=count+1;

        #print dit
        #print dif
        dit=dit/10
        dif=dif/5
        print symbol + ' average dividend in the past 10 years is',dit
        print symbol + ' average dividend in the past 5 years is',dif
    else:
        print 'no data available for: ' + symbol
    return dif

def get_estimate(symbol):
    base_url = 'https://www.google.com/finance?q=TPE:'
    content = urllib.urlopen(base_url + symbol).read()
    m = re.findall('<td class="val">(.*?)\s', content)
    dif=0
    if m:
        for i in range(len(m)):
            if i== 5 :
              print ' P/E ratio is ',m[i]
            if i == 7:
              print ' estimate EPS is ',m[i]
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
    dif = get_avgdividend(symbol)
    r1=dif*20;
    print 'historical reasonable price for 5% retrun might be ',r1
    r1=dif*25;
    print 'historical reasonable price for 4% retrun might be ',r1
    r1=dif*50;
    print 'historical reasonable price for 2% retrun might be ',r1
    get_estimate(symbol);



stocklist = open(sys.argv[1]).read().splitlines()

print '\n'
for line in stocklist:
  p_price(line)
  print '\n'
