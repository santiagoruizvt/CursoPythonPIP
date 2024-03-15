import charts
import read_csv


def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def get_country_data(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  return result

def get_population_by_country(data):
  new_country_data = dict(filter(lambda item: 'Population' in item[0] and 'Percentage' not in item[0],data[0].items()))
  for key, value in new_country_data.items():
    new_country_data[key] = int(value)
    
  return new_country_data


if __name__ == '__main__':
  data = read_csv.read_csv('./app/data.csv')
  country = str(input("Ingrese un pais -->"))
  country_info= get_country_data(data,country)
  #print(country_info)
  population_by_country = get_population_by_country(country_info)
  print(population_by_country)
  labels = population_by_country.keys()
  values = population_by_country.values()
  charts.generate_bar_chart(labels,values)
  

