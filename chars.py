from spells import all_spells, Spell
from weapons import all_weapons, Weapon


class Char:
    def __init__(self, name):
        base_spells = [x for x in all_spells if x.name in ["poison dart", "teleport", "heal", "arcane shot"]]
        base_weapons = [x for x in all_weapons if x.name in ["stick", "dagger"]]
        self.name = name
        self.gold = 0
        self.prepared_weapons = base_weapons.copy()
        self.owned_weapons = base_weapons.copy()
        self.backpack = []
        self.prepared_spells = base_spells.copy()
        self.known_spells = base_spells.copy()
        self.spells_equipped = []

    def weapon_damage(self, style='STR'):
        if style == 'DEX':
            return round(self.DEXweapon['damage'] + self.DEX / 20)
        elif style == 'STR':
            return round(self.STRweapon['damage'] + self.STR / 20)


class Mage(Char):
    def __init__(self, name):
        super().__init__(name)
        self.maxHP = self.HP = 12
        self.maxMP = self.MP = 100
        self.STR = 20
        self.DEX = 30


class Rogue (Char):
    def __init__(self, name):
        super().__init__(name)
        self.maxHP = self.HP = 15
        self.maxMP = self.MP = 20
        self.STR = 30
        self.DEX = 100


class Fighter(Char):
    def __init__(self, name):
        super().__init__(name)
        self.maxHP = self.HP = 18
        self.maxMP = self.MP = 0
        self.STR = 100
        self.DEX = 50


class Enemy:
    def __init__(self, name, HP, attack, skill=None):
        self.name = name
        self.maxHP = self.HP = HP
        self.attack = attack
        self.skill = skill
