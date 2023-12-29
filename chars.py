from battle_resources.spells import all_spells
from battle_resources.weapons import all_weapons


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
        self.skills = []
        self.atk_buff_status = 1
        self.def_buff_status = 1

    def rest(self):
        pass

    def buy_sell_item(self):
        pass

    def learn_spell(self):
        pass

    def prepare_spell(self):
        pass


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
    def __init__(self, name, HP, attack, skill):
        self.name = name
        self.maxHP = self.HP = HP
        self.attack = attack
        self.skill = skill
        self.atk_buff_status = 1
        self.def_buff_status = 1
        self.skill_cooldown = 0

    def action(self, player):
        damage_dealt = self.attack["damage"]*self.atk_buff_status/player.def_buff_status
        player.HP -= damage_dealt
        print(f"{self.name} dealt {round(damage_dealt)} damage with a {self.attack['name']}")

    def use_skill(self, player, enemy):
        self.skill.user = 'enemy'
        self.skill.action(player, enemy)
        self.skill_cooldown += 1
