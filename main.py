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
            break
        except ValueError:
            print("Type a valid number.")
            continue
    player_base = Char(char_name)
    possibilities = {1: Fighter(player_base), 2: Mage(player_base), 3: Rogue(player_base)}
    player = possibilities[char_class]
    return player


def battle(player, enemy):
    teleported = False
    poisondmg = 0
    while True:
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
                    print(f"You dealt {player.weapon_damage('STR')} dmg with {player.STRweapon['name']}.")
                    break 
                elif attack == "2":
                    enemy.HP -= player.weapon_damage('DEX')
                    print(f"You dealt {player.weapon_damage('DEX')} dmg with a {player.DEXweapon['name']}.")
                    break
            elif action == "2":
                print("Use 1- poison dart(0 MP), 2- teleport(10 MP), 3- heal (20 MP) or 4- arcane shot (30 MP)")
                magic = input()
                if magic == "1":
                    print(f"You shoot a poison dart that deals {round(1+player.maxMP/20)} dmg and poisons by "
                          f"{round(player.maxMP / 20)} points.")
                    poisondmg += player.maxMP/20
                    enemy.HP -= 1 + player.maxMP/20
                    break
                elif magic == "2" and player.MP >= 10:
                    teleported = True    
                    player.MP -= 10
                    break
                elif magic == "3" and player.MP >= 20:
                    difference = player.maxHP - player.HP
                    heal = 15 + player.maxMP/20
                    if heal > difference:
                        heal = difference
                    player.HP += heal
                    print(f"You were healed by {round(heal)} HP.")
                    player.MP -= 20
                    break
                elif magic == "4" and player.MP >= 30:
                    print(f"You fire a magic arrow that deals {round(player.maxMP / 5)} damage")
                    enemy.HP -= player.maxMP/5
                    player.MP -= 30
                    break
                
            print("Not a valid choice")
            player_feedback()

        if teleported:
            print("You teleported back to the merchant.")
            break

# enemy turn

        if poisondmg > 0:
            enemy.HP -= poisondmg
            print(f"Your stacked poison dealt {poisondmg} dmg.")
        player_feedback()
        

def game():
    player = character_creation()
    player_feedback()
    bad = Enemy("teste", 50, {"name": "knife", "damage": 2}, {})
    battle(player, bad)
    return


game()
