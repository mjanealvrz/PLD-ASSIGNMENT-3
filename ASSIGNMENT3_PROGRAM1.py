import customtkinter as Ctk
from customtkinter import CTkFont, CTkImage
import tkinter as tk
from tkinter import PhotoImage

Ctk.set_appearance_mode("transparent")


def sign_in():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

    root.destroy()
    welcome_page()
    
def welcome_page():
     win = Ctk.CTk()
     win.title("Fruits Haven Boutique")
     win.geometry("1000x1000")
     scg_image = tk.PhotoImage(file="secondbg.png")
     scg_label = tk.Label(win, image=scg_image)
     scg_label.place(relwidth=1, relheight=1)

     frame = Ctk.CTkFrame(win, width=900, height=500, fg_color="transparent",border_width=brdr_width, border_color="#4F7942", bg_color= "transparent", corner_radius=50)
     frame.place(relx=0.5, rely=0.5, anchor= "center")

     lexenda_font= CTkFont(family="Impact",size=50,weight="bold")
     label = Ctk.CTkLabel(frame, text= "Welcome to Fruits Haven Boutique!", font=lexenda_font,bg_color="transparent", fg_color="transparent", text_color="#013220")
     label.place(relx=0.5, rely=0.5, anchor= "center")
     helv367 = Ctk.CTkFont(family="Helvetica",size=20,weight="bold")
     click_button =Ctk.CTkButton(frame, text="Open Shop",fg_color="#009E60",border_color="#4F7942", width=50, height= 20,border_width=brdr_width, font=helv367, command=opens_shop)
     click_button.place(relx=0.5, rely=0.7, anchor="center")

     win.mainloop()
     win.destroy()

def opens_shop():
     window = Ctk.CTk()
     window.title("Shop Now!")
     window.geometry("1000x1000")

     frame_two = Ctk.CTkFrame(window, width=700, height=700, fg_color="#D0F0C0", border_width=5)
     frame_two.place(relx=0.5, rely=0.5, anchor="center")
     
     apple_quantity_label = Ctk.CTkLabel(frame_two, text="Enter the quantity of the Apples:", width=10, font=helv36 ) 
     apple_quantity_label.place(relx=0.2, rely=0.3, anchor= "center")
     apple_quantity_ent = Ctk.CTkEntry(frame_two, width= 250, height= 50, border_color="#4F7942")
     apple_quantity_ent.place(relx=0.6, rely=0.3, anchor="center")

     orange_quantity_label = Ctk.CTkLabel(frame_two, text="Enter the quantity of the Oranges:", width=10, font=helv36 )
     orange_quantity_label.place(relx=0.2, rely=0.5, anchor="center")
     orange_quantity_ent = Ctk.CTkEntry(frame_two, width= 250, height= 50, border_color="#4F7942")
     orange_quantity_ent.place(relx=0.6, rely=0.5, anchor="center")

     total_amount = Ctk.CTkButton(frame_two, text= "Click to Buy!", fg_color="#009E60",border_color="#4F7942",border_width=brdr_width, font=helv36,width= 250, height= 70, command=lambda: shop_now(apple_quantity_ent, orange_quantity_ent, buy_button))
     total_amount.place(relx=0.5, rely=0.7,anchor= "center" )
     buy_button = Ctk.CTkLabel(frame_two, text= "Total:", width= 250, height= 50, font=helv36)
     buy_button.place(relx=0.5, rely=0.8, anchor="center")

     window.mainloop()
def shop_now(apple_quantity_ent, orange_quantity_ent, buy_button):
    apple_price = 20
    orange_price = 25
    num_apples = int(apple_quantity_ent.get())
    num_oranges = int(orange_quantity_ent.get())
    total_amount = (num_apples * apple_price) + (num_oranges * orange_price)
    buy_button.configure(text=f"The total amount to pay is: {total_amount} pesos")

  
root = Ctk.CTk()
root.title("Sign-In Page")
root.geometry("500x500")
bg_image = tk.PhotoImage(file="bgboutique.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
helv36 = Ctk.CTkFont(family="Helvetica",size=15,weight="bold")
forge_color = "#009E60"
back_color= "#C1E1C1"
brdr_width = 2

frame = Ctk.CTkFrame(root, width=300, height=250, fg_color="transparent")
frame.place(relx=0.5, rely=0.5, anchor= "center")

username_label = Ctk.CTkLabel(frame, text="Username:", width=10, font=helv36)
username_label.place(relx=0.2, rely=0.3, anchor= "center")
username_entry = Ctk.CTkEntry(frame )
username_entry.place(relx=0.6, rely=0.3, anchor="center")

password_label = Ctk.CTkLabel(frame, text="Password:", width=10, font=helv36)
password_label.place(relx=0.2, rely=0.5, anchor="center")
password_entry = Ctk.CTkEntry(frame, show="*") 
password_entry.place(relx=0.6, rely=0.5, anchor="center")

sign_in_button = Ctk.CTkButton(frame, text="Sign In", fg_color="#009E60",border_color="#4F7942", width=10,border_width=brdr_width, font=helv36, command=sign_in)
sign_in_button.place(relx=0.5, rely=0.7, anchor="center")


root.mainloop()
 















