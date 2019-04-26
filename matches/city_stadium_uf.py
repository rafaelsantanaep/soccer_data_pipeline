from table_soup import table_soup
import re
from removing_characters import removing_characters

def getting_city_stadium_uf():
    soup_object = table_soup('city_stadium_uf')
    state_format = re.compile('.*-.*-\s(.*)')
    stadium_format = re.compile('^(.*)-')
    city_format = re.compile('-(.*)-')
        
    stadium = []
    city = []
    uf = []

    for i in soup_object:
        string = removing_characters(i)
        try:
            stadium.append(stadium_format.findall(string).pop())
            city.append(city_format.findall(string).pop())
            uf.append(state_format(string).pop())
        except:
            stadium.append('A definir')
            city.append('A definir')
            uf.append('A definir')

    print(stadium, 'stadium')

    return stadium, city, uf