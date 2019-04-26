from bs4 import BeautifulSoup
import requests


def table_soup(information):
    """
    This function will return the soup objects demanded to get information
    about the matches.

    Information can take three values:
    - "abbreviations"
    - "datetime_stadium"

    ** abbreviations **:
    If the value abbreviation is passed, it will return all the teams in all matches.
    Where each even index will be the home team and the even indexes will be the away team.

    ** datetime **:
    If the value "datetime_stadium" is passed, it will return an object that contains the
    values for the datetime of the match and where the game will take place. 
    The odd indexes represent the datetime and the even indexes represent the stadium and city.
    """
    # getting the html page from cbf webiste
    r = requests.get('https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019')
    
    # parsing with beautiful soup
    soup = BeautifulSoup(r.content, 'html.parser')


    # getting the whole table
    table = soup.find(attrs={'class':'aside-rodadas swiper-container'})
    
    if information == 'abbreviations':
        return table.find_all(attrs={'class':'time-sigla'})
    elif information == 'date and time':
        return table.find_all(attrs={'class':'partida-desc text-1 color-lightgray p-b-15 block uppercase text-center'})
    elif information == 'city_stadium_uf':
        return table.find_all(attrs={'class':'partida-desc text-1 color-lightgray block uppercase text-center'})
    else:
        print('nothing')