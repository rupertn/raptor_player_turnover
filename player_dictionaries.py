import pandas as pd

df = pd.read_csv('data/roster_clean.csv')

nicknames = dict(zip(df.initials.str.lower(), df.name.str.lower()))

nicknames['kuz'] = 'kyle kuzma'
nicknames['bron'] = 'lebron james'
nicknames['lbj'] = 'lebron james'
nicknames['zu'] = 'ivica zubac'
nicknames['zo'] = 'lonzo ball'
nicknames['wes'] = 'wesley matthews'
nicknames['kief'] = 'markieff morris'
nicknames['kieff'] = 'markieff morris'

del nicknames['am']
del nicknames['it']
del nicknames['js']

# TODO: deal with JR abbreviation
# TODO: fix ennis and dennis problem

first_to_full = dict(zip(df.first_name.str.lower(), df.name.str.lower()))

del first_to_full['talen']
del first_to_full['jordan']

last_to_full = dict(zip(df.last_name.str.lower(), df.name.str.lower()))

del last_to_full['bryant']
del last_to_full['cook']
del last_to_full['wear']
del last_to_full['ball']
del last_to_full['hart']