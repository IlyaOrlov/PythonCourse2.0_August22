import pytest
from tasks import mylen, myrange


class TestTasksSuite:
    def test_mylen(self):
        l = [1, 45, 32, 9]
        assert(mylen(l) == 4)

    def test_myrange(self):
        assert(myrange(5) == list(range(5)))
        assert(myrange(10, 20) == list(range(10, 20)))
        assert(myrange(10, 20, 3) == list(range(10, 20, 3)))
        assert(myrange(20, 10, -2) == list(range(20, 10, -2)))
        assert(myrange(20, 10, 0) == list(range(20, 10, 0)))


if __name__ == '__main__':
    pytest.main()
