#!/bin/bash

file=./NG00026_geno0.02.rmdup.king

king -b "${file}.bed" \
    --unrelated \
    --degree 2 \
    --cpus 5 \
    --prefix NG00026_geno0.02.rmdup.king > king.log