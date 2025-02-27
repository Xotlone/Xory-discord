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
        self.experience = Experience() if experience is None else experience
        self.equipment = [] if equipment is None else equipment
        self.organizations = organizations
        self.additional = additional
        self.author_id = author_id
        self.armor_class = None
        self.initiative = None
        self.speed = None

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
