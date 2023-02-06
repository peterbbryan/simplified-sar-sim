"""
Logic to describe ground reflectivity.
"""


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
