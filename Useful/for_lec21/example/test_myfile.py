import pytest
from myfile import fun


class TestMyFile:
    @pytest.fixture(
        scope='function',
        params=[(10, 20, 30), (-10, -20, -30), (10, 0, 10), (10, -10, 0)],
        ids=lambda args: f"Test fun with args: {args}"
    )
    def parametrizer(self, request):
        return request.param

    def test_fun(self, parametrizer):
        arg1, arg2, res = parametrizer
        assert(fun(arg1, arg2) == res)

    # def test_fun_1(self):
    #     assert(fun(10, 20) == 30)
    #
    # def test_fun_2(self):
    #     assert(fun(-10, -20) == -30)
    #
    # def test_fun_3(self):
    #     assert(fun(10, 0) == 10)
