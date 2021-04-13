x = int(str(float(5)))
#set

#2
x = 'aa' == 'AA'
#Bool

#3
x = {i: i**2 for i in range(5)}
# dict

#4
x = set(list((5, 6, 7)))
#set

#5
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
#NoneType

#6
x = [].append('j')
#list
#7
for i in range(10):
		if i < 5:
				x = 'hello'
		else:
				x = 5
#Int

#8
x = input('Enter and integer: ')
# STR

#9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
#list

#10
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter')
#str
