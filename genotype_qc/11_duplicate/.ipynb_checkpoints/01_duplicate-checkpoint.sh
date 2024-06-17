#!/bin/bash
#SBATCH --job-name=geno_filter_11
#SBATCH --cpus-per-task=4
#SBATCH --mem=44G
#SBATCH --time=48:00:00
#SBATCH --output=geno_filter_11%j.out
#SBATCH --error=geno_filter_11%j.err
file=genotype_qc/10_geno/geno_filter_10.sampleqc.geno

exe_plink=plink1.9/plink

${exe_plink} --bfile ${file} \
            --list-duplicate-vars suppress-first

${exe_plink} --bfile ${file} \
            --exclude ./plink.dupvar \
            --make-bed \
            --out geno_filter_11
