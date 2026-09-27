# ask the user a number between 1 and 100
# take in the number and check if it is valid
# if its it valid generate a random number. if its not valid ask the user to input a number again
# if the number is lower than the random number, say too low
# if the number is higher than the random number, say too high
# kepp on asking the user to input a number until they guess the correct number
import random
from unittest import result


def check_guessed_number(generatedNum, guessNum): 
        
        if generatedNum == guessNum:
            return True
        elif guessNum < generatedNum:
            print("Your guess is too low. Try again.")
            return False
        elif guessNum > generatedNum:
            print("Your guess is too high. Try again.")
            return False
        else:  
            print("Invalid input. Please enter a number between 1 and 100.")
            int(input("Choose a number between 1 - 100! ")) 

        return False

#MAIN

generatedNum = random.randint(1, 100)
print("Welcome to the number guessing game!")

while True:
    guessNum = input("Choose a number between 1 - 100! ")
    try:
        guessNum = int(guessNum)
        if guessNum < 1 or guessNum > 100:
            print("Please enter a number between 1 and 100.")
            continue
        else:
            result = check_guessed_number(generatedNum, guessNum)
            if result == True:
                print("Congratulations! You guessed the correct number.")
                break   
    except ValueError:
        print("Please enter a valid integer.")
        continue









        
