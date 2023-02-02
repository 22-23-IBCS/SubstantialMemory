from graphics import*
import time
def main():
    win = GraphWin("demo", 500, 500)
    ball=Circle(Point(250,250), 10)
    x=0
    start=time.time()
    posy=ball.getCenter().getY()
    ball.draw(win)
    while (posy-10)>0:
        now=time.time()
        x=x+9.8*(now-start)
        ball.move(0,x)
        posy=ball.getCenter().getY()

if __name__ == "__main__":
    main()
