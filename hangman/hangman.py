from string import ascii_lowercase
import random

def random_countries(file):
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num): continue
        line = aline
    return line

def new_game():
    try:
        with open("countries.txt") as f:
            country = random_countries(f)
            splitcountry = country.strip().lower().split("|")
            start_game(splitcountry[1])
    except IOError as error:
        print ("Sorry, I can't open the source file :'(")

def convertasterix(guess, countryname):
    glue = ""
    asterixfound = False
    for letter in countryname:
        if letter in guess:
            glue += letter
        elif (letter == " "):
            glue += " "
        else:
            asterixfound = True
            glue += "*"

    return [asterixfound, glue]

def start_game(countryname):
    print ("""
    Hello there, I want the play game. 
    I'll give to you a country name and you'll guess the country. You have only 3 guess and don't forget, you can exit from the game with -q.
     """)

    guess = []
    remainguess = 3

    while True:

        asterix = convertasterix(guess, countryname)

        print("Remain Guess: ", remainguess)
        print("Country Name: ", asterix[1])
        inp = input("Please write a letter or your guess: ").lower()
        guess.append(inp)

        if(countryname.find(inp) == -1):
            remainguess = remainguess - 1

        asterixagain = convertasterix(guess, countryname)

        if (inp == "-q"):
            print("You're leaving from game. Bye Bye! Country name was: ", countryname)
            break

        if(inp == countryname or asterixagain[0] == False):
            print("Congrat! You're guess was right!")
            break

        if(remainguess==0):
            print("You haven't any guess right. Bye Bye! Country name was: ", countryname)
            break

new_game()