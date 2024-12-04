class Student:
    def __init__(self, name, roll_number):
        """
        Initialize the Student with name, roll number, and an empty dictionary for marks.
        """
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        """
        Add or update the marks for a specific subject.
        """
        self.marks[subject] = mark
        print(f"Added/Updated marks for {subject}: {mark}")

    def get_average(self):
        """
        Calculate and return the average of all marks.
        """
        if len(self.marks) == 0:
            print("No marks available to calculate the average.")
            return 0.0
        total_marks = sum(self.marks.values())
        average = total_marks / len(self.marks)
        return average

    def display_details(self):
        """
        Display the student's details including name, roll number, and average marks.
        """
        average_marks = self.get_average()
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {average_marks:.2f}")


# Example Usage
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Add marks for subjects
student1.add_marks("Math", 85)
student1.add_marks("Science", 90)
student1.add_marks("English", 88)

student2.add_marks("Math", 75)
student2.add_marks("Science", 80)
student2.add_marks("History", 78)

# Display details
print("\nStudent 1 Details:")
student1.display_details()

print("\nStudent 2 Details:")
student2.display_details()
