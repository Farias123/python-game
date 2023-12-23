class Skill:
    def __init__(self, name, type, damage=None, de_buff_magnitude=None):
        self.name = name
        self.type = type
        self.damage = damage
        self.de_buff_magnitude = de_buff_magnitude

    def action(self):
        pass


all_skills = []
