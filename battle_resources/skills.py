class Skill:
    def __init__(self, name, type, damage=None, de_buff_magnitude=None, user=None):
        self.name = name
        self.type = type
        self.damage = damage
        self.de_buff_magnitude = de_buff_magnitude
        self.user = user

    def action(self, player, enemy):
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
                print(f"You reached your maximum power using {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name} reached its maximum power using {self.name}")
        else:
            if self.user == 'player':
                print(f"You are getting stronger using {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name} is getting stronger using {self.name}")

    def atk_debuff(self, oponent, enemy):
        oponent.atk_buff_status *= self.de_buff_magnitude

        if oponent.atk_buff_status <= 0.5:
            oponent.atk_buff_status = 0.5
            if self.user == 'player':
                print(f"{enemy.name}'s power was fully decreased by {self.name}")
            elif self.user == 'enemy':
                print(f"Your power was fully decreased by {self.name}")
        else:
            if self.user == 'player':
                print(f"You are decreasing {enemy.name}'s power with {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name} is decreasing your power with {self.name}")

    def def_buff(self, skill_user, enemy):
        skill_user.def_buff_status *= self.de_buff_magnitude

        if skill_user.def_buff_status >= 2.0:
            skill_user.def_buff_status = 2.0
            if self.user == 'player':
                print(f"You reached your maximum defense with {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name} reached its maximum defense with {self.name}")
        else:
            if self.user == 'player':
                print(f"Your defense is building with {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name}'s defense is building {self.name}")

    def def_debuff(self, oponent, enemy):
        oponent.def_buff_status *= self.de_buff_magnitude

        if oponent.def_buff_status <= 0.5:
            oponent.def_buff_status = 0.5
            if self.user == 'player':
                print(f"{enemy.name}'s defense was fully decreased by {self.name}")
            elif self.user == 'enemy':
                print(f"Your defense was fully decreased by {self.name}")
        else:
            if self.user == 'player':
                print(f"You are decreasing {enemy.name}'s defense with {self.name}")
            elif self.user == 'enemy':
                print(f"{enemy.name} is decreasing your defense with {self.name}")

    def freeze(self, oponent, enemy):
        pass

    def burn(self, oponent, enemy):
        pass


all_skills = []
