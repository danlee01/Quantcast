import pytest
from most_active_cookie import most_active_cookie

class TestCorrectness:

    def test_one(self):
        assert most_active_cookie("test.csv", "2018-12-09") == "AtY0laUfhglK3lC7"

    def test_two(self):
        res = "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG"
        assert most_active_cookie("test.csv", "2018-12-08") == res