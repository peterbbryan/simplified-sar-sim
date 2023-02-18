"""
Logic for radar simulation.
"""

from .scene import Scene


class Simulation:  # pylint: disable=too-few-public-methods
    """
    Simulation of radar emitter and receiver.
    """

    def __init__(self, scene: Scene):
        self.t = 0  # pylint: disable=invalid-name
        self._scene = scene

    def increment_time(self, increment_step: int = 1) -> None:
        """
        Increment time by increment_step.

        Args:
            increment_step:
        """

        self.t += increment_step
