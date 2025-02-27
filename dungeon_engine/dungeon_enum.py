from enum import Enum, auto

__all__ = (
    'DamageType',
    'CharacterSlot',
    'Alignment',
    'WeaponType',
    'ActionType',
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
    back = auto()
    belt = auto()
    glasses = auto()
    head = auto()
    l_arm = auto()
    l_feet = auto()
    l_leg = auto()
    l_wrist = auto()
    neck = auto()
    r_arm = auto()
    r_feet = auto()
    r_leg = auto()
    r_wrist = auto()
    torso = auto()

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


class WeaponType(Enum):
    simple = auto()
    simple_ranged = auto()
    martial = auto()
    martial_ranged = auto()


class ActionType(Enum):
    move = auto()
    interact = auto()
    communicate = auto()
    action = auto()
    bonus_action = auto()
    reaction = auto()
    attack = auto()
    cast = auto()
    dash = auto()
    disengage = auto()
    dodge = auto()
    help_ = auto()
    hide = auto()
    hold_action = auto()
    seatch = auto()
