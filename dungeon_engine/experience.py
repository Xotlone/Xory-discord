from typing import Self, Union

__all__ = (
    'Experience'
)


class Experience:
    """Class for storing and calculating experience parameters such as level
    and profficiency bonus"""

    LEVEL_TO_EXP = (0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000,
                     64000, 85000, 100000, 120000, 140000, 165000, 195000,
                     225000, 265000, 305000, 355000)

    def __init__(self, points: int = 0):
        self.points = points

    @property
    def points(self): return self._points

    @points.setter
    def points(self, val: int):
        if val < 0: raise ValueError('Experience points cannot be lower than '
                                     '0.')
        self._points = val
        self.level = Experience.get_level(val)
        self.profficiency_bonus = Experience.get_profficiency_bonus(val)

    def __hash__(self): return hash(self.points)

    def __int__(self): return self.points

    def __eq__(self, other: Union[Self, int]):
        if isinstance(other, Experience): return self.points == other.points
        elif isinstance(other, int): return self.points == other

    def __lt__(self, other: Union[Self, int]):
        if isinstance(other, Experience): return self.points < other.points
        elif isinstance(other, int): return self.points < other

    def __gt__(self, other: Union[Self, int]):
        if isinstance(other, Experience): return self.points > other.points
        elif isinstance(other, int): return self.points > other

    def __le__(self, other: Union[Self, int]):
        if isinstance(other, Experience): return self.points <= other.points
        elif isinstance(other, int): return self.points <= other

    def __ge__(self, other: Union[Self, int]):
        if isinstance(other, Experience): return self.points >= other.points
        elif isinstance(other, int): return self.points >= other

    @staticmethod
    def get_level(points: int) -> int:
        """Calculates the level depending on experience"""

        for idx, i in enumerate(Experience.LEVEL_TO_EXP):
            if Experience.LEVEL_TO_EXP[min(len(Experience.LEVEL_TO_EXP)-1,
                                            idx+1)] > points >= i:
                return idx+1
        return len(Experience.LEVEL_TO_EXP)

    @staticmethod
    def get_profficiency_bonus(points: int) -> int:
        """Calculates the profficiency bonus depending on experience"""

        return max(2, int((points / 100) ** (1 / 3)))

    @staticmethod
    def get_points(level: int) -> int:
        """Calculates the number of points in a level"""

        if level < 1: raise ValueError('Level cannot be lower than 1.')
        elif level > 20: raise ValueError('Level cannot be higher than 20.')
        return Experience.LEVEL_TO_EXP[level-1]

    @classmethod
    def from_points(cls, points: int = 0):
        """Returns instance created from points"""

        return cls(points)

    @classmethod
    def from_level(cls, level: int = 1):
        """Returns instance created from level"""

        return cls(Experience.get_points(level))
