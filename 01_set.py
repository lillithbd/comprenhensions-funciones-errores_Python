#texto
set_countries = {'col','mex','bol', 'col'}
print(set_countries)
print(type(set_countries))

#números 
set_numbers = {1,2,2,443,23}
print(set_numbers)

#varios tipos de datos
set_types = {1, 'hola', False, 12.12}
print(set_types)

#crear conjuntos a partir de otro elemento
set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = (('abc', 'obj', 'as', 'cbv'))
print(set_from_tuples)

numbers = [1,2,3,4,5,6,1,2]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
