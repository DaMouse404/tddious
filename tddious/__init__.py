import pandas

from .combat_features import (
    add_attack_columns,
    add_speed_column,
    add_type_columns,
    add_win_columns,
    stat_differences
)

def extract_features(combats, pokemon):
    combats = add_win_columns(combats)
    combats = add_type_columns(combats, pokemon)
    combats = add_speed_column(combats, pokemon)
    combats = add_attack_columns(combats, pokemon)
    combats = pandas.concat(
        [stat_differences(combats, pokemon), combats],
        axis=1
    )
    combats.drop(
        ['First_pokemon', 'Second_pokemon'],
        axis=1, inplace=True
    )
    return combats