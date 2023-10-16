class RomanNumeral:
    def __init(self):
        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        converted_number = 0
        i = 0

        while i < len(s):
            current_number = self.map[s[i]]

            if i + 1 < len(s):
                next_number = self.map[s[i + 1]]
                if current_number < next_number:
                    converted_number += next_number - current_number
                    i += 2
                else:
                    converted_number += current_number
                    i += 1
            else:
                converted_number += current_number
                i += 1

        return converted_number

import unittest

class TestRomanNumeralConversion(unittest.TestCase):
    def test_single_letters(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("I"), 1)
        self.assertEqual(roman_converter.romanToInt("V"), 5)
        self.assertEqual(roman_converter.romanToInt("X"), 10)
        self.assertEqual(roman_converter.romanToInt("L"), 50)
        self.assertEqual(roman_converter.romanToInt("C"), 100)
        self.assertEqual(roman_converter.romanToInt("D"), 500)
        self.assertEqual(roman_converter.romanToInt("M"), 1000)

    def test_many_letters(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("XI"), 11)

    def test_subtractive_notation(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("IV"), 4)

    def test_with_and_without_subtractive_notation(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("XIV"), 14)
        self.assertEqual(roman_converter.romanToInt("XXIV"), 24)

    def test_repetition(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("II"), 2)
        self.assertEqual(roman_converter.romanToInt("III"), 3)

    def test_first_number(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt("I"), 1)

    def test_invalid_letter(self):
        roman_converter = RomanNumeral()
        with self.assertRaises(KeyError):
            roman_converter.romanToInt("Z")

    def test_invalid_and_valid_letters(self):
        roman_converter = RomanNumeral()
        with self.assertRaises(KeyError):
            roman_converter.romanToInt("XIZ")

    def test_not_valid(self):
        roman_converter = RomanNumeral()
        with self.assertRaises(ValueError):
            roman_converter.romanToInt("VV")

    def test_null(self):
        roman_converter = RomanNumeral()
        self.assertEqual(roman_converter.romanToInt(""), 0)

if __name__ == '__main__':
    unittest.main()
