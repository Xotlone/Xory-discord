from enum import Enum, auto

__all__ = (
    'DamageType'
)


class DamageType(Enum):
    acid = auto()
    bludgeoning = auto()
    cold = auto()
    fire = auto()
    force = auto()
    lightning = auto()
    necrotic = auto()
    piercing = auto()
    poison = auto()
    psychic = auto()
    radiant = auto()
    slashing = auto()
    thunder = auto()

    def __str__(self): return self.name

    @staticmethod
    def names() -> tuple[str, ...]:
        """Returns list of damage types"""
        return tuple(filter(lambda x: '__' not in x,
                            DamageType.__dict__))[-13:]


class CharacterSlot(Enum):
    r_feet = auto()
    l_feet = auto()
    r_leg = auto()
    l_leg = auto()
    belt = auto()
    torso = auto()
    back = auto()
    r_arm = auto()
    l_arm = auto()
    r_wrist = auto()
    l_wrist = auto()
    neck = auto()
    head = auto()
    glasses = auto()

    def __str__(self): return self.name


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

class WeaponTypes(Enum):
    simple = auto()
    simple_ranged = auto()
    martial = auto()
    martial_ranged = auto()
