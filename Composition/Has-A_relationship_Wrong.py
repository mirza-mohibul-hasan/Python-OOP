class Engine:
    def __init__(self,cc):
        self.cc=cc

    def start(self):
        print("Engine started............")

    def stop(self):
        print("Engine stopped............")

class Car(Engine): # IS-A relationship
    def __init__(self, cc, name):
        super().__init__(cc)
        self.name=name


    def run(self):
        self.start()
    def details(self):
        print(self.name)
        print("Engine:",self.cc,"cc")

ob = Car(4367, "Land Range Rover")
ob.details()

        
    

