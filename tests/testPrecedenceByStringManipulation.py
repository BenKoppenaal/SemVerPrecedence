import unittest

from SymVerPrecedence.precedenceByStringManipulation import determinePrecedence


class TestSemVerPrecedence(unittest.TestCase):
    def testExactSameVersion(self):
        result = determinePrecedence("1.1.1", "1.1.1")
        self.assertEqual(result, True)

    def testMajorDifferenceByOneHigher(self):
        result = determinePrecedence("2.0.0", "1.0.0")
        self.assertEqual(result, True)

    def testMajorDifferenceByOneLower(self):
        result = determinePrecedence("1.0.0", "2.0.0")
        self.assertEqual(result, False)

    def testMajorEqualMinorDifferenceByOneHigher(self):
        result = determinePrecedence("1.2.0", "1.1.0")
        self.assertEqual(result, True)

    def testMajorEqualMinorDifferenceByOneLower(self):
        result = determinePrecedence("1.1.0", "1.2.0")
        self.assertEqual(result, False)

    def testMajorEqualMinorEqualPatchDifferenceByOneHigher(self):
        result = determinePrecedence("1.1.2", "1.1.1")
        self.assertEqual(result, True)

    def testMajorEqualMinorEqualPatchDifferenceByOneLower(self):
        result = determinePrecedence("1.1.1", "1.1.2")
        self.assertEqual(result, False)

    def testExactSameVersionCoreDifferenceByHighPrerelease(self):
        result = determinePrecedence("1.1.1-alpha", "1.1.1")
        self.assertEqual(result, False)

    def testExactSameVersionCoreDifferenceByLowPrerelease(self):
        result = determinePrecedence("1.1.1", "1.1.1-alpha")
        self.assertEqual(result, True)

    def testDoubleDigitMajorHasPrecedence(self):
        result = determinePrecedence("10.10.10", "9.9.9")
        self.assertEqual(result, True)

    def testDoubleDigitMajorHasNoPrecedence(self):
        result = determinePrecedence("9.9.9", "11.11.11")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
