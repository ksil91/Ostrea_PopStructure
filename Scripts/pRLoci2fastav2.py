__author__ = 'ksil91'

import sys

def Loci2fastaOut(infileName,outfileName, positions):

    lociDict = {}
    ## read in your data file
    infile = open(infileName, "r")
    ## create an empty output file
    outfile = open(outfileName, "w")
    pos = open(positions, "r")
    chrom = []
    pos.next()
    for line in pos:
        ch = int(line.split()[0])-1
        chrom.append(str(ch))
    pos.close()
    ## parse the loci in your data file
    loci = infile.read().split("|")

    ## write the first read from each locus to the output file in fasta format
    for loc in range(0,len(loci),2):
        if loc+1 < len(loci):
            if loci[loc+1] in chrom:
                seqs = loci[loc].split("\n")
                best_seq = ""
                nmissing = 1000
                for s in seqs:
                    if "\\" not in s and s != "" and "*" not in s:
                        seq = s.split()[1]
                        if (seq.count("N") + seq.count("-")) < nmissing:
                            best_seq = seq
                            nmissing = seq.count("N")+seq.count("-")
                print >>outfile, ">"+loci[loc+1]+"\n"+best_seq
    infile.close()
    outfile.close()

def Loci2fastaOut2(infileName,outfileName, positions):

    lociDict = {}
    ## read in your data file
    infile = open(infileName, "r")
    ## create an empty output file
    outfile = open(outfileName, "w")
    pos = open(positions, "r")
    chrom = []
    for line in pos:
        ch = int(line.split()[0])-1
        chrom.append(str(ch))
    pos.close()
    ## parse the loci in your data file
    loci = infile.read().split("|")

    ## write the first read from each locus to the output file in fasta format
    for loc in range(0,len(loci),2):
        if loc+1 < len(loci):
            seqs = loci[loc].split("\n")
            best_seq = ""
            nmissing = 1000
            for s in seqs:
                if "\\" not in s and s != "" and "*" not in s:
                    seq = s.split()[1]
                    if (seq.count("N") + seq.count("-")) < nmissing:
                        best_seq = seq
                        nmissing = seq.count("N")+seq.count("-")
            if loci[loc+1] in chrom:
                print >>outfile, ">"+loci[loc+1]+"|m75x60-OL-maf025-biu\n"+best_seq
            else:
                print >>outfile, ">"+loci[loc+1]+"\n"+best_seq
    infile.close()
    outfile.close()

def main(argv):
    #get arguments from command line
    inf = argv[1]
    outf = argv[2]
    posf = argv[3]
    Loci2fastaOut(inf, outf, posf)

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
