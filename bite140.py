import pandas as pd

data = "http://projects.bobbelderbos.com/data/summer.csv"


def athletes_most_medals():
    table = pd.read_csv(data)
    data_men = table.loc[table.Gender == 'Men']
    data_women = table.loc[table.Gender == 'Women']
    men = data_men.groupby('Athlete', as_index=False).agg('count').sort_values(by='Medal', ascending=False).iloc[0][
        'Athlete']
    men_medal = \
    data_men.groupby('Athlete', as_index=False).agg('count').sort_values(by='Medal', ascending=False).iloc[0]['Medal']
    women = data_women.groupby('Athlete', as_index=False).agg('count').sort_values(by='Medal', ascending=False).iloc[0][
        'Athlete']
    women_medal = \
    data_women.groupby('Athlete', as_index=False).agg('count').sort_values(by='Medal', ascending=False).iloc[0]['Medal']
    return {men: men_medal, women: women_medal}
print(athletes_most_medals())

ret = athletes_most_medals()

larisa = "LATYNINA, Larisa"
michael = "PHELPS, Michael"

assert larisa in ret
assert ret[larisa] == 18

assert michael in ret
assert ret[michael] == 22