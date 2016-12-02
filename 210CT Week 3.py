
##function to reverse the words in a strings
def revWords(string):
    splitString = string.split()    #splits the string into a list
    #print(splitString)
    revLst = []
    revString = ""

    for reverse in splitString:     #inserts each word in the string as the first
        revLst.insert(0,reverse)
    #print(revLst)       

    for word in revLst:     #reconstructs the string
        revString  += word + " "
    return(revString)

##function to check whether a number is prime or not by dividing the number by all numbers below it
def isPrime(number,primeCheck = None):
    
    if number <= 1:  #special case 
        print(number, "is not a prime number")
        return False


    if primeCheck is None:          #assigns a number to the second parameter of the function
        primeCheck = number - 1     #this is the number that will be reduced with each recursve call to check if a number is prime
        
    while primeCheck >= 2:      #base case
        if number % primeCheck == 0:        #if the reminder of number divided by primeCheck is equal to 0, number isn't prime
            print (number, "is not a prime number")
            return False
        else:
            return isPrime(number, primeCheck-1)    #call the function again decreasing the primeCheck by 1
##    else:
    print (number, "is a prime number")
    return True


def removeVowels(string):   
    if string == "":
        return string
    elif string[0] in "aeiouAEIOU":         #checks the character which has index 0 if its a vowel, if true it calls the function again starting from the 
        return removeVowels(string[1:])     #next character
    return string[0] + removeVowels(string[1:])     #if the character at index 0 is not a vowel, it calls the function from the next character but adds the 
                                                    #one it was checking to the beginning of the string
        


print(revWords("This is awesome"))
print("\n-------\n")
print(revWords("Hello my name is Damian"))
print("\n-------\n")
print(revWords("I don't like Mondays"))
print("\n-------\n")
print(revWords("It's nearly Christmas!!!"))
print("\n-------\n")
print(isPrime(8))
print("\n-------\n")
print(isPrime(5))
print("\n-------\n")
print(isPrime(10))
print("\n-------\n")
print(isPrime(13))
print("\n-------\n")
print(isPrime(2))
print("\n-------\n")
print(isPrime(1))
print("\n-------\n")
print(removeVowels("beautiful"))
print("\n-------\n")
print(removeVowels("Damian"))
print("\n-------\n")
print(removeVowels("Games Technology"))
print("\n-------\n")
print(removeVowels(""))
