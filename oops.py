class Car:
    is_running=False
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        self.is_running = True
        print(f'{self.model}{self.make} car is running')
    def stop(self):
        self.is_running = False
        print(f'{self.model}{self.make} car is stopped')
    def info(self):
        print(f'{self.model}{self.make} car info')
        print(f'Make: {self.make}')
        print(f'{self.is_running}')
c=Car('Ford','Mustang',1999)
c2=Car('Ford','Mustang',9009)
c.start()
c.stop()
c.info()
c2.info()
class Bank:
    def __init__(self,account_number,holder_name,initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.initial_balance = initial_balance
    def deposit(self,amount):
        self.initial_balance = self.initial_balance + amount
        print(f'{self.account_number}{self.holder_name} is deposited to {self.initial_balance}')
    def withdraw(self,amount):
        if self.initial_balance >= amount:
            self.initial_balance = self.initial_balance - amount
            print(f'{self.account_number}{self.holder_name} is withdrawn from {self.initial_balance}')
        else:
            print(f'{self.account_number}{self.holder_name} is not withdrawn shold be +ve')
    def balence(self):
        print(f'{self.account_number}{self.holder_name} has{self.initial_balance}balanced')
    def info_Details(self):
        print(f'{self.account_number}{self.holder_name} has{self.initial_balance}balanced')
B=Bank(202,'DD',0   )
B.deposit(100)
B.withdraw(100)
B.info_Details()
B.balence()
B.deposit(100)
B.balence()
B.withdraw(1000)
class Shape:
    def __init__(k,name):
        k.name = name
    def display(k):
        print(f'This is {k.name}')
class TwoD(Shape):
    def __init__(k,name,sides):
        super().__init__(name)
        k.sides = sides
    def display_sides(k):
        print(f'This is {k.sides}')
class Square(TwoD):
    def __init__(self,side_length,name="square",sides=4,):
        super().__init__(name,sides)
        self.side_length = side_length
    def Area(self):
        print(f'This is {self.name} ')
        print(f'This is {self.sides} side')
        print(f'This is Area{self.side_length**2} ')
s=Shape('square')
s.display()
s=Square(side_length=5)
s.Area()

class fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other):
        num = (self.num* other.den) + \
              (other.num * self.den)
        den = self.den * other.den
        return fraction(num, den)
    def __eq__(self, other):
        return (self.num * other.den ==
                other.num * self.den)
S=fraction(1,2)
S2=fraction(1,3)
S3=fraction(2,3)
print(S+S2+S3)
print(S+S2)
print(S,S2)
print(S==S2)
class employee:
    def __init__(self,employee_id ,name ,salary):
        self.employee_id = employee_id
        self.name = name
        self._salary = salary
    def get_info(self):
        return f'Employee {self.employee_id} {self.name}{self._salary}has info'
    def get_salary(self):
        return self._salary
    def set_salary(self,salary):
        if int(salary) < 0:
            raise ValueError('Salary cannot be negative')
        else:
            self._salary = salary
            print(f'Salary set to {self._salary}')
class Manager(employee):
    def __init__(self,employee_id,name ,salary,department):
        super().__init__(employee_id,name ,salary)
        self.department = department
    def assign_task(self,employee,task_description):
        print(f"Manager {self.name} assigned'{task_description}'to{employee.name}.)")
    def get_manager_info(self):
        return f"Manager {self.name} assigned'{self.department}'s info{self._salary}"
E=employee(2,'James',2000)

print(E.get_info())
print(E.get_salary())
E.set_salary("200")
print(E.get_salary())
M=Manager(1,'James',2000,"IT")
M.assign_task(E,"k")
print(M.get_manager_info())