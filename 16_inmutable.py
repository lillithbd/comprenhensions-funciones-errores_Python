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

#con esto copiamos la lista original para trabajarla en una nueva variable
def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('New List')
print(new_items)
print('Old List')
print(items)

#Al trabajar con un diccionario hay referencia en memoria