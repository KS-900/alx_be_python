import unittest
from simple_calculator import SimpleCalculator  # type: ignore # Import the class to be tested

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of SimpleCalculator for each test
        self.calc = SimpleCalculator()

    # Test for addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Test for subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    # Test for multiplication
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(0, 3), 0)

    # Test for division
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 6, 0)  # Test for division by zero

# Run the tests
if __name__ == "__main__":
    unittest.main()