#!/bin/bash
#
#SBATCH -p gpu
#SBATCH --nodes=2
module load libs/tensorflow/1.2
module unload Python/2.7.12-foss-2016b
module unload libs/cudnn/5.1-cuda-8.0
module load libs/cudnn/8.0-cuda-8.0
source activate py36

cd $SLURM_SUBMIT_DIR
mpirun -np 2 osprey worker --n-iter 20 config.yaml
