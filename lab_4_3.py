k = int(input('Введите количество случайных элементов списка\n'))

from random import randint
A = [0]*k
for i in range(k):
	A[i] = randint(1, 20)
print(A)

def func_3(L):
	B = []
	max = 0
	min = 100
	for j in range(k):
		if L[j] > max:
			max = L[j]
			j_max = j

	for j in range(k):
		if L[j] < min:
			min = L[j]
			j_min = j
	A[j_max] = min
	A[j_min] = max
	
	return(print(L))
	
func_3(A)
	
	
	
	
