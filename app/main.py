import utils
import read_csv
import charts
'''
data = [
    {
      'Country': 'Colombia',
      'Population': 300
    },
    {
      'Country': 'Bolivia',
      'Population': 300
    }  
  ]
'''

'''
def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input('Type Country ==> ')
  
  result = utils.poputation_by_country(data, 'Colombia')
  print(result)

#este if hace que si el modulo main es llamado  desde la terminal se ejecuta el método run por defecto
if __name__ == '__main__':
  run()
'''

'''
def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country ==> ')
  result = utils.poputation_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
    

#este if hace que si el modulo main es llamado  desde la terminal se ejecuta el método run por defecto
if __name__ == '__main__':
  run()
'''

def run():
  data = read_csv.read_csv('./app/data.csv')
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
#este if hace que si el modulo main es llamado  desde la terminal se ejecuta el método run por defecto
if __name__ == '__main__':
  run()