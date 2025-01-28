class agent:
    def __init__(self,name,age):
        print("Welcome to the game")
        self.name=name
        self.age=age
        self.health=100
        self.alive=True

    def current_health(self):
        print("Current health of",self.name,' is',self.health)

    def punched(self):
        self.health-=10
    
    def shooted(self):
        self.health-=50
    
    def is_alive(self):
        if self.health>0:
            self.alive=True
        else:
            self.alive=False
        
    def info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("health: ",self.health)
        print("Alive: ",self.alive)
        print("-"*60)

p1=agent("Sudharhan",19)
p1.current_health()
p1.punched()
p1.shooted()
p1.shooted()
p1.info()


p2=agent("reddy",40)
p2.shooted()
p2.info()



p3=agent("reddy",50)
p3.info()