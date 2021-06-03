import unittest

from menuitem import MenuItem
from menu import Menu
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