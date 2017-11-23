#!/usr/bin/env python2.7
import kol1
import unittest


class TestCorrectTilt(unittest.TestCase):
	def amount_of_cycles_input(self):
		self.assertEqual(self.amount_of_cycles_input,5)


if __name__ == '__main__':
	unittest.main()
