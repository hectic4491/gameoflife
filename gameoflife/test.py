import tkinter as tk
from functools import partial


def OpenWindow(root):

    securityWindow = tk.Toplevel()
    securityWindow.title("Submit?")
    securityWindow.geometry("200x100")
    securityWindow.rowconfigure(0, weight=1)
    securityWindow.columnconfigure(0, weight=1)

    securityFrame = tk.Frame(master=securityWindow)
    securityFrame.rowconfigure([0, 1], weight=1)
    securityFrame.columnconfigure([0, 1], weight=1)

    SecurityLabel = tk.Label(master=securityFrame,
                             text="Submit Changes?")

    YesButton = tk.Button(master=securityFrame,
                          text="Yes",
                          command=partial(SubmitYes, securityWindow, root))

    NoButton = tk.Button(master=securityFrame,
                         text="No",
                         command=partial(SubmitNo, securityWindow))

    securityFrame.grid(row=0,
                       column=0,
                       sticky="nsew")

    SecurityLabel.grid(row=0,
                       column=0,
                       columnspan=2,
                       sticky="ew")

    YesButton.grid(row=1,
                   column=0,
                   sticky="ew",
                   padx=5,
                   pady=5)
 
    NoButton.grid(row=1,
                  column=1,
                  sticky="ew",
                  padx=5,
                  pady=5)




def SubmitYes(securityWindow, root):
    securityWindow.destroy()
    root.geometry("400x300")
    print("Yes")




def SubmitNo(securityWindow):
    securityWindow.destroy()
    print("No")




### MAIN ###
def main():
    root = tk.Tk()
    root.title("Big Window")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    #root.attributes("-zoomed", False)

    rootFrame = tk.Frame(master=root)
    rootFrame.pack(fill=tk.BOTH, expand=True)

    btn = tk.Button(master=rootFrame,
                    text="Submit Settings",
                    command=partial(OpenWindow, root),
                    width=20,
                    height=4)

    btn.pack()

    root.update_idletasks()
    root.mainloop()




if __name__ == "__main__":
    main()