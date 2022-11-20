list = []
k = int(input('Введите количество элементов\n'))
for n in range(1,k + 1):
	list.append(n)
print(list)

def func_1(l):
	list_new = []
	for num in l:
		if l.index(num) % 2 != 0:
			list_new.append(num)
	return(print(list_new))		
			
		
func_1(list)
