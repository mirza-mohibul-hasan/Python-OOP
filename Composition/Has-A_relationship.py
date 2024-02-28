class Engine:
    def __init__(self,cc):
        self.cc=cc

    def start(self):
        print("Engine started............")

    def stop(self):
        print("Engine stopped............")

class Car:
    def __init__(self, cc, name):
        self.name=name
        self.engine=Engine(cc)


    def run(self):
        self.engine.start()

    def details(self):
        print(self.name)
        print("Engine:",self.engine.cc,"cc")

ob = Car(4367, "Land Range Rover")
ob.details()

        
    

