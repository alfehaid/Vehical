import time

from car import Car


class Attacker:
    types = ['SVFL', 'MVFL', 'SPFL', 'MPFL']

    def __init__(self, car, network, attack_type):
        self.attack_type = attack_type
        self.car = car
        self.car.network = network
        self.car.type = 'attacker'
        self.car.attack_type = self.attack_type
        self.network = network

    def __str__(self):
        return str(self.car)

    def join_attacker_network(self):
        self.network.attackers.append(Attacker(self.car, self.network, self.attack_type))

    def attack(self):
        self.car.step()

    def report(self):
        return self.car.report()
