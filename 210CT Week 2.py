import math

##function to find the highest perfect square which is less or equal to its parameter
def perfSquare(number):

    num = math.sqrt(number) 
    num = math.floor(num)       #rounds down num
    num = num**2
    return(num)

print(perfSquare(35))
print("\n-----------\n")
print(perfSquare(36))
print("\n-----------\n")
print(perfSquare(26))
print("\n-----------\n")










    


    
    
    
