class TestMyStuff:
    def test_type(self):
        assert type(1) == int

    def test_strs(self):
        assert "python".upper() == "PYTHON"
        assert "python".capitalize() == "Python"
