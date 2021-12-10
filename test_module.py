import pytest
from most_active_cookie import most_active_cookie
class TestCorrectness:

    def test_one(self, capfd):
        most_active_cookie("test.csv", "2018-12-09")
        out, err = capfd.readouterr()
        assert out == "AtY0laUfhglK3lC7\n"

    def test_multiple(self, capfd):
        res = "4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\nSAZuXPGUrfbcn5UA\n"
        most_active_cookie("test.csv", "2018-12-08")
        out, err = capfd.readouterr()
        assert out == res

    def test_none(self, capfd):
        most_active_cookie("test.csv", "2018-12-06")
        out, err = capfd.readouterr()
        assert out == ""
