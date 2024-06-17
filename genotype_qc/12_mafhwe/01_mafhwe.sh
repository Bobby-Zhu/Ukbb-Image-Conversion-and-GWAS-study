#!/bin/bash
#SBATCH --job-name=geno_filter_12
#SBATCH --cpus-per-task=4
#SBATCH --mem=44G
#SBATCH --time=48:00:00
#SBATCH --output=geno_filter_12_%j.out
#SBATCH --error=geno_filter_12_%j.err
file=11_duplicate/geno_filter_11

plink1.9/plink --bfile ${file} \
      --not-chr 23 \
      --maf 0.01 \
      --hwe 1e-06 \
      --make-bed \
      --out geno_filter_12

