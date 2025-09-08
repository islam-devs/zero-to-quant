# import libraries
import random

# Subprograms
def my_part():
    print("We are going to play a game. I want you to pick a number then do" \
    "a series of calculations. I bet you know what the result of those calculations" \
    "will be!" )
    answer = random.randint(10,49)
    print(f"*You* This will be the answer. Select a number between 10-49: {answer}")
    factor = 99 - answer
    return answer, factor

def friend_part(answer, factor):

    friendGuess = int(input("*Player* Pick any number 50-99: "))
    factorAndfriendGuess = friendGuess + factor
    calcResult = friendGuess - ((factorAndfriendGuess % 100) + 1)
    print(f"I said the answer was {answer} and the calculation result is {calcResult}")

if __name__ == "__main__":
    answer, factor = my_part()
    friend_part(answer, factor)
