class Weather:
    def __init__(self, location):
        """
        Initialize the weather report for a location with default values.
        """
        self.location = location
        self.temperature = None  # Default value for temperature
        self.humidity = None  # Default value for humidity

    def update_weather(self, temp, hum):
        """
        Update the temperature and humidity for the location.
        """
        self.temperature = temp
        self.humidity = hum
        print(f"Weather updated for {self.location}.")

    def display_weather(self):
        """
        Display the weather details in a formatted way.
        """
        if self.temperature is not None and self.humidity is not None:
            print(f"Weather Report for {self.location}:")
            print(f"  Temperature: {self.temperature}°C")
            print(f"  Humidity: {self.humidity}%")
        else:
            print(f"No weather data available for {self.location}. Please update the weather first.")

# Example Usage
# Create a Weather instance
city_weather = Weather("Chennai")

# Display weather details before updating
city_weather.display_weather()

# Update weather details
city_weather.update_weather(32, 75)

# Display weather details after updating
city_weather.display_weather()
