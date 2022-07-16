import tkinter as tk
import tkinter.font as tkFont
import pandas as pd


with open("morse.csv") as file:
    data = pd.read_csv(file, index_col=0, names=['morse'])

class App:
    def __init__(self, root):
        # setting title
        root.title("Converter")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_13 = tk.Button(root)
        GButton_13["anchor"] = "s"
        GButton_13["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times', size=14)
        GButton_13["font"] = ft
        GButton_13["fg"] = "#ffffff"
        GButton_13["justify"] = "center"
        GButton_13["text"] = "Let's translate"
        GButton_13["relief"] = "raised"
        GButton_13.place(x=190, y=230, width=214, height=78)
        GButton_13["command"] = self.translate_word

        self.input_word = tk.Entry(root)
        self.input_word["borderwidth"] = "1px"
        self.input_word["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        self.input_word["font"] = ft
        self.input_word["fg"] = "#333333"
        self.input_word["justify"] = "center"
        self.input_word["text"] = "Your word"
        self.input_word.place(x=190, y=140, width=212, height=79)

        GMessage_483 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=18)
        GMessage_483["font"] = ft
        GMessage_483["fg"] = "#333333"
        GMessage_483["justify"] = "center"
        GMessage_483["text"] = "Text to Morse Code Converter"
        GMessage_483.place(x=90, y=30, width=429, height=99)

        self.morse_word = tk.Message(root)

        self.morse_word["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=16)
        self.morse_word["font"] = ft
        self.morse_word["fg"] = "#333333"
        self.morse_word["justify"] = "center"
        self.morse_word["text"] = "Message"
        self.morse_word.place(x=190, y=340, width=214, height=99)

    def translate_word(self):
        user_word = self.input_word.get()
        new_word = ''
        for capital in user_word:
            new_word += data.morse[capital.capitalize()] + ' '
        self.morse_word["text"] = new_word
