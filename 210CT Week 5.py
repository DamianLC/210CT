##function to find the longest sub sequence in ascending order
def longestSubSequence(n):

    longestSeqFound = []
    currentSeq = []

    for i in range(len(n)):

        if i < len(n)-1 and n[i] < n[i+1]: #if the index which i is currently on is smaller than the length of the sequence 
            currentSeq.append(n[i])        #and the number is smaller than next one it will append that number to the list
            #print(currentSeq)
            

        else:               #appends the number to the list if the conditions of the if statement aren't met 
            currentSeq.append(n[i])         #last number of the current sequence
            #print(currentSeq)

            if len(currentSeq) > len(longestSeqFound):  #compares the length of sequences to check which one is bigger
                longestSeqFound = currentSeq            
                #print(longestSeqFound)

            currentSeq = []     #clears the list so the new sequence can be placed here and compared to the longest one

    return(longestSeqFound)
    
print(longestSubSequence([1,2,3,4,1,6,1,7,8,1,2,3,4,5,6,7]))









        



