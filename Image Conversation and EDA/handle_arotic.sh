#!/bin/bash -l

# spawner for batched image conversion jobs

while read batch; do

  target_dir=$( echo $batch)



  sbatch --export=target_dir=$target_dir --job-name=handle_arotic_1_$batch --output=handle_arotic_1_$batch.%J handle_arotic.sbatch;
  sleep 1;

done < handle_arotic.txt