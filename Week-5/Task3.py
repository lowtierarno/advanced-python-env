class Person:
    def __init__(self, name, age):
        # Encapsulation
        self._name = name
        self._age = age

    def introduce(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old."

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the constructor of the parent class
        super().__init__(name, age)
        self.student_id = student_id

    # Method Overriding
    def introduce(self):
        return f"Hi, I'm {self._name}, a student with ID: {self.student_id}."

def display_info(person_object):
    # Polymorphism
    print(person_object.introduce())

if __name__ == "__main__":
    # Create instances
    general_person = Person("John", 45)
    university_student = Student("Alice", 20, "S12345")

    print("--- Demonstration ---")
    
    # Demonstrate Inheritance and Polymorphism
    display_info(general_person)
    display_info(university_student)
    
    # Demonstrate Encapsulation
    print(f"\nAccessing protected attribute (Encapsulation): {university_student._name}")