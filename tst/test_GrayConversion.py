import unittest
from src.GrayConversion import GrayConversion


class TestGray(unittest.TestCase):

    def from_b_to_g(self):
        self.assertEqual(GrayConversion('0000').from_b_to_g(), '0000')
        self.assertEqual(GrayConversion('0001').from_b_to_g(), '0001')
        self.assertEqual(GrayConversion('0010').from_b_to_g(), '0011')
        self.assertEqual(GrayConversion('0011').from_b_to_g(), '0010')
        self.assertEqual(GrayConversion('0100').from_b_to_g(), '0110')
        self.assertEqual(GrayConversion('0101').from_b_to_g(), '0111')
        self.assertEqual(GrayConversion('0110').from_b_to_g(), '0101')
        self.assertEqual(GrayConversion('0111').from_b_to_g(), '0100')
        self.assertEqual(GrayConversion('1000').from_b_to_g(), '1100')
        self.assertEqual(GrayConversion('1001').from_b_to_g(), '1101')
        self.assertEqual(GrayConversion('1010').from_b_to_g(), '1111')
        self.assertEqual(GrayConversion('1011').from_b_to_g(), '1110')
        self.assertEqual(GrayConversion('1100').from_b_to_g(), '1010')
        self.assertEqual(GrayConversion('1101').from_b_to_g(), '1011')
        self.assertEqual(GrayConversion('1110').from_b_to_g(), '1001')
        self.assertEqual(GrayConversion('1111').from_b_to_g(), '1000')

    def from_g_to_b(self):
        self.assertEqual(GrayConversion('0000').from_g_to_b(), '0000')
        self.assertEqual(GrayConversion('0001').from_g_to_b(), '0001')
        self.assertEqual(GrayConversion('0011').from_g_to_b(), '0010')
        self.assertEqual(GrayConversion('0010').from_g_to_b(), '0011')
        self.assertEqual(GrayConversion('0110').from_g_to_b(), '0100')
        self.assertEqual(GrayConversion('0111').from_g_to_b(), '0101')
        self.assertEqual(GrayConversion('0101').from_g_to_b(), '0110')
        self.assertEqual(GrayConversion('0100').from_g_to_b(), '0111')
        self.assertEqual(GrayConversion('1100').from_g_to_b(), '1000')
        self.assertEqual(GrayConversion('1101').from_g_to_b(), '1001')
        self.assertEqual(GrayConversion('1111').from_g_to_b(), '1010')
        self.assertEqual(GrayConversion('1110').from_g_to_b(), '1011')
        self.assertEqual(GrayConversion('1010').from_g_to_b(), '1100')
        self.assertEqual(GrayConversion('1011').from_g_to_b(), '1101')
        self.assertEqual(GrayConversion('1001').from_g_to_b(), '1110')
        self.assertEqual(GrayConversion('1000').from_g_to_b(), '1111')