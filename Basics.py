# Trying to work with data types

# Trying with numbers
import math
a = 4
math.sqrt(a)
math.sin(a)

b = 3.14
c = 3.67
round(b)
round(c)
math.floor(b)
math.floor(C)
math.cell(b)
math.cell(c)

# Trying with strings
a = 'hello'
print(a)
a.upper()
a = 'HELLO'
a.lower()
a = 'hello'
a.capitalize()
a.replace('l','a')

# Trying with list
a = 'learn.python.com'
a.split('.')

# Trying with formatting
a = 22
b = 'I am '
message = b + str(a)

a = 22
b = 1998
message = 'I am {}. I was born in {}.'.format(a,b)
message

#Trying with list
a = [1, 6, 8, 5, 2]
a[0]
a[2:4] #last symbol was not printed
a.append(99)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c.reverse()
c.sort()

# Trying with vocabulary
catalog_item = {
	"type":"phone",
	"vendor":"Apple"
}

catalog_item['audio_jack'] = False
print(catalog_item)
print(catalog_item['type'])

item_name = catalog_item['type'] + ' '+catalog_item['vendor']
print(item_name)
print(catalog_item.get('price'))
print(catalog_item.get('Discount','Скидок нет!'))
model in catalog_item
model not in catalog_item
del catalog_item['price']