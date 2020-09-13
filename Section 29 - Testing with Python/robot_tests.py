from robot import Robot
import unittest

class RobotTests(unittest.TestCase):
    #instead of the writing mega_man = Robot("Megaman", battery = 50) for every test, we can write setUp
    def setUp(self):
        self.mega_man = Robot("Megaman", battery = 50)

    def test_charge(self):
        #mega_man = Robot("Megaman", battery = 50)
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        #mega_man = Robot("Megaman", battery=50)
        self.assertEqual(self.mega_man.say_name(), "BEEP BEEP BOOP BOOP. I am MEGAMAN")
        self.assertEqual(self.mega_man.battery, 49)
    
    def test_new_skill_success(self):
        #mega_man = Robot("Megaman", battery=50)
        self.mega_man.learn_new_skill(20, "walking")
        self.assertEqual(self.mega_man.skills[0], "walking", "Walking should be inserted into the skills array")
        self.assertEqual(self.mega_man.battery, 30, "Battery should be decreased by the amount of skill cost")

    def test_new_skill_error(self):
        #mega_man = Robot("Megaman", battery=50)
        self.mega_man.learn_new_skill(51, "walking")
        self.assertEqual(self.mega_man.learn_new_skill(51, "walking"), "ERROR! Not enough charge to perform the operation. Please charge!")

    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main()