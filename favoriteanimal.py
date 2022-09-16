class tiger:
    def __init__(self, height, color, stripes):
        self.stripePattern = stripes
        self.numLegs = 4
        self.color = color
        self.height = height

    def getstripePattern(self):
        return self.stripePattern
    
    def setstripePattern(self, stripes):
        self.stripePattern = stripes

def main():
    tiger1 = tiger("2.5m", "orange", "stripeless")
    tiger2 = tiger("4m", "scarlet", "stripePattern3")
    print("tiger 1 has " + tiger1.getstripePattern() + " pattern")
    print("tiger 2 has " + tiger2.getstripePattern() + " pattern")
    tiger1.setstripePattern("stripePattern1")
    print("tiger 1 now has " + tiger1.getstripePattern() + " pattern")
if __name__ == "__main__":
    main()
    
        
