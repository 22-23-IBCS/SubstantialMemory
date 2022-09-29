import turtle

class Artist:
    def __init__(self,t):
        self.t = t

    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def circle(self, size = 100):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size/100)

    def star(self, size = 100):
        for i in range(5):
            self.t.right(144)
            self.t.forward(size)

    def polygon(self, size=100, sides=3):
        for i in range (sides):
            self.t.right(360/sides)
            self.t.forward(size)

    def smile(self):
        for i in range(360):
            self.t.right(1)
            self.t.forward(1)
        self.t.right(90)
        self.t.penup()
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.pendown()
        self.t.right(90)
        self.t.forward(35)
        self.t.penup()
        self.t.right(90)
        self.t.forward(40)
        self.t.right(90)
        self.t.pendown()
        self.t.forward(35)
        self.t.right(180)
        self.t.penup()
        self.t.forward(50)
        self.t.pendown()
        for i in range (180):
            self.t.left(1)
            self.t.forward(1/3)
            
def main():
    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    art = Artist(t)
    art.smile()
    art.circle()
    art.square()
    art.triangle()
    art.star()
    art.polygon(100,19)

if __name__=="__main__":
    main()
