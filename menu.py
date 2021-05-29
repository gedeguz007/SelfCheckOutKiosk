from menuitem import MenuItem

class Menu():
    def __init__(self):
        self.menuItems = []

    def addmenuItems(self, itemName):
        self.menuItems.append(itemName)

    def getmenuItems(self):
        return self.menuItems

    def removeItem(self, itemName):
        return self.menuItems.remove(itemName)

    def setItem(self, itemName):
        return self.menuItems.set(itemName)