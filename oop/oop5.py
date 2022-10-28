class Employee:

    def __init__(self,first_name,last_name,payment):
        self.first = first_name
        self.last = last_name
        self.pay = payment
        
    #This decorator enables us to access the email method as an attribute
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        firstname,lastname = name.split(' ')
        self.first = firstname
        self.last = lastname

    
    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None
    
emp1 = Employee("Rushikesh","Yadwade",45000)

emp1.fullname = 'Test User'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname







