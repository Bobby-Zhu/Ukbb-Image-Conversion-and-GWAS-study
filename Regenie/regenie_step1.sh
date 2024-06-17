#!/bin/bash

module load regenie/3.4.1
regenie \
  --step 1 \
  --bed $1 \
  --extract $2 \
  --covarFile $3 \
  --phenoFile $4 \
  --apply-rint \
  --bsize 100 \
  --out $5
