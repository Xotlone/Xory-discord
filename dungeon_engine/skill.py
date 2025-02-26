from typing import Union, Self

__all__ = (
    'Profficiency',
    'Skill',
)


class Profficiency:
    """Profficiency of something"""

    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        if val not in Profficiency.names():
            raise ValueError(f'The profficiency level "{val}" is not exist')
        self._name = val

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, val: int):
        if val < 0 or val > 2:
            raise ValueError('The profficiency level should be in the '
                             'range [0, 2]')
        self._level = val

    def __hash__(self): return hash(self.name)

    def __int__(self): return self.level

    def __str__(self): return self.name

    def __eq__(self, other: Union[Self, int, str]):
        if isinstance(other, Profficiency): return self.level == other.level
        elif isinstance(other, int): return self.level == other
        elif isinstance(other, str): return self.name == other
        else: raise TypeError(f'Unexpected type "{type(other)}" for __eq__')

    @staticmethod
    def names() -> tuple[str, ...]:
        """Returns list of profficiency names"""
        return tuple(filter(lambda x: '__' not in x,
                            Profficiency.__dict__))[-3:]

    @classmethod
    def from_int(cls, val: int):
        """Return Profficiency class from int"""
        try:
            result = cls(cls.names()[val], val)
        except IndexError:
            raise ValueError('The profficiency level should be in the '
                             'range [0, 2]')
        return result

    @classmethod
    def lack_of_knowledge(cls):
        return cls('lack_of_knowledge', 0)

    @classmethod
    def profficiency(cls):
        return cls('profficiency', 1)

    @classmethod
    def competence(cls):
        return cls('competence', 2)


class Skill:
    def __init__(self, name: str, level: Union[Profficiency, int]):
        self.name = name
        self.level = level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val: str):
        if val not in Skill.names():
            raise ValueError(f'Skill "{val}" is not exist')
        self._name = val

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, val: Union[Profficiency, int]):
        if isinstance(val, int): val = Profficiency.from_int(val)
        self._level = val

    def __hash__(self): return hash((self.name, self.level))

    def __int__(self): return int(self.level)

    def __str__(self): return self.name

    @staticmethod
    def names() -> tuple[str, ...]:
        """Returns list of skill names"""
        return tuple(filter(lambda x: '__' not in x, Skill.__dict__))[-18:]

    @classmethod
    def acrobatics(cls, level: Union[Profficiency, int] = 0):
        return cls('acrobatics', level)

    @classmethod
    def animal_handling(cls, level: Union[Profficiency, int] = 0):
        return cls('animal_handling', level)

    @classmethod
    def arcana(cls, level: Union[Profficiency, int] = 0):
        return cls('arcana', level)

    @classmethod
    def athletics(cls, level: Union[Profficiency, int] = 0):
        return cls('athletics', level)

    @classmethod
    def deception(cls, level: Union[Profficiency, int] = 0):
        return cls('deception', level)

    @classmethod
    def history(cls, level: Union[Profficiency, int] = 0):
        return cls('history', level)

    @classmethod
    def insight(cls, level: Union[Profficiency, int] = 0):
        return cls('insight', level)

    @classmethod
    def intimidation(cls, level: Union[Profficiency, int] = 0):
        return cls('intimidation', level)

    @classmethod
    def investigation(cls, level: Union[Profficiency, int] = 0):
        return cls('investigation', level)

    @classmethod
    def medicine(cls, level: Union[Profficiency, int] = 0):
        return cls('medicine', level)

    @classmethod
    def nature(cls, level: Union[Profficiency, int] = 0):
        return cls('nature', level)

    @classmethod
    def perception(cls, level: Union[Profficiency, int] = 0):
        return cls('perception', level)

    @classmethod
    def peformance(cls, level: Union[Profficiency, int] = 0):
        return cls('peformance', level)

    @classmethod
    def persuasion(cls, level: Union[Profficiency, int] = 0):
        return cls('persuasion', level)

    @classmethod
    def religion(cls, level: Union[Profficiency, int] = 0):
        return cls('religion', level)

    @classmethod
    def sleight_of_hand(cls, level: Union[Profficiency, int] = 0):
        return cls('sleight_of_hand', level)

    @classmethod
    def stealth(cls, level: Union[Profficiency, int] = 0):
        return cls('stealth', level)

    @classmethod
    def survival(cls, level: Union[Profficiency, int] = 0):
        return cls('survival', level)
