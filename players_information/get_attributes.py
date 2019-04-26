def get_attributes(soup_data, player_data):
    import re
    
    pattern = pattern = re.compile('\sid="(\w*)"\s')
    
    shirt_number = soup_data[0].text
    birth_age = str(soup_data[1].text)
    birth, age = birth_age.split(' ')
    age = int(age.replace('(', '').replace(')',''))
    height = soup_data[3].text
    height = str(height).replace(',', '').replace('m', '').strip()


    feet = soup_data[4].text
    joined_in = soup_data[5].text
    contract_until = soup_data[7].text
    name = player_data[0].text
    id_ = pattern.findall(str(player_data)).pop()
    
    
    return {'id': id_,
            'name': name,
            'shirt_number': shirt_number, 
            'birthday': birth,
           'age': age, 
            'height': height, 
            'feet': feet,
           'joined_in': joined_in, 
            'contract_until': contract_until}