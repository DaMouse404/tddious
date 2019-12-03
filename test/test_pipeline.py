import pandas

from pandas.testing import assert_frame_equal
from tddious import extract_features

def test_pipeline():
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv')
    combats = pandas.read_csv('test/fixtures/combats.csv')

    features = extract_features(combats, pokemon)


def test_extract_features():
    combats = pandas.read_csv('test/fixtures/combats_head.csv')
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv')
    expected_features = pandas.read_csv('test/fixtures/features_head.csv')
    print(list(expected_features))
    print(list(extract_features(combats,pokemon)))
    assert_frame_equal(extract_features(combats, pokemon), expected_features)