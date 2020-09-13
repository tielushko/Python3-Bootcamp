class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        self.battery = battery
        self.skills = skills
    
    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery >= 0:
            self.battery -= 1
            return f"BEEP BEEP BOOP BOOP. I am {self.name.upper()}"
        return f"ERROR! Not enough charge to perform the operation. Please charge!"

    def learn_new_skill(self, cost, skill):
        if self.battery >= cost: 
            self.skills.append(skill)
            self.battery -= cost
            return f"WOAH! I just learnt how to {skill.upper()}"
        return "ERROR! Not enough charge to perform the operation. Please charge!"