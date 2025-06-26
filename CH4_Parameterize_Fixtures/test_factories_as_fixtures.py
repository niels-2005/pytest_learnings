def test_fact_fixture(setup01):
    assert type(setup01("list")) == list
    assert type(setup01("tuple")) == tuple
