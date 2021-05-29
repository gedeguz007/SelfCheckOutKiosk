class Payment():

    def __init__(self, paymentAmount):
        self.paymentAmount =  paymentAmount

    def __str__(self):
        self.paymentAmount = round(self.paymentAmount, 2)
        result = "The total amount will be $" + str(self.paymentAmount) + "."
        return result