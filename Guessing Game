import random
 
#Variables for the code
password = []
guess = []
 
firstNumber = 0
secondNumber = 0
count = 0
slots = 0
correct = 0
score = 0
 
#This defines player's input
def player_input():
   guess.append(int(input("Your turn. Guess the password: ")))
 
 
print(
   "Hello, welcome to the guessing game. The rules to the game are simple.                                                          "
)
 
print(
   "To win the game you have to guess a password. The code will be four numbers that ranges from 1 to 10. A players score will be counted when they guess the password. The player wins if they guess in under 15 guesses, but you may still guess until you get it right                                                                                "
)
 
#While the variable firstNumber is less then 4, the program will pick random intergers from 1 to 10 for the password. Code made by my collaborator
 
while (firstNumber < 4):
   password.append(random.randint(1, 10))
   firstNumber = firstNumber + 1
 
 
while (correct != 4):
   correct = 0
   slots = 0
   secondNumber = 0
 
   while (secondNumber < 4):
       player_input()
       secondNumber = secondNumber + 1
 
   while (slots < 4):
       if (guess[slots] == password[slots]):
           correct = correct + 1
           slots = slots + 1
       else:
           slots = slots + 1
 
   guess.clear()
 
   print(("You guessed ") + str(correct) + (
       " correct numbers in this attempt.                                                                                                   "
   ))
   count = count + 1
 
#Code to let player know they have lost was made by my collaborator
   if (correct == 4):
       if (count > 14):
           print(
               "Good try, but you have exceeded 15 guesses. You have lost the game.                                            "
           )
 
print(("Congratulations on getting them right. It took you ") + str(count) +
     (" tries."))
