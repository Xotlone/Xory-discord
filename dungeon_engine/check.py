from typing import Union, Self
from random import randint

__all__ = (
    'Check',
)


class Check:
    def __init__(self, dice: tuple[int, int] = (1, 20), mod: int = 0):
        self.dice = dice
        self.mod = mod
        self.rolls = [randint(1, dice[1]) + mod for i in range(dice[0])]
        self.result = sum(self.rolls)

    def __int__(self): return self.result

    def __eq__(self, other: Union[Self, int]):
        if isinstance(other, Check): return self.result == other.result
        elif isinstance(other, int): return self.result == other

    def __lt__(self, other: Union[Self, int]):
        if isinstance(other, Check): return self.result < other.result
        elif isinstance(other, int): return self.result < other

    def __gt__(self, other: Union[Self, int]): return not self.__lt__(other)

    def __le__(self, other: Union[Self, int]):
        if isinstance(other, Check): return self.result <= other.result
        elif isinstance(other, int): return self.result <= other

    def __ge__(self, other: Union[Self, int]): return not self.__le__(other)

    @classmethod
    def roll(cls, dice: tuple[int, int] = (1, 20), mod: int = 0):
        return cls(dice, mod)
