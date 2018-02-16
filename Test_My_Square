import unittest
import Quadratfunktion
import math
import replaced print with return

class Test_My_Square(unittest.TestCase):

  def test_my_square(self):
    self.assertListEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], my_square())

  def test_simon(self):
    self.assertEqual(my_square_root_between_0_10(0), 0)
    self.assertEqual(my_square_root_between_0_10(10), 100)
    self.assertEqual(my_square_root_between_0_10(5), 25)
    self.assertEqual(my_square_root_between_0_10(-1), "number is not in the defined range")
    self.assertEqual(my_square_root_between_0_10(11), "number is not in the defined range")


if __name__ == "__main__":
  unittest.main()
