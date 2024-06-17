#!/bin/bash

file=genotype_qc/04_mafhwe/geno_filter_4

plink1.9/plink --bfile ${file} \
      --mind 0.05 \
      --make-bed \
      --out geno_filter_5

