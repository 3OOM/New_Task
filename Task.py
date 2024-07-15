
# Assignment Code

traffic_light ="Green"
speed_limit =60

class Vehicle:
    def start_engine(self):
        message ="Engine started."
        print(message)


class Car(Vehicle):
    def __init__(self, make):
        self.make =make

    def start_engine(self):
        message ="Car engine started."
        print(message)



class Bike(Vehicle):
    def __init__(self, bike_type):
       self.type=bike_type

    def start_engine(self):
        message ="Bike engine started."
        print(message)




my_car =Car(make="Supra")
my_bike =Bike(bike_type="Sports")

#Calling Functions
my_car.start_engine()

my_bike.start_engine()

print("Traffic Light: "  + traffic_light)
print(f"Speed Limit: {speed_limit}")
