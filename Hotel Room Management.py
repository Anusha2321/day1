class HotelRoom:
    def __init__(self, room_number, rate_per_night):
        
        self.room_number = room_number
        self.is_occupied = False
        self.rate_per_night = rate_per_night

    def book_room(self):
        
        if not self.is_occupied:
            self.is_occupied = True
            print(f"Room ",self.room_number,"has been booked.")
        else:
            print(f"Room",self.room_number," is already occupied.")

    def checkout_room(self):
        
        if self.is_occupied:
            self.is_occupied = False
            print("Room",self.room_number," has been checked out.")
        else:
            print("Room",self.room_number,"is already vacant.")

    def display_status(self):
        
        status = "Occupied" if self.is_occupied else "Vacant"
        print(f"Room Number: {self.room_number}, Rate per Night: {self.rate_per_night}, Status: {status}")


# Example Usage
room1 = HotelRoom(101, 1500)
room2 = HotelRoom(102, 2000)

# Display initial status
room1.display_status()
room2.display_status()

# Book a room
room1.book_room()
room1.display_status()

# Try booking the same room again
room1.book_room()

# Checkout a room
room1.checkout_room()
room1.display_status()

# Try checking out an already vacant room
room1.checkout_room()

# Book another room
room2.book_room()
room2.display_status()
