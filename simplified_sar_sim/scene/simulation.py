"""
Logic for radar simulation.
"""


class Simulation:  # pylint: disable=too-few-public-methods
    """
    Simulation of radar emitter and receiver.
    """

    def __init__(self):
        self.t = 0  # pylint: disable=invalid-name

    def increment_time(self, increment_step: int = 1) -> None:
        """
        Increment time by increment_step.

        Args:
            increment_step:
        """
