import inspect
import types

import fire
import matplotlib.pyplot as plt
from rich.prompt import Prompt

from simplified_sar_sim.scene import SimpleReflectivityFunctions


class Visualizations:
    """
    Visualizations to confirm that things are doing what I think.
    """

    @staticmethod
    def visualize_sample_scenes():
        """
        Visualize a sample scene before trying to reconstruct with SAR.
        """
        
        # get the static methods from our simple reflectivity function class
        funcs = dict(inspect.getmembers(
            SimpleReflectivityFunctions,
            predicate=lambda x: isinstance(x, types.FunctionType),
        ))

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
