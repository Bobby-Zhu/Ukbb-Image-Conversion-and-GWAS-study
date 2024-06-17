#!/bin/bash

file=genotype_qc/06_hetero/geno_filter_6.3

plink1.9/plink --bfile ${file} \
      --indep-pairwise 50 5 0.5 \
      --out geno_filter_7.2

plink1.9/plink --bfile ${file} \
      --extract NG00026.prune.in \
      --make-bed \
      --out geno_filter_7.2.pruned
