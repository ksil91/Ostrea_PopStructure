# Ostrea_PopStructure
This repository contains code and Jupyter Notebooks detailing analyses of Genotype-by-Sequencing (GBS) data in the Olympia oyster (*Ostrea lurida*), as presented in:

* Silliman K. Population structure, genetic connectivity, and adaptation in the Olympia oyster (*Ostrea lurida*) along the west coast of North America. *Evolutionary Applications*, In press. [doi: 10.1111/eva.12766](https://onlinelibrary.wiley.com/doi/abs/10.1111/eva.12766)

This repository is intended to facilitate full reproducibility of the paper, as well as demonstrate how to perform a variety of population genetic analyses on reduced-representation genomic SNP data. Please submit a Github issue if you have any difficulty accessing data or following along with the notebooks.

## GBS_KS_Protocol.docx
Wet lab protocol followed for constructing GBS libraries for sequencing, based on the original protocol by [Elshire et al. 2011](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019379) and incorporating modifications suggested by [Ben Winger](https://www.wingerlab.org/) and [Abraham Palmer's lab](http://palmerlab.org/protocols-data/).

## Assembly folder

## Making_Files folder
*  **Filtering_VCF.ipynb**: Notebook on how to filter a .vcf file from ipyrad for excess heterozygosit, and missing data, using a combination of VCFTools and custom scripts.
*  **MakingFilesR.ipynb**: Jupyter R notebook for converting a .vcf file into input files for various popgen analyses.

## Analysis folder
* OutlierR.ipynb: R Jupyter notebook detailing detection of outlier loci using OutFLANK, Bayescan, and pcadapt. 
* PCA_x45m75.ipynb: R Jupyter notebook detailing how to make PCA plots from an Adegenet object using Adegenet and pcaviz.
* Fst.ipynb: R Jupyter notebook detailing how to calculate pairwise Fst across all populations and make a heatmap of the values, as well as conduct a Mantel text of water distance and FST Also calculates basic popgen stats like heterozygosity.
* TreeMix.ipynbL R Jupyter notebook for plotting output of TreeMix and evaluating model fit for different numbers of migration events.

## Scripts folder
The Scripts folder has various scripts for filtering loci and converting file formats, including subsetSNPs.py for selecting one SNP per GBS loci from a .vcf file and .spid files for PGD Spider.






