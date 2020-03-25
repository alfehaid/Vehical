from attacker import Attacker
from car import Car


# Forging Random Posititions using Multiple IDs
class MVFL(Attacker):
    attack_type = 'MVFL'

    def __init__(self, car, network,num_spoofs=2):
        super().__init__(car, network, self.attack_type)
        self.spoof_cars = []
        self.join_attacker_network()

        for x in range(num_spoofs):

            spoof_car = Car.random()
            spoof_car.id = next(self.car.id_generator)
            spoof_car.type = 'virtual'
            spoof_car.attack_type = self.attack_type
            spoof_car.network = network
            self.spoof_cars.append(spoof_car)

        network.attackers.append(self)

    def attack(self):
        for spoof_car in self.spoof_cars:
            self.network.inject_point(spoof_car)
            spoof_car.randomize()

    def __str__(self):
        return "\n".join(spoof_car.report() for spoof_car in self.spoof_cars)

    def report(self):
        return "\n".join(spoof_car.report() for spoof_car in self.spoof_cars)
