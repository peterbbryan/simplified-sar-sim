import inspect
import types

import fire
import matplotlib.pyplot as plt
import numpy as np
from rich.prompt import Prompt

from simplified_sar_sim.scene import Scene, SimpleReflectivityFunctions


class Visualizations:
    """
    Visualizations to confirm that things are doing what I think.
    """

    @staticmethod
    def visualize_distance_matrix(
        n_rows: int = 100, n_cols: int = 100, sensor_row: int = 50, sensor_col: int = 50
    ) -> None:
        """
        Visualize distance to each row column location.
        """
        
        dummy_reflectivity = np.zeros((n_rows, n_cols))

        scene = Scene(reflectivity_density_function=dummy_reflectivity)
        distances = scene.get_distance_matrix(sensor_loc=(sensor_row, sensor_col))
        
        plt.imshow(distances)
        plt.colorbar()
        plt.xlabel("Column")
        plt.ylabel("Row")
        plt.show()

    @staticmethod
    def visualize_sample_scenes() -> None:
        """
        Visualize a sample scene before trying to reconstruct with SAR.
        """

        # get the static methods from our simple reflectivity function class
        funcs = dict(
            inspect.getmembers(
                SimpleReflectivityFunctions,
                predicate=lambda x: isinstance(x, types.FunctionType),
            )
        )

        selection = Prompt.ask(
            "Which sample scene would you like to see?", choices=funcs.keys()
        )

        scene = funcs[selection]()  # TODO: add support for CLI args, kwargs.

        plt.imshow(scene)
        plt.colorbar()
        plt.xlabel("Column")
        plt.ylabel("Row")
        plt.show()


if __name__ == "__main__":
    fire.Fire(Visualizations)
