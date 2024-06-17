#!/bin/bash

file=genotype_qc/06_hetero/geno_filter_6.3

plink1.9/plink --bfile ${file} \
      --check-sex \
      --out geno_filter_wo_prune_7.1
