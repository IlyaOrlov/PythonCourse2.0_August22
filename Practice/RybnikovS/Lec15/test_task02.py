import pytest
from task02 import Money


class TestWithPytestSuite:

    @classmethod
    def setup_class(cls):
        print('Before test suite')

    @classmethod
    def teardown_class(cls):
        print('After test suite')

    def test_add(self):
        assert(Money(50, 60) + Money(100, 60) == Money(151, 20))

    def test_sub(self):
        assert(Money(50, 30) - Money(100, 60) == Money(-50, 30))

    def test_ge(self):
        assert((Money(200, 30) >= Money(100, 60)) is True)

    def test_ge_rub_eq_t(self):
        assert((Money(100, 90) >= Money(100, 60)) is True)

    def test_ge_rub_eq_f(self):
        assert((Money(100, 10) >= Money(100, 60)) is False)

    def test_gt(self):
        assert((Money(200, 30) > Money(100, 60)) is True)

    def test_gt_rub_eq_t(self):
        assert((Money(100, 90) > Money(100, 60)) is True)

    def test_gt_rub_eq_f(self):
        assert((Money(100, 30) > Money(100, 60)) is False)


if __name__ == '__main__':
    pytest.main()
