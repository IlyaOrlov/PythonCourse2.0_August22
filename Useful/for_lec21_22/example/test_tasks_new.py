import pytest
from tasks import mylen, myrange


class TestTasksSuite:
    def test_mylen(self):
        l = [1, 45, 32, 9]
        assert(mylen(l) == 4)

    @pytest.fixture(
        scope='function',
        params=[5, 10, 2],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrizer(self, request):
        return request.param

    def test_myrange(self, parametrizer):
        args = parametrizer
        assert(myrange(args) == list(range(args)))


if __name__ == '__main__':
    pytest.main()
