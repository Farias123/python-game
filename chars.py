class Char:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.STRweapon = {"name": "stick", "damage": 5}
        self.DEXweapon = {"name": "dagger", "damage": 5}
        self.backpack = []
        self.spells = [
            {"name": "poison dart", "cost": 0}, {"name": "teleport", "cost": 10}, {"name": "heal", "cost": 20},
            {"name": "arcane shot", "cost": 30}
        ]
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

        if skill is not None:
            self.skill = skill