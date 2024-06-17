#!/bin/bash

file=geno_filter_7.2.pruned

plink --bfile ${file} \
      --check-sex \
      --out geno_filter_7.3.pruned
