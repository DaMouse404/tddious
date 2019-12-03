import pandas

from pandas.testing import assert_frame_equal

from tddious import extract_features
from tddious.combat_features import (add_columns, add_type_columns, add_win_columns, add_speed_column, stat_differences)

pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
combats = pandas.read_csv('test/fixtures/combats_head.csv')

def test_add_columns():
    expected_features = pandas.read_csv('test/fixtures/combats_with_columns.csv')
    assert_frame_equal(add_columns(combats, pokemon), expected_features)

def test_type_columns():
    combats_with_columns = pandas.read_csv('test/fixtures/combats_with_columns.csv')
    expected_features = pandas.read_csv('test/fixtures/combats_with_type_columns.csv')

    assert_frame_equal(add_type_columns(combats_with_columns), expected_features)

def test_win_columns():
    more_combats = pandas.read_csv('test/fixtures/combats_head_1000.csv')
    expected_features = pandas.read_csv('test/fixtures/combats_with_win_columns.csv')

    assert_frame_equal(add_win_columns(more_combats), expected_features)


def test_speed_column():
    combats_with_columns = pandas.read_csv('test/fixtures/combats_with_columns.csv')
    expected_features = pandas.read_csv('test/fixtures/combats_with_speed_column.csv')

    assert_frame_equal(add_speed_column(combats_with_columns), expected_features)


def test_stat_differences():
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
    combats = pandas.read_csv('test/fixtures/combats_head_1000.csv')
    expected_features = pandas.read_csv('test/fixtures/combats_with_stat_difference.csv')

    print(list(stat_differences(combats, pokemon)))
    print(list(expected_features))

    assert_frame_equal(stat_differences(combats, pokemon), expected_features)