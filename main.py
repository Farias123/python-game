import os
from random import random
from time import sleep
from chars import Char, Fighter, Mage, Rogue, Enemy
from battle_resources.skills import Skill
from battle_resources.spells import Spell


def save_game():
    # jsons
    pass


def player_feedback():
    sleep(0.2)
    input("Press enter to continue")
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def custom_input():
    return input(">")


def character_creation():
    print("Hi there adventurer. In this adventure you will have to make choices.")
    print("To select options you need to type the number next to the option you want.")
    print("What's your name?")
    char_name = custom_input()
    print("What a beautiful name!")
    while True:
        try:
            print("Choose your class:")
            print("1-Fighter")
            print("2-Mage")
            print("3-Rogue")
            char_class = int(custom_input())
            if char_class not in range(1, 4):
                raise ValueError
            break
        except ValueError:
            print("Not a valid choice.")
            player_feedback()
            continue
    player_base = Char(char_name)
    possibilities = {1: Fighter(player_base), 2: Mage(player_base), 3: Rogue(player_base)}
    player = possibilities[char_class]
    return player


def enemy_turn(player, enemy):
    if enemy.skill_cooldown <= 0:
        action = random()

        if action < 0.5:
            enemy.use_skill(player, enemy)
            return
    else:
        enemy.skill_cooldown -= 1
    enemy.action(player)


def battle(player, enemy):
    spell = Spell("placeholder", 0)
    while enemy.HP > 0:
        while True:
            print(f"You have {round(player.HP)} HP and {player.MP} MP.")
            print(f"{enemy.name} has {round(enemy.HP)} HP.")
            print("Your turn, what will you do?")
            print("1- Attack \n2- Use magic")
            action = custom_input()

            if action == "1":
                available_weapons = {player.prepared_weapons.index(x) + 1: x for x in player.prepared_weapons}
                print(f" Which weapon will you use?")
                for k, v in available_weapons.items():
                    print(f"{k}- {v.name}")
                try:
                    attack = int(custom_input())
                    if attack in range(1, len(available_weapons) + 1):
                        weapon = available_weapons[attack]
                        weapon.action(player, enemy)
                        break
                except:
                    pass

            elif action == "2":
                available_spells = {player.prepared_spells.index(x) + 1: x for x in player.prepared_spells}
                print("Which spell will you use?")
                for k, v in available_spells.items():
                    print(f"{k}- {v.name} ({v.cost} MP)")
                try:
                    old_spell = spell
                    magic = int(custom_input())
                    if magic in range(1, len(available_spells) + 1):
                        spell = available_spells[magic]
                        spell.action(spell, player, enemy)

                        if spell.end_effect is None and old_spell.end_effect is not None:
                            spell.end_effect = old_spell.end_effect
                        break
                except:
                    pass

            print("Not a valid choice")
            player_feedback()

        if enemy.HP < 0:
            break

        enemy_turn(player, enemy)

        if spell is not None:
            if spell.end_effect is not None:
                spell.end_effect()

            if spell.end_break is not None:
                if spell.end_break: break

        player_feedback()
    if enemy.HP <= 0:
        print(f"You defeated the enemy {enemy.name}")
        return True  # victory
    else:
        return False  # ran away


def game():
    player = character_creation()
    player_feedback()
    enemy_skill = Skill("atk_debuff", "atk_debuff", user='enemy', de_buff_magnitude=0.75)
    bad = Enemy("teste", 50, {"name": "knife", "damage": 2}, enemy_skill)
    victory = battle(player, bad)
    # level up
    return


game()
