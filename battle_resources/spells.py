class Spell:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.action = None
        self.end_effect = None
        self.end_break = None


def poison_dart_action(spell, player, enemy):
    damage_dealt = (1 + player.maxMP / 20)*player.atk_buff_status/enemy.def_buff_status
    print(f"You shoot a poison dart that deals {round(damage_dealt)} dmg and poisons by "
          f"{round(player.maxMP / 20)} points.")
    spell.poisondmg = player.maxMP / 20
    enemy.HP -= damage_dealt
    # cost = 0

    def end_effect():
        if spell.poisondmg > 0:
            poison_dmg = spell.poisondmg*player.atk_buff_status/enemy.def_buff_status
            enemy.HP -= poison_dmg
            print(f"Your stacked poison dealt {round(poison_dmg)} dmg.")
            spell.poisondmg -= 2

    spell.end_effect = end_effect
    player.MP -= spell.cost


def teleport_action(spell, player, enemy):
    # cost = 10
    spell.end_break = True

    def end_effect():
        print("You teleported back to the merchant.")

    spell.end_effect = end_effect
    player.MP -= spell.cost


def heal_action(spell, player, enemy):
    # cost = 20
    difference = player.maxHP - player.HP
    heal = 15 + player.maxMP / 20
    if heal > difference:
        heal = difference
    player.HP += heal
    print(f"You were healed by {round(heal)} HP.")
    player.MP -= spell.cost

def arcane_shot_action(spell, player, enemy):
    # cost = 30
    dmg = (player.maxMP/5)*player.atk_buff_status/enemy.def_buff_status
    print(f"You fire a magic arrow that deals {round(dmg)} damage")
    enemy.HP -= dmg
    player.MP -= spell.cost


actions = [poison_dart_action, teleport_action, heal_action, arcane_shot_action]
all_spells = [Spell("poison dart", 0), Spell("teleport", 10), Spell("heal", 20),
              Spell("arcane shot", 30)]

for i in range(len(all_spells)):
    all_spells[i].action = actions[i]
