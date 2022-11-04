import random

class Human:
    def __init__(self, name='Human', job=None, hom=None, car=None):
        self.name = name
        self.maney = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.hopping('food')
        else:
            if self.satiety >= 100
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20
                self.hopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
