class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def calculate_mileage(self):
        return self.year / 80


class Motorcycle(Vehicle):
    def calculate_mileage(self):
        return self.year / 40


class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.towing_capacity = year * 4

    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car("Toyota", "Model1", 2000)
car_mileage = car.calculate_mileage()
print("Car Mileage: ", car_mileage)

motorcycle = Motorcycle("BMW", "Model2", 2002)
motorcycle_mileage = motorcycle.calculate_mileage()
print("Motorcycle Mileage: ", motorcycle_mileage)

truck = Truck("Ford", "Model3", 2000)
truck_towing_capacity = truck.calculate_towing_capacity()
print("Truck Towing Capacity: ", truck_towing_capacity)
