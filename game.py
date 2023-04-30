import os
from time import sleep

class char:
    def __init__(self, name, type):

        self.name = name
        self.gold = 0
        self.STRweapon = {"name":"stick", "damage":5}
        self.DEXweapon = {"name":"dagger", "damage":5}

        if type == "2":
            self.type = "mage"
            self.maxHP = self.HP = 24
            self.maxMP = self.MP = 100
            self.STR = 20
            self.DEX = 30

        elif type == "3":
            self.type = "rogue"
            self.maxHP = self.HP = 30
            self.maxMP = self.MP = 20
            self.STR = 30
            self.DEX = 100

        else:
            self.type = "fighter"
            self.maxHP = self.HP = 36
            self.maxMP = self.MP = 0
            self.STR = 100
            self.DEX = 50

class enemy:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP 

def characterCreation():
    print("Hi there adventurer. In this adventure you will have to make choices.")
    print("To select options you need to type the number next to the option you want.")
    charName = input("What's your name? ")
    print("What a beautiful name!")
    print("Choose your class:")
    print("1-Fighter")
    print("2-Mage") 
    print("3-Rogue")
    charClass = input()
    os.system("clear")
    player = char(charName,charClass)
    return player

def battle(player, enemy):
    while True:
        os.system("clear")
        print("You have ",round(player.HP)," HP and ",player.MP,"MP.")
        print(enemy.name," has ", round(enemy.HP)," HP.")
        print("Your turn, what will you do?")
        action = input("1- Attack or 2- magic")
        if action == "1":
            print("Use 1-", player.STRweapon["name"]," or 2-",player.DEXweapon["name"])
            attack = input()
            if attack == "1":
                enemy.HP -= player.STRweapon["damage"]+(player.STR)/20
                print("You dealt ",round(player.STRweapon["damage"]+(player.STR)/20)," points of damage.")
            elif attack == "2":
                enemy.HP -= player.DEXweapon["damage"]+(player.DEX)/20
                print("You dealt ",round(player.DEXweapon["damage"]+(player.DEX)/20)," points of damage.")
        elif action == "2":
            magic = input("Use 1-???, 2- teleport(30 MP) or 3- fireball(50 MP)")
        sleep(2)
        

def game():
    player = characterCreation()
    os.system("clear")
    bad = enemy("mau",10)
    battle(player,bad)
    return

game()