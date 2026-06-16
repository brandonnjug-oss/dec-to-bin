import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Binary Converter")
root.geometry("730x275")

decNumInput = tk.StringVar()
binNumOutpt = tk.StringVar()
binNumOutpt.set('00000000')

title = tk.Label(root, text="Decimal to Binary Converter", font=("Sergoe UI", 30, 'bold'))
title.pack(pady=15)

inptFrame = tk.Frame()
inptFrame.pack(anchor="w", pady=0,)

promptText = tk.Label(inptFrame, text=" Decimal Number: ", font=("Segoe UI", 24))
promptText.pack(side="left")

numInpt = ttk.Entry(inptFrame, textvariable=decNumInput, font=("Segoe UI", 24), width=26)
numInpt.pack(side="left")

def on_change():
    on_enter()

decNumInput.trace_add("write", lambda *args: on_change())

guideTxt = tk.Label(root, text=" ", font=("Segoe UI", 18))
guideTxt.pack()

outptFrame = tk.Frame()
outptFrame.pack(anchor="w")

outptTxt = tk.Label(outptFrame, text=' Binary Equivalent: ', font=("Segoe UI", 24))
outptTxt.pack(side="left", pady=10)
numOutpt = tk.Entry(outptFrame, textvariable=binNumOutpt, state="readonly", font=("Segoe UI", 24), width=26)
numOutpt.pack(side="left")


def on_enter():
    decNum = decNumInput.get()
    while True:
        if decNum != "":
            try:
                decNum = int(decNum)
            except ValueError:
                binNumOutpt.set(" Error. Enter an integer")
                break
        else:
            binNumOutpt.set("00000000")
            break
        
        if decNum > 16777215:
            binNumOutpt.set(" Error. Number too big")
            break

        if decNum < -8388607:
            binNumOutpt.set(" Error. Number too small")
            break
        
        binNum = bin(decNum).replace('0b', '')
        #binNum = binNum.zfill((len(binNum) + 7) // 8 * 8)
        #binNum = ' '.join(binNum[i:i+8] for i in range(0, len(binNum), 8))
        binNumOutpt.set(binNum)
        break

numInpt.bind("<Return>", lambda e: on_enter())

root.mainloop()