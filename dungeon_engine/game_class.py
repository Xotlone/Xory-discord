from ability import Ability
from experience import Experience
from feature import Feature
from item import Item
from skill import Skill

__all__ = (
    'ClassPath',
    'Class',
)

class ClassPath:
    """Class for storing a separate list of features of a game class path."""

    def __int__(self, name: str, description: str = ''):
        self.name = name
        self.description = description
        self.features = []

    def add_feature(self, feature: Feature):
        """Add feature to class path."""

        feature.in_path = True
        self.features.append(feature)


class Class:
    """Game class."""

    def __init__(self, name: str, description: str, level: int = 1,
                 hit_dice: tuple[int, int] = (1, 8),
                 proficiencies: list[str] = None,
                 saving_throws: list[Ability] = None,
                 skills: list[Skill] = None, skill_count: int = 2,
                 start_equipment: list[Item] = None,
                 features: list[Feature] = None,
                 class_path: ClassPath = None, *other):
        self.name = name
        self.description = description
        self.level = Experience.from_level(level)
        self.hit_dice = hit_dice
        self.proficiencies = [] if proficiencies is None else proficiencies
        self.saving_throws = [] if saving_throws is None else saving_throws
        self.skills = [] if skills is None else skills
        self.skill_count = skill_count
        self.start_equipment = [] if start_equipment is None \
                                  else start_equipment
        self.features = [] if features is None else features
        self.class_path = class_path
        self.other = other

    @property
    def features(self) -> list[Feature]:
        all_features = []
        if self.class_path is not None:
            for feature in self.class_path.features:
                all_features.append(feature)
        [all_features.append(i) for i in self._features]
        return all_features

    @features.setter
    def features(self, val: list[Feature]): self._features = val
