class MenuItem():

    def __init__(self, itemID, itemName, costPerUnit):
        self.itemID  = itemID
        self.itemName = itemName
        self.costPerUnit = costPerUnit

    def getitemID(self):
        return self.itemID

    def getitemName(self):
        return self.itemName

    def getcostPerUnit(self):
        return self.costPerUnit

    def __str__(self):
        return self.itemName