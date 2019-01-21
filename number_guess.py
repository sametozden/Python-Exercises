import random

print("""

Make a prediction between 1 and 1000

Remaining predictions: 10
""")


randnumber = random.randint(1,1000)
remain_prediction = 10

while True:

    prediction = int(input("Your prediction:"))

    if(prediction == randnumber):
        print("Congratulations, your prediction is right. Number is", randnumber)
        break
    elif(prediction < randnumber):
        print("Wrong prediction. Try a bigger number.")
        remain_prediction -= 1

    elif(prediction > randnumber):
        print("Wrong prediction. Try a smaller number.")
        remain_prediction -= 1

    if(remain_prediction == 0):
        print("Sorry, you have not prediction right")
        break