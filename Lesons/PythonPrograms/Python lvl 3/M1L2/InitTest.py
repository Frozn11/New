class Car:

    def __init__(self, year, color, car_brand = "mercedes"):
        self.year = year
        self.color = color
        self.car_brand = car_brand
        

    def info(self):
        print("Year of car is", self.year)
        print("Color is", self.color)
        print("Car brand is", self.car_brand)


car = Car(year=2023, color="white")
car.info()