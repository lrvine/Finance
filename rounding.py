import sys

def round_to_base(x, base=5):
    return int(base * round(float(x)/base))

def round_to_nth_digits_after_decimal_point_with_base_m(x,n=5,m=5):
    x = x*(10**(n+1))
    x = round_to_base(x, 10)
    x = x/10
    x = round_to_base(x , m)
    x = x/float(10**n)
    return x

if __name__ == "__main__":
	try:
		print round_to_nth_digits_after_decimal_point_with_base_m(float(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
		print '\n'
    	except KeyboardInterrupt:
        	print "\n\nUser Press Ctrl+C,Exit"

