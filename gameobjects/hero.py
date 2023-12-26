from . import Weapon
from . import Armor
from . import Backpack


class Hero:
    """ Главный герой, за которого будет играть пользователь """

    # Каждые 1000 опыта будет повышаться уровень
    EXP_FOR_LEVEL_UP = 1000

    def __init__(self,
                 name: str,
                 max_hp: int = 100,
                 hp: int = 100,
                 total_exp: int = 0,
                 weapon_in_hands: Weapon | None = None,
                 equipped_armor: Armor | None = None,
                 money: int = 0
                 ) -> None:
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.total_exp = total_exp
        self.weapon_in_hands = weapon_in_hands
        self.equipped_armor = equipped_armor
        self.money = money

        self.level = total_exp // self.EXP_FOR_LEVEL_UP
        self.current_exp = total_exp % self.EXP_FOR_LEVEL_UP
        self.backpack = Backpack()
