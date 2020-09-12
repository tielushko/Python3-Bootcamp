import unittest
from activities import eat, nap, is_funny

"""you can add documentation to each of the tests with """""" string. """

#in order to see all of the documentation, run the python file with an -v flag


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy = True),
            "I am eating broccoli because my body is a temple!"
        )
    
    def test_eat_unhealthy(self):
        """You gave up healthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I am eating pizza because YOLO!"
        )

    def test_eat_unhealthy_bool(self):
        """is healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who gives?")

    def test_short_nap(self):
        """Test for cool short nap"""
        self.assertEqual(
            nap(1),
            "I am feeling refreshed after my 1 hour nap."
        )

    def test_long_nap(self):
        """Test for bleh long nap"""
        self.assertEqual(
            nap(3),
            "Ugh, I overslept. I didn't mean to nap for 3 whole hours."
        )
    
    def test_tim_isnt_funny(self):
        """test for not funny tim"""
        self.assertEqual(
            is_funny("tim"),
            False
        )

    def test_rest_are_funny(self):
        """test for very funny bunch"""
        self.assertTrue(
            is_funny("blue"), "blue should be funny" #we can add message to the tester as a second argument
        )
        self.assertTrue(
            is_funny("dave"), "dave should be funny" #we can add message to the tester as a second argument
        )
        self.assertTrue(
            is_funny("tony"), "tony should be funny" #we can add message to the tester as a second argument
        )
    
if __name__ == "__main__":
    unittest.main()

