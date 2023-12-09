class employee:
    'this is employee class'
    name = 'empty'
    def printname(self):
        print(self.name)


emp = employee()
emp.printname()

print(employee.__dict__)
print("______________")

emp.city ="algiers"
print(emp.__dict__) #will print dict {"city":"algiers"} 
