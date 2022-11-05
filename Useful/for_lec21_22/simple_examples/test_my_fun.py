from unittest import TestCase


class TestMylen(TestCase):
    @classmethod
    def setUpClass(cls):
        print("Before test suite")

    @classmethod
    def tearDownClass(cls):
        print("After test suite")

    def setUp(self):
        print("Before test")

    def tearDown(self):
        print("After test")

    def test_mylen(self):
        pass

    def test_mylen2(self):
        self.fail()
