import unittest
import sys

def calcFactorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestCalcFactorial(unittest.TestCase):

    def testZero(self):
        self.assertEqual(calcFactorial(0), 1)

    def testOne(self):
        self.assertEqual(calcFactorial(1), 1)

    def testSmallNumber(self):
        self.assertEqual(calcFactorial(5), 120)

    def testLargeNumber(self):
        self.assertEqual(calcFactorial(10), 3628800)

    def testNegativeNumber(self):
        with self.assertRaises(ValueError):
            calcFactorial(-3)

    def testOverflow(self):
        with self.assertRaises(ValueError):
            calcFactorial(1000)

    def testNearLimit(self):
        self.assertEqual(calcFactorial(20), 2432902008176640000)


if __name__ == '__main__':
    unittest.main()