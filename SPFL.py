from attacker import Attacker
from car import Car


# Forging Path using Single ID
class SPFL(Attacker):
    attack_type = 'SPFL'

    def __init__(self, car, network):
        super().__init__(car, network, self.attack_type)
        self.join_attacker_network()

        # self.attack_type = 'SPFL'
        self.spoof_car = Car.random()
        self.spoof_car.type = 'virtual'
        self.spoof_car.attack_type = self.attack_type
        self.spoof_car.id = self.car.id
        self.spoof_car.generate_xpath()
        self.spoof_car.generate_ypath()
        self.spoof_car.network = network
        network.attackers.append(self)

    def attack(self):
        self.network.inject_point(self.spoof_car)
        self.spoof_car.step()

    def __str__(self):
        return str(self.spoof_car)

    def report(self):
        return self.spoof_car.report()
