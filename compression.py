import math

#compression experiment 

bitstring = ''
originalmsg = 'This is a test message.'

def getmaxbits(msg):
	lmsg = string2int(msg)
	maxbits = len(str(lmsg)) * (math.log(10)/math.log(2))
	return maxbits

def string2int(msg):
	lmsg = 0
	for i in msg:
		lmsg = (lmsg*10)+ord(i)
	return lmsg

def decompress():
	print 'bitstring: ' + bitstring 
	print 'bitstring len: ' + str(len(bitstring))
	print 'ascii bits: ' + str(getmaxbits(originalmsg))
	
	

def compress(msg):
	global bitstring
	while(msg>1):
		if msg % 2 != 0:
			msg+=1
			bitstring += '0'
		else:
			bitstring += '1'
		msg /= 2	
		

def main(message):
	compress(message)
	decompress()


main(string2int(originalmsg))
