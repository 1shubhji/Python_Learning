class Supplements:
    
    def __init__(self,productName, prodcutQuantity, productPrice):
        self.productName = productName
        self.prodcutQuantity = prodcutQuantity
        self.productPrice = productPrice
    
    def supplementInfo(self):
        print(f"So this supplement is {self.productName} and it's {self.prodcutQuantity}gm of packet cost's you around {self.productPrice}. So Very helpful prodcut. ")

s1 = Supplements("Creatine Monohydrate",100,599)

s1.supplementInfo()
print(s1.productName)