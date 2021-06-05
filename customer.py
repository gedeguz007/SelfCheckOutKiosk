class Customer:
    def __init__(self, customerID, customerName, customerEmail, customerPhonenumber):
        self.customerID = customerID
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.customerPhonenumber = customerPhonenumber

    def getcustomerID(self):
        return self.customerID

    def setcustomerID(self):
        self.customerID = customerID

    def getcustomerName(self):
        return self.customerName

    def getcustomerEmail(self):
        return self.customerEmail

    def getcustomerPhonenumber(self):
        return self.customerPhonenumber

    def __str__(self):
        return self.customerName
