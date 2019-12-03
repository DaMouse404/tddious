import pandas

from .combat_features import (
    add_columns,
    add_speed_column,
    add_type_columns,
    add_win_columns
)

def extract_features(combats, pokemon):
    combats = add_columns(combats, pokemon)
    combats = add_speed_column(combats)
    combats = add_type_columns(combats)
    combats = add_win_columns(combats)
    combats = stat_difference(combats)
    return combats