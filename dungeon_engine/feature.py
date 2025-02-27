from typing import Any

from experience import Experience

__all__ = (
    'Trait',
    'Feature',
)


class Trait:
    """Class of racial traits."""

    def __init__(self, name: str, description: str = '',
                 effects: dict[str, Any] = None):
        self.name = name
        self.description = description
        self.effects = {} if effects is None else effects

    def use(self):
        """Main function for activate feature."""

        pass


class Feature(Trait):
    """Class of D&D class features."""

    def __init__(self, name: str, description: str = '', unlock_level: int = 1,
                 effects: dict[str, Any] = None):
        super().__init__(name, description, effects)
        self.unlock_level = Experience.from_level(unlock_level)
        self.in_path = False
