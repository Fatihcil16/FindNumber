import time # import time because generate a random number

min=0 # dont change that number because i didn't use random library i tried create a algorithm and it doesn't support minimum number yet


max=50 #my random will be between 0 and 50

def Random_Number(range):
    random=int(time.time()*1000) #time.time() function gives random values
                                 # i need milliseconds number that's why i multiplied by 1000
                                 #but it is in float thats why i convert to int
    random %= range # if i need the values from 0-range then we need to get the value less than range
    return random   #return random number from function

randomNumber=Random_Number(max)

while 1:#we create an infinite loop because our program needs to run until we find correct number
    userNumber=int(input("Please guess a number between {} and {} : ".format(min,max))) #we guess a number between max and min number
    if userNumber<=max and userNumber>=min:
        if userNumber==randomNumber:
            print("Congratulations! You guessed the number correctly. ")
            break
        elif userNumber<randomNumber:
            print("You guessed a number less than the correct number")
            min=userNumber
        else:#last opt will be usernumber>randomNumber thats why i used else but we could use elif
            print("You guessed a number larger than the correct number")
            max = userNumber
    else:
        print("Are you seriously why did not you try find correct number ?? \n")