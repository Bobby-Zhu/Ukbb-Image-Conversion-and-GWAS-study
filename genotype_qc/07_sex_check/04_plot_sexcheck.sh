#!/bin/bash

source /data1/sanghyeon/Projects/NIAGADS_QC/src/source.sh

sexcheck_wo_prune=NG00026_wo_prune.sexcheck
sexcheck_w_prune=NG00026_pruned.sexcheck
Rscript 07.2_sexcheck_plot.R ${sexcheck_wo_prune} ${sexcheck_w_prune}