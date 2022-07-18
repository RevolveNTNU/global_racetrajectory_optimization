import numpy as np
import csv


def export_traj_race(file_paths: dict,
                     traj_race: np.ndarray) -> None:
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    This function is used to export the generated trajectory into a file. The generated files get an unique UUID and a
    hash of the ggv diagram to be able to check it later.

    Inputs:
    file_paths:     paths for input and output files {ggv_file, traj_race_export, traj_ltpl_export, lts_export}
    traj_race:      race trajectory [s, x, y, psi, k, vx, ax]
    """
    # export race trajectory
    with open(file_paths["traj_race_export"], 'w') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["s","x","y","psi","k","vx","ax"])
        writer.writerow(["closed"])
        writer.writerows(traj_race)

# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
