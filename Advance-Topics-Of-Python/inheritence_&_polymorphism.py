class Engine:
    def __init__(self,engineModel, type):
        self.engineModel = engineModel
        self.type = type
        print("Parent Class is here, Hi Buddy !")

    def enginePower(self):
        print("This engine is very Heavy")

    def speed(self):
        print("This engine will go at the speed of 200km/h .")


class Car(Engine):
    def __init__(self, engineModel, type,brand,color,model):
        super().__init__(engineModel, type)
        self.brand = brand
        self.color = color
        self.model = model
        

    def speed(self):
        super().speed()
        print('This is my car speed and it will go to 400km/h. ')


car1 = Car("V8","Pta ni","Ferrari","Red","KuchBhi")
car1.speed()