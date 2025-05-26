import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents.copy()
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}
        for color in drawn_balls:
            drawn_dict[color] = drawn_dict.get(color, 0) + 1
        success = all(drawn_dict.get(color, 0) >= count for color, count in expected_balls.items())
        if success:
            success_count += 1
    return success_count / num_experiments
