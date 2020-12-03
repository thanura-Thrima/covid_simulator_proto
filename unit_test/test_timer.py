import unittest
from source.time_ import TimeInformer


class TestTimeInformer(unittest.TestCase):

    def test_numberOfTicksPerHour(self):
        timer =TimeInformer(12)
        self.assertEqual(timer.numberOfTickPerHour,12, "Should be 12")

    def test_numberOfTicksPerDay(self):
        timer =TimeInformer(12)
        self.assertEqual(timer.numberofTickPerDay,12*24, "Should be 288")

    def test_update_1(self):
        timer =TimeInformer(12)
        timer.update(120)
        self.assertEqual(timer.hours,10, "Should be 10")
        self.assertEqual(timer.days,0, "Should be 0")
        self.assertEqual(timer.isDay,True,"should be a dayTime")

    def test_update_2(self):
        timer =TimeInformer(12)
        timer.update(180)
        self.assertEqual(timer.hours,15, "Should be 10")
        self.assertEqual(timer.days,0, "Should be 0")
        self.assertEqual(timer.isDay,False,"should be a nightTime")

    def test_update_3(self):
        timer =TimeInformer(12)
        timer.update(289)
        self.assertEqual(timer.hours,0, "Should be 0")
        self.assertEqual(timer.days,1, "Should be 1")
        self.assertEqual(timer.isDay,True,"should be a dayTime")
