from table_soup import table_soup


def home_or_away_team():
    """
    This function will iterate over the soup object.

    If the index is odd, it will place the value inside the home_team list.
    On the other hand, if the value is odd, the value will be placed at the
    away_team list.
    
    """
    abbreviations = table_soup('abbreviations')
    teams_home = []
    teams_away = []

    for i in range(0, len(abbreviations), 2):
        teams_home.append(abbreviations[i].text)
    
    for i in range(1, (len(abbreviations) - 1), 2):
        teams_away.append(abbreviations[i].text)

    return teams_home, teams_away