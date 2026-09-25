class bank:
    def withdrow(self,amount):
        return "bank withdrow"

class HDFC(bank):
    def withdrow(self,amount):
        if amount <= 20000:
            print(f"HDFC withdrawal {amount}Rs successful")
        else:
            print("HDFC has unsuccessful withdrow coze of max limit")


class AXIS(bank):
    def withdrow(self,amount):
        if amount <= 30000:
            print(f"AXIS withdrawal {amount}Rs successful")
        else:
            print("AXIS has unsuccessful withdrow coze of max limit")


Banks = [HDFC(),AXIS()]
amounts=[15000,35000]

for bank, amount in zip(Banks, amounts) :
    bank.withdrow(amount)