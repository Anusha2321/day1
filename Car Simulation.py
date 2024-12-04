class Car:
    def __init__(self, make, model):
        """
        Initialize a car with make, model, and default fuel level of 100.
        """
        self.make = make
        self.model = model
        self.fuel_level = 100  # Default fuel level

    def drive(self, distance):
        """
        Drive the car, reducing the fuel level based on the distance.
        """
        required_fuel = distance / 10  # 1 unit of fuel for every 10 km
        if self.fuel_level >= required_fuel:
            self.fuel_level -= required_fuel
            print(f"Car driven for {distance} km. Fuel level is now {self.fuel_level:.2f}.")
        else:
            print("Not enough fuel to drive the requested distance. Please refuel.")

    def refuel(self, amount):
        """
        Refuel the car, increasing the fuel level by the specified amount.
        """
        if self.fuel_level + amount > 100:
            self.fuel_level = 100
            print("Fuel tank is now full.")
        else:
            self.fuel_level += amount
            print(f"Car refueled. Fuel level is now {self.fuel_level:.2f}.")

    def display_status(self):
        """
        Display the car's make, model, and current fuel level.
        """
        print(f"Car Make: {self.make}, Model: {self.model}, Fuel Level: {self.fuel_level:.2f}")

# Example Usage
# Create a car instance
my_car = Car("Toyota", "Corolla")

# Display car status
my_car.display_status()

# Drive the car
my_car.drive(50)  # Reduces fuel by 5
my_car.drive(600)  # Attempt to drive more than fuel allows

# Refuel the car
my_car.refuel(30)  # Adds 30 units
my_car.refuel(80)  # Attempts to overfill

# Display car status again
my_car.display_status()
