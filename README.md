## \* Rendering problems? 
Recently, Github has sporadically had problems rendering the .ipynb notebooks. If this happens, you can always copy the URL for the specific notebook and view the notebook at https://nbviewer.jupyter.org/ . \([Referenced in this Github issue](https://github.com/jupyter/notebook/issues/3035)\). In the future I'll be looking into a more stable/convenient way to share notebooks.

# Ostrea_PopStructure
This repository contains code and Jupyter Notebooks detailing assembly and analyses of Genotype-by-Sequencing (GBS) data in the Olympia oyster (*Ostrea lurida*), as presented in:

* Silliman K. Population structure, genetic connectivity, and adaptation in the Olympia oyster (*Ostrea lurida*) along the west coast of North America. *Evolutionary Applications*, In press. [doi: 10.1111/eva.12766](https://onlinelibrary.wiley.com/doi/abs/10.1111/eva.12766)

This repository is intended to facilitate full reproducibility of the paper, as well as demonstrate how to perform a variety of population genetic analyses on reduced-representation genomic SNP data. If you are only interested in replicating or practicing the popgen analyses, I recommend downloading the Dryad repository and using the **MakingFilesR.ipynb** to create the desired input files, then checking out the relevant notebooks in the **Analysis** folder. Please submit a Github issue if you have any difficulty accessing data or following along with the notebooks.

## Associated data repositories
* [NCBI SRA (# SRP174167)](https://www.ncbi.nlm.nih.gov/sra/SRP174167): Raw demultiplexed DNA sequences for all samples with $>$ 200,000 raw sequencing reads.
* [Dryad repository](https://doi.org/10.5061/dryad.114j8m1): VCF files of all filtered SNPs, putative neutral SNPs, and putative outlier SNPS, FASTA file of outlier GBS loci, sample metadata, parameter file for ipyrad, and parameter files for EEMS.

## GBS_KS_Protocol.docx
Wet lab protocol followed for constructing GBS libraries for sequencing, based on the original protocol by [Elshire et al. 2011](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019379) and incorporating modifications suggested by [Ben Winger](https://www.wingerlab.org/) and [Abraham Palmer's lab](http://palmerlab.org/protocols-data/).

## Assembly folder
Two python notebooks detailing how to go from raw sequencing data or raw data from NCBI SRA to assembled GBS loci using the [*ipyrad* API](https://ipyrad.readthedocs.io/).
* **Final-c85-bestrep.ipynb**: Assembles GBS loci using the best replicate for each sequenced individual. Includes instructions for downloading raw demultiplexed sequence reads from NCBI SRA using the *ipyrad* API.
* **Demultiplex.ipynb**: Notebook detailing the demultiplex step for *ipyrad*.
* **Replicate_Files.tsv**: Tab-delimited file listing replicate sequencing runs for each individual. The first column lists the best replicate used in **Final-c85-bestrep.ipynb**.

## Making_Files folder
*  **Filtering_VCF.ipynb**: Notebook on how to filter a .vcf file made by ipyrad for excess heterozygosity, minor allele frequency, linkage, and missing data, using a combination of VCFTools and custom scripts.
*  **MakingFilesR.ipynb**: Jupyter R notebook for converting a filtered .vcf file into input files for various popgen analyses, primarily using the *radiator* R package. Also includes instructions for running EEMS on a cluster. Use this notebook for to convert the VCF files from the Dryad repository into input files for other popgen analyses. 


## Analysis folder
* **OutlierR.ipynb**: R Jupyter notebook detailing detection of outlier loci using OutFLANK, Bayescan, and pcadapt. 
* **PCA_x45m75.ipynb**: R Jupyter notebook detailing how to make PCA plots from an Adegenet object using Adegenet and pcaviz.
* **Fst.ipynb**: R Jupyter notebook detailing how to calculate pairwise Fst across all populations and make a heatmap of the values, as well as conduct a Mantel text of water distance and FST. Also calculates basic popgen stats like heterozygosity.
* **TreeMix.ipynb**: R Jupyter notebook for plotting output of TreeMix and evaluating model fit for different numbers of migration events.
* **StructureIP.ipynb**: Python Jupyter notebook for excecuting the *ipyrad Analysis Toolkit* API for STRUCTURE.

## Scripts folder
The Scripts folder has various scripts for filtering loci and converting file formats, including subsetSNPs.py for selecting one SNP per GBS loci from a .vcf file and .spid files for PGD Spider.






