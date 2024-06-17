#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=shared
#SBATCH --time=100:00:00
#SBATCH --mem=44G
#SBATCH --cpus-per-task=16
#SBATCH --output=%x.oe%j


# Define file paths
BED_FILE_PATH="/gpfs/home/bzhu/work/ukbb_cardiac/new_target/GWA_tutorial/genotype_qc/12_mafhwe/geno_filter_12"
EXTRACT_FILE_PATH="/gpfs/group/torkamani/bzhu/ukbb_project/ukbb_cardiac/new_target/GWA_tutorial/genotype_qc/12_mafhwe/geno_filter_regenie.prune.in"
COVARIATE_FILE_PATH="/gpfs/group/torkamani/bzhu/ukbb_project/ukbb_cardiac/new_target/data/covariates_df.tsv"
PHENO_FILE_PATH="/gpfs/group/torkamani/bzhu/ukbb_project/ukbb_cardiac/new_target/data/adjusted_filtered_$1.tsv"

# Outputs
OUTPUT_STEP1="normalized_result/fit_bin_out_$1"
PRED_LIST="${OUTPUT_STEP1}_pred.list"
OUTPUT_STEP2="normalized_result/test_bin_out_firth_$1"

# Call regenie_step1.sh
./regenie_step1.sh $BED_FILE_PATH $EXTRACT_FILE_PATH $COVARIATE_FILE_PATH $PHENO_FILE_PATH $OUTPUT_STEP1

# Call regenie_step2.sh
./regenie_step2.sh $BED_FILE_PATH $COVARIATE_FILE_PATH $PHENO_FILE_PATH $PRED_LIST $OUTPUT_STEP2


