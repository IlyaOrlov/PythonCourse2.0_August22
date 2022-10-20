import pytest
import sys
sys.path.append("./code")
from myfile import sumfun


class TestMyfileSuite:
    @pytest.fixture(
        scope='function',
        params=[(10, 20, 30), (-10, -20, -30), (-10, 20, 10)],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrizer(self, request):
        return request.param

    def test_sumfun(self, parametrizer):
        params = parametrizer
        args = params[:-1]
        exp_res = params[-1]
        res = sumfun(*args)
        assert res == exp_res
