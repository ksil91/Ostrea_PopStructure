__author__ = 'Katherine Silliman and Michael A. Alcorn'

## Code to subset one SNP per GBS locus from a VCF file. Chooses the SNP
## with the highest sample coverage. If there is a tie, chooses the 1st SNP in the loci. (may change to random)
## May be specific to VCF format output from ipyrad.

import sys
def subsetSNPs(inputfile, outputfile):
    IN = open(inputfile, "r")
    OUT = open(outputfile, "w")

    current_locus = None
    best_NS = 0
    best_line = None
    snps = 0
    loci = 0
    for line in IN:
        if line[0] == "#":
             # Write header.
             OUT.write(line)
        else:
            snps += 1
            parts = line.split()
            locus = parts[0]
            if current_locus != locus:
                if current_locus is not None:
                    loci += 1
                    OUT.write(best_line)
                
                current_locus = locus
                best_NS = 0
                best_line = ""
            
            # Column 7 is INFO column of VCF file.
            NS = float(parts[7].split(";")[0].split("=")[1])
            if NS > best_NS:
                best_NS = NS
                best_line = line
            
    loci += 1
    OUT.write(best_line)
    IN.close()
    print("Total SNPS: " + str(snps) + "\nUnlinked SNPs: " + str(loci))
    OUT.close()


def main(argv):
    #get arguments from command line, first name of the infile .vcf then name of the outfile .vcf
    invcf = argv[1]
    outfile = argv[2]
    subsetSNPs(invcf, outfile)
    

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)

