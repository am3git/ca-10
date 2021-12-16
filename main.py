class Car:
    def __init__(self, year="0", model="new", fuel_type="green"):
        self.year = year
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        print("Driving..")

    def park(self):
        print("Parked..")

    def fill(self):
        print("Filled..")

    def report(self):
        print(f"Year:{self.year} | Model:{self.model} | Fuel:{self.fuel_type}")


class ElectricCar(Car):
    def __init__(self, year="0", model="new", fuel_type="electric"):
        super().__init__(year, model, fuel_type)

    def parent_drive(self):
        super().drive()

    def parent_park(self):
        super().park()

    def charge(self):
        print("Battery is full")

    def autopilot(self):
        print("Autopilot is ON ")

    def parent_report(self):
        super().report()

ford = Car(2020, "Ford", "Gas")
ford.report()
ford.drive()
ford.park()
ford.fill()

print("\n")

volt = ElectricCar(2000, "Volt", "Electric")
volt.parent_report()
volt.parent_drive()
volt.parent_park()
volt.charge()
volt.autopilot()

print("\n")

opel = Car(1990, "Opel", "Diesel")
opel.report()
opel.drive()
opel.park()
opel.fill()
