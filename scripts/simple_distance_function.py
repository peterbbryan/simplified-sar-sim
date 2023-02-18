import fire
import matplotlib.pyplot as plt
import numba
import numpy as np

from functools import partial
from typing import Callable, Tuple, List

pulse_function = Callable[[int], Tuple[np.ndarray, bool]]


def radar_response_by_distance_time(
    distance: np.ndarray, pulse_start_t: int, current_t: int
) -> Tuple[np.ndarray, bool]:
    """
    Radar response function calculation.

    Args:
        distance:
        pulse_start_t:
        current_t:
    Returns:
        Tuple of radar response and whether the function is still relevant.
    """

    assert current_t >= pulse_start_t, "Current time earlier than pulse start time"

    response = (np.abs(distance - (current_t - pulse_start_t)) < 1).astype(int)

    return response, np.any(response)


def get_distance_matrix(
    arr_shape: Tuple[int, int], sensor_loc: Tuple[int, int]
) -> np.ndarray:
    """
    Get row, cols for two-dimensional matrix.

    Args:
        arr_shape: Tuple of row, col matrix shape.
        sensor_loc: Tuple of row, col of simulated sensor location.
    Returns:
        Distance from sensor to each row, col location in scene.
    """

    assert len(arr_shape) == 2, "Only two-dimensional array are supported"

    n_rows, n_cols = arr_shape
    sensor_row, sensor_col = sensor_loc

    # create a matrix of row and column indices
    row_col_matrix = np.mgrid[0:n_rows, 0:n_cols]
    row_inds, col_inds = row_col_matrix

    # calculate differences
    row_inds -= sensor_row
    col_inds -= sensor_col

    # euclidean distance from sensor to each pixel location
    l2_distance = np.sqrt((row_inds**2) + (col_inds**2))

    plt.figure()
    plt.ion()

    pulse_functions: List[pulse_function] = []

    for t in range(10000):
        if t % 100 == 0:
            prf = partial(
                radar_response_by_distance_time, distance=l2_distance, pulse_start_t=t
            )
            pulse_functions.append(prf)

        responses, relevances = list(zip(*[f(current_t=t) for f in pulse_functions]))

        summed_responses = np.sum(response for response in responses)

        # remove stale response functions
        pulse_functions = [
            f for f, relevance in zip(pulse_functions, relevances) if relevance
        ]

        # if t % 20 == 0:
        #    plt.imshow(summed_responses)
        #    plt.show()
        #    plt.pause(0.00001)


if __name__ == "__main__":
    fire.Fire(get_distance_matrix)
