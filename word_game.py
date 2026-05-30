import random
import os
import time

# Colors Adding.. (ANSI Code)- American National Standards Institute.
Red = "\033[91m"
Green = "\033[92m"
Yellow = "\033[93m"
Blue = "\033[94m"
Purple = "\033[95m"
Orange = "\033[38;5;208m" 
Cyan = "\033[96m"
Reset = "\033[0m"


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

words = ["anya","loid","thorn","ayanokoji","gojo","blue","tanha","jisoo", "jenni", "rose","lalisa","anthew","georgia","virginia","emily","victoria","shelley","rosaline","bruno","horikita","dualipa","ariana","beowulf","swift","ozana","shakira","kandal","tulip","damian"]
score = 0
playing = True

clear()
print("-"*44)   #First design
print(Blue,"~~~~~>...}Welcome To Our Word Game{...<~~~~~", Reset)
print("-"*44)


for i in range(1, 101):
    print(f"Loading... {i}%", end="\r", flush=True)
    time.sleep(0.04)
clear()


User_Name = input("Enter Your Name: ").capitalize()

print(Cyan,"The Game Is Starting...",Reset)
time.sleep(2)
clear()


while playing:
    word = random.choice(words)
    jumble = "".join(random.sample(word,len(word)))
    chances = 5     #How many time do you want to give them 
    time.sleep(1)
    print(Yellow,"\nThe Jumble Word Is:", jumble,Reset)

    while chances > 0:
        guess = input("\nEnter Your Word:").lower()

        if guess == word:
            score += 10
            print(Green,"\nCorrect Guess!!!",Reset)
            print(Purple,"You Win!!!*-*",Reset)
            break
        else:
            chances -= 1
            if chances > 0:
                print(Red,"\nIncorrect Guess!!!>-<",Reset)
                print(Orange,"\nYou Have Only",chances,"Chances!",Reset)
                print(Cyan,"\nTry Again!",Reset)
            else:
                print(Yellow,"\nAll your chances are gone!",Reset)
                print(Red,"\nYou Lost!!",Reset)
                print(Orange,"\nThe Correct Word is:", word,Reset)
    

    print("-" * 20)
    again = input("Do you want to play again?? {Yes/No}: ").lower()

    if again == "yes":
        print()
        playing = True
    else:
        playing =  False


clear()

print("~" * 26)
print(Purple," ~~ G A M E  O V E R!! ~~",Reset)
print()
print(Blue," Your Final Score Is- ", score,Reset)
print("~" * 26)

exit = input("\n Press Enter To Exit..")
time.sleep(0.01)
clear()

