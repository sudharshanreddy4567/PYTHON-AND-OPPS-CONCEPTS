class person:
    def __init__(self,name,age):

        self.name=name
        self.age=age
        print(self.age)
        print(self.name)
        print('-'*60)

    def run(self):
        print("run")
        print(self.name)

p1=person('sudha',18)
p1=person('reddy',10)
p1=person('neeraj',8)

p1.run()