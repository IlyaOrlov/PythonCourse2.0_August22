import pytest


class TestWithPytestSuite:
    def setup(self):
        print('Before test case')

    def teardown(self):
        print('After test case')

    @classmethod
    def setup_class(cls):
        print('Before test suite')

    @classmethod
    def teardown_class(cls):
        print('After test suite')

    def test_numbers_5_6(self):
        assert(5 * 6 == 30)

    def test_strings_b_2(self):
        assert('b' * 2 == 'bb')

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            a = 10 / 0
