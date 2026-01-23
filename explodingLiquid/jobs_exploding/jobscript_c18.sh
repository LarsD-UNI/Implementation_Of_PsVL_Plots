#!/bin/bash
#SBATCH -J psvl_c18
#SBATCH -D ./
#SBATCH -o ./%x.%j.%N.out
#SBATCH -e ./%x.%j.%N.err
#SBATCH --get-user-env
#SBATCH --export=NONE
#SBATCH --clusters=cm4
#SBATCH --partition=cm4_tiny
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=112
#SBATCH --time=00:15:00

module load slurm_setup
module load cmake
module load gcc

export OMP_NUM_THREADS=112
export OMP_PLACES=cores
export OMP_PROC_BIND=close

echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"

for i in {1..5}; do

echo "Run $i"

$HOME/Projekte/AutoPas/build/examples/md-flexible/md-flexible --yaml-filename explodingLiquid_c18.yaml

done
