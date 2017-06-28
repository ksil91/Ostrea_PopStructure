__author__ = 'ksil91'

import sys

def makeTM(infile,outfile):
	IN = open(infile,"r")
	OUT = open(outfile,"w")
	pops = []
	adict = {}
	next(IN)
	for line in IN:
		stuff = line.strip().split()
		pops.append(stuff[0])
		a1 = stuff[1::2]
		a2 = stuff[2::2]
		adict[stuff[0]] = zip(a1,a2)
	IN.close()
	OUT.write(" ".join(pops)+"\n")
	text = ""
	for loci in range(len(adict[stuff[0]])):
		for p in pops:
			text = text+",".join(map(str,adict[p][loci]))+" "
		if " 0,0" not in text:
			OUT.write(text+"\n")
		text = ""
	OUT.close()

def main(argv):
	#get arguments from command line
	infile_name = argv[1]
	outfile_name = argv[2]
	makeTM(infile_name,outfile_name)

if __name__ == "__main__":
	status = main(sys.argv)
	sys.exit(status)
