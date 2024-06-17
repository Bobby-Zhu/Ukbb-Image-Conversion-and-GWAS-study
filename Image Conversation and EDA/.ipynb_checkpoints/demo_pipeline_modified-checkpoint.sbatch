#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=shared
#SBATCH --time=300:00:00
#SBATCH --cpus-per-task=8

export PYTHONUNBUFFERED=TRUE
module load tensorflow/2.7.0py38-cuda
module load mirtk
export PYTHONPATH=ukbb_project:$PYTHONPATH


python demo_pipeline_modified.py $target_dir

