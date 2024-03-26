'''
#una de las formas de hacer la importación
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

'''
#buena práctica para hacer importaciones
#crear un namespace y allí declarar lo necesario y aquí solamente se llama solamente a la funcion
import pkg
print(pkg.URL)
print(pkg.mod_1.func_1())


