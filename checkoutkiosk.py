from payment import Payment
from menuitem import MenuItem
from menu import Menu

class CheckoutKiosk():

    def __init__(self, quantity):
        self.menuItems = []
        self.quantity = quantity
        
    def addmenuItems(self, menuItem):
        self.menuItems.append(menuItem)

    def getmenuItems(self):
        return self.menuItems

    def getQuantity(self):
        return self.quantity

    def calculateQuantity(self):
        totalQuantity = 0.0
        for i in self.itemName:
            totalQuantity += i.getitemName().quantity
            return totalQuantity

    def calculateTotal(self):
        totalPrice = 0.0
        for p in self.Price:
            totalPrice += p.getitemName().costPerUnit * p.quantity
        paymentAmount = Payment(totalPrice)
        return paymentAmount