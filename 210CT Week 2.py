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



Task 3 - Pseudocode

MATRIXADD(A,B)
	
	result <- list
	rowA <- length(A)
	colA <- length(A[0])
	rowB <- length(B)
	colB <- length(B[0])

	if rowA ≠ rowB
		RETURN false
	
	if colA ≠ colB
		RETURN false

	for i  to range[rowA]
		row <- empty list
		for j to range[colA]
			row <- append A[i][j] + B[i][j]
	result <- append(row)
	RETURN result

MATRIXSUB(A,B)
	
	result <- list
	rowA <- length(A)
	colA <- length(A[0])

	if rowA ≠ rowB
		RETURN false
	
	if colA ≠ colB
		RETURN false


	for i  to range[rowA]
		row <- empty list
		for j to range[colA]
			row <- append A[i][j] - B[i][j]
	result <- append(row)
	RETURN result

MATRIXMULT(A,B)

	 
rowA <- length(A)
	colA <- length(A[0])
rowB <- length(B)
	colB <- length(B[0])

	if colA ≠ rowB
		RETURN false

	result <- list

	for i  to range[rowA]
		for j to range[cola]
			for k to range[rowB]
				result[i][j] += a[i][k] * b[k][j]
	RETURN result

MATRIXFACTORMULT(A,B)

	result <- list
	
	rowA <- length(A)
	colA <- length(A[0])

	for i to range(rowA)
		row <- list
		for j to range(cola)
			row <- append A[i][j] * b
		result <-append(row)
	RETRUN result

A = B*C – 2*(B+C)
A1 <- MATRIXMULT(B,C)
A2 <- MATRIXADD(B,C)
A3 <- MATRIXFACTORMULT(A2,2)
A <- A1 – A3







    


    
    
    
