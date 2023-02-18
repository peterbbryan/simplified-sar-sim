"""
Logic to describe ground reflectivity.
"""

import numpy as np

from types import MappingProxyType
from typing import Callable, Dict, List, Tuple, Union


class Scene:  # pylint: disable=too-few-public-methods
    """
    Scene of spatial ground reflectivity function.
    """

    def __init__(self, width: int, height: int):
        """

        Args:
            width: Width of the scene.
            height: Height of the scene.
        """

        del width
        del height

        self._reflectivity_density_function = ...

    @property
    def reflectivity_density_function(self):
        """
        Description of radar reflectivity as a function of location.
        """


class SimpleReflectivityFunctions:
    """
    Some simple reflectivity functions for debugging.
    """

    _DEFAULT_NOISE_FUNCTION = np.random.poisson
    _DEFAULT_NOISE_FUNCTION_ARGS = ()
    _DEFAULT_NOISE_FUNCTION_KWARGS = MappingProxyType({"lam": 10.0})

    @staticmethod
    def one_point_target(
        point_row: int = 100,
        point_col: int = 100,
        point_intensity: int = 40,
        rows: int = 200,
        cols: int = 200,
        background_noise_function: Callable[..., np.ndarray] = _DEFAULT_NOISE_FUNCTION,
        background_noise_function_args: Union[
            List, Tuple
        ] = _DEFAULT_NOISE_FUNCTION_ARGS,
        background_noise_function_kwargs: Dict = _DEFAULT_NOISE_FUNCTION_KWARGS,
    ) -> np.ndarray:
        """
        Simulate a single point response on a clutter background.

        Args:
            point_row: Row of impulse response.
            point_col: Column of impulse response.
            point_intensity: Intensity of response, arbitrary unit.
            rows: Total rows in scene.
            cols: Total columns in scene.
            background_noise_function: Noise func that takes a "size" kwarg of tuple of rows, cols.
        """

        # construct the scene's background contents
        size = (rows, cols)
        background_arr = background_noise_function(
            *background_noise_function_args, **background_noise_function_kwargs, size=size
        )

        # insert point response
        background_arr[point_row, point_col] = point_intensity

        return background_arr