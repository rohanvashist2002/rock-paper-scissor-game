# rock,paper, scissor
import random
def computer():
    while True:
     user_choice=input("Enter your choice in rock/paper/scissor:").lower()
     while user_choice not in ["rock", "paper", "scissor"]:
            user_choice = input("Invalid input. Enter your choice (rock/paper/scissor): ").lower()

     possible_choice=["rock","paper","scissor"]
     computer_choice=random.choice(possible_choice)
     print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

     if(user_choice==computer_choice):
         print(f"Both player choose same {user_choice} thing!! Match is tie!! ")
     elif(user_choice=="rock"):
       if (computer_choice=="paper"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU LOSE!!")
       elif(computer_choice=="scissor"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU WIN!!")
     elif(user_choice=="paper"):
       if (computer_choice=="rock"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU WIN!!")
       elif(computer_choice=="scissor"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU LOSE!!")
     elif(user_choice=="scissor"):
       if (computer_choice=="rock"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU LOSE!!")
       elif(computer_choice=="paper"):
         print(f"User choose {user_choice} and computer choose {computer_choice}..YOU WIN!!")

     play_again = input("Do you want to play again? (yes/no): ").lower()
     while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Do you want to play again? (yes/no): ").lower()

     if play_again != "yes":
      break

print("Welcome to the rock,paper,scissor game!!")
computer()



