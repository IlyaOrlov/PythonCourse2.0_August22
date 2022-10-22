import pytest
from task01 import to_roman


class TestWithPytestSuite:

    @classmethod
    def setup_class(cls):
        print('Before test suite')

    @classmethod
    def teardown_class(cls):
        print('After test suite')

    def test_low_num(self):
        assert (to_roman(1) == "I")

    def test_medium_num(self):
        assert (to_roman(2501) == "MMDI")

    def test_high_num(self):
        assert (to_roman(4999) == "MMMMCMXCIX")

    def test_not_num(self):
        with pytest.raises(SystemExit) as e:
            to_roman("a")
        assert e.type == SystemExit
        assert e.value.code == 666

    def test_more_than(self):
        with pytest.raises(SystemExit) as e:
            to_roman("5000")
        assert e.type == SystemExit
        assert e.value.code == 555


if __name__ == '__main__':
    pytest.main()
