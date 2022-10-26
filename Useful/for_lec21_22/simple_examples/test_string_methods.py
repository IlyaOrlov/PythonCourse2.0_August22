import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    @classmethod
    def setUpClass(cls):
        print('class start')

    @classmethod
    def tearDownClass(cls):
        print('class end')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
