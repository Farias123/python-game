class char:
    def __init__(self, name, type):

        self.name = name
        self.gold = 0
        self.STRweapon = {"name":"stick", "damage":10}
        self.DEXweapon = {"name":"dagger", "damage":10}

        if type == "m":
            self.type = "mage"
            self.maxHP = self.HP = 24
            self.maxMP = self.MP = 100
            self.STR = 20
            self.DEX = 30

        elif type == "r":
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
    print("To select options you need to type the first character of the option you want.")
    charName = input("What's your name? ")
    print(charName,"! What a beautiful name!")
    charClass = input("Choose your class: fighter, mage or rogue ")
    player = char(charName,charClass)
    return player

def battle(player, enemy):
    while True:
        print("Your turn, what will you do?")
        action = input("Attack or magic")
        if action == "a":
            attack = input("Use a ", player.STRweapon["name"]," or a ",player.DEXweapon["name"])
            if attack == player.STRweapon["name"][0]:
                enemy.HP -= player.STRweapon["damage"]+(player.STR)/10
            elif attack == player.DEXweapon["name"][0]:
                enemy.HP -= player.DEXweapon["damage"]+(player.DEX)/10
        elif action == "m":
            magic = input("Use ???, a teleport(30 MP) or a fireball(50 MP)")
        

def game():
    player = characterCreation()


    return




game()