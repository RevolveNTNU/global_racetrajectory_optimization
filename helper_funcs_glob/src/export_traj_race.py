import numpy as np
import csv


def export_traj_race(file_paths: dict,
                     traj_race: np.ndarray) -> None:
    # export race trajectory
    with open(file_paths["traj_race_export"], 'w') as file:
        # make heading reference be the same as the x direction of vehicle
        traj_race[:, 3] += np.pi/2

        writer = csv.writer(file, delimiter=",")
        writer.writerow(["s","x","y","psi","k","vx","ax"])
        writer.writerow(["closed"])
        writer.writerows(traj_race)

# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
