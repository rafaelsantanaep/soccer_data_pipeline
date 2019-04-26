def parsing_money(string):
    if 'M €\xa0\xa0' in string:
        string = string.replace('M €\xa0\xa0', '').strip()
        string = string.replace(',', '.')

    else:
        string = string.replace('mil €\xa0\xa0', '').strip()
        try:
            string = float(string) / 1000
        except:
            pass

    return string