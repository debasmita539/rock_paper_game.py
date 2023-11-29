import random

rock='''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''

---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissor]
user_choice=int(input("what do you want to choose?0 for rock 1 for paper 2 for scissor"))
print(game_images[user_choice])
computer_choice=random.randint(0,2)

print(f"computer choice:")
print(game_images[computer_choice])
if(user_choice==0 and computer_choice==2):
    print("you win")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice < computer_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")

elif user_choice==computer_choice:
    print("it's a draw")
else:
    print("enter invalid ,you lose")


