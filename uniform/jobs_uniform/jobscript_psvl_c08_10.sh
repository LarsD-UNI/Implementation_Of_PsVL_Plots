#!/bin/bash
#SBATCH -J psvl_c08_10
#SBATCH -D ./
#SBATCH -o ./%x.%j.%N.out
#SBATCH -e ./%x.%j.%N.err
#SBATCH --get-user-env
#SBATCH --export=NONE
#SBATCH --clusters=cm4
#SBATCH --partition=cm4_tiny
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=112
#SBATCH --time=02:30:00

module load slurm_setup
module load cmake
module load gcc

export OMP_NUM_THREADS=112
export OMP_PLACES=cores
export OMP_PROC_BIND=close

EXEC="$HOME/Projekte/AutoPas/build/examples/md-flexible/md-flexible"
YAML="uniform_box_length_10.yaml"

for radius in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do

  echo "Radius: $radius"

	for i in {1..5}; do

		echo "Run $i (radius=$radius)"

		$EXEC --yaml-filename "$YAML" --verlet-skin-radius "$radius"

	done
done
