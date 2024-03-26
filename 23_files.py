file = open('./text.txt')
#leer archivo completo
#print(file.read())

#leer archivo línea a línea
#print(file.readline())
#print(file.readline())
#print(file.readline())

#iterar archivo con for
for line in file:
  print(line)
  

file.close()

#opción de abrir archivo automáticamente sin necesidad de decirle hasta cuando abrirlo. No hay necesidad de cerrar el archivo
with open('./text.txt') as file:
  for line in file:
    print(line)

