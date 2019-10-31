from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    data = data.split('\n')[1:]
    for piece in data:
        piece = piece.split(',')
        if piece[-1] not in countries.keys():
            countries[piece[-1]] = [' '.join(piece[:-1][::-1])]
        else:
            countries[piece[-1]].append(' '.join(piece[:-1][::-1]))
    return countries


print(group_names_by_country())