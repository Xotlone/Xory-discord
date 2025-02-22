from enum import Enum, auto


class Parameters(Enum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()

class Skills(Enum):
    ACROBATICS = auto()
    ANIMAL_HANDLING = auto()
    ARCANA = auto()
    ATHLETICS = auto()
    DECEPTION = auto()
    HISTORY = auto()
    INSIGHT = auto()
    INTIMIDATION = auto()
    INVESTIGATION = auto()
    MEDICINE = auto()
    NATURE = auto()
    PERCEPTION = auto()
    PEFORMANCE = auto()
    PERSUASION = auto()
    RELIGION = auto()
    SLEIGHT_OF_HAND = auto()
    STEALTH = auto()
    SURVIVAL = auto()

class Alignment(Enum):
    LAWFUL_GOOD = [0, 0]
    LAWFUL_NEUTRAL = [1, 0]
    LAWFUL_EVIL = [2, 0]
    NEUTRAL_GOOD = [1, 0]
    TRUE_NEUTRAL = [1, 1]
    NEUTRAL_EVIL = [1, 2]
    CHAOTIC_GOOD = [2, 0]
    CHAOTIC_NEUTRAL = [2, 1]
    CHAOTIC_EVIL = [2, 2]

class Proficiency(Enum):
    LACK_OF_KNOWLEDGE = 0
    PROFICIENCY = 1
    COMPETENCE = 2
