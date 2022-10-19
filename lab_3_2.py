list = []
a = int(input('Введите число элементов в списке'))
for number in range(a):
	number = int(input())
	list.append(number)
def nul(l):
	result = list.count(0)
	return(result)
print(nul(list))


