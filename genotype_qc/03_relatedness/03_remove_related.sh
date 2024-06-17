#!/bin/bash

exe_plink=/home/sanghyeon/tools/plink/plink

file=../02_duplicate/NG00026_geno0.02.rmdup

${exe_plink} --bfile $file \
            --remove NG00026_geno0.02.rmdup.kingunrelated_toberemoved.txt \
            --make-bed \
            --out NG00026_geno0.02.rmdup.unrelated