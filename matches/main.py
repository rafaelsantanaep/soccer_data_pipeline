from date_and_time import getting_datetime
from teams_division import home_or_away_team
from city_stadium_uf import getting_city_stadium_uf
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    date, time = getting_datetime()
    home, away = home_or_away_team()
    stadium, city, uf = getting_city_stadium_uf()

    print(len(date), 'date')
    print(len(time), 'time')
    print(len(home), 'home')
    print(len(away), 'away')
    print(len(stadium), 'stadium')
    print(len(city), 'city')
    print(len(uf), 'uf')