from enum import Enum, auto


class Alignment(Enum):
    lawful_good = [0, 0]
    lawful_neutral = [1, 0]
    lawful_evil = [2, 0]
    neutral_good = [1, 0]
    true_neutral = [1, 1]
    neutral_evil = [1, 2]
    chaotic_good = [2, 0]
    chaotic_neutral = [2, 1]
    chaotic_evil = [2, 2]
    def __str__(self): return self.name

class ArmorTypes(Enum):
    light = auto()
    medium = auto()
    heavy = auto()

class WeaponTypes(Enum):
    simple = auto()
    simple_ranged = auto()
    martial = auto()
    martial_ranged = auto()
