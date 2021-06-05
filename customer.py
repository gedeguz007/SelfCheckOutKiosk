class Customer:
    def __init__(self, customerID, firstName, lastName, customerEmail, customerPhonenumber):
        self.customer = Customer(customerID, firstName, lastName, customerEmail, customerPhonenumber)
        self.customerID = customerID

    def getCustomer(self):
        return self.customer

    def setcustomerID(self):
        self.customerID = customerID

    def getcustomerID(self):
        return self.customerID

    def __str__(self):
        return self.customerID
