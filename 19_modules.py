#conocer la ruta de ubicación del archivo
import sys
print(sys.path)

#expresiones regulares
import re
text = 'Mi número de teléfono es 456123444, el código del país es 57, mi número de la suerte es el 7'
result = re.findall('[0-9]+', text)
print(result)

#manejo de horas y fechas
import time
timestamp = time.time()

#formato unix
local = time.localtime()

#formato normal
result = time.asctime(local)
print(timestamp)
print(local)

#utilidad para manejar listas
import collections
numbers = [1,1,1,1,2,4,5,4,3,3,5,21]
counter = collections.Counter(numbers)
print(counter)

