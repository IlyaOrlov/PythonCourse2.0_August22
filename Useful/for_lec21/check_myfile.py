from unittest import mock
import myfile


# def mock_print(arg):
#     mock_print.arg = arg
#
#
# myfile.print = mock_print
# myfile.mysum(10, 20)
# assert mock_print.arg == 30


myfile.print = mock.Mock()
myfile.mysum(10, 20)
myfile.print.assert_called_once_with(30)
