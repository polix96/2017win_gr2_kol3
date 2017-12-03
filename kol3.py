#!/usr/bin/env python2.7
import kol1
import unittest


class TestPlane(unittest.TestCase):
    def setUp(self):
        self.weather1 = kol1.Weather()
        self.plane = kol1.Plane("Kajtek", 30, self.weather1)

    def test_name_of_plane(self):
        self.assertEqual(self.plane.name, "Kajtek")

    def test_tilt_of_plane(self):
        self.assertEqual(self.plane.tilt, 30)

    def test_amount_of_cycles_input(self):
        self.assertEqual(self.plane.amount_of_cycles_input(), 10)

    def test_correct_tilt(self):
        self.plane.correct_tilt()
        self.assertEqual(self.plane.tilt, 26)

    def test_weather_fog(self):
        assert isinstance(self.weather1.fog, str)

    def test_weather_rain(self):
        assert isinstance(self.weather1.rain, str)

    def test_weather_humidity(self):
        assert isinstance(self.weather1.humidity, str)

    def test_weather_change_param_fog(self):
        self.weather1.change_param('fog', 'none')
        self.assertEqual(self.weather1.fog, 'none')

    def test_weather_change_param_rain(self):
        self.weather1.change_param('rain', 'drizzle')
        self.assertEqual(self.weather1.rain, 'drizzle')

    def test_weather_change_param_humidity(self):
        self.weather1.change_param('humidity', '50%')
        self.assertEqual(self.weather1.humidity, '50%')


if __name__ == '__main__':
    unittest.main()

