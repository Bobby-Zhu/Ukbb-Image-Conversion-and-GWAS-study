#!/bin/bash

file=genotype_qc/01_geno/geno_filter1

exe_plink=plink1.9/plink
${exe_plink} --bfile ${file} \
            --list-duplicate-vars suppress-first

${exe_plink} --bfile ${file} \
            --exclude ./plink.dupvar \
            --make-bed \
            --out geno_filter_2
