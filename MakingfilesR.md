Making files for other programs
================
Katherine Silliman

-   [Load adegenet objects](#load-adegenet-objects)
-   [Make input for OutFLANK](#make-input-for-outflank)
-   [Make Treemix file](#make-treemix-file)
-   [Make an EEMS file](#make-an-eems-file)
    -   [OL- with OR](#ol--with-or)
    -   [Plot EEMS](#plot-eems)

Load adegenet objects
=====================

``` r
load("PCA/OL-c80-66-s67-m70x62-maf025-u.adegenet")
load("PCA/All5C-c80-66-s67-m70x62-mac4-u.adegenet")
load("PCA/All-c80-66-m70x62-mac4.adegenet")
g.indF
```

    ## Loading required package: adegenet

    ## Loading required package: ade4

    ## 
    ##    /// adegenet 2.0.1 is loaded ////////////
    ## 
    ##    > overview: '?adegenet'
    ##    > tutorials/doc/questions: 'adegenetWeb()' 
    ##    > bug reports/feature requests: adegenetIssues()

    ## /// GENIND OBJECT /////////
    ## 
    ##  // 137 individuals; 9,170 loci; 18,340 alleles; size: 13.9 Mb
    ## 
    ##  // Basic content
    ##    @tab:  137 x 18340 matrix of allele counts
    ##    @loc.n.all: number of alleles per locus (range: 2-2)
    ##    @loc.fac: locus factor for the 18340 columns of @tab
    ##    @all.names: list of allele names for each locus
    ##    @ploidy: ploidy of each individual  (range: 2-2)
    ##    @type:  codom
    ##    @call: read.structure(file = infile, n.ind = nind.65, n.loc = nloci.m50x65, 
    ##     onerowperind = FALSE, col.lab = 1, col.pop = 2, row.marknames = 1, 
    ##     ask = FALSE)
    ## 
    ##  // Optional content
    ##    @pop: population of each individual (group size range: 3-11)
    ##    @strata: a data frame with 3 columns ( Population, Region, North.South )

``` r
All.g.indm70
```

    ## /// GENIND OBJECT /////////
    ## 
    ##  // 145 individuals; 9,322 loci; 18,644 alleles; size: 14.7 Mb
    ## 
    ##  // Basic content
    ##    @tab:  145 x 18644 matrix of allele counts
    ##    @loc.n.all: number of alleles per locus (range: 2-2)
    ##    @loc.fac: locus factor for the 18644 columns of @tab
    ##    @all.names: list of allele names for each locus
    ##    @ploidy: ploidy of each individual  (range: 2-2)
    ##    @type:  codom
    ##    @call: read.structure(file = infile, n.ind = nind.65, n.loc = nloci.m50x65, 
    ##     onerowperind = FALSE, col.lab = 1, col.pop = 2, row.marknames = 1, 
    ##     ask = FALSE)
    ## 
    ##  // Optional content
    ##    @pop: population of each individual (group size range: 2-11)
    ##    @strata: a data frame with 3 columns ( Population, Region, North.South )

``` r
all.g.ind
```

    ## /// GENIND OBJECT /////////
    ## 
    ##  // 148 individuals; 9,322 loci; 18,644 alleles; size: 14.9 Mb
    ## 
    ##  // Basic content
    ##    @tab:  148 x 18644 matrix of allele counts
    ##    @loc.n.all: number of alleles per locus (range: 2-2)
    ##    @loc.fac: locus factor for the 18644 columns of @tab
    ##    @all.names: list of allele names for each locus
    ##    @ploidy: ploidy of each individual  (range: 2-2)
    ##    @type:  codom
    ##    @call: read.structure(file = infile, n.ind = nind.65, n.loc = nloci.m50x65, 
    ##     onerowperind = FALSE, col.lab = 1, col.pop = 2, row.marknames = 1, 
    ##     ask = FALSE)
    ## 
    ##  // Optional content
    ##    @pop: population of each individual (group size range: 1-11)
    ##    @strata: a data frame with 3 columns ( Population, Region, North.South )

Make input for OutFLANK
=======================

``` r
#Write file with allele counts per individual for OutFLANK
write.table(g.indF@tab, file = "Outlier/OL-66-m70x62-maf025.tab",sep = "\t",row.names = T,col.names = T,quote = F )
write.table(strata(g.indF)$Population, file = "Outlier/OL-66-m70x62-maf025.pop",sep = "\t",row.names = F,col.names = F,quote = F )
write.table(strata(g.indF)$Region, file = "Outlier/OL-66-m70x62-maf025.regs",sep = "\t",row.names = F,col.names = F,quote = F )
```

Make Treemix file
=================

``` r
OL.gp <- genind2genpop(g.indF,pop=strata(g.indF)$Population)
```

    ## 
    ##  Converting data from a genind to a genpop object... 
    ## 
    ## ...done.

``` r
write.table(OL.gp$tab, file="Treemix/OL-m70x62-maf025.gp",sep = "\t",row.names = T,col.names = T,quote = F )
system('python ../../Methods/Scripts/genpop2Treemix.py Treemix/OL-m70x62-maf025.gp Treemix/OL-m70x62-maf025.TM.txt')
system('gzip Treemix/OL-m70x62-maf025.TM.txt')
```

Make an EEMS file
=================

OL- with OR
-----------

``` r
suf <- "EEMS/OL-m70x62-maf025"
geno <- g.indF@tab
stopifnot(identical(g.indF@type, 'codom'))
# Get rid of non-biallelic loci
multi.loci <- names(which(g.indF@loc.n.all != 2))
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

    ##   [1] -6.39 -3.04 -2.05 -1.77 -1.39 -1.22 -1.04 -0.94 -0.80 -0.79 -0.75
    ##  [12] -0.74 -0.71 -0.70 -0.69 -0.68 -0.67 -0.66 -0.65 -0.64 -0.64 -0.63
    ##  [23] -0.63 -0.62 -0.61 -0.61 -0.60 -0.59 -0.59 -0.58 -0.58 -0.57 -0.57
    ##  [34] -0.57 -0.57 -0.56 -0.56 -0.55 -0.55 -0.54 -0.54 -0.53 -0.53 -0.53
    ##  [45] -0.53 -0.52 -0.51 -0.51 -0.51 -0.50 -0.49 -0.49 -0.49 -0.49 -0.48
    ##  [56] -0.48 -0.47 -0.47 -0.47 -0.47 -0.46 -0.46 -0.45 -0.45 -0.45 -0.44
    ##  [67] -0.44 -0.43 -0.43 -0.43 -0.43 -0.42 -0.42 -0.42 -0.41 -0.41 -0.41
    ##  [78] -0.41 -0.40 -0.40 -0.40 -0.39 -0.39 -0.39 -0.38 -0.38 -0.38 -0.38
    ##  [89] -0.37 -0.37 -0.37 -0.36 -0.36 -0.36 -0.35 -0.35 -0.35 -0.35 -0.35
    ## [100] -0.34 -0.34 -0.34 -0.33 -0.33 -0.33 -0.33 -0.32 -0.32 -0.32 -0.31
    ## [111] -0.31 -0.31 -0.30 -0.30 -0.30 -0.29 -0.29 -0.29 -0.28 -0.27 -0.27
    ## [122] -0.27 -0.26 -0.26 -0.25 -0.25 -0.24 -0.24 -0.23 -0.22 -0.22 -0.21
    ## [133] -0.20 -0.19 -0.16 -0.15 73.84

``` r
sort(round(eigen(diffs.v2)$values, digits = 2))
```

    ##   [1] -4.62 -2.07 -1.44 -1.33 -1.02 -0.93 -0.91 -0.71 -0.66 -0.64 -0.61
    ##  [12] -0.60 -0.59 -0.58 -0.58 -0.57 -0.56 -0.56 -0.55 -0.55 -0.54 -0.54
    ##  [23] -0.53 -0.52 -0.52 -0.51 -0.51 -0.51 -0.50 -0.49 -0.48 -0.48 -0.47
    ##  [34] -0.47 -0.47 -0.46 -0.46 -0.45 -0.45 -0.45 -0.44 -0.44 -0.44 -0.43
    ##  [45] -0.43 -0.43 -0.43 -0.42 -0.42 -0.42 -0.41 -0.41 -0.41 -0.40 -0.40
    ##  [56] -0.40 -0.39 -0.39 -0.39 -0.39 -0.39 -0.38 -0.38 -0.38 -0.38 -0.38
    ##  [67] -0.37 -0.37 -0.37 -0.36 -0.36 -0.36 -0.36 -0.35 -0.35 -0.35 -0.35
    ##  [78] -0.34 -0.34 -0.34 -0.34 -0.33 -0.33 -0.33 -0.32 -0.32 -0.32 -0.32
    ##  [89] -0.32 -0.31 -0.31 -0.31 -0.30 -0.30 -0.30 -0.30 -0.30 -0.29 -0.29
    ## [100] -0.29 -0.28 -0.28 -0.28 -0.27 -0.27 -0.26 -0.26 -0.26 -0.26 -0.25
    ## [111] -0.25 -0.25 -0.25 -0.24 -0.23 -0.23 -0.23 -0.23 -0.23 -0.22 -0.22
    ## [122] -0.22 -0.21 -0.21 -0.20 -0.20 -0.20 -0.19 -0.19 -0.19 -0.19 -0.18
    ## [133] -0.17 -0.17 -0.16 -0.16 59.75

Make distance matrix

``` r
## Get gps coordinates.
pop2gps <- read.table(file = "../Making_Files/OLPop2Int_Loc.txt", header=T)
names <- indNames(g.indF)
N = length(names)
gps_matrix = matrix(data = NA, nrow = N, ncol = 2)
for(i in 1:nrow(pop2gps)){
    popmatch <- grep(pop2gps[i,1],names,value=FALSE)
    for(j in popmatch){
        gps_matrix[j,2] <- pop2gps$Latitude[i]
        gps_matrix[j,1] <- pop2gps$Longitude[i]
    }
}
```

Write file for v1

``` r
write.table(diffs.v1, paste(suf,".v1.diffs",sep=""), 
            col.names = FALSE, row.names = FALSE, quote = FALSE)
write.table(gps_matrix, paste(suf,".v1.coord",sep=""),col.names = FALSE, row.names = FALSE,quote = FALSE)
```

``` r
gind.xOR <- g.indF[!(indNames(g.indF) %in% c("OR1_1","OR1_7","OR1_11","OR1_12","OR1_1B_6","OR1_2","OR1_3","OR1_4","OR1_5","OR1_6","OR1_7w_6")),drop=TRUE]

suf <- "EEMS/OL-m70x62-maf025-xOR1"
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

    ##   [1] -6.34 -2.45 -2.04 -1.74 -1.35 -1.13 -1.02 -0.93 -0.79 -0.78 -0.74
    ##  [12] -0.73 -0.71 -0.69 -0.69 -0.68 -0.67 -0.66 -0.65 -0.64 -0.63 -0.63
    ##  [23] -0.62 -0.61 -0.61 -0.60 -0.60 -0.59 -0.58 -0.58 -0.57 -0.57 -0.57
    ##  [34] -0.56 -0.56 -0.55 -0.55 -0.55 -0.55 -0.54 -0.53 -0.53 -0.53 -0.52
    ##  [45] -0.52 -0.51 -0.51 -0.50 -0.50 -0.50 -0.49 -0.48 -0.48 -0.48 -0.47
    ##  [56] -0.47 -0.47 -0.46 -0.46 -0.46 -0.45 -0.45 -0.45 -0.44 -0.44 -0.44
    ##  [67] -0.43 -0.43 -0.43 -0.42 -0.42 -0.42 -0.41 -0.41 -0.41 -0.40 -0.40
    ##  [78] -0.40 -0.40 -0.39 -0.39 -0.38 -0.38 -0.38 -0.38 -0.37 -0.37 -0.37
    ##  [89] -0.36 -0.36 -0.36 -0.36 -0.35 -0.35 -0.35 -0.34 -0.34 -0.34 -0.33
    ## [100] -0.33 -0.33 -0.32 -0.32 -0.32 -0.32 -0.31 -0.31 -0.30 -0.30 -0.29
    ## [111] -0.29 -0.29 -0.29 -0.28 -0.27 -0.27 -0.27 -0.26 -0.25 -0.25 -0.25
    ## [122] -0.24 -0.23 -0.22 -0.21 -0.21 -0.20 -0.18 -0.15 70.26

``` r
sort(round(eigen(diffs.v2)$values, digits = 2))
```

    ##   [1] -4.58 -1.73 -1.43 -1.31 -0.98 -0.93 -0.81 -0.70 -0.66 -0.64 -0.61
    ##  [12] -0.60 -0.59 -0.58 -0.57 -0.57 -0.56 -0.56 -0.55 -0.54 -0.54 -0.53
    ##  [23] -0.52 -0.52 -0.52 -0.51 -0.51 -0.50 -0.49 -0.48 -0.48 -0.48 -0.47
    ##  [34] -0.47 -0.46 -0.46 -0.45 -0.45 -0.45 -0.45 -0.44 -0.44 -0.43 -0.43
    ##  [45] -0.43 -0.42 -0.42 -0.42 -0.41 -0.41 -0.41 -0.40 -0.40 -0.40 -0.39
    ##  [56] -0.39 -0.39 -0.39 -0.38 -0.38 -0.38 -0.38 -0.38 -0.37 -0.37 -0.37
    ##  [67] -0.36 -0.36 -0.36 -0.36 -0.36 -0.36 -0.35 -0.35 -0.34 -0.34 -0.34
    ##  [78] -0.33 -0.33 -0.33 -0.32 -0.32 -0.32 -0.32 -0.32 -0.31 -0.31 -0.31
    ##  [89] -0.31 -0.30 -0.30 -0.30 -0.30 -0.29 -0.29 -0.28 -0.28 -0.28 -0.27
    ## [100] -0.27 -0.27 -0.26 -0.26 -0.26 -0.25 -0.25 -0.25 -0.24 -0.24 -0.23
    ## [111] -0.23 -0.23 -0.22 -0.22 -0.22 -0.21 -0.21 -0.21 -0.20 -0.20 -0.20
    ## [122] -0.19 -0.19 -0.19 -0.18 -0.17 -0.17 -0.16 -0.16 56.82

Make distance matrix

``` r
## Get gps coordinates.
pop2gps <- read.table(file = "../Making_Files/OLPop2Int_Loc.txt", header=T)
names <- indNames(gind.xOR)
N = length(names)
gps_matrix = matrix(data = NA, nrow = N, ncol = 2)
for(i in 1:nrow(pop2gps)){
    popmatch <- grep(pop2gps[i,1],names,value=FALSE)
    for(j in popmatch){
        gps_matrix[j,2] <- pop2gps$Latitude[i]
        gps_matrix[j,1] <- pop2gps$Longitude[i]
    }
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

After running, plot EEMS output:

``` r
library(rEEMSplots) #Get from EEMS github
library(rgdal)
```

    ## Loading required package: sp

    ## rgdal: version: 1.2-7, (SVN revision 660)
    ##  Geospatial Data Abstraction Library extensions to R successfully loaded
    ##  Loaded GDAL runtime: GDAL 1.11.3, released 2015/09/16
    ##  Path to GDAL shared files: /usr/share/gdal/1.11
    ##  Loaded PROJ.4 runtime: Rel. 4.9.2, 08 September 2015, [PJ_VERSION: 492]
    ##  Path to PROJ.4 shared files: (autodetected)
    ##  Linking to sp version: 1.2-4

``` r
library(rworldmap)
```

    ## ### Welcome to rworldmap ###

    ## For a short introduction type :   vignette('rworldmap')

``` r
library(rworldxtra)
```

``` r
eems.plots(mcmcpath = "EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1", plotpath = "EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1-plots",longlat = T,add.grid=F,add.outline = T,add.demes = T,projection.in = "+proj=longlat +datum=WGS84",projection.out = "+proj=merc +datum=WGS84",add.map = T,add.abline = T, add.r.squared = T)
```

    ## Input projection: +proj=longlat +datum=WGS84
    ## Output projection: +proj=merc +datum=WGS84

    ## Loading rgdal (required by projection.in)

    ## Loading rworldmap (required by add.map)

    ## Loading rworldxtra (required by add.map)

    ## Using the default DarkOrange to Blue color scheme, with 'white' as the midpoint color.
    ## It combines two color schemes from the 'dichromat' package, which itself is based on
    ## a collection of color schemes for scientific data graphics:
    ##  Light A and Bartlein PJ (2004). The End of the Rainbow? Color Schemes for Improved Data
    ##  Graphics. EOS Transactions of the American Geophysical Union, 85(40), 385.
    ## See also http://geog.uoregon.edu/datagraphics/color_scales.htm

    ## Using 'euclidean' distance to assign interpolation points to Voronoi tiles.

    ## Processing the following EEMS output directories :

    ## EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1

    ## Plotting effective migration surface (posterior mean of m rates)

    ## EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1

    ## Using the default DarkOrange to Blue color scheme, with 'white' as the midpoint color.
    ## It combines two color schemes from the 'dichromat' package, which itself is based on
    ## a collection of color schemes for scientific data graphics:
    ##  Light A and Bartlein PJ (2004). The End of the Rainbow? Color Schemes for Improved Data
    ##  Graphics. EOS Transactions of the American Geophysical Union, 85(40), 385.
    ## See also http://geog.uoregon.edu/datagraphics/color_scales.htm

    ## Plotting effective diversity surface (posterior mean of q rates)

    ## EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1

    ## Using the default DarkOrange to Blue color scheme, with 'white' as the midpoint color.
    ## It combines two color schemes from the 'dichromat' package, which itself is based on
    ## a collection of color schemes for scientific data graphics:
    ##  Light A and Bartlein PJ (2004). The End of the Rainbow? Color Schemes for Improved Data
    ##  Graphics. EOS Transactions of the American Geophysical Union, 85(40), 385.
    ## See also http://geog.uoregon.edu/datagraphics/color_scales.htm

    ## Plotting posterior probability trace

    ## EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1

    ## Plotting average dissimilarities within and between demes

    ## EEMS/OL-c80-m70x62-maf025-xOR1_results/OL-m70x62maf025-xOR1-nD400-ch1
