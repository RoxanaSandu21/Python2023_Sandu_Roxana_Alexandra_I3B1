class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_salary(self):
        pass

    def get_role(self):
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id)
        self.salary = salary
        self.team_size = team_size

    def get_salary(self):
        return self.salary

    def get_role(self):
        return "Manager"

    def manage_team(self):
        print(self.name, " is managing a team of ", self.team_size, " employees.")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def get_salary(self):
        return self.salary

    def get_role(self):
        return "Engineer"

    def write_code(self):
        print(self.name, " is writing code in ", self.programming_language)


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def get_salary(self):
        return self.salary

    def get_role(self):
        return "Salesperson"

    def meet_sales_target(self):
        if self.sales_target:
            print(self.name, " has met the sales target.")
        else:
            print(self.name, " has not met the sales target yet.")


manager = Manager("Alice", 1, 8000, 5)
engineer = Engineer("Bob", 2, 7000, "Python")
salesperson = Salesperson("Charlie", 3, 6000, True)

print(manager.name, "-", manager.get_role())
manager.manage_team()

print(engineer.name, "-", engineer.get_role())
engineer.write_code()

print(salesperson.name, "-", salesperson.get_role())
salesperson.meet_sales_target()
