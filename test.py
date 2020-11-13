import unittest

from main import determinePrecedence


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

    def testMajorEqualMinorByOneHigher(self):
        result = determinePrecedence("1.2.0", "1.1.0")
        self.assertEqual(result, True)

    def testMajorEqualMinorByOneLower(self):
        result = determinePrecedence("1.1.0", "1.2.0")
        self.assertEqual(result, False)

    def testMajorEqualMinorEqualPatchByOneHigher(self):
        result = determinePrecedence("1.1.2", "1.1.1")
        self.assertEqual(result, True)

    def testMajorEqualMinorEqualPatchByOneLower(self):
        result = determinePrecedence("1.1.1", "1.1.2")
        self.assertEqual(result, False)

# TODO: Add prerelease examples


if __name__ == '__main__':
    unittest.main()
