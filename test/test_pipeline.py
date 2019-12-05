import pandas

from pandas.testing import assert_frame_equal
from tddious import extract_features

def test_pipeline():
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
    combats = pandas.read_csv('test/fixtures/combats.csv')

    features = extract_features(combats, pokemon)


def test_extract_features():
    combats = pandas.read_csv('test/fixtures/combats_head.csv')
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
    expected_features = pandas.read_csv('test/fixtures/features_head.csv')

    assert_frame_equal(extract_features(combats, pokemon), expected_features)