from typing import Union, Self

from ability import Ability, Abilities

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
    """Skill related to ability"""

    def __init__(self, name: str, level: Union[Profficiency, int],
                 related: Ability):
        self.name = name
        self.level = level
        self.related = related

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
        return cls('acrobatics', level, Ability.dexterity())

    @classmethod
    def animal_handling(cls, level: Union[Profficiency, int] = 0):
        return cls('animal_handling', level, Ability.wisdom())

    @classmethod
    def arcana(cls, level: Union[Profficiency, int] = 0):
        return cls('arcana', level, Ability.intelligence())

    @classmethod
    def athletics(cls, level: Union[Profficiency, int] = 0):
        return cls('athletics', level, Ability.strength())

    @classmethod
    def deception(cls, level: Union[Profficiency, int] = 0):
        return cls('deception', level, Ability.charisma())

    @classmethod
    def history(cls, level: Union[Profficiency, int] = 0):
        return cls('history', level, Ability.intelligence())

    @classmethod
    def insight(cls, level: Union[Profficiency, int] = 0):
        return cls('insight', level, Ability.wisdom())

    @classmethod
    def intimidation(cls, level: Union[Profficiency, int] = 0):
        return cls('intimidation', level, Ability.charisma())

    @classmethod
    def investigation(cls, level: Union[Profficiency, int] = 0):
        return cls('investigation', level, Ability.intelligence())

    @classmethod
    def medicine(cls, level: Union[Profficiency, int] = 0):
        return cls('medicine', level, Ability.wisdom())

    @classmethod
    def nature(cls, level: Union[Profficiency, int] = 0):
        return cls('nature', level, Ability.intelligence())

    @classmethod
    def perception(cls, level: Union[Profficiency, int] = 0):
        return cls('perception', level, Ability.wisdom())

    @classmethod
    def performance(cls, level: Union[Profficiency, int] = 0):
        return cls('performance', level, Ability.charisma())

    @classmethod
    def persuasion(cls, level: Union[Profficiency, int] = 0):
        return cls('persuasion', level, Ability.charisma())

    @classmethod
    def religion(cls, level: Union[Profficiency, int] = 0):
        return cls('religion', level, Ability.intelligence())

    @classmethod
    def sleight_of_hand(cls, level: Union[Profficiency, int] = 0):
        return cls('sleight_of_hand', level, Ability.dexterity())

    @classmethod
    def stealth(cls, level: Union[Profficiency, int] = 0):
        return cls('stealth', level, Ability.dexterity())

    @classmethod
    def survival(cls, level: Union[Profficiency, int] = 0):
        return cls('survival', level, Ability.wisdom())

    def calculate(self, profficiency_bonus: int, abilities: Abilities):
        return (int(self.level) * profficiency_bonus
                + abilities(self.related).modifier)


class Skills:
    """Set of skills"""

    def __init__(self, acrobatics: int = 10, animal_handling: int = 10,
                 arcana: int = 10, athletics: int = 10, deception: int = 10,
                 history: int = 10, insight: int = 10, intimidation: int = 10,
                 investigation: int = 10, medicine: int = 10, nature: int = 10,
                 perception: int = 10, performance: int = 10,
                 persuasion: int = 10, religion: int = 10,
                 sleight_of_hand: int = 10, stealth: int = 10,
                 survival: int = 10):
        self.acrobatics = Skill.acrobatics(acrobatics)
        self.animal_handling = Skill.animal_handling(animal_handling)
        self.arcana = Skill.arcana(arcana)
        self.athletics = Skill.athletics(athletics)
        self.deception = Skill.deception(deception)
        self.history = Skill.history(history)
        self.insight = Skill.insight(insight)
        self.intimidation = Skill.intimidation(intimidation)
        self.investigation = Skill.investigation(investigation)
        self.medicine = Skill.medicine(medicine)
        self.nature = Skill.nature(nature)
        self.perception = Skill.perception(perception)
        self.performance = Skill.performance(performance)
        self.persuasion = Skill.persuasion(persuasion)
        self.religion = Skill.religion(religion)
        self.sleight_of_hands = Skill.sleight_of_hand(sleight_of_hand)
        self.stealth = Skill.stealth(stealth)
        self.survival = Skill.survival(survival)
