while True:

    number = input("Enter a number: ")

    if(number=="x"):
        print ("Goodbye...")
        break;

    if(number.isdigit()):
        number = int(number)
        f = 1;
        for i in range(2,number+1):
            f *= i
        print ("Factorial: ", f)

    else:
        print ("Please enter a number. '{}' isn't a number. ".format(number))