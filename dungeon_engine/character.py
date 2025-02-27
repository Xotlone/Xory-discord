from ability import Ability
from background import Background
from game_class import Class
from experience import Experience
from dungeon_enum import Alignment
from item import Item
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
                 background: Background, race: Race, abilities: list[Ability],
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
