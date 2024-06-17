#!/bin/bash

file=gwas_data/merged_file/chrome_merged

plink1.9/plink --bfile ${file} \
        --remove indiv.sampleQC.toberemoved \
        --make-bed \
        --out geno_filter_9.sampleqc
        # --update-sex indiv.sexinfo \
