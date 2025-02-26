from typing import Union, Self

from dungeon_enum import DamageType, CharacterSlot

__all__ = (
    'Item',
)


class Price:
    """A class for storing the value of something"""

    CURRENCY_DIGIT = (1, 10, 50, 100, 1000)

    def __init__(self, value: list = None):
        self.value = [] if value is None else value

    @property
    def value(self): return self._value

    @value.setter
    def value(self, val: list):
        if isinstance(val, list):
            if len(val) > 5:
                raise TypeError('In Price value too many elements. Max - 5')
            self._value = val
            self._raw = 0
            for idx, i in enumerate(val):
                self._raw += Price.CURRENCY_DIGIT[idx] * i
        else:
            raise TypeError('Price value must be integer or list[5]')

    @property
    def copper(self): return self.value[0]

    @copper.setter
    def copper(self, val: int):
        if val < 0:
            raise ValueError('The number of coins cannot be negative.')
        self._value[0] = val

    @property
    def silver(self): return self.value[1]

    @silver.setter
    def silver(self, val: int):
        if val < 0:
            raise ValueError('The number of coins cannot be negative.')
        self._value[1] = val

    @property
    def electrum(self): return self.value[2]

    @electrum.setter
    def electrum(self, val: int):
        if val < 0:
            raise ValueError('The number of coins cannot be negative.')
        self._value[2] = val

    @property
    def golden(self): return self.value[3]

    @golden.setter
    def golden(self, val: int):
        if val < 0:
            raise ValueError('The number of coins cannot be negative.')
        self._value[3] = val

    @property
    def platinum(self): return self.value[4]

    @platinum.setter
    def platinum(self, val: int):
        if val < 0:
            raise ValueError('The number of coins cannot be negative.')
        self._value[4] = val

    def __hash__(self): return hash(self._raw)

    def __eq__(self, other: Union[Self, int, list]):
        if isinstance(other, Price): return self._raw == other._raw
        elif isinstance(other, int): return self._raw == other
        elif isinstance(other, list): return self._raw == Price(other)._raw
        else: raise TypeError(f'Price cannot be compared with {type(other)}')

    def __lt__(self, other: Union[Self, int, list]):
        if isinstance(other, Price): return self._raw < other._raw
        elif isinstance(other, int): return self._raw < other
        elif isinstance(other, list): return self._raw < Price(other)._raw
        else: raise TypeError(f'Price cannot be compared with {type(other)}')

    def __gt__(self, other: Union[Self, int, list]):
        if isinstance(other, Price): return self._raw > other._raw
        elif isinstance(other, int): return self._raw > other
        elif isinstance(other, list): return self._raw > Price(other)._raw
        else: raise TypeError(f'Price cannot be compared with {type(other)}')

    def __le__(self, other: Union[Self, int, list]):
        if isinstance(other, Price): return self._raw <= other._raw
        elif isinstance(other, int): return self._raw <= other
        elif isinstance(other, list): return self._raw <= Price(other)._raw
        else: raise TypeError(f'Price cannot be compared with {type(other)}')

    def __ge__(self, other: Union[Self, int, list]):
        if isinstance(other, Price): return self._raw >= other._raw
        elif isinstance(other, int): return self._raw >= other
        elif isinstance(other, list): return self._raw >= Price(other)._raw
        else: raise TypeError(f'Price cannot be compared with {type(other)}')


class Item:
    """Main parental class"""

    def __init__(self, name: str, description: str, price: Price = None,
                 weight: int = None):
        self.name = name
        self.description = description
        self.price = Price() if price is None else price
        self.weight = 0 if weight is None else weight
        self.is_use = False
        self.on_slot = CharacterSlot.back

    @property
    def weight(self): return self._weight

    @weight.setter
    def weight(self, val: int):
        if val < 0: raise ValueError('Weight cannot have a negative value.')
        self._weight = val

    def __hash__(self):
        return hash((self.name, self.description, self.price, self.weight))

    def __eq__(self, other: Self): return hash(self) == hash(other)


class ArmorType:
    """D&D armor type class"""

    def __init__(self, name: str, taking_off_time: int, putting_on_time: int):
        self.name = name
        self.taking_off_time = taking_off_time # In seconds
        self.putting_on_time = putting_on_time # In seconds

    @property
    def taking_off_time(self): return self._taking_off_time

    @taking_off_time.setter
    def taking_off_time(self, val: int):
        if val < 6: raise ValueError('The minimum time to remove armor is 6 '
                                     'seconds.')
        self._taking_off_time = val

    @property
    def putting_on_time(self):
        return self._putting_on_time

    @putting_on_time.setter
    def putting_on_time(self, val: int):
        if val < 6: raise ValueError('The minimum time to wear armor is 6 '
                                     'seconds.')
        self._putting_on_time = val

    @staticmethod
    def types() -> tuple[str, ...]:
        """Returns list of armor types"""
        return tuple(filter(lambda x: '__' not in x, ArmorType.__dict__))[-4:]

    @classmethod
    def light_armor(cls):
        return cls('Light armor', 60, 60)

    @classmethod
    def medium_armor(cls):
        return cls('Medium armor', 60, 300)

    @classmethod
    def heavy_armor(cls):
        return cls('Heavy armor', 300, 600)

    @classmethod
    def shield(cls):
        return cls('Shield', 6, 6)


class Armor(Item):
    """D&D armor class"""

    def __init__(self, name: str, description: str, price: Price = None,
                 weight: int = None, armor_type: ArmorType = None,
                 armor_class: int = 10, required_strength: int = 0,
                 stealth_penalty: bool = False):
        super().__init__(name, description, price, weight)
        self.armor_type = armor_type
        self.armor_class = armor_class
        self.required_strength = required_strength
        self.stealth_penalty = stealth_penalty

    @property
    def armor_class(self): return self._armor_class

    @armor_class.setter
    def armor_class(self, val: int):
        if val < 10:
            raise ValueError(f'Armor "{self.name}" cannot have an armor class '
                             'lower than 10.')
        if val < 11:
            raise Warning(f'Armor "{self.name}" is useless due to its low '
                          'armor class.')
        self._armor_class = val

    def __lt__(self, other: Union[Self, int]):
        if isinstance(other, Armor):
            return self.armor_class < other.armor_class
        elif isinstance(other, int):
            return self.armor_class < other
        else:
            raise TypeError('Armor class cannot be compared with'
                              f' {type(other)}')

    def __gt__(self, other: Union[Self, int]):
        if isinstance(other, Armor):
            return self.armor_class > other.armor_class
        elif isinstance(other, int):
            return self.armor_class > other
        else:
            raise TypeError('Armor class cannot be compared with'
                            f' {type(other)}')

    def __le__(self, other: Union[Self, int]):
        if isinstance(other, Armor):
            return self.armor_class <= other.armor_class
        elif isinstance(other, int):
            return self.armor_class <= other
        else:
            raise TypeError('Armor class cannot be compared with'
                            f' {type(other)}')

    def __ge__(self, other: Union[Self, int]):
        if isinstance(other, Armor):
            return self.armor_class >= other.armor_class
        elif isinstance(other, int):
            return self.armor_class >= other
        else:
            raise TypeError('Armor class cannot be compared with'
                            f' {type(other)}')


class Property:
    def __init__(self, name: str, description: str, **kwargs):
        self.name = name
        self.description = description
        self.values = kwargs


class Damage:
    def __init__(self, type_: Union[DamageType, int, str],
                 value: tuple[int, int] = (0, 0)):
        self.type_ = type_
        self.value = value

    @property
    def type_(self): return self._type_

    @type_.setter
    def type_(self, val: Union[DamageType, int, str]):
        if isinstance(val, int) and not len(DamageType.names()) > val >= 0:
            raise ValueError(f'Incorrect damage type with index {val}')
        elif isinstance(val, str) and val.lower() not in DamageType.names():
            raise ValueError(f'Incorrect damage type with name "{val}"')
        self._type_ = val


class Weapon(Item):
    def __init__(self, name: str, description: str, price: Price = None,
                 weight: int = None, damage: Damage = None,
                 properties: list[Property] = None,
                 is_improvised: bool = False, is_silvered: bool = False):
        super().__init__(name, description, price, weight)
        self.damage = Damage(DamageType.bludgeoning) if None else damage
        self.properties = properties
        self.is_improvised = is_improvised
        self.is_silvered = is_silvered
