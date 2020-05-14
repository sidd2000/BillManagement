# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:34:48 2020

@author: Siddhant
"""

from tkinter import *
from interface1 import *
import pandas as pd
from IPython.display import HTML
from tabulate import tabulate

sno = 1
df = ""
bill = ""
window2 = ""

def dataframe():
    global sno, df, name, address, contact
    amount = [rate[i] * quantity[i] for i in range(len(quantity))]
    total = sum(amount)

    df = pd.DataFrame(columns =['S.No','Customer Name','Address','Contact','Item No.','Item','Item Description','Rate','Quantity','Amount'] )
    
    itemnumber = 1
    for i in range(len(quantity)):
        df = df.append({'S.No' : sno,
                        'Customer Name' : name,
                        'Address' : address,
                        'Contact' : contact,
                        'Item No.' : itemnumber,
                        'Item' : item[i],
                        'Item Description' : desc[i],
                        'Rate' : rate[i],
                        'Quantity' : quantity[i],
                        'Amount' : amount[i]}, ignore_index = True)
        itemnumber += 1
        sno = ' '
        name = ' '
        address = ' '
        contact = ' '
    df = df.append({'S.No' : " ",
                   'Customer Name' : " ",
                   'Address' : " ",
                   'Contact' : " ",
                   'Item No.' : " ",
                   'Item' : " ",
                   'Item Description' : " ",
                   'Rate' : " ",
                   'Quantity' : " ",
                   'Amount' : "Total: {0}".format(total)}, ignore_index = True)
    df = df.append({'S.No' : " ",
                   'Customer Name' : " ",
                   'Address' : " ",
                   'Contact' : " ",
                   'Item No.' : " ",
                   'Item' : " ",
                   'Item Description' : " ",
                   'Rate' : " ",
                   'Quantity' : " ",
                   'Amount' : " "}, ignore_index = True)

    pd.set_option('display.expand_frame_repr', False)
    
    
def close():
    global window2
    window2.destroy()
    #print("Hello")


def file():
    global sno, bill
    try:
        bill = pd.read_csv("Bill Data.csv")
        tempdf = bill.fillna('')
        l1 = tempdf['S.No'].tolist()
        l1 = l1[::-1]
        temp = [i for i in l1 if type(i) == float]
        sno = int(temp[0]) + 1
    except:
        bill = pd.DataFrame(columns =['S.No','Customer Name','Address','Contact','Item No.','Item','Item Description','Rate','Quantity','Amount'] )
        sno = 1
        
        
def save():
    global bill
    bill = bill.append(df, ignore_index = True)
    bill.to_csv("Bill Data.csv", index = False)
    close()

def errorinterface():
    global window2
    window2 = Tk()
    Label(window2, text = error,font = "TimesNewRoman 20 bold").grid(row = 1, column = 0, sticky = W)
    Button(window2, text = "OK", width = 10, command = close).grid(row = 500, column = 0,sticky = W)
    window2.mainloop()
    
    
def interface():
    global window2
    window2 = Tk()
    frame = Frame(window2, width = 1500, height = 1500)
    frame.pack()
    tbox = Text(frame)
    tbox.insert(END,tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    tbox.place(x =10, y = 10, width = 1400, height = 550)
    Button(window2, text = "SAVE", width = 10, command = save).place(x = 10, y = 580, width = 80, height = 40)
    Button(window2, text = "CANCEL", width = 10, command = close).place(x = 130, y = 580, width = 80, height = 40)

    window2.mainloop()

if error == "":
    file()
    dataframe()
    interface()
else:
    errorinterface()