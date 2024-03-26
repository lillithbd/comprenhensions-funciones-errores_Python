#asignacion de valores de argumentos por defecto
def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result = find_volume()

print(result)

#enviar un valor de parámetro determinado

result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)
