import tkinter
import pickle
import pygame
import math
import random
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GAME
def game():
    # pause the background music
    #pygame.mixer.music.pause()

    # game window
    pygame.init()#set game window
    screen = pygame.display.set_mode((1366,768))
    width = screen.get_width()
    height = screen.get_width()

    # background image
    background = pygame.image.load("D:\Amrit\College\SSN\CS\Hawk-eye\Game_bg.png")
    screen.blit(background, [0, 0])

    # frame rate
    clock = pygame.time.Clock()

    # timer
    font = pygame.font.SysFont(None, 40)
    counter = 120
    text1 = font.render(str(counter), True, (255, 255, 255))
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)

    # sphere
    def sphere():
        global cx, cy, sphere_choice, sphere1, sphere2
        sphere1 = pygame.image.load("D:\Amrit\College\SSN\CS\Hawk-eye\Yellow_Sphere.png")
        sphere2 = pygame.image.load("D:\Amrit\College\SSN\CS\Hawk-eye\Red_Sphere.png")
        sphere_choose = [sphere1, sphere2, sphere2, sphere1] # random sphere generation
        sphere_choice = random.choice(sphere_choose)
        cx = random.randint(50, 1000) # sphere location
        cy = random.randint(100, 650)
        screen.blit(sphere_choice, [cx, cy])

    sphere() # first sphere

    # start
    font = pygame.font.Font("freesansbold.ttf", 28)
    start = font.render("Click the first sphere to start!", True, (255, 255, 255))
    screen.blit(start, (550, 20))

    # points
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    Text_X = 1000 # position of the points
    Text_Y = 20

    def show_score(x, y):
        score = font.render("Score :" + str(points), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def Points_File(x):
        count = 0
        points_file_r = open("D:\Amrit\College\SSN\CS\Hawk-eye\Points1.dat", "rb")
        Previous_points = pickle.load(points_file_r)
        print("yes")
        points_file_r.close()
        points_file_w = open("D:\Amrit\College\SSN\CS\Hawk-eye\Points1.dat", "wb")
        for i in Previous_points:
            if i[0] == username1:
                i[1].append(x)# append the new points with the old ones
                count = count + 1
                print(Previous_points)
                pickle.dump(Previous_points, points_file_w)
        if count == 0:
            Previous_points.append([username1, [x]])
            print(Previous_points)
            pickle.dump(Previous_points, points_file_w)
        points_file_w.close()

    # quit pygame
    game_font = pygame.font.SysFont("Corbel", 35)
    text = game_font.render("quit", True, (255, 255, 255))

    # main loop
    running = True
    while running:

        for event in pygame.event.get():
            clock.tick(60)

            # quit
            if event.type == pygame.QUIT:
                running = False
            screen.blit(background, (0, 0))
            screen.blit(sphere_choice, (cx, cy))

            # timer
            if event.type == timer_event:
                counter -= 1
                text1 = font.render(str(counter), True, (255, 255, 255))
                if counter == 0:
                    Points_File(points)
                    play1()
                    pygame.quit()
            screen.blit(text1, (50, 50))

            # sphere generation
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sphere_choice == sphere1:
                    x = pygame.mouse.get_pos()[0]#left click
                    y = pygame.mouse.get_pos()[1]#right click
                    click = pygame.mouse.get_pressed()
                    sqx = (x - cx) ** 2
                    sqy = (y - cy) ** 2
                    if math.sqrt(sqx + sqy) < 80 and click[0] == 1 or click[2] == 1:
                        if click[0] == 1:
                            points = points + 200
                        elif click[2] == 1:
                            points = points - 50
                        screen.blit(background, (0, 0))
                        sphere()
                    elif math.sqrt(sqx + sqy) > 80 and click[0] == 1 or click[2] == 1:
                        screen.blit(background, (0, 0))
                        sphere()

                if sphere_choice == sphere2:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    click = pygame.mouse.get_pressed()
                    sqx = (x - cx) ** 2
                    sqy = (y - cy) ** 2
                    if math.sqrt(sqx + sqy) < 80 and click[2] == 1 or click[0] == 1:
                        if click[0] == 1:
                            points = points - 50
                        elif click[2] == 1:
                            points = points + 200
                        screen.blit(background, (0, 0))
                        sphere()
                    elif math.sqrt(sqx + sqy) > 80 and click[0] == 1 or click[2] == 1:
                        screen.blit(background, (0, 0))
                        sphere()

            # quit button
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    play1()
                    print(points)
                    Points_File(points)
                    pygame.quit()
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(screen, (170, 170, 170), [width / 2, height / 2, 140, 40])
            else:
                pygame.draw.rect(screen, (100, 100, 100), [width / 2, height / 2, 140, 40])
            screen.blit(text, (width / 2 + 50, height / 2))

        # points
        show_score(Text_X, Text_Y)
        pygame.display.update()

#STATS
def close11():
    stats_page.destroy()
    play1()

def close12():
    stats_page.destroy()

def stats():
    global stats_page
    stats_page = tkinter.Tk() # creating a window
    stats_page.geometry = ("1366*768")
    stats_page.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\Stats_bg.png") # background image
    label1 = tkinter.Label(stats_page, image=bg)
    label1.place(x=0, y=0)
    points_list1 = []
    points_list2 = []
    attempts = []
    max_score = 0
    points_text = ""
    points_file = open("D:\Amrit\College\SSN\CS\Hawk-eye\Points1.dat","rb")
    points_list = pickle.load(points_file)
    for i in points_list:
        if i[0]==username1:
            points_list1 = i[1]
    points_list1.sort(reverse=True) # sorting the points in descending order
    len_points_list1 = len(points_list1)
    if len_points_list1>5:
        for i in range(0,5):
            points_text = points_text + " , " + str(points_list1[i])
            points_text.lstrip(",")
            points_list2.append(points_list1[i])
    else:
        for i in points_list1:
            points_text = points_text + " , " + str(i)
            points_text.lstrip(",")
            points_list2.append(i)
    for i in range(len(points_list2)):
        attempts.append(i)
    for i in points_list:
        if max_score <= max(i[1]):
            max_score = max(i[1])
    print(points_text)
    My_label = tkinter.Label(stats_page, text=points_text, fg='yellow', bg="black", font=60) # printing the points
    My_label.place(x=300, y=300)
    My_label1 = tkinter.Label(stats_page, text=str(max_score), fg='yellow', bg="black", font=60)  # printing the points
    My_label1.place(x=400, y=400)
    My_label2 = tkinter.Label(stats_page, text="Top 5 scores of "+ username1 + ":", fg='yellow', bg="black", font=60)#printing the username
    My_label2.place(x=90, y=300)
    My_label3 = tkinter.Label(stats_page, text="Overall highest score is : ", fg='yellow', bg="black",font=60)  # printing the username
    My_label3.place(x=90, y=400)
    My_Button = tkinter.Button(stats_page, text='Back', padx=50, pady=15, bg='black', fg='yellow', font=40, command=close11)
    My_Button.place(x=700, y=550)
    My_Button2 = tkinter.Button(stats_page, text='Quit', padx=50, pady=15, bg='black', fg='yellow', font=40, command=close12)
    My_Button2.place(x=700, y=650)

    #plot graph
    data = {"Attempts": attempts, "Points": points_list2}#creating a database
    df = DataFrame(data, columns = ["Attempts", "Points"])
    figure2 = plt.Figure(figsize=(5, 4), dpi=75)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, stats_page)
    line2.get_tk_widget().place(x=900, y=200)
    df = df[['Attempts', 'Points']].groupby('Attempts').sum()
    df.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    points_file.close()
    stats_page.mainloop()

# PLAY
def close8():
    play.destroy()
    rules1()


def close6():
    play.destroy()

def close9():
    play.destroy()
    game()

def close10():
    play.destroy()
    stats()

def play1():
    #pygame.mixer.music.unpause()#continue the bg music
    global play
    print("play")
    play = tkinter.Tk()
    play.geometry = ("1366*768")
    play.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\Play_bg.png")
    label1 = tkinter.Label(play, image=bg)
    label1.place(x=0, y=0)
    My_label = tkinter.Label(play, text="Lets Play!!!", fg='yellow', bg="black", font=60)
    My_label.place(x=700, y=20)
    My_Button = tkinter.Button(play, text='Quit', padx=50, pady=15, bg='black', fg='yellow', font=40, command=close6)
    My_Button.place(x=700, y=700)
    My_Button2 = tkinter.Button(play, text="Rules", padx=50, pady=15, fg="yellow", bg="black", font=50, command=close8)
    My_Button2.place(x=700, y=500)
    My_Button3 = tkinter.Button(play, text="Play", padx=50, pady=15, fg="yellow", bg="black", font=50, command=close9)
    My_Button3.place(x=700, y=400)
    My_Button4 = tkinter.Button(play, text="Stats", padx=50, pady=15, fg="yellow", bg="black", font=50, command=close10)
    My_Button4.place(x=700, y=600)
    play.mainloop()

# RULES
def close7():
    rules.destroy()
    play1()

def rules1():
    global rules
    rules = tkinter.Tk()
    rules.geometry("1366x768")
    rules.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\Rules_bg.png")
    Label1 = tkinter.Label(rules, image=bg)
    Label1.place(x=0, y=0)
    My_Text = tkinter.Text(rules, fg="yellow", bg="black", height=20, font=40, width=84) # rules
    p = """Welcome to the game!!

    These are the RULES of the game:
    	1 . Each player will have a time limit of 2 minutes. The player must click on as many balls as possible within that time range.

    	2 . Thre are 2 types of balls - Yellow and Red. The point system for each ball is given below:

    						1 . Yellow - Left Click - +200
    							   - Right Click - (-50)

    						2 . Red - Left Click - (-50)
    							- Right Click - +200

    	3 . Once the timer ends , The player will be able to see his/her stats on the stats page. 

    	4 . To Pause the game, The player must Alt + f4. The game will be halted and the player must restart the game.

    	5 . Close the RULES window to continue the game

    Thank you for playing the game!!"""
    My_Text.insert(tkinter.INSERT, p)
    My_Text.place(x=400, y=200)
    My_Button2 = tkinter.Button(rules, text="Back", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close7)
    My_Button2.place(x=700, y=700)
    rules.mainloop()

# LOGIN
def close4():
    login.destroy()

def login_file():
    global username1, password1
    username1 = My_Entry5.get() # get username
    password1 = MyEntry6.get() # get password
    login_file = open("D:\Amrit\College\SSN\CS\Hawk-eye\Regist_file.dat", "rb")
    login_list = pickle.load(login_file)
    print(login_list)
    for i in login_list:
        if i[0] == username1 and i[1] == password1:#check if username is in database
            print("Login Succesful")
            close4()
            play1()
    login_file.close()

def login1():
    global login, My_Entry5, MyEntry6
    login = tkinter.Tk()
    login.geometry("1366x768")
    login.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\hawkeye.png")
    Label1 = tkinter.Label(login, image=bg)
    Label1.place(x=0, y=0)
    My_label = tkinter.Label(login, text="Welcome to the Login!", fg="yellow", bg="black", font=60)  # create Welcome
    My_label.place(x=650, y=20)
    My_Button = tkinter.Button(login, text="Submit", padx=50, pady=15, bg="black", fg="yellow", font=40,
                               command=login_file)  # create Submit
    My_Button.place(x=700, y=600)
    MyLabel2 = tkinter.Label(login, text="Username:", fg="yellow", bg="black", font=60)  # create Username
    MyLabel2.place(x=100, y=170)
    MyLabel3 = tkinter.Label(login, text="Password:", fg="yellow", bg="black", font=60)  # create Password
    MyLabel3.place(x=100, y=400)
    My_Entry5 = tkinter.Entry(login, font=40)  # create username input
    My_Entry5.place(x=150, y=250, height=30, width=350)
    MyEntry6 = tkinter.Entry(login, font=40)
    MyEntry6.place(x=150, y=480, height=30, width=350)
    My_Button2 = tkinter.Button(login, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close4)
    My_Button2.place(x=700, y=700)
    login.mainloop()

# REGISTRATION
def submit():
    if username == confirmuser and password == confirmpass:
        login1()
        print("Registration was succesful")

def close5():
    root.destroy()

def regist():
    global username, password, confirmuser, confirmpass
    username = My_Entry.get()
    password = MyEntry2.get()
    confirmuser = MyEntry3.get()
    confirmpass = MyEntry4.get()
    regist_file1 = open("D:\Amrit\College\SSN\CS\Hawk-eye\Regist_file.dat", "rb")
    regist_list1 = pickle.load(regist_file1)
    regist_list1.append([username, password]) # adding the username and password to the database
    regist_file1.close()
    regist_file2 = open("D:\Amrit\College\SSN\CS\Hawk-eye\Regist_file.dat", "wb")
    pickle.dump(regist_list1, regist_file2)
    regist_file2.close()
    root.destroy()
    submit()

def registration():
    global root, My_Entry, MyEntry2, MyEntry3, MyEntry4
    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\hawkeye.png")
    Label1 = tkinter.Label(root, image=bg)
    Label1.place(x=0, y=0)
    My_label = tkinter.Label(root, text="Welcome to the Registration!", fg="yellow", bg="black",
                             font=60)  # create Welcome
    My_label.place(x=650, y=20)
    MyLabel2 = tkinter.Label(root, text="Username:", fg="yellow", bg="black", font=60)  # create Username
    MyLabel2.place(x=100, y=170)
    MyLabel3 = tkinter.Label(root, text="Password:", fg="yellow", bg="black", font=60)  # create Password
    MyLabel3.place(x=100, y=400)
    MyLabel4 = tkinter.Label(root, text=" Confirm Username:", fg="yellow", bg="black",
                             font=60)  # create Confirm username
    MyLabel4.place(x=900, y=170)
    MyLabel5 = tkinter.Label(root, text="Confirm Password:", fg="yellow", bg="black",
                             font=60)  # create confirm password
    MyLabel5.place(x=900, y=400)
    My_Entry = tkinter.Entry(root, font=40)  # create username input
    My_Entry.place(x=150, y=250, height=30, width=350)
    MyEntry2 = tkinter.Entry(root, font=40)
    MyEntry2.place(x=150, y=480, height=30, width=350)
    MyEntry3 = tkinter.Entry(root, font=40)
    MyEntry3.place(x=900, y=250, height=30, width=350)
    MyEntry4 = tkinter.Entry(root, font=40)
    MyEntry4.place(x=900, y=480, height=30, width=350)
    My_Button = tkinter.Button(root, text="Submit", padx=50, pady=15, bg="black", fg="yellow", font=40,
                               command=regist)  # create Submit
    My_Button.place(x=700, y=600)
    My_Button2 = tkinter.Button(root, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close5)
    My_Button2.place(x=700, y=700)
    root.mainloop()

# MAIN
def close1():
    main.destroy()
    login1()

def close3():
    main.destroy()

def close2():
    main.destroy()
    registration()

def main1():
    global main
    main = tkinter.Tk()
    main.geometry("1366x768")
    main.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="D:\Amrit\College\SSN\CS\Hawk-eye\Homebg.png")
    pygame.mixer.init()#background music
    pygame.mixer.music.load("D:\Amrit\College\SSN\CS\Hawk-eye\inception-soundtrack-hd-12-time-hans-zimmer_7OaFJh3k.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()
    Label1 = tkinter.Label(main, image=bg)
    Label1.place(x=0, y=0)
    My_Text = tkinter.Text(main, fg="yellow", bg="black", height=3, font=40, width=40)
    p = '''W E L C O M E          TO       

                                H A W K - E Y E '''
    My_Text.insert(tkinter.INSERT, p)
    My_Text.place(x=550, y=10)
    My_Button = tkinter.Button(main, text="Login", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close1)
    My_Button.place(x=300, y=400)
    My_Button1 = tkinter.Button(main, text="Registration", padx=50, pady=15, bg="black", fg="yellow", font=40,
                                command=close2)
    My_Button1.place(x=1000, y=390)
    My_Button2 = tkinter.Button(main, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close3)
    My_Button2.place(x=700, y=600)
    main.mainloop()

main1()
