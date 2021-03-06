class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f"Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"
        for skill_name, skill_mana in self.skills.items():
            result += f"==={skill_name} - {skill_mana}\n"
        return result








