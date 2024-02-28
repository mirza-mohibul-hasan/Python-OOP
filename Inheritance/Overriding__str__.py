class Person(object):

    def __init__(self,name) -> None:
        self.name=name
        print(self)

    # def __str__(self):
    #     return self.name
    
ob = Person("Abdullah")