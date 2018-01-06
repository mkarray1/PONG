from tkinter import *
from time import *
from math import *
from random import *
root = Tk()
s = Canvas( root, width=700, height=700, background = "black" )
s.pack()

#Imports and Starting values
yBallSpeed2 = 0
bolt2 = PhotoImage(file="background pic2.gif")
bolt4 = PhotoImage(file="background pic4.gif")
xStar = []
yStar = []
StarSpeed = 2
xStar2 = []
yStar2 = []

def BackGround():
    global xStar, yStar,StarSpeed, i,snow, snowcolour
    snowcolour="white"
    for i in range(150):
        newxStar = randint(0,700)
        newyStar = randint(0,700)
        xStar.append(newxStar)
        yStar.append(newyStar)
        
        snow=s.create_oval(xStar[i],yStar[i],xStar[i]+5,yStar[i]+5,fill=snowcolour)
        xStar[i]=xStar[i]+StarSpeed
        yStar[i]=yStar[i]+StarSpeed
        s.update()
        
def BackGround2():
        global xStar2,yStar2
        for i in range(150):
            newxStar2 = randint(0,700)
            newyStar2 = randint(0,700)
            xStar2.append(newxStar2)
            yStar2.append(newyStar2)
        
            snow2=s.create_oval(xStar2[i],yStar2[i],xStar2[i]+5,yStar2[i]+5,fill="white")
            s.update()
        
def drawIntroScreen():
    global playButton, line1,line2,easyButton, normalButton, instructionsButton, hardButton,bolt1,bolt2,bolt3,bolt4,bgpic2,bgpic4,bgpic5,bgpic6,bgpic7,intropong1,intropong2,line3, line4,introBall1,introBall2

    #Drawing Bolts
    bgpic2 = s.create_image(20,50,image=bolt2)
    bgpic6 = s.create_image(20,100,image=bolt2)
    bgpic7 = s.create_image(650,500,image=bolt2)
    bgpic4 = s.create_image(50,130,image=bolt4)
    bgpic5 = s.create_image(620,10,image=bolt4)
    BackGround2()
    #Drawing intro designs
    intropong1 = s.create_oval(100,600,175,610,fill="white")
    intropong2 = s.create_oval(550,600,625,610,fill="white")
    introBall1 = s.create_oval(130,560,150,580,fill="red")
    introBall2 = s.create_oval(580,560,600,580,fill="red")
    
    #Intro information
    line1 = s.create_text(200, 450, text= "Click a difficulty when ready",font="Times 25", fill="white", anchor=W)
    line2 = s.create_text(220, 300, text="PONG", font="Times 90", fill="white", anchor=W)
    line3 = s.create_rectangle(220,250,540,260,fill="blue")
    line4 = s.create_rectangle(220,340,540,350,fill="blue")

    easyButton = Button(root, text="EASY",font="Times 20", command=easyButtonPressed, anchor=CENTER)
    easyButton.pack()
    easyButton.place(x=320, y=500)

    normalButton = Button(root, text= "MEDIUM",font="Times 20", command=normalButtonPressed, anchor=CENTER)
    normalButton.pack()
    normalButton.place(x=300, y=575)

    hardButton = Button(root, text="HARD",font="Times 20", command=hardButtonPressed, anchor=CENTER)
    hardButton.pack()
    hardButton.place(x=320, y=650)

    instructionsButton=Button(root,text="Instructions",font="Times 20",command=instructionsButtonPressed, anchor=CENTER)
    instructionsButton.pack()
    instructionsButton.place(x=25,y=400)
    s.update()


def setInitialValues():
    global ySpeeds, xStar,yStar,StarSpeed,xBall,yValue,giftLife,bolt1,bolt2,bolt3,bolt4,xValue,BallOutOfBounds,showBox, box,retry, easySpeed, Score1, gift, yBall, box, lifecolour, initialLifeText,BallRadius,xBallSpeed2,yBallSpeed2,initialScoreText,Score02,newScore2,Score2, xInvisiball, yInvisiball, ballSpeed, xPong, yPong,xSpeed,ySpeed,xBallSpeed,yBallSpeed,Score, Lives, initialLifeText,initialLifeText2,heart,heart1, heart2, heart3, heart4, heart5, TimesPressedEnter, Score0, newScore, xPong2, yPong2, PongLength1, PongLength2, difference, timeStart,timeFinish

    #BallInformation
    xBallSpeed = 5
    yBallSpeed = 5
    xBall = 400
    yBall = 200
    xBallSpeed2 = 5
    BallRadius = 20
    xInvisiball = 400
    yInvisiball = 200

 
    # More Image Imports
    heart = PhotoImage(file= "heart.gif")
    heart = heart.subsample(20,20)
    gift = PhotoImage(file= "presentbox.gif")
    gift = gift.subsample(3,3)

    #Pong Information
    xPong = 100
    yPong = 400
    xPong2 = 600
    yPong2= 400
    PongLength1 = 50
    PongLength2 = 50
    ySpeed = 0

    #Initial Score
    Score = 0
    Score2 = 0
    Score0 = s.create_text(400,100,text=Score,font = "Times 30", fill="red", anchor=W)
    Score02 = s.create_text(200,100,text=Score,font= "Times 30", fill="red", anchor=W)
    newScore2 = 0
    newScore = 0

    #Mystery Box Info
    yValue = randint(100,600)
    xValue = 300
    Lives = 5
    giftLife = randint(1,4)
    retry = 0
    box = 0
    showBox = False
    
def KeyPressedHandler(event):
    global ySpeed, xBall, yBall, Lives, easySpeed, newLifeText,xBallSpeed,yBallSpeed, LifeText, TimesPressedEnter, heart1, heart2, heart3, heart4, heart5, xInvisiball, yInvisiball, xBallSpeed2, yBallSpeed2, lifecolour,PongLength1,enter
    #Up and Down Key commands
    if event.keysym == "Up":
        ySpeed=-5

    if event.keysym == "Down":
        ySpeed = 5
    
    if xPong > xBall or  xPong2 < xBall:
         if event.keysym == "Return":

            #Resetting Values if Enter is pressed
            PongLength1 = 50
            xBall = 400
            yBall = randint(100,300)
            xInvisiball = xBall
            yInvisiball = yBall
            s.update()
            if yBallSpeed2<0:
                yBallSpeed2 = yBallSpeed2*-1
            if yBallSpeed<0:
                yBallSpeed = yBallSpeed*-1
           
            #Restarting Game
            if Score == 5 or Score2 == 5:
                endGame()
                

    
def KeyUpHandler(event):
    global ySpeed

    ySpeed = 0
def introScreen():
    global inst1,inst2,inst3,inst4,BackButton

    #instructions screen
    inst1 = s.create_text(50, 100, text= "Use the arrow keys to move up and down in ",font="Times 25", fill="white", anchor=W)
    inst2 = s.create_text(50, 150, text= "an attempt to hit the ball past the opponent",font="Times 25", fill="white", anchor=W)
    inst3 = s.create_text(50, 200, text= "while not letting it past you. First to 5",font="Times 25", fill="white", anchor=W)
    inst4 = s.create_text(50, 250, text= "points wins. ",font="Times 25", fill="white", anchor=W)
    BackButton = Button(root,text="Back To Menu",font="Times 20",command=BackButtonPressed, anchor=CENTER)
    BackButton.pack()
    BackButton.place(x=350,y=300)

def instructionsButtonPressed():
    global yBallSpeed2,playButton, line1,line2,easyButton, normalButton, hardButton,xBallSpeed,easySpeed,bgpic2,bgpic4,bgpic5,bgpic6,bgpic7,intropong1,intropong2,line3, line4, introBall1,introBall2
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    instructionsButton.destroy()
    s.delete(line1,line2,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4,introBall1,introBall2)
    s.update()
    introScreen()


    
def easyButtonPressed():
    global yBallSpeed2,playButton, line1,line2,easyButton, normalButton, hardButton,xBallSpeed,easySpeed,bgpic2,bgpic4,bgpic5,bgpic6,bgpic7,intropong1,intropong2,line3, line4,introBall1,introBall2
    easySpeed = 5-0.1
    yBallSpeed2 = easySpeed
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    instructionsButton.destroy()
    s.delete(line1,line2,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4, introBall1,introBall2)
    s.update()
    runGame()


def normalButtonPressed():
    global yBallSpeed2,playButton, line1,line2,easyButton, normalButton, hardButton, xBallSpeed,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4, introBall1,introBall2
    mediumSpeed = 4.9999999
    yBallSpeed2 = mediumSpeed
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    instructionsButton.destroy()
    s.delete(line1,line2,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4, introBall1,introBall2)
    s.update()
    runGame()

def BackButtonPressed():
    global inst1,inst2,inst3,inst4,BackButton
    s.delete(inst1,inst2,inst3,inst4) 
    BackButton.destroy()
    drawIntroScreen()

def hardButtonPressed():
    global yBallSpeed2,playButton, line1,line2, easyButton, normalButton, hardButton,xBallSpeed,yBallSpeed,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4, introBall1,introBall2
    hardSpeed = 4.9999999999999988999
    yBallSpeed2 = hardSpeed
    easyButton.destroy()
    normalButton.destroy()
    hardButton.destroy()
    instructionsButton.destroy()
    s.delete(line1,line2,bgpic2,bgpic4,bgpic5,bgpic6,intropong1,intropong2,bgpic7,line3, line4, introBall1,introBall2)
    s.update()
    runGame()  

def endGame():
    global pong,ball,pong2, TryAgain,newScore, newLifeText,Score0, initialScoreText, initialLifeText,Score2,newScore2,Score02,retry,win,loss

    #Ending the game
    s.delete(pong,ball,pong2,Score0,  newScore,newScore2,Score02,retry)
    s.update()
    if Score2 == 5:
        win=s.create_text(250,300, text= "YOU WIN!", fill="white",font= "Times 40", anchor=W)
        s.update()
    if Score == 5:
        loss = s.create_text(200,300,text="YOU LOSE.",fill="white", font= "Times 40", anchor=W)
        s.update()
    TryAgain = Button(root, text = "Back To Main Menu", font = "Times 40", command = TryAgainPressed, anchor=CENTER)
    TryAgain.pack()
    TryAgain.place(x = 120, y = 500)

def TryAgainPressed():
    global TryAgain,ball,pong2,pong,newScore,Score0,newLifeText,snow
    #Restarting the game
    TryAgain.destroy()
    if Score2 == 5:
        s.delete(win)

    if Score == 5:
        s.delete(loss)

    snowcolour="black"
    drawIntroScreen()

def drawBall():
    global xBall,yBall, ball
    #Initial Ball drawing
    ball = s.create_oval(xBall,yBall,xBall+BallRadius,yBall+BallRadius,fill="red")


    
def UpdateBall():
    global xBall,yBall, xBallSpeed, yBallSpeed, x1Wall, xPong

    #Updating the ball every frame
    xBall = xBall + xBallSpeed
    yBall = yBall + yBallSpeed

    if xPong+5 == xBall+xBallSpeed and yPong-15<=yBall+xBallSpeed<=yPong+PongLength1+10:
        xBallSpeed = xBallSpeed*-1

    if yBall+yBallSpeed <= upWall:
        yBallSpeed = yBallSpeed*-1

    if yBall+BallRadius+yBallSpeed>=downWall:
        yBallSpeed=yBallSpeed*-1

    if xPong2+5==xBall+xBallSpeed and yPong2-15<=yBall+xBallSpeed<=yPong2+PongLength2+10:
         xBallSpeed=xBallSpeed*-1

def BallOutOfBounds():
    global BallOutOfBounds
    if xPong-10>xBall or xPong2+60<xBall:
        BallOutOfBounds = "true"
        LivesLeft()

def drawBall2():
    global  xInvisiball,yInvisiball,ball2

    #Invisible Ball
    ball2 = s.create_oval(xInvisiball,yInvisiball,xInvisiball+BallRadius,yInvisiball+BallRadius)

def updateBall2():
    global xBall,yBall, xBallSpeed, yBallSpeed, x1Wall, xPong, xInvisiball, yInvisiball, xBallSpeed2, yBallSpeed2

    #Updating Invisible ball
    xInvisiball = xInvisiball + xBallSpeed2
    yInvisiball = yInvisiball + yBallSpeed2


    if xPong+5 == xInvisiball +xBallSpeed:
        xBallSpeed2 = xBallSpeed2*-1

    if yInvisiball+yBallSpeed2 <= upWall:
        yBallSpeed2 = yBallSpeed2*-1

    if yInvisiball+BallRadius+yBallSpeed2>=downWall:
        yBallSpeed2 = yBallSpeed2*-1

    if xPong2+5 == xInvisiball+xBallSpeed2 and yPong2-15 <= yInvisiball+xBallSpeed2 <= yPong2+PongLength2+10:
         xBallSpeed2=xBallSpeed2*-1

#Initial Pong Drawings
def drawPong():
    global xPong,yPong, pong
    pong = s.create_oval(xPong, yPong, xPong+10,yPong+PongLength1,fill="white")

def drawPong2():
    global xPong2, yPong2, pong2
    pong2 = s.create_oval(xPong2,yPong2,xPong2+10,yPong2+PongLength2,fill="white")
    
#Updating Pongs
def UpdatePong():
    global ySpeed,yPong
    
    yPong = yPong+ySpeed

    if xBall<xPong-20 or  xBall>xPong2+20:
        yPong=300

def UpdatePong2():
    global yPong2, timeStart,yInvisiball
   
    yPong2=yInvisiball-10
    if  xBall<xPong-20 or  xBall>xPong2+20:
        yPong2=300



def drawBox():
    global box, PongLength1, xValue, yValue,showBox,giftLife
        
    #Mystery Box Activation and Deletion
    box = s.create_image(xValue,yValue, image=gift)

    if xValue-15<xBall<xValue+25 and yValue-40<yBall<yValue+30:
                Score2 = giftLife+0.1
                xValue = -50
                yValue = -50
                showBox = False
                
                PongLength1 = PongLength1+25
                s.delete(box)
                s.update()
        
def DrawWall():
    global Wall, x1Wall,y1Wall,x2Wall,y2Wall
    x1Wall=700
    y1Wall=0
    x2Wall=700
    y2Wall=700
    Wall=s.create_rectangle(x1Wall,y1Wall,x2Wall,y2Wall,fill="blue")

def DrawRoof():
    global upWall
    upWall=0
    Roof=s.create_rectangle(0,-10,700,upWall,fill="black")

def DrawGround():
    global downWall
    downWall=700
    Ground=s.create_rectangle(0,downWall,800,710,fill="black")

def ScoreCount():
    global Score, Score0, newScore, PongLength1,newScore2,Score2
       
    if xPong>xBall>xPong-10:
        s.delete( Score0,newScore)
        Score = Score+1
        newScore = s.create_text(400,100,text=Score,font = "Times 30", fill="red", anchor=W)
    if xPong2<xBall<xPong2+10:
        s.delete(Score02,newScore2)
        Score2 = Score2+1
        newScore2 = s.create_text(200,100,text=round(Score2,0),font= "Times 30", fill="red", anchor=W)

#Death Text
def LivesLeft():
    global Lives,heart1,heart2,heart3,heart4, heart5, newLifeText,heart,lifecolour,BallOutOfBounds, enter,x1,y1,retry
    s.delete(retry)
    x1=150
    y1=500
    retry = s.create_text(x1, y1, text= "Press ENTER to continue",font="Times 30", fill="white", anchor=W)
    
    if BallOutOfBounds==False:
        
        s.update()
        
    
#calling all functions
def runGame():
    global pong,pong2, i, showBox,box
    setInitialValues()
    DrawWall()
    DrawRoof()
    DrawGround()
    while Score!=5 and Score2!=5:
        
        if Score2==giftLife or Score2==giftLife:
            showBox= True
            
        else:
            showBox= False 

        if xPong>xBall or xPong2<xBall:
            BallOutOfBounds = True

        else:
            BallOutOfBounds = False

        drawPong()
        drawPong2()
        UpdatePong()
        UpdatePong2()
        ScoreCount()
        drawBall2()
        updateBall2()

        if showBox==True:
            drawBox()

        if BallOutOfBounds==True:
            LivesLeft()

        if BallOutOfBounds==False:
            s.delete(retry)

        drawBall()
        UpdateBall()
        s.update()
        s.delete(pong, ball,ball2,pong2,box)


root.after(0,drawIntroScreen)

s.bind("<Key>", KeyPressedHandler)
s.bind("<KeyRelease>", KeyUpHandler)
s.pack()
s.focus_set()
root.mainloop()

        
