#Ryan Barber Assignment 7.2 2/22/26

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()