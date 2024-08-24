name = 'products.txt'

file = open(name, 'r')

print(file)

print(file.read())

file.close()

print(file.read())