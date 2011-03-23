import sys

# note the two escape sequences below
# assuming $=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
# assuming _=[]
v = []
v.append("+_") # 0
v.append("-~-_") # 1
v.append("-~-~-_") # 2
v.append("-~-~-~-~-_") # 4
v.append("-~-~-_ << -~-~-_") # 8
v.append("-~-~-~-~-_ << -~-~-_") # 16
v.append("-~-~-_ << -~-~-~-~-_") # 32
v.append("-~-~-~-~-_ << -~-~-~-~-_") # 64


def getCode (x):
	z = x
	p = 0
	sys.stdout.write("__+=$[")
	if z == 0:
		sys.stdout.write("+(" + v[p] + ")")
	p = 1
	while z >= 1:
		if (z % 2 == 1):
			sys.stdout.write("+(" + v[p] + ")")
			#sys.stdout.write(",")
		p = p + 1
		z = z >> 1
	sys.stdout.write("]\n")

code = "x='';for(i=96;++i<123;)x+=String.fromCharCode(i);"
print "$=\" !\\\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\""
print "__=\"\""
for c in code:
	getCode(ord(c) - 32)

