from cgitb import enable
from tkinter import *
from WebScraper import getStockPriceDict, scrapeStockPrice
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

global stockPriceHistory
stockPriceHistory = []
global counter
counter = [0]

def clickFunc():
    global stock
    stock = entry.get()

    if(stock != ""):
        global newLabel
        stockPrice = scrapeStockPrice(stock)
        stockPriceHistory.append(stockPrice)
        if(stockPrice == "-1"):
            newLabel = Label(root, text="INVALID STOCK TICKER", font=("Courier", 12))
            newLabel.pack()
            newButton['state'] = DISABLED
            return
        newLabel = Label(root, text="The price of " + stock + " is $" + stockPrice, font=("Courier", 12))
        newLabel.pack()
        newButton['state'] = DISABLED

def deleteStock():
    newLabel.destroy()
    newButton['state'] = ACTIVE
    stockPriceHistory.clear()
    return

def animateGraph(i):
    print("counter " + str(counter))
    print("history " + str(stockPriceHistory))

    plt.cla()
    plt.plot(counter, stockPriceHistory)

    counter.append(counter[-1] + 20)
    stockPriceHistory.append(float(scrapeStockPrice(stock)))
    return

def startGraph():
    plt.style.use('fivethirtyeight')
    plt.tight_layout()
    ani = FuncAnimation(plt.gcf(), animateGraph, interval = 20000)
    
    plt.show()
    return

root = Tk(className="StockWebScraper")
root.geometry("300x300")
root.resizable(width=False, height=False)


entry = Entry(root, width="30")
entry.insert(0, "Ex. AMD, MSFT, SPY...")
entry.pack()

newButton = Button(root, text="Add stock ticker", pady="20", padx="30", command=clickFunc)
newButton.pack()

deleteButton = Button(root, text="Remove stock ticker", pady="20", padx="30", command=deleteStock)
deleteButton.pack()

graphButton = Button(root, text="Graph current stock", pady="20", padx="30", command=startGraph)
graphButton.pack()


root.mainloop()