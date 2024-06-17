#!/bin/bash -l

# spawner for batched image conversion jobs

while read batch; do

  target_dir=$( echo $batch)



  sbatch --export=target_dir=$target_dir --job-name=segementation_1_$batch --output=segementation_1_$batch.%J demo_pipeline_modified.sbatch;
  sleep 1;

done < segementation.txt

