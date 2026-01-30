#!/bin/bash
#SBATCH -J c08_LOG
#SBATCH -D ./
#SBATCH -o ./%x.%j.%N.out
#SBATCH -e ./%x.%j.%N.err
#SBATCH --get-user-env
#SBATCH --export=NONE
#SBATCH --clusters=cm4
#SBATCH --partition=cm4_tiny
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=112
#SBATCH --time=00:07:00

module load slurm_setup
module load cmake
module load gcc

export OMP_NUM_THREADS=112
export OMP_PLACES=cores
export OMP_PROC_BIND=close

EXEC="$HOME/Projekte/AutoPas/build/examples/md-flexible/md-flexible"
YAML1="fallingDrop_psvl_c08.yaml"
YAML2="fallingDrop_vlc_c08.yaml"

for radius in 0.3 0.7; do

  echo "Radius: $radius"

	for i in 1; do

		$EXEC --yaml-filename "$YAML1" --verlet-skin-radius "$radius"
		$EXEC --yaml-filename "$YAML2" --verlet-skin-radius "$radius"

	done
done
