class A:
    def __init__(self, name, nameclass=None):
        self.name = nameclass B(A):
    def __init__(self, personName, personAge):
        self.age = personAge
        A.nam = personName
    def __str__(self):
        return'Person(name =' +self.name +',Age:'+str(self.age)+')' = B("ree, 21")
    print (b.__str__())