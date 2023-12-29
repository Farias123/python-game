class Skill:
    def __init__(self, name, type, damage=None, de_buff_magnitude=None, user=None):
        self.name = name
        self.type = type
        self.damage = damage
        self.de_buff_magnitude = de_buff_magnitude
        self.user = user

    def action(self, player, enemy):
        text = ''
        possible_users = {"player": player, "enemy": enemy}
        try:
            skill_user = possible_users.get(self.user)
            if self.user == 'player':
                oponent = enemy
            elif self.user == 'enemy':
                oponent = player
        except Exception as e:
            raise Exception(f'Usuário não atribuído: {e}')

        if self.type == 'atk_buff':
            self.atk_buff(skill_user, enemy)

        elif self.type == 'atk_debuff':
            self.atk_debuff(oponent, enemy)

        elif self.type == 'def_buff':
            self.def_buff(skill_user, enemy)

        elif self.type == 'def_debuff':
            self.def_debuff(oponent, enemy)

        elif self.type == 'freeze':
            self.freeze(skill_user, enemy)

        elif self.type == 'burn':
            self.burn(oponent, enemy)

    def atk_buff(self, skill_user, enemy):
        skill_user.atk_buff_status *= self.de_buff_magnitude

        if skill_user.atk_buff_status >= 2.0:
            skill_user.atk_buff_status = 2.0
            if self.user == 'player':
                print("You reached your maximum power")
            elif self.user == 'enemy':
                print(f"{enemy.name} reached its maximum power")
        else:
            if self.user == 'player':
                print("You are getting stronger")
            elif self.user == 'enemy':
                print(f"{enemy.name} is getting stronger")

    def atk_debuff(self, oponent, enemy):
        oponent.atk_buff_status *= self.de_buff_magnitude

        if oponent.atk_buff_status <= 0.5:
            oponent.atk_buff_status = 0.5
            if self.user == 'player':
                print(f"{enemy.name} reached its minimum power")
            elif self.user == 'enemy':
                print("You reached your minimum power")
        else:
            if self.user == 'player':
                print(f"{enemy.name} is getting weaker")
            elif self.user == 'enemy':
                print("You are getting weaker")

    def def_buff(self, skill_user, enemy):
        skill_user.def_buff_status *= self.de_buff_magnitude

        if skill_user.def_buff_status >= 2.0:
            skill_user.def_buff_status = 2.0
            if self.user == 'player':
                print("You reached your maximum defense")
            elif self.user == 'enemy':
                print(f"{enemy.name} reached its maximum defense")
        else:
            if self.user == 'player':
                print("Your defense is building")
            elif self.user == 'enemy':
                print(f"{enemy.name}'s defense is building")

    def def_debuff(self, oponent, enemy):
        oponent.def_buff_status *= self.de_buff_magnitude

        if oponent.def_buff_status <= 0.5:
            oponent.def_buff_status = 0.5
            if self.user == 'player':
                print(f"{enemy.name} reached its minimum defense")
            elif self.user == 'enemy':
                print("You reached your minimum defense")
        else:
            if self.user == 'player':
                print(f"{enemy.name}'s defense is getting weaker")
            elif self.user == 'enemy':
                print("Your defense is getting weaker")

    def freeze(self, oponent, enemy):
        pass

    def burn(self, oponent, enemy):
        pass


all_skills = []
