#!/bin/bash
# rm call rate 0.98 and chr==0

file=../09_sample_qc_final/geno_filter_9.sampleqc

plink1.9/plink --bfile ${file} \
      --geno 0.02 \
      --chr 1-26 \
      --make-bed \
      --out geno_filter_10.sampleqc.geno

