a = True
b = False

print('1)', a and b)
print('2)', (a and b) or b)
print('3)', (a and b) or not(a and b))
print('4)', a and b or not (a or b) or b)
print('5)', b and b or not a and (a or b or a) or not (a or b))
print('6)', 1 << 2)
print('7)', 1 & 0 | 1 >> 1)
print('8)', 1 & 0 | 1 >> 0)
print('9)', 0b101 & 0b111 ^ 0b111 | 0b010)

