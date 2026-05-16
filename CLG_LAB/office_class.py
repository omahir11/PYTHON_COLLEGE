class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"Name: {self.name},Age:{self.age}")
class Employee(Person):
    def __init__(self,name,age,erp_id,department):
        super().__init__(name,age)
        self.erp_id=erp_id
        self.department=department
    def display_employee(self):
        print(f"Erp ID:{self.erp_id},Department:{self.department}")
class Manager(Employee):
    def __init__(self,name,age,erp_id,department,team_size):
        super().__init__(name,age,erp_id,department)
        self.team_size=team_size
    def display_manager(self):
        print(f"team Size:{self.team_size}")
manager=Manager("edwin",25,"E101","IT",10)
manager.display_person()
manager.display_employee()
manager.display_manager()
