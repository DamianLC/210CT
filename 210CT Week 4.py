##binary search function that searches for a value between two given points
def binarySearch(sequence, targetLow, targetHigh):
    first = 0       
    last = len(sequence) - 1 
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2 
        if targetLow <= sequence[midpoint] <= targetHigh: #if the midpoint is between the two given 
            found = True                                # points then the number is in the list
        else:
            if targetHigh < sequence[midpoint]:   #if the higher point is smaller than the midpoint
                last = midpoint - 1             #look in the left hand side of the list
            else:
                first = midpoint + 1        #if the higher point is bigger than the midpoint
    return found                            #look in the right hand side of the list

print(binarySearch([2,3,5,7,9,13,],10,14))

