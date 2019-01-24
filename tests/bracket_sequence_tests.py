"""
тесты для bracket_sequence
"""

import unittest
from bracket_sequence.bracket_sequence import bracket_seqence_checker


class BracketSequence(unittest.TestCase):
    # TRUE
    def test_empty_string(self):
        """
        пустая строка
        :return:
        """
        self.assertTrue(bracket_seqence_checker(''))

    def test_simple_good_seq(self):
        """
        элементарная правильная последовательность
        :return:
        """
        self.assertTrue(bracket_seqence_checker('()'))

    def test_inner_seq(self):
        """
        правильная последовательность с 1 вложенной правильной последовательностью
        :return:
        """
        self.assertTrue(bracket_seqence_checker('[()]'))

    def test_inner_seq_2(self):
        """
        длинная правильная последовательность с несколькими вложенностями
        :return:
        """
        self.assertTrue(bracket_seqence_checker('[{}({([()])})]'))

    def test_long_seq(self):
        """
        очень длинная последовательность с вложенностями
        :return:
        """
        self.assertTrue(bracket_seqence_checker('[[[[[[[[[[[[[]]]]]]]]]]({()})]]]'))

    # FALSE
    def test_odd_len(self):
        """
        последовательность нечётной длинны
        :return:
        """
        self.assertFalse(bracket_seqence_checker('[[]'))

    def test_bad_seq(self):
        """
        последовательность с переставленными типами закрывающих скобок
        :return:
        """
        self.assertFalse(bracket_seqence_checker('[(])'))

    def test_opening_seq(self):
        """
        последовательность только из открывающих скобок
        :return:
        """
        self.assertFalse(bracket_seqence_checker('[['))

    def test_closing_seq(self):
        """
        последовательность только из закрывающих скобок
        :return:
        """
        self.assertFalse(bracket_seqence_checker('))'))

    def test_bad_long_seq(self):
        """
        длинная последовательность с переставленными закрывающими скобками
        :return:
        """
        self.assertFalse(bracket_seqence_checker('[()]{}{[()[(])()]()}'))

    # ERRORS
    def test_bad_type(self):
        """
        передаём неправильный тип данных
        :return:
        """
        with self.assertRaises(Exception):
            bracket_seqence_checker(123456)

    def test_bytes_good_seq(self):
        """
        пытаемся передать правильную последовательность, но неправильного типа.
        bytes намеренно не поддерживаем
        :return:
        """
        with self.assertRaises(Exception):
            bracket_seqence_checker(b'[()]')

    def test_bytes_bad_seq(self):
        """
        пытаемся передать неправильную последовательность, но неправильного типа.
        bytes намеренно не поддерживаем
        :return:
        """
        with self.assertRaises(Exception):
            bracket_seqence_checker(b'[]]]]')
