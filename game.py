import os
from time import sleep

class char:
    def __init__(self, name, type):

        self.name = name
        self.gold = 0
        self.STRweapon = {"name":"stick", "damage":5}
        self.DEXweapon = {"name":"dagger", "damage":5}
        self.backpack = []

        if type == "2":
            self.type = "mage"
            self.maxHP = self.HP = 12
            self.maxMP = self.MP = 100
            self.STR = 20
            self.DEX = 30

        elif type == "3":
            self.type = "rogue"
            self.maxHP = self.HP = 15
            self.maxMP = self.MP = 20
            self.STR = 30
            self.DEX = 100

        else:
            self.type = "fighter"
            self.maxHP = self.HP = 18
            self.maxMP = self.MP = 0
            self.STR = 100
            self.DEX = 50

class enemy:
    def __init__(self, name, HP, attack):
        self.name = name
        self.HP = HP
        self.attack = attack

def playerFeedback():
    sleep(0.5)
    input("Press enter to continue")
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

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
    player = char(charName,charClass)
    return player

def battle(player, enemy):
    teleported = False
    poisondmg = 0
    while True:
        while True:
            print("You have ",round(player.HP)," HP and ",player.MP,"MP.")
            print(enemy.name," has ", round(enemy.HP)," HP.")
            print("Your turn, what will you do?")
            print("1- Attack or 2- magic")
            action = input()
            if action == "1":
                print("Use 1-", player.STRweapon["name"]," or 2-",player.DEXweapon["name"])
                attack = input()
                if attack == "1":
                    enemy.HP -= player.STRweapon["damage"]+(player.STR)/20
                    print("You dealt ",round(player.STRweapon["damage"]+(player.STR)/20)," dmg with a",player.STRweapon["name"],".")
                    break 
                elif attack == "2":
                    enemy.HP -= player.DEXweapon["damage"]+(player.DEX)/20
                    print("You dealt ",round(player.DEXweapon["damage"]+(player.DEX)/20)," dmg with a", player.DEXweapon["name"],".")
                    break
            elif action == "2":
                print("Use 1- poison dart(0 MP), 2- teleport(10 MP), 3- heal (20 MP) or 4- arcane shot (30 MP)")
                magic = input()
                if magic == "1":
                    print("You shoot a poison dart that deals",round(1+player.maxMP/20),"dmg and poisons by",round(player.maxMP/20),"points.")
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
                    print("You were healed by",round(heal),"HP.")
                    player.MP -= 20
                    break
                elif magic == "4" and player.MP >= 30:
                    print("You fire a magic arrow that deals",round(player.maxMP/5),"damage")
                    enemy.HP -= player.maxMP/5
                    player.MP -= 30
                    break
                
            print("Not a valid choice")
            playerFeedback()

                
        if teleported == True:
            print("You teleported back to the merchant.")
            break

#enemy turn

        if poisondmg > 0:
            enemy.HP -= poisondmg
            print("Your stacked poison dealt",poisondmg,"dmg.")
        playerFeedback()
        

def game():
    player = characterCreation()
    playerFeedback()
    bad = enemy("teste",50,{"name":"knife","damage":2})
    battle(player,bad)
    return

game()