import random
import time
class Player:
    def __init__(self, age, health):
        self.age = age
        self.health = health
    def deletehealth(self):
        self.health -= 10
class Enemy:
    def __init__(self, age, health):
        self.age = age
        self.health = health
    def deletehealth(self):
        self.health -= 10
player = Player(22, 200)
enemy = Enemy(34, 300,)

while player.health > 0 or enemy.health > 0:
    print(f"Your health: {player.health} Enemy's health: {enemy.health}")
    input("Ready?")
    print("Let's see who's turn is it.....")
    time.sleep(1.2)
    turn = random.choice(["Your turn!", "Enemy's turn!"])
    print(turn)
    time.sleep(0.8)
    if turn == "Enemy's turn!":
        print("Ready.........")
        time.sleep(1)
        deal_damage = random.randint(1, 2)
        if deal_damage == 2:
            player.deletehealth()
            print("OUCH!")
        else:
            print("Enemy missed!")
    elif turn == "Your turn!":
        print("Ready....")
        time.sleep(1)
        deal_damage = random.randint(1, 2)
        if deal_damage == 1:
            enemy.deletehealth()
            print('Enemy got hit!')
        else:
            print("You missed!")
    else:
        print("what")
if player.health > 0:
    print("gg")
elif enemy.health > 0:
    print("ouch")