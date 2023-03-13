from tkinter import *
from tkinter import messagebox
import webbrowser
import pygame

pygame.mixer.init()

def click():
    global cookie_counter
    cookie_counter += cookie_gain
    counter['text'] = cookie_counter
    def play_sound():
        pygame.mixer.music.load("nomnomnom.mp3")
        pygame.mixer.music.play()
    play_sound()


def autoclick_fonc():
    global cookie_counter
    global autoclick_gain
    global autoclick_price
    global autoclick_active
    global cookie_counter
    
    if cookie_counter < autoclick_price:
        messagebox.showinfo("Error", "Not enough cookies")
    else:
        autoclick_active = True
        autoclick_gain += 1
        cookie_counter -= autoclick_price
        autoclick_price *= 2
        counter['text'] = cookie_counter
        text_pay_autoclick['text'] = f"Payer {autoclick_price} pour augmenter vos cookies\nde {autoclick_gain + 1} chaque seconde."

        
        def autoclick_loop():
            global cookie_counter
            autoclick_active
            if autoclick_active:
                cookie_counter += autoclick_gain
                counter['text'] = cookie_counter
                root.after(1000, autoclick_loop)
        autoclick_loop()



def bonus_fonc():
    global cookie_counter
    global cookie_gain
    global bonus_price
    if cookie_counter < bonus_price:
        messagebox.showinfo("Error", "Not enough cookies")
    else:
        cookie_gain *= 2
        cookie_counter -= bonus_price
        bonus_price *= 2
        text_pay_bonus['text'] = f"Payer {bonus_price} cookies pour augmenter\nla récolte des cookies"
        counter['text'] = cookie_counter   
 

def open_github():
   webbrowser.open_new("https://github.com/Shirofr")

bg_color="#5F9AFF"
cookie_counter = 0
cookie_gain = 1
autoclick_gain = 0
bonus_price = 20
autoclick_price = 1000
autoclick_active = False

root = Tk()
root.geometry("1040x513")
root.resizable(width=False, height=False)
root.config(bg=bg_color)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Github", command=open_github)
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

frame_title = Frame(root, bg=bg_color)

label_title = Label(frame_title, text='Cookie Clicker', bg=bg_color, fg='white', font=("Helvetica", 40))
label_title.pack(expand=YES, pady=10)

frame_title.pack(expand=False)

grid_frame = Frame(root, bg=bg_color)

counter = Label(grid_frame, text=cookie_counter, bg=bg_color, fg='black', font=("Helvetica", 30))
counter.grid(row=0, column=0, sticky=(W, E), pady=40)
bonus = Label(grid_frame, text='Bonus', bg=bg_color, fg='black', font=("Helvetica", 30))
bonus.grid(row=0, column=1, sticky=(W, E), pady=40)
autoclick = Label(grid_frame, text='Autoclick', bg=bg_color, fg='black', font=("Helvetica", 30))
autoclick.grid(row=0, column=2, sticky=(W, E), pady=40)

text_click_cookie = Label(grid_frame, text='Cliquer sur le cookie\npour augmenter vos cookies', bg=bg_color, fg='white', font=("Helvetica", 10))
text_click_cookie.grid(row=1, column=0, sticky=(W, E), padx=20, pady=20)
text_pay_bonus = Label(grid_frame, text=f'Payer {bonus_price} cookies pour augmenter\nla récolte des cookies', bg=bg_color, fg='white', font=("Helvetica", 10))
text_pay_bonus.grid(row=1, column=1, sticky=(W, E), padx=20, pady=20)
text_pay_autoclick = Label(grid_frame, text=f"Payer {autoclick_price} pour augmenter vos cookies\nde {autoclick_gain + 1} chaque seconde.", bg=bg_color, fg='white', font=("Helvetica", 10))
text_pay_autoclick.grid(row=1, column=2, sticky=(W, E), padx=20, pady=20)

cookie_image = PhotoImage(file='cookie.png')
cookie_button = Button(grid_frame, image=cookie_image, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=click)
cookie_button.grid(column=0, row=2, sticky=(W, E), pady=10)

plus_image = PhotoImage(file="plus.png",)
bonus_button = Button(grid_frame, image=plus_image, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=bonus_fonc)
bonus_button.grid(column=1, row=2, sticky=(W, E), pady=10)

plus_image_2 = PhotoImage(file="plus.png",)
autoclick_button = Button(grid_frame, image=plus_image_2, bg=bg_color, bd=0, highlightthickness=0, activebackground=bg_color, command=autoclick_fonc)
autoclick_button.grid(column=2, row=2, sticky=(W, E), pady=10)

grid_frame.pack()

root.mainloop()