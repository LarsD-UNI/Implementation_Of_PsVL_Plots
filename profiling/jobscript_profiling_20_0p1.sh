#!/bin/bash
#SBATCH -J LOG_08
#SBATCH -D ./
#SBATCH -o ./%x.%j.%N.out
#SBATCH -e ./%x.%j.%N.err
#SBATCH --get-user-env
#SBATCH --export=NONE
#SBATCH --clusters=cm4
#SBATCH --partition=cm4_tiny
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=112
#SBATCH --time=00:30:00

module load slurm_setup
module load cmake
module load gcc

module load intel-oneapi-vtune

export OMP_NUM_THREADS=112
export OMP_PLACES=cores
export OMP_PROC_BIND=close

EXEC="$HOME/Projekte/AutoPas/build/examples/md-flexible/md-flexible"
YAML1="uniform_box_length_20.yaml"
YAML2="uniform_box_length_vlc_20.yaml"

RESULT_DIR="$SLURM_SUBMIT_DIR/vtune_${SLURM_JOB_ID}"

for radius in 0.7; do

  echo "Radius: $radius"

	for i in 1; do

		vtune -collect memory-consumption -r "${RESULT_DIR}_psvl" -- $EXEC --yaml-filename "$YAML1" --verlet-skin-radius "$radius"

		vtune -collect memory-consumption -r "${RESULT_DIR}_vlc" -- $EXEC --yaml-filename "$YAML2" --verlet-skin-radius "$radius"
		

	done
done
