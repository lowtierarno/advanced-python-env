class Employee:
    def __init__(self, name, salary):
        self.name = name
        # Private attribute
        self.__salary = salary

    def get_salary(self):
        # Getter method to access the private salary attribute.
        return self.__salary

    def get_role(self):
        # Returns the general role of the employee.
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # Inherit name and salary from Employee
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        # Overrides the parent method to return a specific role.
        return "Manager"

    def get_bonus(self):
        # Additional method specific to the Manager class.
        return self.bonus

def print_employee_details(employee_list):
    """
    Accepts a list of Employee objects and prints their details.
    Shows polymorphism as it calls get_role() on different object types.
    """
    print(f"{'Name':<10} | {'Role':<10} | {'Salary':<10}")
    print("-" * 35)
    for emp in employee_list:
        print(f"{emp.name:<10} | {emp.get_role():<10} | {emp.get_salary():<10}")

if __name__ == "__main__":
    # 1. Create a list of Employee and Manager objects
    staff = [
        Employee("Alice", 50000),
        Manager("Bob", 80000, 15000),
        Employee("Charlie", 45000)
    ]

    # 2. Demonstrate the function
    print_employee_details(staff)
    
    # 3. Demonstrate specific Manager method
    manager_bob = staff[1]
    print(f"\nSpecific Bonus for {manager_bob.name}: {manager_bob.get_bonus()}")