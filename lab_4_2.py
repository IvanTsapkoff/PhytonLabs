k = int(input('Введите число элементов\n'))

from random import randint
A = [0]*k
for i in range(k):
	A[i] = randint(1,9)
print(A)

def func_2(L):
	B = []
	for j in range(1, k - 1):
		if L[j] > L[j-1]:
			B.append(L[j])
	return(print(B))
	
func_2(A)
