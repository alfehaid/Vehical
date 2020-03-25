from config import Config
from random import shuffle

from coord import Coord

conf = Config()


class Network:

    # The network that contains the friendly
    # cars and the misbehaving attacker cars
    def __init__(self, normal_cars, attackers):
        self.normal_cars = normal_cars
        self.attackers = attackers
        self.injected_points = []
        self.occupied = {}
        for car in normal_cars:
            while self.position_taken(car.position):
                car.randomize()
            self.occupy(car.position)

    def __str__(self):
        return "\n".join([car.report() for car in self.normal_cars]) + "\n" + "\n".join(
            [car.report() for car in self.attackers])

    def step(self):
        self.occupied = {}
        for car in self.normal_cars:
            car.step()
        for attacker in self.attackers:
            attacker.attack()

    def report(self):
        reports = []
        for attacker in self.attackers:
            reports.append(attacker.report())
        for car in self.normal_cars:
            reports.append(car.report())
        shuffle(reports)
        with open(conf.DATA_FILE, 'a') as fd:
            fd.write('\n'.join(reports))
            fd.write('\n')
            fd.close()

    def inject_point(self, car):
        self.injected_points.append(car)
        self.occupied[Coord(car.position.x, car.position.y)] = True

    def occupy(self, pos):
        self.occupied[Coord(pos.x, pos.y)] = True

    def position_taken(self, pos):
        return pos in self.occupied
