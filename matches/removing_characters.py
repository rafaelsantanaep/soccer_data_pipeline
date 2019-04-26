def removing_characters(soup):
    string = str(soup.text).lower() \
    .replace('detalhes do jogo', '') \
    .replace('\n', '') \
    .replace('\r', '') \
    .strip()
    return string