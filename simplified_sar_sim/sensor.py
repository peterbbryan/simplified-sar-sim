from typing import Tuple


class Sensor:
    """
    Logic to simulate and emitter-receiver.
    """

    def __init__(self):
        ...

    @property
    def position(self) -> Tuple[int, int]:
        """
        Position of sensor.
        """
