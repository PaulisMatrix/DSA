#inheritance 


class Employee:

    raise_amount = 1.04

    def __init__(self,first_name,last_name,payment):
        self.first = first_name
        self.last = last_name
        self.pay = payment
        self.email = first_name + "." + last_name + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #OR Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        
        super().__init__(first,last,pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.fullname())



dev1 = Developer("Rushikesh","Yadwade",80000,"Python")
dev2 = Developer("Test","User",6000,"C++")

mgr1 = Manager("Susan","Smith",90000,[dev1])
#mgr1.add_emp(dev2)

#mgr1.remove_emp(dev1)

#mgr1.print_emps()
#print(mgr1.email)


print(issubclass(Developer,Employee))
