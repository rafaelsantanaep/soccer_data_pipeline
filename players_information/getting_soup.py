from bs4 import BeautifulSoup
def getting_soup(soup, index, identifier_one, identifier_two):
    return soup.find_all(attrs=identifier_one)[index].find_all(attrs=identifier_two)