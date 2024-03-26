
#iteracion sencilla
for i in range(1, 11):
  print(i)

#para manejar la iteración manualmente sin necesidad del for
my_iter = iter(range(1,4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#hay que tener en cuenta hasta que punto se debe iterar manualmente para evitar el error de StopIteration