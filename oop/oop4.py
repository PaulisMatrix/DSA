#Magic or Dunder Methods


class Employee:
    
    raise_amount = 1.04 

    def __init__(self,first_name,last_name,payment):
        self.first = first_name
        self.last = last_name
        self.pay = payment
        self.email = first_name + "." + last_name + "@email.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #This function is meant to be the unambigous representation of the object
    #and should be used for debugging or logging,etc.
    def __repr__(self):
        return "'{}','{}',{}".format(self.first,self.last,self.pay)

    #Readble representation of an object and is meant to display to the enduser
    def __str__(self):
       return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Rushikesh","Yadwade",35000)
emp2 = Employee("Test","User",40000)

#print(emp1)

#print(emp1 + emp2)

#print(emp1 + emp2)

print(repr(emp1))
print(str(emp1))
print(emp1)

#print(emp1.__repr__())
#print(emp1.__str__())

 
