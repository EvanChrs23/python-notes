class Car:

    def __init__(self, brand, accelerate, brake):
        self.brand = brand
        self.speed = 0
        self.accelerate = accelerate
        self.brake = brake

    def increase_speed(self):
        self.speed += self.accelerate
        print(f"Car Brand: {self.brand:<10}Car Speed: {self.speed} km/h")

    def decrease_speed(self):
        self.speed -= self.brake
        print(f"Car Brand: {self.brand:<10}\t\tCar Speed: {self.speed} km/h")

car1 = Car("BYD", 5, 4)
car2 = Car("Proton", 4, 3)

car1.increase_speed()
car2.increase_speed()
car1.decrease_speed()
car2.decrease_speed()