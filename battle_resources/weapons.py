class Weapon:
    def __init__(self, name, basedmg, style):
        self.name = name
        self.basedmg = basedmg
        self.style = style

    def damage(self, player):
        if self.style == 'DEX':
            mod = player.DEX/20
        elif self.style == 'STR':
            mod = player.STR/20

        return round(self.basedmg + mod)

    def action(self, player, enemy):
        damage_dealt = self.damage(player)*player.atk_buff_status/enemy.def_buff_status
        enemy.HP -= damage_dealt
        print(f"You dealt {damage_dealt} dmg with a {self.name}.")


all_weapons = [Weapon("stick", 5, "STR"), Weapon("dagger", 5, "DEX")]
