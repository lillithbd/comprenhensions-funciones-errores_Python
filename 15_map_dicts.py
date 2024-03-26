items = [
  {
    'product' : 'camisa',
    'price': 100
  },
  {
    'product' : 'pantalones',
    'price': 300
  },
  {
    'product' : 'pantalones 2',
    'price': 200
  }
]

#Obtener sólo las listas
prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

#agregar un atributo nuevo a items
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item
#al modificar un atributo el estado original se ajusta (esto puede ser un problema)
new_items = list(map(add_taxes, items))
print(new_items)
print(items)
