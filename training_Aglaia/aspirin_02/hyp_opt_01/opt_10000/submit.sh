#!/bin/bash
#
#SBATCH -p gpu
#SBATCH --nodes=1
module load libs/tensorflow/1.2
module unload Python/2.7.12-foss-2016b
module unload libs/cudnn/5.1-cuda-8.0
module load libs/cudnn/8.0-cuda-8.0
source activate root

cd $SLURM_SUBMIT_DIR
osprey worker --n-iter 15 config.yaml
