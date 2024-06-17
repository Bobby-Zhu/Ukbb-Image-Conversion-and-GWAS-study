#!/bin/bash
#SBATCH --job-name=geno_filter_regenie
#SBATCH --cpus-per-task=4
#SBATCH --mem=44G
#SBATCH --time=48:00:00
#SBATCH --output=geno_filter_regenie%j.out
#SBATCH --error=geno_filter_regenie%j.err
file=/gpfs/home/bzhu/work/ukbb_cardiac/new_target/GWA_tutorial/genotype_qc/12_mafhwe/geno_filter_12

/gpfs/home/bzhu/plink1.9/plink --bfile ${file} --maf 0.01 --indep-pairwise 1000 100 0.5 --out geno_filter_regenie

