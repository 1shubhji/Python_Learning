class Sports_Academy:
    name = "xyz sports academy"
    
    def __init__(self,sports, fee, timming):
        self.sports = sports
        self.fee = fee
        self.timming = timming

    # this is a instance method
    def infoAboutYourSports(self):
        print(f"So your sport is {self.sports}, and your fee is {self.fee} for a month.your timming of your sports is {self.timming}")

    # this is a static method
    @staticmethod
    def rulesOfAcademy():
        print('''
                1. pls come on time
                2. And always bring your kit 
                ''')

    #this is a class method
    @classmethod
    def nameOfAcademy(cls):
        print(f"So our academy name is {cls.name}.")  
    
    # Magic method also known as dunder Method and also known as double underscore methods.
    def __str__(self):
        return f"so your sport name is {self.sports} and your fee is {self.fee}."
    
    def __add__(self, other):
        return self.fee + other.fee


sport1 = Sports_Academy("Kabaddi",1500,"5pm-7pm")
sport2 = Sports_Academy("cricket",2500,"3pm-5pm")
sport3 = Sports_Academy("wrestling",3500,"10am-12pm")

sport3.nameOfAcademy()


sport1.rulesOfAcademy()

sport2.infoAboutYourSports()

print(sport1 + sport2)