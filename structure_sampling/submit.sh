#!/bin/bash
#
#SBATCH -p gpu
#SBATCH --nodes=1
#SBATCH --mem=1500
module load libs/tensorflow-1.2
module unload Python/2.7.12-foss-2016b

cd $SLURM_SUBMIT_DIR
python structureSampling.py
