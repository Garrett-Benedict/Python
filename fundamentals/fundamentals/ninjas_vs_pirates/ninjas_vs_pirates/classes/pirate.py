class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    def gun(self , ninja):
        ninja.health -= self.strength*self.speed/2
        return self
    def rum (self):
        self.strength += 30
        return self
    def oranges(self):
        self.health += 20
    def sand(self , ninja):
        ninja.speed -= 3

