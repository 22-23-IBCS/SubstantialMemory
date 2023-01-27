from graphics import *
from Button import *
def main():
    win = GraphWin("My window", 800, 600)
    noun= Text(Point(80,100), ("Noun"))
    noun.draw(win)
    n1= Entry(Point(200,100),15)
    n1.draw(win)

    noun2= Text(Point(80,200), ("Noun2"))
    noun2.draw(win)
    n2= Entry(Point(200,200),15)
    n2.draw(win)

    Verb= Text(Point(80,300), ("Verb"))
    Verb.draw(win)
    v= Entry(Point(200,300),15)
    v.draw(win)
    
    adj= Text(Point(80,400), ("Adjective"))
    adj.draw(win)
    a= Entry(Point(200,400),15)
    a.draw(win)

    exc= Text(Point(80,500), ("Exclamation"))
    exc.draw(win)
    x= Entry(Point(200,500),15)
    x.draw(win)


    B= Button(win,Point(600,400), Point(700,500), "tomato", "Generate")
    while True:
        m=win.getMouse()
        if B.isClicked(m):
            n1=n1.getText()
            n2=n2.getText()
            v=v.getText()
            a=a.getText()
            x=x.getText()
            win.close
            win1= GraphWin("MadLib", 800, 600)
            Story= Text(Point(250,250), (n1 + " was having an amazing day till"))
            Story1= Text(Point(250,260), ("he was told by his mom to " + v +". "))
            Story2= Text(Point(250,270), ("They yelled " + x +". " + n2 + " laughed in response"))
            Story.draw(win1)
            Story1.draw(win1)
            Story2.draw(win1)
if __name__ == "__main__":
    main()
