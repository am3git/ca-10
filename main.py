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

ford = Car(2020, "Ford", "Gas")
ford.report()
ford.drive()
ford.park()
ford.fill()