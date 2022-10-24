import pytest
from tasks import myrange


class TestMyrangeSuite:
    @pytest.fixture(
        scope='function',
        params=[(0, 5), (10, 20), (10, 20, 3), (20, 10, -2), (20, 10, 0)],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrize_myrange(self, request):
        return request.param

    def test_myrange(self, parametrize_myrange):
        range_args = parametrize_myrange
        assert myrange(*range_args) == list(range(*range_args))


if __name__ == '__main__':
    pytest.main()
