import unittest
from main import Hat, experiment

class TestHat(unittest.TestCase):
    def test_hat_contents(self):
        hat = Hat(red=3, blue=2)
        self.assertEqual(sorted(hat.contents), ['blue', 'blue', 'red', 'red', 'red'])

    def test_draw(self):
        hat = Hat(green=5)
        drawn = hat.draw(2)
        self.assertEqual(len(drawn), 2)
        self.assertEqual(len(hat.contents), 3)

    def test_experiment(self):
        hat = Hat(blue=3, red=2, green=6)
        probability = experiment(hat, {'red':1, 'green':2}, 4, 1000)
        self.assertTrue(0 <= probability <= 1)

if __name__ == "__main__":
    unittest.main()
