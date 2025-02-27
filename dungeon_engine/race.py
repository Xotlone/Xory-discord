from feature import Trait

__all__ = (
    'Subrace',
    'Race',
)


class Subrace:
    """Class for storing parameters of subrace."""

    def __init__(self, name: str, description: str,
                 traits: list[Trait] = None):
        self.name = name
        self.description = description
        self.traits = [] if traits is None else traits


class Race(Subrace):
    """Class for storing parameters of race."""

    def __init__(self, name: str, description: str,
                 traits: list[Trait] = None, subraces: list[Subrace] = None):
        super().__init__(name, description, traits)
        self.subraces = subraces
