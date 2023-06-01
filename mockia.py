import string
import random
from graphics import*
from Button import*
def genDict(shift):
    letters= list(string.ascii_lowercase)
    code={" ":" "}
    for i  in range(len(letters)):
        place=(i+shift)%26
        letter={letters[i]:letters[place]}
        code.update(letter)
    return code
def encoder(text):
    letters= list(string.ascii_lowercase)
    shift=random.randint(1,10)
    code=genDict(shift)
    encodedMessage=""
    sym=["!","@","#","$","%","^","&","*","<",">"]
    for char in text:
        if char not in code:
            a="only lowercase letters"
            return a
    for i in range(len(text)):
        encodedMessage=encodedMessage+code[text[i]]
    sym=sym[shift-1]
    pos=random.randint(1,len(text)-1)
    encodedMessage=encodedMessage[0:pos] + sym + encodedMessage[pos:len(text)]
    return encodedMessage
def decoder(text):
    sym=["!","@","#","$","%","^","&","*","<",">"]
    i=1
    for code in sym:
        if code in text:
            shift=26-(sym.index(code)+1)
            text=text.replace(code,"")
            i=0
            break
    if i == 1:
        a="not the program's encryption"
        return a
    code=genDict(shift)
    for char in text:
        if char not in code:
            a="only lowercase letters"
            return a
    decodedMessage=""
    for char in text:
        decodedMessage=decodedMessage+code[char]
    return decodedMessage
            
def main():
    win = GraphWin("Encryption", 800, 900)
    b1=Button(win, Point(300,300), Point(500,375), "salmon", "Encode")
    b2=Button(win, Point(300,450), Point(500,525), "salmon", "Decode")
    Quit = quitButton(win, Point(650,750), Point(750,825))
    

    m=win.getMouse()
    while True:
        m = win.getMouse()
        if b1.isClicked(m):
            win1 = GraphWin("Encrypt", 800, 800)
            sent=Entry(Point(200,500),15)
            sent.draw(win1)
            go=Button(win1, Point(650,650), Point(750,725), "salmon", "GO")
            m = win1.getMouse()
            if go.isClicked(m):
                sent=sent.getText()
                win1.close()
                sent=encoder(sent)
                print(sent)
                win2 = GraphWin("Encrypt", 800, 900)
                sent1= Text(Point(400,450), ("your encoded message is " + sent))
                sent1.draw(win2)
                end1=Button(win2, Point(650,150), Point(750,225), "salmon", "end")
                m = win2.getMouse()
                if end1.isClicked(m):
                    win2.close()
        if b2.isClicked(m):
            win1 = GraphWin("Decode", 800, 800)
            sent=Entry(Point(200,500),15)
            sent.draw(win1)
            go=Button(win1, Point(650,650), Point(750,725), "salmon", "GO")
            m = win1.getMouse()
            if go.isClicked(m):
                sent=sent.getText()
                win1.close()
                sent=decoder(sent)
                print(sent)
                win2 = GraphWin("Decode", 800, 900)
                sent1= Text(Point(400,450), ("your decoded message is " + sent))
                sent1.draw(win2)
                end1=Button(win2, Point(650,150), Point(750,225), "salmon", "end")
                m=win2.getMouse()
                if end1.isClicked(m):
                    win2.close()
        
        if Quit.isClicked(m):
            break
    win.close()
        
            
            

if __name__ == "__main__":
    main()
