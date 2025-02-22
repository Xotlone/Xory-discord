import typing

import enums


class Item:
    all_items = []

    def __init__(self, name: str, description: str,
                 category: typing.Union[str, None] is None, charges: int = 1):
        self.name = name,
        self.description = description
        self.category = category
        self.charges = charges
        Item.all_items.append(self)

class Influence:
    def __init__(self, parameter: typing.Any, operator: str, value: int):
        self.parameter = parameter
        self.operator = operator
        self.value = value

class Background:
    def __init__(self, name: str, description: str,
                 influence: typing.List[Influence], items: typing.List[Item]):
        self.name = name
        self.description = description
        self.influence = influence
        self.items = items

class RaceFeature:
    def __init__(self, name: str, description: str,
                 influence: typing.List[Influence]):
        self.name = name
        self.description = description
        self.influence = influence

class Subrace:
    def __init__(self, name: str, description: str,
                 features: typing.List[RaceFeature]):
        self.name = name
        self.description = description
        self.features = features

class Race(Subrace):
    def __init__(self, name: str, description: str,
                 features: typing.List[RaceFeature],
                 subraces: typing.List[Subrace]):
        super().__init__(name, description, features)
        self.subraces = subraces

class Spell:
    def __init__(self, name: str, description: str):
        pass

class CharacterList:
    def __init__(self, *, author_id: int, name: str,
                 classes: typing.List[str, int],
                 background: Background,
                 race: Race,
                 alignment: typing.Union[enums.Alignment, None],
                 experience_point: int = 0, inspiration: bool = False,
                 parameters: typing.Dict[enums.Parameters, int],
                 skills: typing.Dict[enums.Skills, enums.Proficiency],
                 personality_traits: str, ideals: str, bonds: str,
                 flaws: str,
                 equipment: typing.Union[typing.List[typing.Any], None],
                 gender: str, age: int,
                 height: typing.Union[int, None] = None,
                 weight: typing.Union[int, None] = None,
                 skin: str = '', eyes: str = '', hair: str = '',
                 appearance: str = '', organizations: str = '',
                 additional: str = '',
                 prepared_spells: typing.Union[typing.List[Spell], None] =
                 None):
        pass