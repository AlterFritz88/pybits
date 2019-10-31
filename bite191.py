data = """Luke Skywalker,172,77
          C-3PO,167,75
          R2-D2,96,32
          Darth Vader,202,136
          Leia Organa,150,49
          Owen Lars,178,120
          Beru Whitesun lars,165,75
          R5-D4,97,32
          Biggs Darklighter,183,84
          Obi-Wan Kenobi,182,77
          Anakin Skywalker,188,84
          Chewbacca,228,112
          Han Solo,180,80
          Greedo,173,74
          Jek Tono Porkins,180,110
          Yoda,66,17
          Palpatine,170,75
          Boba Fett,183,78.2
          IG-88,200,140
          Bossk,190,113
"""


def person_max_bmi(data=data):
    """Return (name, BMI float) of the character in data that
       has the highest BMI"""
    high = ('none', 0)
    for row in data.strip().split('\n'):
        height, mass = row.split(',')[1], row.split(',')[2]
        if float(mass) / ((int(height) / 100) ** 2) > high[1]:
            high = (row.strip().split(',')[0], round(float(mass) / ((int(height) / 100) ** 2), 2))
    return high

print(person_max_bmi())