from table_soup import table_soup
import re
from removing_characters import removing_characters

def getting_datetime():
    soup_object = table_soup('date and time')

    date_format = re.compile('\w*,\s(\d{2}\/\d{2}\/\d{4})')
    time_format = re.compile('\d{2}:\d{2}')

    date = []
    time = []

    for i in soup_object:
        string = removing_characters(i)
        try:
            date.append(date_format.findall(string).pop())
            time.append(time_format.findall(string).pop())
        except:
            date.append('')
            time.append('')

    return date, time