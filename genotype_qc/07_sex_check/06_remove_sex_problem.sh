#!/bin/bash

file=../06_hetero/NG00026_geno0.02.rmdup.unrelated.others.mafhwe.mind.rmhet

plink --bfile ${file} \
      --remove sexcheck.pruned.rmlist \
      --make-bed \
      --out NG00026_geno0.02.rmdup.unrelated.others.mafhwe.mind.rmhet.sexcheck
