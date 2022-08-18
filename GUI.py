from cgitb import enable
from tkinter import *
from WebScraper import getStockPriceDict, scrapeStockPrice

global counter
root = Tk(className="StockWebScraper")
root.geometry("300x200")
root.resizable(width=False, height=False)

def clickFunc():
    stock = entry.get()

    if(stock != ""):
        global newLabel
        stockPrice = scrapeStockPrice(stock)
        if(stockPrice == "-1"):
            newLabel = Label(root, text="INVALID STOCK TICKER.", font=("Courier", 12))
            newLabel.pack()
            newButton['state'] = DISABLED
            return
        newLabel = Label(root, text="The price of " + stock + " is $" + stockPrice, font=("Courier", 12))
        newLabel.pack()
        newButton['state'] = DISABLED

def deleteStock():
    newLabel.destroy()
    newButton['state'] = ACTIVE
    return

entry = Entry(root, width="30")
entry.insert(0, "Ex. AMD, MSFT, SPY...")
entry.pack()

newButton = Button(root, text="Add stock ticker", pady="20", padx="30", command=clickFunc)
newButton.pack()

deleteButton = Button(root, text="Remove stock ticker", pady="20", padx="30", command=deleteStock)
deleteButton.pack()

root.mainloop()