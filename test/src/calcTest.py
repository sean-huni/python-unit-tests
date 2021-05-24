import unittest
from main.src.service.calcs.calc import Division

class CalcServiceTest(unittest.TestCase):
    div = Division

    '''
    Calc Service DivideBy - Positive Test
    '''
    def test_givenCalcService_whenDivideBy_thenReturnResultSuccess(self):
        a = 5
        b = 5
        res = self.div.divideBy(self, a, b)
        self.assertEqual(1, res)

    '''
       Calc Service DivideBy - Negative Test
       '''
    def test_givenCalcService_whenDivideByZero_thenReturnThrowZeroDivisionError(self):
        a = 5
        b = 0
        with self.assertRaises(ZeroDivisionError):
            self.div.divideBy(self, a, b)


if __name__ == '__main__':
    unittest.main()
