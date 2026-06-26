# Welcome back! This is Mercina v1.1!
# (And yes, I'm now formal using caps)
# Let's get started. Same libraries (tho I'm thinking about adding TTS)

import random
import time

# Creating the Player Class (but it also works for enemies)
class Player:
    def __init__(self, age, health):
        self.age = age
        self.health = health
    # And I have updated the 'deletehealth' function but now it's 'take_health'
    def take_health(self, attack_type):
        if attack_type == "high_acc":
            self.health -= 30
            print("It hits!")
        elif attack_type == "low_acc":
            self.health -= 70
            print("IT'S A CRITICAL HIT!")

# Now let's create both the player and enemy

player = Player(22, 200)
enemy = Player(34, 300)


# The game loop, obviously.

while True:

    # This is the turn system, using the amazing 'random' library


    print(f"Your health: {player.health} Enemy's health: {enemy.health}")
    input("Ready? ")
    print("Let's see who's turn is it.....")
    time.sleep(1.2)
    turn = random.choice(["Your turn!", "Enemy's turn!"])
    print(turn)
    time.sleep(0.8)

    # Now this is the Enemy's turn system.
    # I've updated this quite a lot so check it out.
    # First off, we have a variable 'choice'.
    # You need to understand there are two 'attack_type' values possible:
    # A 'high_acc' attack or a 'low_acc' attack or high_accuracy and low_accuracy
    # However, if 'choice' is above 70, it will choose between healing and a high_accuracy attack
    # Using the sub_choice variable.


    if turn == "Enemy's turn!":
        print("What will the enemy choose?")
        choice = random.randint(1, 100)
        time.sleep(2)
        if choice <= 70:
            print("He chose a high accuracy attack!")
            player.take_health("high_acc")
            time.sleep(2)
            print(f"Your health: {player.health}")
        elif choice > 70:
            sub_choice = random.randint(1, 7)
            if sub_choice < 5:
                print("He chose to heal!")
                enemy.health += 20
                time.sleep(1)
                print(f"He has healed! His health: {enemy.health}")
                time.sleep(2)
            else:
                print("He chose a low accuracy attack!")
                time.sleep(2)
                player.take_health("low_acc")
                time.sleep(1)
                print(f"Your health: {player.health}")


    # Here, I've added an interactive menu with the three options:
    # High accuracy, low damage attack
    # Low accuracy, high damage attack
    # Or healing. You can choose all three of course. Healing is always possible.
    elif turn == "Your turn!":
        while True:
             print("""YOUR OPTIONS:
                1. Low Damage, High Accuracy Attack
                2. High Damage, Low Accuracy Attack
                3. Heal""")
             option = int(input("Choose an option."))
             if option == 1:
                print("Will it hit? Let's find out.....")
                time.sleep(2)
                deal_damage = random.randint(1, 100)
                if deal_damage < 90:
                    enemy.take_health("high_acc")
                    break
                else:
                    print("No! It missed!")
                    break
             elif option == 2:
                print("Will it hit? Let's find out....")
                time.sleep(2)
                deal_damage = random.randint(1, 100)
                if deal_damage < 30:
                    enemy.take_health("low_acc")
                    break
                else:
                    print("Nope! Didn't hit.")
                    break
             elif option == 3:
                player.health += 20
                time.sleep(2)
                print(f"You've healed! Current health: {player.health}")
                break
    # And here's a simple checking system to determine who's the winner.

    if player.health > 0 and enemy.health <= 0:
        print("Congrats! You've won.")
        break
    elif enemy.health > 0 and player.health <= 0:
        print("You've lost!")
        break

# If you're here, I appreciate you taking the time to reading my code.
# Thank you and I'll see you in Mercina v1.2!


