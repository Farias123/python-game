
# {"name": "poison dart", "cost": 0}, {"name": "teleport", "cost": 10}, {"name": "heal", "cost": 20},
# {"name": "arcane shot", "cost": 30}

class Spell:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.action = None
        self.end_effect = None
        self.end_break = None


def poison_dart_action(spell, player, enemy):
    print(f"You shoot a poison dart that deals {round(1 + player.maxMP / 20)} dmg and poisons by "
          f"{round(player.maxMP / 20)} points.")
    spell.poisondmg = player.maxMP / 20
    enemy.HP -= 1 + player.maxMP / 20
    # cost = 0

    def end_effect():
        if spell.poisondmg > 0:
            enemy.HP -= spell.poisondmg
            print(f"Your stacked poison dealt {spell.poisondmg} dmg.")
            spell.poisondmg -= 2

    spell.end_effect = end_effect


def teleport_action(spell, player, enemy):
    # cost = 10
    spell.end_break = True

    def end_effect():
        print("You teleported back to the merchant.")

    spell.end_effect = end_effect


def heal_action(spell, player, enemy):
    # cost = 20
    difference = player.maxHP - player.HP
    heal = 15 + player.maxMP / 20
    if heal > difference:
        heal = difference
    player.HP += heal
    print(f"You were healed by {round(heal)} HP.")


def arcane_shot_action(spell, player, enemy):
    # cost = 30
    dmg = player.maxMP/5
    print(f"You fire a magic arrow that deals {round(dmg)} damage")
    enemy.HP -= dmg


actions = [poison_dart_action, teleport_action, heal_action, arcane_shot_action]
all_spells = [Spell("poison dart", 0), Spell("teleport", 10), Spell("heal", 20),
              Spell("arcane shot", 30)]

for i in range(len(all_spells)):
    all_spells[i].action = actions[i]
