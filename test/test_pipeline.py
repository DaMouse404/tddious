import pandas

from sklearn.metrics import accuracy_score
from pandas.testing import assert_frame_equal
from tddious import (extract_features, train_model)

def test_pipeline():
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
    combats = pandas.read_csv('test/fixtures/combats.csv')

    features = extract_features(combats, pokemon)
    model = train_model(features)


def test_extract_features():
    combats = pandas.read_csv('test/fixtures/combats_head.csv')
    pokemon = pandas.read_csv('test/fixtures/pokemon.csv', index_col=0)
    expected_features = pandas.read_csv('test/fixtures/features_head.csv')

    assert_frame_equal(extract_features(combats, pokemon), expected_features)


def test_train_model():
    training_features = pandas.read_csv('test/fixtures/training_features.csv')
    training_values = pandas.read_csv('test/fixtures/training_values.csv', header=None)

    testing_features = pandas.read_csv('test/fixtures/testing_features.csv')
    testing_values = pandas.read_csv('test/fixtures/testing_values.csv', header=None)

    model = train_model(training_features, training_values)
    predictions = model.predict(testing_features)

    assert accuracy_score(predictions, testing_values) >= 0.95