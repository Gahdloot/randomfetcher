import unittest

from main import RanGenrator

class TestRand(unittest.TestCase):
    def test_list_size(self):
        """
        This is to check that the lenght of Random-Genrator is always 4
        """
        expected_lenght = 4
        returned_lenght = len(RanGenrator(30))
        self.assertEqual(returned_lenght, expected_lenght)

    def test_sum_of_random(self):
        """
        This is to test that the sum of the Random-Generator always results to the initial input
        """
        user_input = 30
        returned_sum = sum(RanGenrator(30))
        self.assertEqual(returned_sum, user_input)



if __name__ == '__main__':
    unittest.main()
