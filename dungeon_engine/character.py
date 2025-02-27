from ability import Abilities
from background import Background
from game_class import Class
from experience import Experience
from dungeon_enum import Alignment
from item import *
from race import Race
from skill import Skill

__all__ = (
    'Appearance',
    'Social',
    'Character',
)


class Appearance:
    """Class for storing appearance."""

    def __init__(self, gender: str, age: int, height: int = None,
                 weight: int = None, skin: str = '', eyes: str = '',
                 hair: str = '', detailes: str = ''):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.skin = skin
        self.eyes = eyes
        self.hair = hair
        self.detailes = detailes


class Social:
    """Class for storing social parameters."""

    def __init__(self, alignment: Alignment = None,
                 personality_traits: str = '', ideals: str = '',
                 bonds: str = '', flaws: str = ''):
        self.alignment = alignment
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws


class Character:
    """D&D character class."""

    def __init__(self, name: str, classes: list[Class],
                 background: Background, race: Race, abilities: Abilities,
                 skills: list[Skill], appearance: Appearance, social: Social,
                 experience: Experience = None, equipment: list[Item] = None,
                 organizations: str = '', additional: str = '',
                 author_id: int = None):
        self.name = name
        self.classes = classes
        self.background = background
        self.race = race
        self.abilities = abilities
        self.skills = skills
        self.appearance = appearance
        self.social = social
        self.experience = experience
        self.equipment = [] if equipment is None else equipment
        self.organizations = organizations
        self.additional = additional
        self.author_id = author_id
        self.armor_class = None
        self.initiative = None
        self.speed = None
        self.max_hp = None
        self.hp = self.max_hp

    @property
    def experience(self): return self._experience

    @experience.setter
    def experience(self, val: Experience = None):
        result = val
        if val is None:
            result = sum(map(lambda x: x.level, self.classes))
            result = Experience.from_level(result)
        self._experience = result

    @property
    def armor_class(self): return self._armor_class

    @armor_class.setter
    def armor_class(self, val: int = None):
        result = val
        if val is None:
            race_ac = max(10, self.race.effect('armor_class')(self))

            equipment_ac = 10
            for eq in self.equipment:
                if isinstance(eq, Armor) and eq.is_use:
                    current_ac = eq.armor_class(self.abilities)
                    equipment_ac = max(equipment_ac, current_ac)

            for eq in self.equipment:
                if (isinstance(eq, Armor)
                        and eq.type_ == ArmorType.shield()
                        and eq.is_use):
                    race_ac += eq.armor_class
                    equipment_ac += eq.armor_class

            result = max(race_ac, equipment_ac)

        self._armor_class = result

    @property
    def initiative(self): return self._initiative

    @initiative.setter
    def initiative(self, val: int = None):
        race_initiative = self.race.effect('initiative')(self)
        self._initiative = max(race_initiative,
                             self.abilities.dexterity.modifier)
        if val is not None: self._initiative += val

    @property
    def speed(self): return self._speed

    @speed.setter
    def speed(self, val: int = None):
        self._speed = self.race.effect('speed')
        if val is not None: self._speed += val

    @property
    def max_hp(self): return self._max_hp

    @max_hp.setter
    def max_hp(self, val: int = None):
        result = val
        if val is None:
            result = self.classes[0].max_hit
            if self.experience.level == 1: self._max_hp = result
            else:
                result += ((self.classes[0].max_hit / 2 + 1)
                           * (self.classes[0].level - 1))
                if len(self.classes) > 1:
                    for class_ in self.classes[1:]:
                        result += (class_.max_hit / 2 + 1) * class_.level
        self._max_hp = result

# Segment for tests
'''cls1 = Class('cls1', '', 5, (1, 8))
cls2 = Class('cls2', '', 6, (1, 12))
back = Background('', '')
race = Race('race', '')
abil = Abilities()
skls = [Skill.nature()]
aprn = Appearance('', 0)
soci = Social()
char = Character('char', [cls1, cls2], back, race, abil, skls, aprn, soci)
print(char.max_hp)'''
