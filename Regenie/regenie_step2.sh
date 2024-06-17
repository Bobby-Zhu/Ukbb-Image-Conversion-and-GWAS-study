#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=shared
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=4

module load regenie/3.4.1
regenie \
  --step 2 \
  --bed $1 \
  --covarFile $2 \
  --phenoFile $3 \
  --apply-rint \
  --bsize 200 \
  --firth \
  --approx \
  --pThresh 0.01 \
  --pred $4 \
  --out $5

