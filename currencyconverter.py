from tkinter import *
import ttkbootstrap as tb
import requests
url = "https://exchangerate-api.p.rapidapi.com/rapid/latest/USD"

headers = {
	"X-RapidAPI-Key": "d5d85c7d1emsh71eeda810b69f8dp19bd2bjsn3ec37358c824",
	"X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com"
}

main_window = tb.Window(themename="cyborg")
# main_window.geometry("600x350")
win_frame_1 = tb.Frame()
win_frame_1.grid(row = 2 , column=0)
win_frame_2 = tb.Frame()
win_frame_2.grid(row = 0 , column=0)
user_amount = tb.Entry(win_frame_1, bootstyle="info")
user_amount.grid(row=0, column=0)

currency_codes = [
    "USD",
    "CAD",
    "GBP",
    "EUR",
    "JPY",
    "CNY",
    "INR",
    "BRL",
    "AUD",
    "ZAR",
    "RUB",
    "SAR",
    "KRW",
    "MXN"
]

unit = ""
user_unit = ""
entry_var = StringVar()
def space(row_no, col_no):
    space_1 = tb.Label(win_frame_1)
    space_1.grid(row=row_no, column=col_no)

def space_win(row_no, col_no):
    space_2 = tb.Label(main_window)
    space_2.grid(row=row_no, column=col_no)

def chooseCurrency(x):
    global user_unit
    user_unit = x
    user_currency.config(text=x)
    
def convertCurrency(x):
    global unit
    unit = x
    convert_currency.config(text=x)
def convert_rave():
#-------------------------------------------------------------------------------------------
    url = f'https://exchangerate-api.p.rapidapi.com/rapid/latest/{user_unit}'
    headers = {
        "X-RapidAPI-Key": "d5d85c7d1emsh71eeda810b69f8dp19bd2bjsn3ec37358c824",
        "X-RapidAPI-Host": "exchangerate-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    rates_currency = dict(response.json())
    multiplyBy = rates_currency["rates"][unit]
    user_amount_enterd = float(user_amount.get())
    entry_var.set(f'{round(multiplyBy,2)*user_amount_enterd}')
#----------------------------------------------------------------------------------------------    

    
user_currency = tb.Menubutton(win_frame_1, bootstyle="danger", text="Currency")
user_currency.grid(row=0, column=1) 
currency_menu = tb.Menu(user_currency)
currency_str = StringVar()


convert_to_label = tb.Label(win_frame_1, text="Conver to Currency :", bootstyle="primary")

convert_to_label.grid(row=2, column=0)
# ----------------------------------------------------------------
space(1, 0)
space(1, 1)
# ----------------------------------------------------------------
convert_currency = tb.Menubutton(win_frame_1, bootstyle="danger", text="Currency")
convert_currency.grid(row=2, column=1)
convert_currency_str = StringVar()
convert_currency_menu = tb.Menu(convert_currency)

for i in currency_codes:
    currency_menu.add_radiobutton(
        label=i, variable=currency_str, command=lambda i=i: chooseCurrency(i)
    )
    convert_currency_menu.add_radiobutton(
        label=i, variable=convert_currency_str, command=lambda i=i: convertCurrency(i)
    )
convert_currency["menu"] = convert_currency_menu
user_currency["menu"] = currency_menu

# -------------------------------------
space(3, 0)
space(3, 1)
# --------------------------------------
Final_Output_label = tb.Label(win_frame_1, text="Result :", bootstyle="primary")
Final_Output_label.grid(row=4, column=0)
Final_Output_Entry = tb.Entry(win_frame_1, bootstyle="info", state="readonly" , textvariable=entry_var)
Final_Output_Entry.grid(row=4, column=1)

# ---------------------------------------
space_win(1,0)
space(5,0)
submit_button = tb.Button(win_frame_1 , text = "Convert" , bootstyle="success , outline" ,width=40,command = convert_rave)
submit_button.grid(row=6 , columnspan=5)
main_window.mainloop()
