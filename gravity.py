from graphics import*
import time
def main():
    win = GraphWin("demo", 500, 500)
    ball=Circle(Point(250,250), 10)
    x=0
    posy=ball.getCenter().getY()
    ball.draw(win)
    now=time.time()
    while True:
        while (posy+25)<500:
            now1=now
            now=time.time()
            posy=ball.getCenter().getY()
            ball.move(0,x)
            x=x+9.8*(now-now1)
            now=time.time()
            print("1")
        while x>0:
            now1=now
            now=time.time()
            negx= x-2*x
            ball.move(0, negx)
            x=x-9.8*(now-now1)
            posy=ball.getCenter().getY()
            now=time.time()
            print(x)
            print(negx)
        if posy>450:
            break
    while (posy+25)<500:
            now1=now
            now=time.time()
            posy=ball.getCenter().getY()
            ball.move(0,x)
            x=x+9.8*(now-now1)
            now=time.time()
            print("1")
    

        

if __name__ == "__main__":
    main()
