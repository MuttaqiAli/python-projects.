# python project2.py
import random
n= random.randint(1,100)
a=-1
guesses=0
print("you have to choose a number between 1 to 100. select the dificulty level EASY or MEDIUM or HARD")
dificulty= input("Enter the dificulty: ")
if (dificulty == "easy"):
    max_guesses=10
    print("you have 10 tries")

elif (dificulty == "medium"):
    max_guesses=7
    print("you have 7 tries")

elif (dificulty == "hard"):
    max_guesses=5
    print("you have 5 tries")

else:
    print("user input is unmatched defult dificulty medium is selected")
    max_guesses=7
    print("you have 7 tries")

while( a!=n  and max_guesses >= guesses):
    a=int(input("Enter the number: "))
    if(a>n):
        print(f"too High!  decrease the guessed number\n. you have {max_guesses-guesses} tries left")
        guesses += 1
    
    elif(a<n):
        print(f"too low!  increse the guessed number\n . you have {max_guesses-guesses} tries left")
        guesses += 1

    elif(a==n):
        print(f"congatulations! \n you guessed number {n} correctly in {guesses} guesses")
    else:
        print(f"the number is {n}. Better luck next time!")

