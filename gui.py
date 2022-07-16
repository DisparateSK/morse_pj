import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Converter")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_13=tk.Button(root)
        GButton_13["anchor"] = "s"
        GButton_13["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=14)
        GButton_13["font"] = ft
        GButton_13["fg"] = "#ffffff"
        GButton_13["justify"] = "center"
        GButton_13["text"] = "Let's translate"
        GButton_13["relief"] = "raised"
        GButton_13.place(x=190,y=230,width=214,height=78)
        GButton_13["command"] = self.GButton_13_command

        GLineEdit_712=tk.Entry(root)
        GLineEdit_712["borderwidth"] = "1px"
        GLineEdit_712["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_712["font"] = ft
        GLineEdit_712["fg"] = "#333333"
        GLineEdit_712["justify"] = "center"
        GLineEdit_712["text"] = "Entry"
        GLineEdit_712.place(x=190,y=140,width=212,height=79)

        GMessage_483=tk.Message(root)
        ft = tkFont.Font(family='Times',size=18)
        GMessage_483["font"] = ft
        GMessage_483["fg"] = "#333333"
        GMessage_483["justify"] = "center"
        GMessage_483["text"] = "Text to Morse Code Converter"
        GMessage_483.place(x=90,y=30,width=429,height=99)

        GMessage_405=tk.Message(root)
        GMessage_405["anchor"] = "s"
        GMessage_405["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_405["font"] = ft
        GMessage_405["fg"] = "#333333"
        GMessage_405["justify"] = "center"
        GMessage_405["text"] = "Message"
        GMessage_405.place(x=190,y=340,width=214,height=78)

    def GButton_13_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
