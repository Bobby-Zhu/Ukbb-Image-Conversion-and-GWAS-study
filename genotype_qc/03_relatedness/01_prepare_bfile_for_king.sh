#!/bin/bash
exe_plink=/home/sanghyeon/tools/plink/plink

file=../02_duplicate/NG00026_geno0.02.rmdup

${exe_plink} --bfile $file \
            --chr 1-22 \
            --maf 0.05 \
            --geno 0.01 \
            --make-bed \
            --out NG00026_geno0.02.rmdup.king