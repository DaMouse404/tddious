import pandas

from tddious import extract_features

def test_pipeline():
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv')

    features = extract_features(pokemon)