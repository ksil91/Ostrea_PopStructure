# Ostrea_PopStructure
This repository contains code and notebooks detailing preliminary analyses of Genotype-by-Sequencing (GBS) data in the Olympia oyster (Ostrea lurida).

## Scripts folder
The Scripts folder has various scripts for filtering loci and converting file formats, including subsetSNPs.py for selecting one SNP per GBS loci from a .vcf file and .spid files for PGD Spider.

## Notebooks
* Ol-c80-66-making files.ipynb: Jupyter notebook with steps for secondary filtering of a .vcf file from ipyrad. The output .vcf of this notebook is then converted to a .str file in PGD Spider for loading in to Adegenet (and actually running Structure).
* pca.OLL.md: Markdown version of a RMarkdown notebook detailing how to make PCA plots from an Adegenet object using Adegenet and pcaviz.
* Fst_heatmap.md: Markdown version of a RMarkdown notebook detailing how to calculate pairwise Fst across all populations and make a heatmap of the values. Also calculates basic popgen stats like heterozygosity.
* MakingFilesR.md: Markdown version of a RMarkdown notebook detailing how to to create input files for the following programs from an Adegenet genind object:
  * Treemix
  * EEMS (both input files and plotting figures)
  * OutFLANK



