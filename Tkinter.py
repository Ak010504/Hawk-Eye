import tkinter
import pickle
import pygame

#LOGIN
def close4():
    login.destroy()

def login_file():
    global username1, password1
    username1 = My_Entry5.get()
    password1 = MyEntry6.get()
    login_file = open("Regist_file.dat", "rb")
    login_list = pickle.load(login_file)
    print(login_list)
    for i in login_list:
        if i[0]==username1 and i[1]==password1:
            print("Login Succesful")
            close4()
    login_file.close()

def login1():
    global login, My_Entry5, MyEntry6
    login = tkinter.Tk()
    login.geometry("1600x900")
    login.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="hawkeye.png")
    Label1 = tkinter.Label(login, image=bg)
    Label1.place(x=0, y=0)
    My_label = tkinter.Label(login, text="Welcome to the Login!", fg="yellow", bg="black", font=60)#create Welcome
    My_label.place(x=650, y=20)
    My_Button = tkinter.Button(login, text="Submit", padx=50, pady=15, bg="black", fg="yellow", font=40, command=login_file)#create Submit
    My_Button.place(x=700, y=600)
    MyLabel2 = tkinter.Label(login, text="Username:", fg="yellow", bg="black", font=60)#create Username
    MyLabel2.place(x=100, y=170)
    MyLabel3 = tkinter.Label(login, text="Password:", fg="yellow", bg="black", font=60)#create Password
    MyLabel3.place(x=100, y=400)
    My_Entry5=tkinter.Entry(login, font=40)#create username input
    My_Entry5.place(x=150, y=250, height=30, width=350)
    MyEntry6=tkinter.Entry(login, font=40)
    MyEntry6.place(x=150, y=480, height=30, width=350)
    My_Button2 = tkinter.Button(login, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close4)
    My_Button2.place(x=700, y=700)
    login.mainloop()

#REGISTRATION
def submit():
    if username == confirmuser and password == confirmpass:
        login1()
        print("Registration was succesful")

def close5():
    root.destroy()

def regist():
    global username, password , confirmuser, confirmpass
    username = My_Entry.get()
    password = MyEntry2.get()
    confirmuser = MyEntry3.get()
    confirmpass = MyEntry4.get()
    regist_file1 = open("Regist_file.dat", "rb")
    regist_list1 = pickle.load(regist_file1)
    regist_list1.append([username, password])
    regist_file1.close()
    regist_file2 = open("Regist_file.dat","wb")
    pickle.dump(regist_list1,regist_file2)
    regist_file2.close()
    root.destroy()
    submit()

def registration():
    global root, My_Entry, MyEntry2, MyEntry3, MyEntry4
    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file= "Blue.png")
    Label1 = tkinter.Label(root, image=bg)
    Label1.place(x=0, y=0)
    My_label = tkinter.Label(root, text="Welcome to the Registration!", fg="yellow", bg="black", font=60)#create Welcome
    My_label.place(x=650, y=20)
    MyLabel2 = tkinter.Label(root, text="Username:", fg="yellow", bg="black", font=60)#create Username
    MyLabel2.place(x=100, y=170)
    MyLabel3 = tkinter.Label(root, text="Password:", fg="yellow", bg="black", font=60)#create Password
    MyLabel3.place(x=100, y=400)
    MyLabel4 = tkinter.Label(root, text=" Confirm Username:", fg="yellow", bg="black", font=60)#create Confirm username
    MyLabel4.place(x=1100, y=170)
    MyLabel5 = tkinter.Label(root, text="Confirm Password:", fg="yellow", bg="black", font=60)#create confirm password
    MyLabel5.place(x=1100, y=400)
    My_Entry=tkinter.Entry(root, font=40)#create username input
    My_Entry.place(x=150, y=250, height=30, width=350)
    MyEntry2=tkinter.Entry(root, font=40)
    MyEntry2.place(x=150, y=480, height=30, width=350)
    MyEntry3=tkinter.Entry(root, font=40)
    MyEntry3.place(x=1100, y=250, height=30, width=350)
    MyEntry4=tkinter.Entry(root, font=40)
    MyEntry4.place(x=1100, y=480, height=30, width=350)
    My_Button = tkinter.Button(root, text="Submit", padx=50, pady=15, bg="black", fg="yellow", font=40, command=regist)#create Submit
    My_Button.place(x=700, y=600)
    My_Button2 = tkinter.Button(root, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close5)
    My_Button2.place(x=700, y=700)
    root.mainloop()

#MAIN
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
    main.geometry("1600x900")
    main.attributes('-fullscreen', True)
    bg = tkinter.PhotoImage(file="Homebg.png")
    pygame.mixer.init()
    pygame.mixer.music.load("inception-soundtrack-hd-12-time-hans-zimmer_7OaFJh3k.mp3")
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
    My_Button1 = tkinter.Button(main, text="Registration", padx=50, pady=15, bg="black", fg="yellow", font=40, command=close2)
    My_Button1.place(x=1000, y=390)
    My_Button2 = tkinter.Button(main, text="Close", padx=50, pady=15, bg="black", fg="yellow", font=40,command=close3)
    My_Button2.place(x=700, y=600)
    main.mainloop()

main1()