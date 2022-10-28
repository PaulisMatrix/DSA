#python object-oriented programming

#instance variables are unique to specific instances or objects
#class variables are shared i.e they can be accessed by all the instances or objects of the class.

#Regular methods automatically pass an instance as a first argument known as "self"
#Class methods automatically pass a class as a first argument known as "cls"

class Employee:
    
    raise_amount = 1.04 
    num_of_emps = 0

    def __init__(self,first_name,last_name,payment):
        self.first = first_name
        self.last = last_name
        self.pay = payment
        self.email = first_name + "." + last_name + "@email.com"

        Employee.num_of_emps += 1

    def fullname(self):
        print(f'FirstName: {self.first} LastName: {self.last}')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #regular method to class method
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)  #create the new emp

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp1 = Employee('Rushikesh','Yadwade',30000)
emp2 = Employee('Test','User',40000)


import datetime
my_date = datetime.date(2018,5,10)
print(Employee.is_workday(my_date))



#emp_str_1 = 'New-User-10000'
#emp_str_2 = 'Bay-Max-90000'

#new_emp = Employee.from_string(emp_str_1)

#print(new_emp.first)
#print(new_emp.last)
#print(new_emp.email)
#print(new_emp.pay)


#Employee.set_raise_amount(1.05)  #Employee.raise_amount = 1.05

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

#print(Employee.num_of_emps)

#print(emp1.__dict__)
#print(Employee.__dict__)

#Employee.fullname(emp1)
#Employee.fullname(emp2)
#emp1.fullname()
#emp2.fullname()

#print(emp1.email,"\t",emp1.pay)
#print(emp2.email,"\t",emp2.pay)