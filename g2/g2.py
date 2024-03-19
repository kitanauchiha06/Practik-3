import random
import time 

class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def follow_hero(self, hero):
        print(f"Soldier {self.number} is following Hero {hero.number}")

class Hero:
    def __init__(self, number):
        self.number = number
        self.level = 1

    def increase_level(self):
        self.level += 1

hero1 = Hero(1)
hero2 = Hero(2)

soldiers_team1 = []
soldiers_team2 = []

for i in range(10):
    soldier = Soldier(i+1, random.choice([1, 2]))
    if soldier.team == 1:
        soldiers_team1.append(soldier)
    else:
        soldiers_team2.append(soldier)

if len(soldiers_team1) > len(soldiers_team2):
    hero1.increase_level()
else:
    hero2.increase_level()

print("Number of soldiers in Team 1:", len(soldiers_team1))
print("Number of soldiers in Team 2:", len(soldiers_team2))

time.sleep (2)

hero1_soldier = random.choice(soldiers_team1)
hero1_soldier.follow_hero(hero1)

print(f"Hero {hero1.number} and Soldier {hero1_soldier.number}")

