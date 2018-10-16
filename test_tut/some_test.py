import unittest
import some_unit

class Test(unittest.TestCase):
    'Test Class'

    @classmethod
    def setUpClass(cls):
        print('SO........')

    @classmethod
    def tearDownClass(cls):
        print('SO?..')

    def test_add(self):
        'short description for ADD method'
        self.assertEqual(some_unit.MyMath.add(1, 2), 3)

    def test_subtract(self):
        'short description for SUB method'
        self.assertEqual(some_unit.MyMath.subtract(3, 2), 1)

    def setUp(self):
        self.shortDescription()
        print()
        print('_'*10)

    def tearDown(self):
        print('tear down for ...')
        self.shortDescription()

if __name__ == '__main__':
    unittest.main()