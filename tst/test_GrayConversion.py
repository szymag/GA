import unittest
from src.GrayConversion import GrayConversion


class TestGray(unittest.TestCase):

    def test_from_b_to_g(self):
        self.assertEqual(GrayConversion('0000').to_gray(), '0000')
        self.assertEqual(GrayConversion('0001').to_gray(), '0001')
        self.assertEqual(GrayConversion('0010').to_gray(), '0011')
        self.assertEqual(GrayConversion('0011').to_gray(), '0010')
        self.assertEqual(GrayConversion('0100').to_gray(), '0110')
        self.assertEqual(GrayConversion('0101').to_gray(), '0111')
        self.assertEqual(GrayConversion('0110').to_gray(), '0101')
        self.assertEqual(GrayConversion('0111').to_gray(), '0100')
        self.assertEqual(GrayConversion('1000').to_gray(), '1100')
        self.assertEqual(GrayConversion('1001').to_gray(), '1101')
        self.assertEqual(GrayConversion('1010').to_gray(), '1111')
        self.assertEqual(GrayConversion('1011').to_gray(), '1110')
        self.assertEqual(GrayConversion('1100').to_gray(), '1010')
        self.assertEqual(GrayConversion('1101').to_gray(), '1011')
        self.assertEqual(GrayConversion('1110').to_gray(), '1001')
        self.assertEqual(GrayConversion('1111').to_gray(), '1000')

    def test_from_g_to_b(self):
        self.assertEqual(GrayConversion('0000').from_gray(), '0000')
        self.assertEqual(GrayConversion('0001').from_gray(), '0001')
        self.assertEqual(GrayConversion('0011').from_gray(), '0010')
        self.assertEqual(GrayConversion('0010').from_gray(), '0011')
        self.assertEqual(GrayConversion('0110').from_gray(), '0100')
        self.assertEqual(GrayConversion('0111').from_gray(), '0101')
        self.assertEqual(GrayConversion('0101').from_gray(), '0110')
        self.assertEqual(GrayConversion('0100').from_gray(), '0111')
        self.assertEqual(GrayConversion('1100').from_gray(), '1000')
        self.assertEqual(GrayConversion('1101').from_gray(), '1001')
        self.assertEqual(GrayConversion('1111').from_gray(), '1010')
        self.assertEqual(GrayConversion('1110').from_gray(), '1011')
        self.assertEqual(GrayConversion('1010').from_gray(), '1100')
        self.assertEqual(GrayConversion('1011').from_gray(), '1101')
        self.assertEqual(GrayConversion('1001').from_gray(), '1110')
        self.assertEqual(GrayConversion('1000').from_gray(), '1111')

if __name__ == '__main__':
    unittest.main()
