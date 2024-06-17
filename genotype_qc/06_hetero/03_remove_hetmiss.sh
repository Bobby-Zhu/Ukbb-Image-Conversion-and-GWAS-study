#!/bin/bash

cat NG00026.het_5sdout | cut -f1,2 | grep -v "FID" > hetmiss_toberemoved
# grep -v 는 header를 제거하기 위해서

file=../05_mind/NG00026_geno0.02.rmdup.unrelated.others.mafhwe.mind

plink --bfile ${file} \
      --remove hetmiss_toberemoved \
      --make-bed \
      --out ./NG00026_geno0.02.rmdup.unrelated.others.mafhwe.mind.rmhet
