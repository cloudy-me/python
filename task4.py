class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'The car {self.name} is moving')

    def stop(self):
        print(f'The car {self.name} stopped')

    def turn(self):
        direction = input('Turn direction: ')
        print('The car turned', direction)

    def show_speed(self):
        print(f'Your speed is {self.speed}km/h')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Your speed {self.speed}km/h is very high for a town car!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Your speed {self.speed} is very high for a work car!')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car = Car(80, 'green', 'Audi', False)
car.show_speed()
car.go()
print(car.is_police)
print(car.name)
print(car.color)

work_car = WorkCar(70, 'white', 'BMW')
print(work_car.name)
print(work_car.is_police)
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(30, 'blue', 'Lexus')
print(police_car.is_police)
police_car.show_speed()
