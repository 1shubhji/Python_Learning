class MobilePhone:
    def __init__(self,brand,battery,password):
        self.brand = brand
        self._battery = battery
        self._password = password

    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self,charge):
        if 0 <= charge <= 100:
            self._battery = charge

        else:
            raise ValueError("charge must be between 0 and 100.")

    @property    
    def password(self):
        return "******"
    
    @password.setter
    def password(self,p):
        if len(str(p)) == 6:
            self._password = p
        else:
            raise ValueError("Hey password must be alphabets and of 6 length")