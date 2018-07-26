# Ostrea_PopStructure
This repository contains code and notebooks detailing preliminary analyses of Genotype-by-Sequencing (GBS) data in the Olympia oyster (*Ostrea lurida*). These notebooks are a work in progress, so may change often as I clearly annotate them and decide on methodological approaches. Once the paper is published this fall, this repository will hold all final, annotated notebooks for analyses presented in the paper.

## Scripts folder
The Scripts folder has various scripts for filtering loci and converting file formats, including subsetSNPs.py for selecting one SNP per GBS loci from a .vcf file and .spid files for PGD Spider.

## Analysis folder
* OutlierR.ipynb: R Jupyter notebook detailing detection of outlier loci using OUTFlank, Bayescan, and pcadapt. 
* PCA_m80x55.ipynb: R Jupyter notebook detailing how to make PCA plots from an Adegenet object using Adegenet and pcaviz.
* Fst.ipynb: R Jupyter notebook detailing how to calculate pairwise Fst across all populations and make a heatmap of the values. Also calculates basic popgen stats like heterozygosity.

## Making_Files folder
Folder with notebooks on how to filter a .vcf file from ipyrad for low coverage individuals, excess heterozygosity, and missing data, using a combination of VCFTools and custom scripts. **Filtering_VCF.ipynb** is the most up to date version.




