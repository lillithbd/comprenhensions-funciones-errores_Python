#r+ permite leer y escribir el archivo, respetando lo que ya tiene
#r+ permite leer y escribir el archivo reemplazando todo el contenido
with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('\n nuevas cosas en este archivo \n')
  file.write('otra línea \n')

