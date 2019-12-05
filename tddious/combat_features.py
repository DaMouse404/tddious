import pandas
import numpy

type_advantages = {
  'Grass': ['Ground', 'Rock', 'Water'],
  'Fire': ['Bug', 'Steel', 'Grass', 'Ice'],
  'Water': ['Ground', 'Rock', 'Fire'],
  'Bug': ['Grass', 'Psychic', 'Dark'],
  'Normal' : [''],
  'Poison': ['Grass', 'Fairy'],
  'Electric': ['Flying', 'Water'],
  'Ground': ['Poison', 'Rock', 'Steel', 'Fire', 'Electric'],
  'Fairy': ['Fighting', 'Dragon', 'Dark'],
  'Fighting' : ['Normal', 'Rock', 'Steel', 'Ice', 'Dark'],
  'Psychic': ['Fighting', 'Poison'],
  'Rock': ['Flying', 'Bug', 'Fire', 'Ice'],
  'Ghost': ['Ghost', 'Psychic'],
  'Ice': ['Flying', 'Ground', 'Grass', 'Dragon'],
  'Dragon': ['Dragon'],
  'Dark': ['Ghost', 'Psychic'],
  'Steel': ['Rock', 'Ice', 'Fairy'],
  'Flying' : ['Fighting', 'Bug', 'Grass']
}
boolean_map = {
  False: 0, True: 1
}

def add_attack_columns(combats, pokemon):
  combats['first_atk_power'] = combats['First_pokemon'].replace(pokemon['Attack'])\
      + combats['First_pokemon'].replace(pokemon['Sp. Atk'])\
      + combats['First_pokemon'].replace(pokemon['Speed'])
  combats['second_atk_power'] = combats['Second_pokemon'].replace(pokemon['Attack'])\
      + combats['Second_pokemon'].replace(pokemon['Sp. Atk'])\
      + combats['Second_pokemon'].replace(pokemon['Speed'])
  return combats

def has_type_advantage(type1, type2):
  return type_advantages[type1].count(type2)

def has_secondary_type(type):
  return 1 if pandas.isnull(type) else 0

def add_type_columns(combats, pokemon):
  type_comparison = pandas.DataFrame({
    'first_type1': combats['First_pokemon'].replace(pokemon['Type 1']),
    'second_type1': combats['Second_pokemon'].replace(pokemon['Type 1'])
  })
  first_type2 = combats['First_pokemon'].replace(pokemon['Type 2'])
  second_type2 = combats['Second_pokemon'].replace(pokemon['Type 2'])

  combats['has_type_advantage_first'] = type_comparison.apply(lambda x: has_type_advantage(x['first_type1'], x['second_type1']), axis=1)
  combats['has_type_advantage_second'] = type_comparison.apply(lambda x: has_type_advantage(x['second_type1'], x['first_type1']), axis=1)
  combats['has_secondary_type_first'] = first_type2.map(has_secondary_type)
  combats['has_secondary_type_second'] = second_type2.map(has_secondary_type)
  return combats

def add_win_columns(combats):
  combats.Winner[combats.Winner == combats.First_pokemon] = 0
  combats.Winner[combats.Winner == combats.Second_pokemon] = 1

  win_rates = (
      combats.groupby('First_pokemon')['Winner'].sum()\
      +combats.groupby('Second_pokemon')['Winner'].sum()
  ).replace(numpy.nan, 0)
  combats['win_rate_first'] = combats['First_pokemon'].map(win_rates)
  combats['win_rate_second'] = combats['Second_pokemon'].map(win_rates)
  return combats

def add_speed_column(combats, pokemon):
  first_speed = combats['First_pokemon'].replace(pokemon['Speed'])
  second_speed = combats['Second_pokemon'].replace(pokemon['Speed'])
  combats['first_more_fast'] = (first_speed > second_speed).map(boolean_map)
  return combats

def stat_differences(combats, pokemon):
  stats=["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed", "Legendary"]
  pokemon['Legendary'] = pokemon['Legendary'].map(boolean_map)
  stats_df=pokemon[stats].T.to_dict("list")
  one=combats.First_pokemon.map(stats_df)
  two=combats.Second_pokemon.map(stats_df)
  temp_list=[]
  for i in range(len(one)):
      temp_list.append(numpy.array(one[i])-numpy.array(two[i]))
  new_test = pandas.DataFrame(temp_list, columns=stats)
  return new_test