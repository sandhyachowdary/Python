#variable = class_name()

#ex: x = employee()

#How many objects we can create in one class
#We can create multiple  number of objects to a class



class employee():
    def assign(self):
        self.idno = 101
        self.name = "Sandhya"
    def display(self):
        print(self.idno)
        print(self.name)

e1 = employee()
e1.assign()
e1.display()


#employee = class, assign,display= instance method, self.idno,name = instance variable , e1= global variable



#example on static and instance variable

class employee():
    company_name = "kvana"
    def assign(self):
        self.idno = 101
        self.name = "sandhya"
    def display(self):
        print(self.idno)
        print(self.name)
        print(employee.company_name)
        print(employee.company_cno)
    company_cno = 9876543210
e1 = employee()
e1.assign()
e1.display()





class employe:
    comp_name = "kvana"
    def assign(self,id,name):
        self.idno = id
        self.name = name

    def display(self):
        print(employe.comp_name)
        print(employe.company_cno)
        print(self.idno)
        print(self.name)
    company_cno = 998876653

e1 = employe()
e1.assign(101,"Sandhya")
e1.display()

e2 = employe()
e2.assign(102,"chow")
e2.display()
print(e1.comp_name)

