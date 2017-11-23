#!/usr/bin/env python2.7
import kol1
import unittest


class TestPlane(unittest.TestCase):
	def setUp(self):
		weather1 = kol1.Weather()
		self.plane=kol1.Plane("Kajtek",30,weather1)

	def test_name_of_plane(self):
		self.assertEqual(self.plane.name,"Kajtek")
	
	def test_tilt_of_plane(self):
		self.assertEqual(self.plane.tilt,30)

	def test_amount_of_cycles_input(self):
		self.assertEqual(self.plane.amount_of_cycles_input(),10)

if __name__ == '__main__':
	unittest.main()
