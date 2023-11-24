import customtkinter as Ctk
import tkinter as tk


Ctk.set_appearance_mode("transparent")
Ctk.set_default_color_theme("green")


def sign_in():
    def buy_fruits():
        money = float(ent_money.get())
        apple_price = float(ent_app_price.get())
        orange_price = float(ent_org_price.get())

        max_apples = int(money / apple_price)
        max_oranges = int(money / orange_price)
        remaining_money_app = money - (max_apples * apple_price)
        remaining_money_or = money - (max_oranges * orange_price)

        result_text = (
            f"You can buy a maximum of {max_apples} apples and {max_oranges} oranges.\n"
            f"With the remaining money after buying apples: {remaining_money_app:.2f}\n"
            f"With the remaining money after buying oranges: {remaining_money_or:.2f}"
        )
        result_label.configure(text=result_text)

    win = Ctk.CTk()
    win.title("Fruits Haven Boutique")
    win.geometry("1000x1000")


    frame = Ctk.CTkFrame(win, width=900, height=800, fg_color="#AFE1AF",border_width=brdr_width, border_color="#4F7942", bg_color= "transparent", corner_radius=50)
    frame.place(relx=0.5, rely=0.5, anchor= "center")
    
    money_label = Ctk.CTkLabel(frame, text="Enter the money you have:",  width=10, font=helv36)
    money_label.place(relx=0.2, rely=0.3, anchor= "center")
    ent_money = Ctk.CTkEntry(frame,  width= 250, height= 50, border_color="#4F7942")
    ent_money.place(relx=0.6, rely=0.3, anchor="center")

    app_label = Ctk.CTkLabel(frame, text="Enter the price of an apple:",  width=10, font=helv36)
    app_label.place(relx=0.2, rely=0.5, anchor="center")
    ent_app_price = Ctk.CTkEntry(frame,  width= 250, height= 50, border_color="#4F7942")
    ent_app_price.place(relx=0.6, rely=0.5, anchor="center")

    org_label = Ctk.CTkLabel(frame, text="Enter the price of an orange:",  width=10, font=helv36)
    org_label.place(relx=0.2, rely=0.7, anchor="center")
    ent_org_price = Ctk.CTkEntry(frame,  width= 250, height= 50, border_color="#4F7942")
    ent_org_price.place(relx=0.6, rely=0.7, anchor="center")

    calculate_button = Ctk.CTkButton(frame, text="Calculate", width= 250, height= 50, font=helv36, command=buy_fruits)
    calculate_button.place(relx=0.5, rely=0.85, anchor="center")

    result_label = Ctk.CTkLabel(frame, text="",  width=10, font=helv36)
    result_label.place(relx=0.5, rely=0.95, anchor="center")

    win.mainloop()

PLD = Ctk.CTk()
PLD.title("Sign-in")
PLD.geometry = ("x500")

bg_image = tk.PhotoImage(file="bgboutique.png")
bg_label = tk.Label(PLD, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
helv36 = Ctk.CTkFont(family="Helvetica",size=15,weight="bold")
forge_color = "#009E60"
back_color= "#C1E1C1"
brdr_width = 2

frame = Ctk.CTkFrame(PLD, width=300, height=300, fg_color="transparent")
frame.place(relx=0.5, rely=0.5, anchor= "center")

username_label = Ctk.CTkLabel(frame, text="Username:", width=10, font=helv36)
username_label.place(relx=0.2, rely=0.3, anchor= "center")
username_entry = Ctk.CTkEntry(frame, )
username_entry.place(relx=0.6, rely=0.3, anchor="center")

password_label = Ctk.CTkLabel(frame, text="Password:", width=10, font=helv36)
password_label.place(relx=0.2, rely=0.5, anchor="center")
password_entry = Ctk.CTkEntry(frame, show="*") 
password_entry.place(relx=0.6, rely=0.5, anchor="center")

sign_in_button = Ctk.CTkButton(frame, text="Sign In", fg_color="#009E60",border_color="#4F7942", width=10,border_width=brdr_width, font=helv36, command=sign_in)
sign_in_button.place(relx=0.5, rely=0.7, anchor="center")


PLD.mainloop()

