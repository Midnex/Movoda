# calculates items/spells needed to reach min timer www.movoda.net


def f(x,y,z):
	print('Items/Spells: ' + str(int(( y - x ) / z)))
	
x = int(input(' Min: '))
y = int(input(' Current : '))
z = int(input(' Reducer: '))

f(x,y,z)
