class Paitent:
    def __init__(self,name,days):
        self.name = name
        self.days = days

    
class generalpaitent(Paitent):
    def calculate_bill(self):
        daily_charge= self.days * 2000
        fixed_charge= 500

        return daily_charge + fixed_charge

class Emergencypaitent(Paitent):
    def calculate_bill(self):
        daily_charge = self.days * 3000
        fixed_charge= 1000

        return daily_charge + fixed_charge

class ICUpaitent(Paitent):
    def calculate_bill(self):
        daily_charge = self.days *5000
        fixed_charge = 2000

        return daily_charge + fixed_charge

paitents = [generalpaitent("YASH",4),
           Emergencypaitent("ARYAN",5),
           ICUpaitent("SAHIL",10)
           ]

for Paitent in paitents:
    print(f"{Paitent.name}, the bill is: {Paitent.calculate_bill()}")