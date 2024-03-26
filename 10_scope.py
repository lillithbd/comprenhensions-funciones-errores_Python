price = 100 #variable global

def increment():
  price = 200
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
#print(result) #no funcionaria porque sólo está definido en la funcion