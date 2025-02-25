from typing import *
import math

from enums import *


def get_level(experience_point: int) -> int:
    """Calculates the level depending on experience"""
    return max(1, int(math.sqrt(experience_point / 100 + 1)))


def get_profficiency_bonus(experience_point: int) -> int:
    """Calculates the profficiency bonus depending on experience"""
    return max(2, int((experience_point / 100) ** (1 / 3)))


class Skill:
    def __init__(self, name: Skills,
                 proficiency: Proficiency = Proficiency.LACK_OF_KNOWLEDGE):
        self.name = name
        self.proficiency = proficiency

    def __eq__(self, other): return hash(self) == hash(other)

    def __hash__(self): return hash(self.name) + hash(self.proficiency.value)


class Price:
    def __init__(self, copper: int = 0, silver: int = 0, electrum: int = 0,
                 golden: int = 0, platinum: int = 0,
                 raw: list[int, int, int, int, int] = None):
        self.copper = copper
        self.silver = silver
        self.electrum = electrum
        self.golden = golden
        self.platinum = platinum
        if raw is None:
            self.raw = [copper, silver, electrum, golden, platinum]
        else:
            self.raw = raw


class Item:
    def __init__(self, name: str, description: str, price: Price = None,
                 weight: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


class Armor(Item):
    def __init__(self, name: str, description: str, price: Price,
                 weight: int, armor_type: ArmorTypes, armor_class: int,
                 required_strength: int = 0, stealth_penalty: bool = False,
                 is_equiped: bool = False):
        super().__init__(name, description, price, weight)
        self._armor_type = armor_type
        self._armor_class = armor_class
        self.required_strength = required_strength
        self.stealth_penalty = stealth_penalty
        self.is_equiped = is_equiped

    @property
    def armor_class(self) -> int:
        return self._armor_class

    @armor_class.setter
    def armor_class(self, new_armor_class):
        if new_armor_class < 10:
            raise ValueError(f'Armor "{self.name}" cannot have an armor class '
                             'lower than 10.')
        if new_armor_class < 11:
            raise Warning(f'Armor "{self.name}" is useless due to its low '
                          'armor class.')
        self._armor_class = new_armor_class


class Weapon(Item):
    pass


class Influence:
    def __init__(self, parameter: str, value: Any):
        self.parameter = parameter
        self.value = value


class Ability:
    def __init__(self, name: str, description: str,
                 opening_conditions: Union[List, Dict[str, int]],
                 duration: int = None, influence: List[Influence] = None):
        self.name = name
        self.description = description
        self.opening_conditions = opening_conditions
        self.duration = duration
        self.influence = influence


class ClassPath:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Class:
    def __init__(self, *, name: str, description: str, level: int = 1,
                 hit_dice: int, proficiencies: list[str],
                 saving_throws: list[Parameters], skills: list[Skill],
                 skill_count: int, start_equipment: list,
                 abilities: list[Ability], class_path: ClassPath = None):
        self.name = name
        self.description = description
        self.level = level
        self.hit_dice = hit_dice
        self.proficiencies = proficiencies
        self.saving_throws = saving_throws
        self.skills = skills
        self.skill_count = skill_count
        self.start_equipment = start_equipment
        self.abilities = abilities
        self.class_path = class_path


class Background:
    def __init__(self, name: str, description: str,
                 skills: list[Skill], tools: list[Item], items: list[Item],
                 feature: str):
        self.name = name
        self.description = description
        self.skills = skills
        self.tools = tools
        self.items = items
        self.feature = feature


class RaceFeature:
    def __init__(self, name: str, description: str,
                 influence: Union[Influence, Skill]):
        self.name = name
        self.description = description
        self.influence = influence


class Subrace:
    def __init__(self, name: str, description: str,
                 features: list[RaceFeature]):
        self.name = name
        self.description = description
        self.features = features


class Race(Subrace):
    def __init__(self, name: str, description: str,
                 features: list[RaceFeature], subraces: list[Subrace] = None):
        super().__init__(name, description, features)
        self.subraces = subraces


class Spell:
    def __init__(self, name: str, description: str):
        pass


class Character:
    def __init__(self, *, author_id: int, name: str,
                 classes: list[Class], background: Background, race: Race,
                 alignment: Alignment, experience_point: int = 0,
                 parameters: Dict[Parameters, int],
                 inspiration: bool = False, armor_class: int = None,
                 speed: int = None, skills: list[Skill],
                 personality_traits: str, ideals: str, bonds: str, flaws: str,
                 equipment: list[Item] = None, gender: str, age: int,
                 height: int = None, weight: int = None, skin: str = '',
                 eyes: str = '', hair: str = '', appearance: str = '',
                 organizations: str = '', additional: str = '',
                 prepared_spells: list[Spell] = None):
        # TODO: Дописать перерасчёт всех внутренних параметров
        self.author_id = author_id
        self.name = name
        self.classes = classes
        self.background = background
        self.race = race
        self.alignment = alignment
        self.experience_point = experience_point
        self.parameters = parameters
        self.inspiration = inspiration
        self.initiative = 0
        self.speed = speed
        self.skills = skills
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.equipment = equipment
        self.armor_class = armor_class
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.skin = skin
        self.eyes = eyes
        self.hair = hair
        self.appearance = appearance
        self.organizations = organizations
        self.additional = additional
        self.prepared_spells = prepared_spells

    @property
    def parameters(self) -> Dict[Parameters, int]:
        result = {}
        for feature in self.race.features:
            influence = feature.influence
            for param in Parameters:
                result[param] = self._parameters[param]
                if (isinstance(influence, Influence) and
                        influence.parameter == param.name.lower()):
                    if influence.value < 0:
                        raise ValueError('The effect on the character\'s '
                                         'parameter cannot have a negative '
                                         f'value! Check the "{feature.name}" '
                                         f'feature of the "{self.race.name}" '
                                         'race.')

                    result[param] += influence.value
        return result

    @parameters.setter
    def parameters(self, new_params: Dict[Parameters, int]):
        for param in Parameters:
            if new_params[param] < 8:
                raise ValueError('Any parameter cannot be lower than 8')
        self._parameters = new_params

    @property
    def proficiency_bonus(self) -> int:
        result = get_profficiency_bonus(self.experience_point)
        if result < 2:
            raise ValueError('Mastery bonus cannot be lower than 2')
        return result

    @property
    def armor_class(self) -> int: return self._armor_class

    @armor_class.setter
    def armor_class(self, new_armor_class: int):
        result = new_armor_class
        if new_armor_class is None:
            item_armor_class = 10
            race_armor_class = 10
            if self.equipment is not None:
                for item in self.equipment:
                    if isinstance(item, Armor) and item.is_equiped:
                        item_armor_class = item.armor_class
                        if 'shield' not in item.name.lower():
                            break

            for feature in self.race.features:
                influence = feature.influence
                if (isinstance(influence, Influence) and
                        influence.parameter == 'armor_class'):
                    if isinstance(influence.value, int):
                        race_armor_class = influence.value
                    elif isinstance(influence.value, list):
                        for parameter in influence.value:
                            race_armor_class += self.parameters[parameter]

            result = max(item_armor_class, race_armor_class)

        if result < 10:
            raise ValueError('Armor class cannot be lower than 10')
        self._armor_class = result

    @property
    def initiative(self) -> int:
        return self._initiative

    @initiative.setter
    def initiative(self, value: int):
        self._initiative = max(1,
                               self.parameters[Parameters.DEXTERITY] + value)

    @property
    def speed(self) -> int:
        result = self._speed
        if self._speed is None:
            for feature in self.race.features:
                influence = feature.influence
                if influence.parameter == 'speed':
                    result = influence.value

        if result < 0:
            raise ValueError('Speed cannot be lower than 0')
        return result

    @speed.setter
    def speed(self, new_speed: int):
        if new_speed is not None and new_speed < 0:
            raise ValueError('Speed cannot be lower than 0')
        self._speed = new_speed

    @property
    def skills(self) -> list[Skill]:
        return self._skills

    @skills.setter
    def skills(self, new_skills: list[Skill]):
        class_skills = set()
        for class_ in self.classes:
            class_skills = class_skills.union(class_.skills)
        background_skills = set(self.background.skills)
        race_skills = {i.influence for i in self.race.features if
                       isinstance(i.influence, Skill)}
        current_skills = set(new_skills[:])
        for skill in current_skills:
            if skill.proficiency.value <= Proficiency.LACK_OF_KNOWLEDGE.value:
                current_skills.remove(skill)

        diff = current_skills - class_skills - background_skills - race_skills
        if diff != set():
            raise Warning(f'"{self.name}" abilities ({", ".join(diff)}) go '
                          'beyond background, classes and race')
        self._skills = new_skills


test_item = Item(
    'test_item',
    'test_desc',
    Price()
)

test_ability = Ability(
    'test_ability',
    'test_desc',
    {'level': 1}
)

test_class = Class(
    name='test_class',
    description='test_desc',
    level=1,
    hit_dice=8,
    proficiencies=[WeaponTypes.SIMPLE, WeaponTypes.MARTIAL],
    saving_throws=[Parameters.DEXTERITY, Parameters.INTELLIGENCE],
    skills=[
        Skill(Skills.ACROBATICS, Proficiency.PROFICIENCY),
        Skill(Skills.SLEIGHT_OF_HAND, Proficiency.PROFICIENCY),
        Skill(Skills.STEALTH, Proficiency.PROFICIENCY),
        Skill(Skills.PERCEPTION, Proficiency.PROFICIENCY),
    ],
    skill_count=4,
    start_equipment=[
        test_item
    ],
    abilities=[test_ability]
)

test_background = Background(
    'test_background',
    'test_desc',
    [
        Skill(Skills.ARCANA, Proficiency.PROFICIENCY),
        Skill(Skills.HISTORY, Proficiency.PROFICIENCY)
    ],
    [test_item],
    [test_item],
    'test_feature'
)

test_race = Race(
    'test_race',
    'test_desc',
    [
        RaceFeature(
            'test_race_feature1',
            'test_desc',
            Skill(Skills.PERSUASION, Proficiency.PROFICIENCY)
        ),
        RaceFeature(
            'test_race_feature2',
            'test_desc',
            Influence('armor_class', 12)
        )
    ]
)

test_character = Character(
    author_id=0,
    name='test_character',
    classes=[test_class],
    background=test_background,
    race=test_race,
    alignment=Alignment.TRUE_NEUTRAL,
    parameters={
        Parameters.DEXTERITY: 8,
        Parameters.INTELLIGENCE: 10,
        Parameters.WISDOM: 12,
        Parameters.CHARISMA: 13,
        Parameters.CONSTITUTION: 14,
        Parameters.STRENGTH: 15
    },
    skills=[
        Skill(Skills.STEALTH, Proficiency.PROFICIENCY),
        Skill(Skills.SLEIGHT_OF_HAND, Proficiency.PROFICIENCY),
        Skill(Skills.HISTORY, Proficiency.PROFICIENCY),
        Skill(Skills.ARCANA, Proficiency.PROFICIENCY)
    ],
    personality_traits='test',
    ideals='test',
    bonds='test',
    flaws='test',
    gender='test',
    age=0
)

print(';\n'.join([f'{k}: {v}' for k, v in test_character.__dict__.items()]))
skill1 = Skill(Skills.STEALTH, Proficiency.PROFICIENCY)
skill2 = Skill(Skills.STEALTH, Proficiency.COMPETENCE)
print(f'\n{skill1 == skill2}')
