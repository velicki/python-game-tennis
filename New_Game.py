from tkinter import *
from tkinter.font import BOLD
import time
import keyboard
import Mica_win
import Bica_win

def game(jezik, p1color, p2color,p1_up,p1_down,p2_up,p2_down):
    WIDTH = 600
    HEIGHT = 530
    xVelocity = 3
    yVelocity = 4
    Tenis_Game = Tk()

    if jezik == "serbian":
        main_text = "TENIS Mica protiv Bice"

    elif jezik == "english":
        main_text = "TENNIS Mica VS Bica"

    try: player1_result
    except: player1_result = 0
    try: player2_result
    except: player2_result = 0
    try: duration
    except: duration = 0

    Tenis_Game.geometry("600x600")             # Velicina prozora
    Tenis_Game.title(main_text)                # Ime prozora
    Tenis_Game.resizable(False, False)

    icon = PhotoImage(file="Icon.png")        # Slika je prebacena u format koji moze da cita python
    Tenis_Game.iconphoto(True, icon)          # Ikonica prozora

    Tenis_Game.config(bg="black")             # Boja pozadine prozora
    
    result_text = StringVar()
    result = Label(Tenis_Game, 
            textvariable=result_text,
            fg="red", 
            bg="black",
            font=("Arial", 15, BOLD)
            )
    result_text.set("Mica: " + str(player1_result) + "| Bica: " + str(player2_result))
    canvas = Canvas(Tenis_Game, width=WIDTH, height=HEIGHT)

    result.grid(row=0, column=0)
    canvas.grid(row=1, column=0)

    teren = PhotoImage(file='teren.png')
    terencan = canvas.create_image(0,0,image=teren,anchor=NW)

    lopta = PhotoImage(file='lopta.png')
    loptacan = canvas.create_image(290,255,image=lopta,anchor=NW)

    igrac1 = canvas.create_rectangle (20,20,40,120,fill=p1color,width=1)    #Prvi igrac kreiran
    igrac2 = canvas.create_rectangle (560,20,580,120,fill=p2color,width=1)  #Drugi igrac kreiran

    while True:
        canvas.coords(terencan)
        position1 = canvas.coords(igrac1)
        position2 = canvas.coords(igrac2)
        coordinates = canvas.coords(loptacan)
        
        if (keyboard.is_pressed(p2_down) and position2[1]<(HEIGHT-100)):
            canvas.move(igrac2,0,5)
        if (keyboard.is_pressed(p1_down) and position1[1]<(HEIGHT-100)):
            canvas.move(igrac1,0,5)
        if (keyboard.is_pressed(p2_up) and position2[1]>0):
            canvas.move(igrac2,0,-5)
        if (keyboard.is_pressed(p1_up) and position1[1]>0):
            canvas.move(igrac1,0,-5)

        if (coordinates[0]>=(WIDTH-65)):
            if (coordinates[1]>position2[1] and coordinates[1]<(position2[1]+100)):  #provera da li je igrac udario lopticu
                player1_result = player1_result
                xVelocity = -xVelocity
                duration += 1
            if (coordinates[0]>=(WIDTH-20)):
                xVelocity = -xVelocity
                player1_result += 1
                duration += 1
                if (player1_result == 10):
                    Tenis_Game.destroy()
                    Mica_win.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down,player1_result,player2_result)
                canvas.coords(loptacan,290,255)
                time.sleep(0.5)
        if (coordinates[0]<=40):
            if (coordinates[1]>position1[1] and coordinates[1]<(position1[1]+100)):
                xVelocity = -xVelocity
                player2_result = player2_result
            if (coordinates[0]<=0): 
                xVelocity = -xVelocity
                player2_result +=1
                if (player2_result == 10):
                    Tenis_Game.destroy()
                    Bica_win.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down,player1_result,player2_result)
                canvas.coords(loptacan,290,255)
                time.sleep(0.5)
        if (coordinates[1]>=(HEIGHT-25) or coordinates[1]<0):
            yVelocity = -yVelocity                             #Loptica se odbija od ivice terena
        if ((duration/10)==1):                                 #brojac - na svaka 4 kruga brzina loptice se povecava
            if (xVelocity > 0):
                xVelocity += 1
            else: xVelocity -= 1
            if (yVelocity > 0):
                yVelocity += 1
            else: yVelocity -= 1
            duration = 0
        canvas.move(loptacan,xVelocity,yVelocity)                                            #Pomera se loptica na ekranu
        result_text.set("Mica: " + str(player1_result) + "| Bica: " + str(player2_result))   #Updatuje se rezultat
        Tenis_Game.update()
        time.sleep(0.01)