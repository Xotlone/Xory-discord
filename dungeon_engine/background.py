import random
from typing import Union

from item import Item, Tool
from language import Language
from skill import Skill

__all__ = (
    'BackgroundSegment',
    'Background',
)


class BackgroundSegment:
    """Social segment of background."""

    def __init__(self, name: str = None, description: str = None,
                 variants: list[str] = None, current_variant: int = None):
        self.name = name
        self.description = description
        self.variants = [] if variants is None else variants
        self.current_variant = current_variant

    def __repr__(self):
        result = ''
        if self.name is not None: result += self.name.upper()
        if self.description is not None:
            if result != '':
                result += '\n\n'
            result += self.description
        if self.variants:
            if result != '':
                result += '\n\n'
            result += '\n'.join(self.variants)
        return result

    def __str__(self): return self.__repr__()

    def random(self) -> Union[str, None]:
        """Assigns a random variant to the current_variant and returns it."""

        self.current_variant = random.choice(self.variants)
        return self.current_variant


class Background:
    """Class for D&D backgrounds."""

    def __init__(self, name: str, description: str, skills: list[Skill] = None,
                 tools: list[Tool] = None, languages: list[Language] = None,
                 items: list[Item] = None, feature: str = '',
                 segments: list[BackgroundSegment] = None):
        self.name = name
        self.description = description
        self.skills = [] if skills is None else skills
        self.tools = [] if tools is None else tools
        self.languages = [] if languages is None else languages
        self.items = [] if items is None else items
        self.feature = feature
        self.segments = [] if segments is None else segments

    def random_segments(self):
        """Randomly determines the current_variant of each segment."""

        [i.random() for i in self.segments]
