from math import floor

from typing import Union

__all__ = (
    'Ability',
    'Abilities',
)


class Ability:
    """Ability for characters and checks"""

    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.modifier: int = 0
        self.value = value

    @property
    def value(self): return self._value

    @value.setter
    def value(self, val: int):
        if val < 1:
            raise ValueError('Ability point cannot be less than 1')
        self._value = val
        self.modifier = floor((val - 10) / 2)

    def __hash__(self): return hash(self.name)

    def __int__(self): return self.value

    def __str__(self): return self.name

    @staticmethod
    def names() -> tuple[str, ...]:
        """Returns list of ability names"""

        return tuple(filter(lambda x: '__' not in x, Ability.__dict__))[2:]

    @classmethod
    def strength(cls, value: int = 10):
        return cls('strength', value)

    @classmethod
    def dexterity(cls, value: int = 10):
        return cls('dexterity', value)

    @classmethod
    def constitution(cls, value: int = 10):
        return cls('constitution', value)

    @classmethod
    def intelligence(cls, value: int = 10):
        return cls('intelligence', value)

    @classmethod
    def wisdom(cls, value: int = 10):
        return cls('wisdom', value)

    @classmethod
    def charisma(cls, value: int = 10):
        return cls('charisma', value)


class Abilities:
    """Set of abilities."""

    def __init__(self, strength: int = 10, dexterity: int = 10,
                 constitution: int = 10, intelligence: int = 10,
                 wisdom: int = 10, charisma: int = 10):
        self.strength = Ability.strength(strength)
        self.dexterity = Ability.dexterity(dexterity)
        self.constitution = Ability.strength(constitution)
        self.intelligence = Ability.intelligence(intelligence)
        self.wisdom = Ability.wisdom(wisdom)
        self.charisma = Ability.charisma(charisma)

    def __call__(self, item: Union[str, Ability]):
        if isinstance(item, Ability): item = item.name

        abilities = tuple(filter(lambda x: '__' not in x, self.__dict__))[:6]
        if item.lower() not in abilities:
            raise ValueError(f'"{item}" not in abilities')
        return eval(f'self.{item.lower()}')
