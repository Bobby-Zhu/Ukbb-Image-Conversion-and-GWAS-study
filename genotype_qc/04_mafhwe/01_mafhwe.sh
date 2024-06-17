#!/bin/bash

file=genotype_qc/02_duplicate/geno_filter_2

plink1.9/plink --bfile ${file} \
      --not-chr 23 \
      --maf 0.01 \
      --hwe 1e-06 \
      --make-bed \
      --out geno_filter_4

