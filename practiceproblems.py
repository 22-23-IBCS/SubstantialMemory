import random
import math
def problem1(x,y,z):
    mean = (z+y+x)/3
    if x < y:
        if y<z:
            median = y
        else:
            if x<z:
                median = z
            else: median = x
    else:
        if x<z:
            median = x
        else:
            if y<z:
                median = z
            else: median = y
    return mean, median

def problem2():
    n=random.randint(1,100)
    if n%2==0:
        x=true
    else:
        x=false
    if n%3==0:
        x=true
    else:
        x=false
    if n%5==0:
        x=true
    else:
        x=false

    if x==true:
        return True
    if x==false:
        return False

def problem3():
    l=[]
    for i in range(10):
        nu=random.randint(1,50)
        l.append(nu)
    mx=l[0]
    mn=l[0]
    for i in l:
        if i>mx:
            mx=i
        if i<mn:
            mn=i
    r=mx-mn
    return mx, mn, r
            
def problem4(x,y):
    l=[x,y]
    r=math.sqrt((x*x+y*y))
    theta=math.asin(y/r)
    return [r,theta]

def problem5():
    name=input("What's your name?")
    name=name.lower()
    score=0
    points={"a":1,"b":3,"c":3,"d":3,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,
            "l":1,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":1,
            "w":4,"x":8,"y":4,"z":10}
    for char in name:
        p=points.get(char)
        score=score+p
    print(score)
    

def main():
    print(problem4(1,2))
if __name__ == "__main__":
    main()


    
