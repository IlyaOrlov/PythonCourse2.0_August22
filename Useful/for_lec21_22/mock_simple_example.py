import unittest.mock as mock


def fun(service):
    service.show()
    service.name = "Hello"
    s = service.get()
    return s


m = mock.Mock()
m.get.return_value = 100
res = fun(m)
assert(m.show.called is True)
assert(res == 100)

