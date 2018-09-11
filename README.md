# Ostrea_PopStructure
This repository contains code and notebooks detailing analyses of Genotype-by-Sequencing (GBS) data in the Olympia oyster (*Ostrea lurida*). These notebooks currently detail the analyses presented in the preprint, but are a work in progress as I work to annotate them clearly. Experienced users of R may still find them useful. Once the paper is published this fall, this repository will hold all final, annotated notebooks for analyses presented in the paper.

## Scripts folder
The Scripts folder has various scripts for filtering loci and converting file formats, including subsetSNPs.py for selecting one SNP per GBS loci from a .vcf file and .spid files for PGD Spider.

## Analysis folder
* OutlierR.ipynb: R Jupyter notebook detailing detection of outlier loci using OUTFlank, Bayescan, and pcadapt. 
* PCA_x45m75.ipynb: R Jupyter notebook detailing how to make PCA plots from an Adegenet object using Adegenet and pcaviz.
* Fst.ipynb: R Jupyter notebook detailing how to calculate pairwise Fst across all populations and make a heatmap of the values, as well as conduct a Mantel text of water distance and FST Also calculates basic popgen stats like heterozygosity.
* TreeMix.ipynbL R Jupyter notebook for plotting output of TreeMix and evaluating model fit for different numbers of migration events.

## Making_Files folder
*  **Filtering_VCF.ipynb**: Notebook on how to filter a .vcf file from ipyrad for excess heterozygosit, and missing data, using a combination of VCFTools and custom scripts.
*  **MakingFilesR.ipynb**: Jupyter R notebook for converting a .vcf file into input files for various popgen analyses.




