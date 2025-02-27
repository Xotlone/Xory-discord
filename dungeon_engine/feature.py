from experience import *

__all__ = (
    'Trait',
    'Feature',
)


class Trait:
    """Class of racial traits."""

    def __init__(self, name: str, description: str = '', *param):
        self.name = name
        self.description = description
        self.param = param

    def use(self):
        """Main function for activate feature."""

        pass


class Feature(Trait):
    """Class of D&D class features."""

    def __init__(self, name: str, description: str = '', unlock_level: int = 1,
                 *param):
        super().__init__(name, description, param)
        self.unlock_level = Experience.from_level(unlock_level)
        self.in_path = False
