#!/bin/bash

fam_initial=gwas_data/merged_file/chrome_merged.fam
fam_sample_qced=genotype_qc/08_2_Ancestry_Filter/filter_fam_by_ancestry_95%.fam

awk 'BEGIN{FS=" "}{OFS="\t"}{print $1,$2}' $fam_initial | sort -i > indiv.all
awk 'BEGIN{FS=" "}{OFS="\t"}{print $1,$2}' $fam_sample_qced | sort -i > indiv.sampleQC

comm -23 indiv.all indiv.sampleQC | awk '{OFS="\t"}{print $1,$2}' > indiv.sampleQC.toberemoved

wc -l $fam_initial $fam_sample_qced indiv.sampleQC.toberemoved

