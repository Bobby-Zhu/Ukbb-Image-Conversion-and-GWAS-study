#!/bin/bash

#SBATCH --job-name=ancestry_filter
#SBATCH --cpus-per-task=4
#SBATCH --mem=44G
#SBATCH --time=48:00:00
#SBATCH --output=geno_filter_%j.out
#SBATCH --error=geno_filter_%j.err
module load python

original_dataset_name="genotype_qc/06_hetero/geno_filter_6.3"
filtered_fam="filter_fam_by_ancestry_95%.fam"
new_filtered_dataset_name="geno_filter_8_95%"


# Run your Python script to filter the FAM file
python filter_fam_by_ancestry.py 

# Now, use PLINK to filter the BIM, BED, and FAM files based on the filtered FAM file
plink1.9/plink --bfile ${original_dataset_name} --keep ${filtered_fam} --make-bed --out ${new_filtered_dataset_name}

