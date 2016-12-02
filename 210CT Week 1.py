import random

##function to randomly shuffle a list of numbers
def randShuffle(n):
 
    shuffledLst = []                        #empty list 
    
    while len(n) > 0:
        randNum = random.choice(n)          #picks a random number 
        shuffledLst.append(randNum)         #adds the number to the list
        n.remove(randNum)                   #removes the number from the orignal list
    return(shuffledLst)


##function to count the amount of trailing 0s in a factorial number
def factorialZeros(number):

    zeroCount = 0           #counter for the trailing 0s
    factorialNum = 1            #start of the factorial caluclation
    revFactorial = []

    for i in range(1,number+1):             #iterates through each number of the user input to calculate the factorial
        factorialNum = factorialNum * i


    for reverse in str(factorialNum):           #reverses the factorial by placing each integer at the beginning
        revFactorial.insert(0, reverse)

    for zeros in revFactorial:          #counts the amount of zeros in a factorial until it reaches a number that isn't a zero
        if zeros == "0":
            zeroCount += 1
        else:
            break
    return(zeroCount)

print(randShuffle([5,3,8,6,1,9,2,7]))
print("\n-----------------\n")
print(factorialZeros(10))
print("\n-----------------\n")
print(factorialZeros(5))
print("\n-----------------\n")
print(factorialZeros(1))
print("\n-----------------\n")
print(factorialZeros(0))
print("\n-----------------\n")
print(factorialZeros(-2))







        


        





