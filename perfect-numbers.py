print ("Press 'x' to exit the program")

while True:

    number = input("Enter a number:")

    if (number == "x"):
        print("Goodbye...")
        break;

    if(number.isdigit()):
        number = int(number)
        f = 1
        total = 0
        while(f < number):
            if(number % f == 0):
                total += f
            f +=1

        if(total == number):
            print("{} is a perfect number".format(number))
        else:
            print("{} is not a perfect number".format(number))

    else:
        print("Please enter a number. '{}' isn't a number. ".format(number))