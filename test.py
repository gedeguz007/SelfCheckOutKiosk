import unittest

from menuitem import MenuItem
from menu import Menu
from customer import Customer
from payment import Payment
from checkoutkiosk import CheckoutKiosk

class MenuItemTest (unittest.TestCase):

    def setUp(self):
        self.menuItem = MenuItem('Burrito1', 'Carne Asada Burrito', 4.99)

    def test_menuItemstring(self):
        self.assertEqual(str(self.menuItem), 'Carne Asada Burrito')

    def test_itemID(self):
        self.assertEqual(self.menuItem.getitemID(), 'Burrito1')

    def test_itemName(self):
        self.assertEqual(self.menuItem.getitemName(), 'Carne Asada Burrito')

    def test_costPerUnit(self):
        self.assertEqual(self.menuItem.getcostPerUnit(), 4.99)

class MenuTest (unittest.TestCase):

    def setUp(self):
        self.menuItem1 = MenuItem('Burrito2', 'Lengua Burrito', 5.49)
        self.menuItem2 = MenuItem('Taco1', 'Carnitas Taco', 1.99)
        self.menu = Menu()
        self.menu.addmenuItems(self.menuItem1)
        self.menu.addmenuItems(self.menuItem2)

    def test_addmenuItems(self):
        self.menuItem3 = MenuItem('Taco2', 'Chicken Taco', 1.99) 
        self.menu.addmenuItems(self.menuItem3)
        items = self.menu.getmenuItems()
        self.assertEqual(len(items), 3)

class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(8617, 'Gabe DeGuzman', 'flipzides@yahoo.com', '123-456-7890')

    def test_customerID(self):
        self.assertEqual(self.customer.getcustomerID(), 8617)

    def test_customerEmail(self):
        self.assertEqual(self.customer.getcustomerEmail(), 'flipzides@yahoo.com')

    def test_customerName(self):
        self.assertEqual(self.customer.getcustomerName(), 'Gabe DeGuzman')
    
    
    def test_customerPhonenumber(self):
        self.assertEqual(self.customer.getcustomerPhonenumber(), '123-456-7890')


"""
Not working: TypeError: __init__() missing 3 required arguments 'itemID', 'itemName', and 'costPerUnit'
class CheckoutKioskTest (unittest.TestCase):

    def setUp(self):
        self.menuItem4 = MenuItem('Burrito3', 'Carnitas Burrito', 5.49)        
        self.menuItems = MenuItem()
        self.menuItem.addmenuItems(self.menuItem4)
        

    def test_addmenuItems(self):
        self.menuItem5 = MenuItem('Taco3', 'Veggie Taco', 1.49)
        self.menuItems.addmenuItems(self.menuItem5)
        items = self.menuItems.getmenuItems()
        self.assertEqual(len(items), 2)

    ##def test_getmenuItems(self):
     ##   self
"""