from mlproject.distance import haversine


def test_haversine():
    assert type(haversine(1,2,2,4)) == float
