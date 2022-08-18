from tkinter import *
from WebScraper import scrapeStockPrice
import itertools
#import pandas as pd

root = Tk(className="Python WebScraper")
root.geometry("700x700")

def clickFunc():
    stock = entry.get()

    if(stock != ""):
        global newLabel
        stockPrice = scrapeStockPrice(stock)
        newLabel = Label(root, text="The price of " + stock + " is $" + stockPrice)
        newLabel.pack()

def deleteStock():
    newLabel.destroy()
    return

entry = Entry(root, width="30")
entry.pack()

newButton = Button(root, text="Add a stock", pady="40", padx="100", command=clickFunc)
newButton.pack()

deleteButton = Button(root, text="Delete", command=deleteStock)
deleteButton.pack(pady="10")


root.mainloop()