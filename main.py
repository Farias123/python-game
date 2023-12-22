import os
from time import sleep
from chars import Char, Fighter, Mage, Rogue, Enemy


def player_feedback():
    sleep(0.5)
    input("Press enter to continue")
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def character_creation():
    print("Hi there adventurer. In this adventure you will have to make choices.")
    print("To select options you need to type the number next to the option you want.")
    char_name = input("What's your name? ")
    print("What a beautiful name!")
    while True:
        try:
            print("Choose your class:")
            print("1-Fighter")
            print("2-Mage")
            print("3-Rogue")
            char_class = int(input())
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


def battle(player, enemy):
    spell = None
    while enemy.HP > 0:
        while True:
            print(f"You have {round(player.HP)} HP and {player.MP} MP.")
            print(f"{enemy.name} has {round(enemy.HP)} HP.")
            print("Your turn, what will you do?")
            print("1- Attack or 2- magic")
            action = input()
            if action == "1":
                print(f"Use 1-{player.STRweapon['name']} or 2-{player.DEXweapon['name']}")
                attack = input()
                if attack == "1":
                    enemy.HP -= player.weapon_damage('STR')
                    print(f"You dealt {player.weapon_damage('STR')} dmg with a {player.STRweapon['name']}.")
                    break
                elif attack == "2":
                    enemy.HP -= player.weapon_damage('DEX')
                    print(f"You dealt {player.weapon_damage('DEX')} dmg with a {player.DEXweapon['name']}.")
                    break
            elif action == "2":
                available_spells = {player.prepared_spells.index(x) + 1: x for x in player.prepared_spells}
                choice_text = "Use "
                for k, v in available_spells.items():
                    choice_text += f"{k}- {v.name} ({v.cost} MP)"
                    if k == 3:
                        choice_text += " or "
                        continue
                    elif k == 4:
                        continue
                    else:
                        choice_text += ", "
                print(choice_text)
                try:
                    old_spell = spell
                    magic = int(input())
                    if magic in range(1, 5):
                        spell = available_spells[magic]
                        spell.action(spell, player, enemy)

                        if spell.end_effect is None and old_spell.end_effect is not None:
                            spell.end_effect = old_spell.end_effect
                        break
                except:
                    pass

            print("Not a valid choice")
            player_feedback()

        if spell is not None:
            if spell.end_effect is not None:
                spell.end_effect()

            if spell.end_break is not None:
                if spell.end_break: break

        # enemy turn

        player_feedback()
    if enemy.HP <= 0:
        print(f"You defeated the enemy {enemy.name}")
        return True  # victory
    else:
        return False  # ran away


def game():
    player = character_creation()
    player_feedback()
    bad = Enemy("teste", 50, {"name": "knife", "damage": 2}, {})
    victory = battle(player, bad)
    # level up
    return


game()
