from graphics import*
from Button import*

def main ():

    win = GraphWin("Character Creation", 800, 900)

    b1 = Button(win, Point(650,50), Point(750,125), "salmon", "Face")
    b2 = Button(win, Point(650,150), Point(750,225), "salmon", "Big Eyes")
    b3 = Button(win, Point(650,250), Point(750,325), "salmon", "Small Eyes")
    b4 = Button(win, Point(650,350), Point(750,425), "salmon", "Big Nose")
    b5 = Button(win, Point(650,450), Point(750,525), "salmon", "Small Nose")
    b6 = Button(win, Point(650,550), Point(750,625), "salmon", "Smile")
    b7 = Button(win, Point(650,650), Point(750,725), "salmon", "Frown")
    Face = Oval(Point(150,50), Point(550,550))

    bigEye1 = Circle(Point(350,250), 40)
    #bigEye1.draw(win)
    bigEye2 = Circle(Point(450,250), 40)
    #bigEye2.draw(win)
    smallEye1 = Circle(Point(350,250), 20)
    #bigEye1.draw(win)
    smallEye2 = Circle(Point(450,250), 20)
    #bigEye2.draw(win)
    bigNose1 = Line(Point(400, 300), Point(500,425))
    bigNose2 = Line(Point(500,425), Point(400,425))
    bigNose = [bigNose1, bigNose2]
    smallNose1 = Line(Point(400, 300), Point(450,350))
    smallNose2 = Line(Point(450,350), Point(400,350))
    smallNose = [smallNose1, smallNose2]
    smile1 = Line(Point(350, 450), Point(400,525))
    smile2 = Line(Point(400,525), Point(450, 450))
    smile = [smile1, smile2]
    frown1 = Line(Point(300, 525), Point(350,450))
    frown2 = Line(Point(350,450), Point(400,525))
    frown = [frown1, frown2]
    Quit = quitButton(win, Point(650,750), Point(750,825))

    m = win.getMouse()
    while True:
        m = win.getMouse()
        if b1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if b2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            bigEye1.undraw()
            bigEye1.draw(win)
            bigEye2.undraw()
            bigEye2.draw(win)

        if b3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye1.draw(win)
            smallEye2.undraw()
            smallEye2.draw(win)

        if b4.isClicked(m):
            smallNose1.undraw()
            smallNose2.undraw()
            bigNose1.undraw()
            bigNose1.draw(win)
            bigNose2.undraw()
            bigNose2.draw(win)
            
        if b5.isClicked(m):
            bigNose1.undraw()
            bigNose2.undraw()
            smallNose1.undraw()
            smallNose1.draw(win)
            smallNose2.undraw()
            smallNose2.draw(win)

        if b6.isClicked(m):
            frown1.undraw()
            frown2.undraw()
            smile1.undraw()
            smile1.draw(win)
            smile2.undraw()
            smile2.draw(win)
            
        if b7.isClicked(m):
            smile1.undraw()
            smile2.undraw()
            frown1.undraw()
            frown1.draw(win)
            frown2.undraw()
            frown2.draw(win)
            
        if Quit.isClicked(m):
            break

        

    win.close()

if __name__ == "__main__":
    main()
