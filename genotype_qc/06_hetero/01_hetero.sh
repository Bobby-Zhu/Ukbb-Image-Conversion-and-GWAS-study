#!/bin/bash

file=genotype_qc/05_mind/geno_filter_5

plink1.9/plink --bfile ${file} \
      --het \
      --missing \
      --out geno_filter_6.1


file=geno_filter_6.1

Rscript 06.xx_hetmissplot.R ${file}


cat ${file}.het_5sdout | cut -f1,2 | grep -v "FID" > hetmiss_toberemoved


file=genotype_qc/05_mind/geno_filter_6.1

plink --bfile ${file} \
      --remove hetmiss_toberemoved \
      --make-bed \
      --out genotype_qc/05_mind/geno_filter_6.3
