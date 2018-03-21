Making files for other programs
================
Katherine Silliman

-   [Make .genind object for PCA and other conversions](#make-.genind-object-for-pca-and-other-conversions)
-   [Make input for Structure from .vcf file.](#make-input-for-structure-from-.vcf-file.)
-   [Make input for Bayescan](#make-input-for-bayescan)
-   [Make input for OutFLANK](#make-input-for-outflank)
-   [Make Treemix file](#make-treemix-file)
-   [Make an EEMS file](#make-an-eems-file)
    -   [OL- with OR](#ol--with-or)
    -   [OL - Without Coos Bay](#ol---without-coos-bay)
    -   [Plot EEMS](#plot-eems)

R Notebook detailing how I take a filtered .vcf file from ipyrad and turn it into other formats for population genetic analyses.

``` r
filtsuf = "OL-c80-66-s67-m70x62-maf025"
```

Make .genind object for PCA and other conversions
=================================================

Uses radiator package by

``` r
library("adegenet") #inputting genetic data from structure, PCA, DAPC
library("radiator") #Conversion from vcf to a lot of other formats
library("dplyr")
```

``` r
rad.maf <- vcf2genind(paste(filtsuf,"-u.vcf",sep=""),filename=paste(filtsuf,"-maf025-u",sep=""),common.markers = F, strata="OL-c80-66-s67.strata", pop.levels = c("Klaskino","Barkeley_Sound","Ladysmith","Victoria","Discovery_Bay","Liberty_Bay","North_Bay","Triton_Cove","Willapa","Netarts","Yaquina","Coos","Humboldt","Tomales","San_Francisco","Elkhorn_Slough","Mugu_Lagoon","San_Diego"),parallel.core = 2)
```

    ## VCF is biallelic

    ## 
    Reading 100 / 9170 loci
    Reading 200 / 9170 loci
    Reading 300 / 9170 loci
    Reading 400 / 9170 loci
    Reading 500 / 9170 loci
    Reading 600 / 9170 loci
    Reading 700 / 9170 loci
    Reading 800 / 9170 loci
    Reading 900 / 9170 loci
    Reading 1000 / 9170 loci
    Reading 1100 / 9170 loci
    Reading 1200 / 9170 loci
    Reading 1300 / 9170 loci
    Reading 1400 / 9170 loci
    Reading 1500 / 9170 loci
    Reading 1600 / 9170 loci
    Reading 1700 / 9170 loci
    Reading 1800 / 9170 loci
    Reading 1900 / 9170 loci
    Reading 2000 / 9170 loci
    Reading 2100 / 9170 loci
    Reading 2200 / 9170 loci
    Reading 2300 / 9170 loci
    Reading 2400 / 9170 loci
    Reading 2500 / 9170 loci
    Reading 2600 / 9170 loci
    Reading 2700 / 9170 loci
    Reading 2800 / 9170 loci
    Reading 2900 / 9170 loci
    Reading 3000 / 9170 loci
    Reading 3100 / 9170 loci
    Reading 3200 / 9170 loci
    Reading 3300 / 9170 loci
    Reading 3400 / 9170 loci
    Reading 3500 / 9170 loci
    Reading 3600 / 9170 loci
    Reading 3700 / 9170 loci
    Reading 3800 / 9170 loci
    Reading 3900 / 9170 loci
    Reading 4000 / 9170 loci
    Reading 4100 / 9170 loci
    Reading 4200 / 9170 loci
    Reading 4300 / 9170 loci
    Reading 4400 / 9170 loci
    Reading 4500 / 9170 loci
    Reading 4600 / 9170 loci
    Reading 4700 / 9170 loci
    Reading 4800 / 9170 loci
    Reading 4900 / 9170 loci
    Reading 5000 / 9170 loci
    Reading 5100 / 9170 loci
    Reading 5200 / 9170 loci
    Reading 5300 / 9170 loci
    Reading 5400 / 9170 loci
    Reading 5500 / 9170 loci
    Reading 5600 / 9170 loci
    Reading 5700 / 9170 loci
    Reading 5800 / 9170 loci
    Reading 5900 / 9170 loci
    Reading 6000 / 9170 loci
    Reading 6100 / 9170 loci
    Reading 6200 / 9170 loci
    Reading 6300 / 9170 loci
    Reading 6400 / 9170 loci
    Reading 6500 / 9170 loci
    Reading 6600 / 9170 loci
    Reading 6700 / 9170 loci
    Reading 6800 / 9170 loci
    Reading 6900 / 9170 loci
    Reading 7000 / 9170 loci
    Reading 7100 / 9170 loci
    Reading 7200 / 9170 loci
    Reading 7300 / 9170 loci
    Reading 7400 / 9170 loci
    Reading 7500 / 9170 loci
    Reading 7600 / 9170 loci
    Reading 7700 / 9170 loci
    Reading 7800 / 9170 loci
    Reading 7900 / 9170 loci
    Reading 8000 / 9170 loci
    Reading 8100 / 9170 loci
    Reading 8200 / 9170 loci
    Reading 8300 / 9170 loci
    Reading 8400 / 9170 loci
    Reading 8500 / 9170 loci
    Reading 8600 / 9170 loci
    Reading 8700 / 9170 loci
    Reading 8800 / 9170 loci
    Reading 8900 / 9170 loci
    Reading 9000 / 9170 loci
    Reading 9100 / 9170 loci
    Reading 9170 / 9170 loci.
    ## Done.

    ##     number of markers with REF/ALT change(s) = 48

    ## Scanning for monomorphic markers...

    ##     Number of markers before = 9170

    ##     Number of monomorphic markers removed = 0

    ## 
    ## Tidy genomic data:

    ##     Number of markers: 9170

    ##     Number of chromosome/contig/scaffold: 9170

    ##     Number of individuals: 137

    ##     Number of populations: 18

    ## 
    ## Writing tidy data set:
    ## OL-c80-66-s67-m70x62-maf025-maf025-u.rad

``` r
info <- as.data.frame(read.table("OL-c80-66-s67.strata",header = T,sep = "\t",stringsAsFactors = F))

mystrats <- as.data.frame(matrix(,nrow = length(indNames(rad.maf$genind.no.imputation)),ncol=5))
colnames(mystrats) <- c("POPULATION","REGION","NS","LATITUDE","LONGITUDE")

for(i in 1:nrow(info)){
    j <- grep(gsub("_","-",info[i,1]),indNames(rad.maf$genind.no.imputation),value=FALSE)
    mystrats[j,1] <-info$STRATA[i] 
    mystrats[j,2] <-info$REGION[i]
    mystrats[j,3] <-info$NS[i]
    mystrats[j,4] <-info$LATITUDE[i]
    mystrats[j,5] <-info$LONGITUDE[i]
}
just.strats <- select(mystrats,c("POPULATION","REGION","NS"))
stratted <- strata(rad.maf$genind.no.imputation, formula= ~NS/REGION/POPULATION, combine = TRUE,just.strats)
stratted@other <- select(mystrats, LATITUDE,LONGITUDE)
```

``` r
save(stratted, file=paste(filtsuf,"-u.genind",sep=""))
```

Make input for Structure from .vcf file.
========================================

``` r
write_structure(rad.maf$tidy.data, filename=paste(filtsuf,"-u",sep=""))
```

Make input for Bayescan
=======================

``` r
x <- write_bayescan(rad.maf$tidy.data, filename=paste(filtsuf,"-u-BS",sep=""))
```

    ## Generating BayeScan file...

    ## Using markers common in all populations:

    ##     Number of markers before = 9170

    ##     Number of markers removed = 11

    ##     Number of common markers between populations) = 9159

    ## Scanning for monomorphic markers...

    ##     Number of markers before = 9159

    ##     Number of monomorphic markers removed = 0

    ##     generating REF/ALT dictionary

    ##     integrating new genotype codings...

    ## writing BayeScan file with:
    ##     Number of populations: 18
    ##     Number of individuals: 137
    ##     Number of biallelic markers: 9159

    ## Writting populations dictionary

    ## Writting markers dictionary

Make input for OutFLANK
=======================

``` r
#Write file with allele counts per individual for OutFLANK
write.table(stratted@tab, file = paste(filtsuf,"-u.tab",sep=""),sep = "\t",row.names = T,col.names = T,quote = F )
#Write 2 files with different strata levels
write.table(strata(stratted)$POPULATION, file = paste(filtsuf,".pop",sep=""),sep = "\t",row.names = F,col.names = F,quote = F )
write.table(strata(stratted)$REGION, file = paste(filtsuf,".reg",sep=""),sep = "\t",row.names = F,col.names = F,quote = F )
```

Make Treemix file
=================

``` r
OL.gp <- genind2genpop(stratted,pop=strata(stratted)$POPULATION)
```

    ## 
    ##  Converting data from a genind to a genpop object... 
    ## 
    ## ...done.

``` r
write.table(OL.gp$tab, file=paste(filtsuf,"-u.gp",sep=""),sep = "\t",row.names = T,col.names = T,quote = F )
system('python ../Scripts/genpop2Treemix.py OL-c80-66-s67-m70x62-maf025-u.gp OL-m70x62-maf025.pop.TM')
system('gzip OL-m70x62-maf025.pop.TM')
```

Make an EEMS file
=================

OL- with OR
-----------

``` r
suf <- "OL-m70x62-maf025"
geno <- stratted@tab
stopifnot(identical(stratted@type, 'codom'))
# Get rid of non-biallelic loci
multi.loci <- names(which(stratted@loc.n.all != 2))
multi.cols <- which(grepl(paste0("^", multi.loci, "\\.\\d+$", collapse = "|"), colnames(geno)))
if (length(multi.cols)) geno <- geno[, - multi.cols]
nloci <- dim(geno)[2] / 2
#Choose allele to be "derived" allele.
geno <- geno[, c(seq(1,ncol(geno),by = 2))]

dim(geno)
```

    ## [1]  137 9170

bed2diff functions

``` r
bed2diffs_v1 <- function(Geno) {
  nIndiv <- nrow(Geno)
  nSites <- ncol(Geno)
  Diffs <- matrix(0, nIndiv, nIndiv)
  
  for (i in seq(nIndiv - 1)) {
    for (j in seq(i + 1, nIndiv)) {
      x <- Geno[i, ]
      y <- Geno[j, ]
      Diffs[i, j] <- mean((x - y)^2, na.rm = TRUE)
      Diffs[j, i] <- Diffs[i, j]
    }
  }
  Diffs
}
bed2diffs_v2 <- function(Geno) {
  nIndiv <- nrow(Geno)
  nSites <- ncol(Geno)
  Miss <- is.na(Geno)
  ## Impute NAs with the column means (= twice the allele frequencies)
  Mean <- matrix(colMeans(Geno, na.rm = TRUE), ## a row of means
                 nrow = nIndiv, ncol = nSites, byrow = TRUE) ## a matrix with nIndiv identical rows of means
  Mean[Miss == 0] <- 0 ## Set the means that correspond to observed genotypes to 0
  Geno[Miss == 1] <- 0 ## Set the missing genotypes to 0 (used to be NA) 
  Geno <- Geno + Mean
  ## Compute similarities
  Sim <- Geno %*% t(Geno) / nSites
  SelfSim <- diag(Sim) ## self-similarities
  vector1s <- rep(1, nIndiv) ## vector of 1s
  ## This chunk generates a `diffs` matrix
  Diffs <- SelfSim %*% t(vector1s) + vector1s %*% t(SelfSim) - 2 * Sim
  Diffs
}
```

``` r
# 137 inds, 9,170 loci
#bed2diffs functions  
diffs.v1 <- bed2diffs_v1(geno)
diffs.v2 <- bed2diffs_v2(geno)
diffs.v1 <- round(diffs.v1, digits = 6)
diffs.v2 <- round(diffs.v2, digits = 6)
```

Check that the dissimilarity matrix has one positive eigenvalue and nIndiv-1 negative eigenvalues, as required by a full-rank Euclidean distance matrix.

``` r
sort(round(eigen(diffs.v1)$values, digits = 2))
```

    ##   [1] -6.39 -3.04 -2.05 -1.77 -1.39 -1.22 -1.04 -0.94 -0.80 -0.79
    ##  [11] -0.75 -0.74 -0.71 -0.70 -0.69 -0.68 -0.67 -0.66 -0.65 -0.64
    ##  [21] -0.64 -0.63 -0.63 -0.62 -0.61 -0.61 -0.60 -0.59 -0.59 -0.58
    ##  [31] -0.58 -0.57 -0.57 -0.57 -0.57 -0.56 -0.56 -0.55 -0.55 -0.54
    ##  [41] -0.54 -0.53 -0.53 -0.53 -0.53 -0.52 -0.51 -0.51 -0.51 -0.50
    ##  [51] -0.49 -0.49 -0.49 -0.49 -0.48 -0.48 -0.47 -0.47 -0.47 -0.47
    ##  [61] -0.46 -0.46 -0.45 -0.45 -0.45 -0.44 -0.44 -0.43 -0.43 -0.43
    ##  [71] -0.43 -0.42 -0.42 -0.42 -0.41 -0.41 -0.41 -0.41 -0.40 -0.40
    ##  [81] -0.40 -0.39 -0.39 -0.39 -0.38 -0.38 -0.38 -0.38 -0.37 -0.37
    ##  [91] -0.37 -0.36 -0.36 -0.36 -0.35 -0.35 -0.35 -0.35 -0.35 -0.34
    ## [101] -0.34 -0.34 -0.33 -0.33 -0.33 -0.33 -0.32 -0.32 -0.32 -0.31
    ## [111] -0.31 -0.31 -0.30 -0.30 -0.30 -0.29 -0.29 -0.29 -0.28 -0.27
    ## [121] -0.27 -0.27 -0.26 -0.26 -0.25 -0.25 -0.24 -0.24 -0.23 -0.22
    ## [131] -0.22 -0.21 -0.20 -0.19 -0.16 -0.15 73.84

``` r
sort(round(eigen(diffs.v2)$values, digits = 2))
```

    ##   [1] -4.62 -2.07 -1.44 -1.33 -1.02 -0.93 -0.91 -0.71 -0.66 -0.64
    ##  [11] -0.61 -0.60 -0.59 -0.58 -0.58 -0.57 -0.56 -0.56 -0.55 -0.55
    ##  [21] -0.54 -0.54 -0.53 -0.52 -0.52 -0.51 -0.51 -0.51 -0.50 -0.49
    ##  [31] -0.48 -0.48 -0.47 -0.47 -0.47 -0.46 -0.46 -0.45 -0.45 -0.45
    ##  [41] -0.44 -0.44 -0.44 -0.43 -0.43 -0.43 -0.43 -0.42 -0.42 -0.42
    ##  [51] -0.41 -0.41 -0.41 -0.40 -0.40 -0.40 -0.39 -0.39 -0.39 -0.39
    ##  [61] -0.39 -0.38 -0.38 -0.38 -0.38 -0.38 -0.37 -0.37 -0.37 -0.36
    ##  [71] -0.36 -0.36 -0.36 -0.35 -0.35 -0.35 -0.35 -0.34 -0.34 -0.34
    ##  [81] -0.34 -0.33 -0.33 -0.33 -0.32 -0.32 -0.32 -0.32 -0.32 -0.31
    ##  [91] -0.31 -0.31 -0.30 -0.30 -0.30 -0.30 -0.30 -0.29 -0.29 -0.29
    ## [101] -0.28 -0.28 -0.28 -0.27 -0.27 -0.26 -0.26 -0.26 -0.26 -0.25
    ## [111] -0.25 -0.25 -0.25 -0.24 -0.23 -0.23 -0.23 -0.23 -0.23 -0.22
    ## [121] -0.22 -0.22 -0.21 -0.21 -0.20 -0.20 -0.20 -0.19 -0.19 -0.19
    ## [131] -0.19 -0.18 -0.17 -0.17 -0.16 -0.16 59.75

V1 is Euclidean, use this matrix.

Make list of GPS coordinates per individual.

``` r
## Get gps coordinates.
gps_matrix <- select(mystrats,c("LONGITUDE","LATITUDE"))
```

Write file for v1

``` r
write.table(diffs.v1, paste(suf,".v1.diffs",sep=""), 
            col.names = FALSE, row.names = FALSE, quote = FALSE)
write.table(gps_matrix, paste(suf,".v1.coord",sep=""),col.names = FALSE, row.names = FALSE,quote = FALSE)
```

OL - Without Coos Bay
---------------------

Coos Bay is a recent transplant from Willapa Bay, so I exclude it from my EEMS analyses.

``` r
gind.xOR <- stratted[!(indNames(stratted) %in% c("OR1-11","OR1-1","OR1-2","OR1-4","OR1-5","OR1-6","OR1-7")),drop=TRUE]

suf <- "OL-xOR1-m70x62-maf025"
geno <- gind.xOR@tab
stopifnot(identical(gind.xOR@type, 'codom'))
# Get rid of non-biallelic loci
multi.loci <- names(which(gind.xOR@loc.n.all != 2))
multi.cols <- which(grepl(paste0("^", multi.loci, "\\.\\d+$", collapse = "|"), colnames(geno)))
if (length(multi.cols)) geno <- geno[, - multi.cols]
nloci <- dim(geno)[2] / 2
#Choose allele to be "derived" allele.
geno <- geno[, c(seq(1,ncol(geno),by = 2))]

dim(geno)
```

    ## [1]  130 9170

``` r
# 130 inds, 9,170 loci
#bed2diffs functions  
diffs.v1 <- bed2diffs_v1(geno)
diffs.v2 <- bed2diffs_v2(geno)
diffs.v1 <- round(diffs.v1, digits = 6)
diffs.v2 <- round(diffs.v2, digits = 6)
```

Check that the dissimilarity matrix has one positive eigenvalue and nIndiv-1 negative eigenvalues, as required by a full-rank Euclidean distance matrix.

``` r
sort(round(eigen(diffs.v1)$values, digits = 2))
```

    ##   [1] -6.34 -2.45 -2.04 -1.74 -1.35 -1.13 -1.02 -0.93 -0.79 -0.78
    ##  [11] -0.74 -0.73 -0.71 -0.69 -0.69 -0.68 -0.67 -0.66 -0.65 -0.64
    ##  [21] -0.63 -0.63 -0.62 -0.61 -0.61 -0.60 -0.60 -0.59 -0.58 -0.58
    ##  [31] -0.57 -0.57 -0.57 -0.56 -0.56 -0.55 -0.55 -0.55 -0.55 -0.54
    ##  [41] -0.53 -0.53 -0.53 -0.52 -0.52 -0.51 -0.51 -0.50 -0.50 -0.50
    ##  [51] -0.49 -0.48 -0.48 -0.48 -0.47 -0.47 -0.47 -0.46 -0.46 -0.46
    ##  [61] -0.45 -0.45 -0.45 -0.44 -0.44 -0.44 -0.43 -0.43 -0.43 -0.42
    ##  [71] -0.42 -0.42 -0.41 -0.41 -0.41 -0.40 -0.40 -0.40 -0.40 -0.39
    ##  [81] -0.39 -0.38 -0.38 -0.38 -0.38 -0.37 -0.37 -0.37 -0.36 -0.36
    ##  [91] -0.36 -0.36 -0.35 -0.35 -0.35 -0.34 -0.34 -0.34 -0.33 -0.33
    ## [101] -0.33 -0.32 -0.32 -0.32 -0.32 -0.31 -0.31 -0.30 -0.30 -0.29
    ## [111] -0.29 -0.29 -0.29 -0.28 -0.27 -0.27 -0.27 -0.26 -0.25 -0.25
    ## [121] -0.25 -0.24 -0.23 -0.22 -0.21 -0.21 -0.20 -0.18 -0.15 70.26

``` r
sort(round(eigen(diffs.v2)$values, digits = 2))
```

    ##   [1] -4.58 -1.73 -1.43 -1.31 -0.98 -0.93 -0.81 -0.70 -0.66 -0.64
    ##  [11] -0.61 -0.60 -0.59 -0.58 -0.57 -0.57 -0.56 -0.56 -0.55 -0.54
    ##  [21] -0.54 -0.53 -0.52 -0.52 -0.52 -0.51 -0.51 -0.50 -0.49 -0.48
    ##  [31] -0.48 -0.48 -0.47 -0.47 -0.46 -0.46 -0.45 -0.45 -0.45 -0.45
    ##  [41] -0.44 -0.44 -0.43 -0.43 -0.43 -0.42 -0.42 -0.42 -0.41 -0.41
    ##  [51] -0.41 -0.40 -0.40 -0.40 -0.39 -0.39 -0.39 -0.39 -0.38 -0.38
    ##  [61] -0.38 -0.38 -0.38 -0.37 -0.37 -0.37 -0.36 -0.36 -0.36 -0.36
    ##  [71] -0.36 -0.36 -0.35 -0.35 -0.34 -0.34 -0.34 -0.33 -0.33 -0.33
    ##  [81] -0.32 -0.32 -0.32 -0.32 -0.32 -0.31 -0.31 -0.31 -0.31 -0.30
    ##  [91] -0.30 -0.30 -0.30 -0.29 -0.29 -0.28 -0.28 -0.28 -0.27 -0.27
    ## [101] -0.27 -0.26 -0.26 -0.26 -0.25 -0.25 -0.25 -0.24 -0.24 -0.23
    ## [111] -0.23 -0.23 -0.22 -0.22 -0.22 -0.21 -0.21 -0.21 -0.20 -0.20
    ## [121] -0.20 -0.19 -0.19 -0.19 -0.18 -0.17 -0.17 -0.16 -0.16 56.82

Make GPS coordinate file. Note it is a little different than when we had all individuals.

``` r
## Get gps coordinates.
xOR.info <- dplyr::filter(info, !grepl("OR1",INDIVIDUALS))
gps_matrix <- matrix(,nrow = length(indNames(gind.xOR)),ncol=2)

for(i in 1:nrow(xOR.info)){
    j <- grep(gsub("_","-",xOR.info[i,1]),indNames(gind.xOR),value=FALSE)
    gps_matrix[j,1] <-xOR.info$LONGITUDE[i]
    gps_matrix[j,2] <-xOR.info$LATITUDE[i]
}
```

Write file for v1

``` r
write.table(diffs.v1, paste(suf,".v1.diffs",sep=""), 
            col.names = FALSE, row.names = FALSE, quote = FALSE)
write.table(gps_matrix, paste(suf,".v1.coord",sep=""),col.names = FALSE, row.names = FALSE,quote = FALSE)
```

Plot EEMS
---------

After running EEMS, plot EEMS output:

``` r
library(rEEMSplots) #Get from EEMS github
library(rgdal)
```

    ## Loading required package: sp

    ## rgdal: version: 1.2-18, (SVN revision 718)
    ##  Geospatial Data Abstraction Library extensions to R successfully loaded
    ##  Loaded GDAL runtime: GDAL 1.11.3, released 2015/09/16
    ##  Path to GDAL shared files: /usr/share/gdal/1.11
    ##  GDAL binary built with GEOS: TRUE 
    ##  Loaded PROJ.4 runtime: Rel. 4.9.2, 08 September 2015, [PJ_VERSION: 492]
    ##  Path to PROJ.4 shared files: (autodetected)
    ##  Linking to sp version: 1.2-7

``` r
library(rworldmap)
```

    ## ### Welcome to rworldmap ###

    ## For a short introduction type :   vignette('rworldmap')

``` r
library(rworldxtra)
```

Make a list of all EEMS directories to plot all the results into 1 plot:

``` r
dirs = c("OLxOR1-m70x62maf025-SkI-nD200-ch1","OLxOR1-m70x62maf025-SkI-nD200-ch2", "OLxOR1-m70x62maf025-SkI-nD300-ch1","OLxOR1-m70x62maf025-SkI-nD300-ch2","OLxOR1-m70x62maf025-SkI-nD350-ch1","OLxOR1-m70x62maf025-SkI-nD350-ch2","OLxOR1-m70x62maf025-SkI-nD400-ch1","OLxOR1-m70x62maf025-SkI-nD400-ch2","OLxOR1-m70x62maf025-SkI-nD500-ch1","OLxOR1-m70x62maf025-SkI-nD500-ch2","OLxOR1-m70x62maf025-SkI-nD600-ch1","OLxOR1-m70x62maf025-SkI-nD600-ch2")
```

**This command does not run well in Notebook. Run in R console**.

``` r
#eems.plots(mcmcpath = dirs, plotpath = "OLxOR1-m70x62maf025-SkI-All-plots",longlat = T,add.grid=F,add.outline = T,add.demes = T,projection.in = "+proj=longlat +datum=WGS84",projection.out = "+proj=merc +datum=WGS84",add.map = T,add.abline = T, add.r.squared = T)
```
