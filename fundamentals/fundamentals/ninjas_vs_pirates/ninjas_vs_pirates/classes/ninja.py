class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    def kunai(self , pirate):
        pirate.health -= self.strength*self.speed/2.5
        return self
    def smokebomb(self , pirate):
        self.speed = 7
        pirate.strength -= 8
        return self
    def herbs(self):
        self.health += 15
        return self
