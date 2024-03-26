set_countries = {'col','mex','bol', 'col'}

#tamaño
size = len(set_countries)
print(size)

#validar si existe dentro de un conjunto
print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

set_countries.add('pe')
print(set_countries)

#actualizar 
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

#intentar borrar un valor que no existe (genera error)
#set_countries.remove('arg')
#print(set_countries)

set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

#limpiar todo el conjuntop
set_countries.clear()
print(len(set_countries))