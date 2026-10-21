class FortniteBot: #Class

    def __init__(self): #Constructor -- Run once at spawn
        self.health = 100 #Attribute

    def take_damage(self, amount): #Method
        self.health -= amount
