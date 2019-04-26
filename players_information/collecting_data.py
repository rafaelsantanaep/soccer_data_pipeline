from get_attributes import get_attributes
from parsing_money import parsing_money
from getting_soup import getting_soup
from bs4 import BeautifulSoup
import requests
from urls import urls
from time import sleep
import pandas as pd
import os

def collecting_data(team_urls, day):
    attributes = []
    for url in team_urls:
        print('parsing:', url)
        r = requests.get(url, headers={'User-Agent': 'Custom'})
        soup = BeautifulSoup(r.content)
        
        length_odd = len(soup.find_all(attrs={'class':'even'}))
        length_even = len(soup.find_all(attrs={'class':'odd'}))
        
        team_name = str(soup.find('h1').text).replace('\n', '')
        
        def getting_soup(soup, index, identifier_one, identifier_two):
            return soup.find_all(attrs=identifier_one)[index].find_all(attrs=identifier_two)

        for i, j in zip(range(length_odd), range(length_even)):
            # attributes of the players with class = odd
            odd_attributes = getting_soup(soup, i, 
                                        {'class':'odd'},{'class':'zentriert'})

            # attributes of the players with class = even
            even_attributes = getting_soup(soup, j, 
                                        {'class':'even'},
                                        {'class':'zentriert'})

            # name and id of the players with class = odd
            player_odd = getting_soup(soup, i, 
                                    {'class':'odd'},
                                    {'class': 'spielprofil_tooltip'})

            # name and id of the players with class = even
            player_even = getting_soup(soup, j, 
                                    {'class':'even'},
                                    {'class':'spielprofil_tooltip'})

            # market value
            mkt_odd = str(soup.find_all(attrs={'class':'odd'})[i].find_all(attrs={'class': 'rechts hauptlink'})[0].text)
            mkt_odd = parsing_money(mkt_odd)

            odd = get_attributes(soup_data=odd_attributes, player_data=player_odd)
            odd['market_value'] = mkt_odd
            odd['team_name'] = team_name
            odd['collection_day'] = day

            attributes.append(odd)

            mkt_even = str(soup.find_all(attrs={'class':'even'})[j].find_all(attrs={'class': 'rechts hauptlink'})[0].text)
            mkt_even = parsing_money(mkt_even)
            even = get_attributes(soup_data=even_attributes, player_data=player_even)
            even['market_value'] = mkt_even
            even['team_name'] = team_name
            even['collection_day'] = day

            attributes.append(even)
        
        sleep(0.333)

    return attributes

if __name__ == "__main__":
    from time import gmtime, strftime
    day = strftime("%Y-%m-%d", gmtime()) 
    data = pd.DataFrame(collecting_data(urls, day))

    columns = ['contract_until','feet','joined_in','market_value','shirt_number']
    
    for i in columns:
        data[i] = data[i].map(str).str.replace('-', '')

    data['collection_day'] = data['collection_day'].str.replace('-', '/')
    
    os.chdir('/home/rafael/Documents/soccer/data')
    filename =  '/home/rafael/Documents/soccer/data/' + '{}.csv'.format(day)
    print(data.head())
    data.to_csv(path_or_buf=filename, index=False)

