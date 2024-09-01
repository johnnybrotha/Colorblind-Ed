from tkinter import *
import random
from tkinter import ttk

colorNamesList = []
colorHexesList = []
RGBList = []

with open("labelledcolorhexes.txt", 'r') as filestream:
    for line in filestream:
        currLine = line.split(",")
        colorNamesList.append(currLine[0][1:-1])
        colorHexesList.append(currLine[1][1:-1])
        RGBList.append([currLine[2][1:-1], currLine[3][1:-1], currLine[4][1:-1]])


# easy 32 choose 9
easy = [7, 12, 18, 24, 25, 27, 42, 45, 47, 49, 50, 54, 82, 87, 88, 92, 93, 98, 127, 124, 131, 158, 161, 147, 135, 137, 107, 112, 55, 80, 33, 36]
    

# medium 80 choose 12
medium = [7, 12, 18, 19, 20, 24, 25, 27, 28, 32, 33, 36, 37, 38, 40, 41, 13, 14, 21, 22, 42, 43, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 60, 64, 67, 68, 69, 72, 80, 82, 85, 87, 88, 89, 92, 93, 96, 97, 98, 99, 104, 105, 107, 110, 112, 118, 120, 113, 116, 123, 124, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 145, 147, 149, 151, 154, 161]

# hard 163 choose 15
hard = list(range(163))



def newSet(difficultyList, batch):
    res = {}
    while len(res) < batch:
        newColorIndex = random.choice(difficultyList)
        res[colorNamesList[newColorIndex]] = colorHexesList[newColorIndex]
    return res



# class structure

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x150")
        self.menu()
    
    def playEasy(self):
        self.colorOptions = newSet(easy, 9)
        self.play()
    def playMed(self):
        self.colorOptions = newSet(medium, 12)
        self.play()
    def playHard(self):
        self.colorOptions = newSet(hard, 15)
        self.play()
    def playImp(self):
        self.colorOptions = newSet(hard, len(hard) // 2)
        self.searchPlay()

    def menu(self):
        self.master.geometry("600x150")
        self.master.title("Menu")
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master)
        self.frame1.pack()
        self.title = Label(self.frame1, text='Choose a Difficulty:', font = ("EB Garamond", 30))
        self.title.grid(column=1, row=0)
        self.easyBtn = Button(self.frame1, text="Easy", command=self.playEasy, font=("EB Garamond", 25))
        self.easyBtn.grid(column=0, row=1)
        self.medBtn = Button(self.frame1, text="Medium", command=self.playMed, font=("EB Garamond", 25))
        self.medBtn.grid(column=1, row=1)
        self.hardBtn = Button(self.frame1, text="Hard", command=self.playHard, font=("EB Garamond", 25))
        self.hardBtn.grid(column=2, row=1)
        self.impBtn = Button(self.frame1, text="Impossible", fg= 'red', command=self.playImp, font=("EB Garamond", 25))
        self.impBtn.grid(column=1, row=2)

    def letterFlips(self, query):
            colors = []
            for color in list(self.colorOptions.keys()):
                for i in range(0, len(color) - len(query) + 1):
                    for j in range(0, len(query)):
                        if query[j] not in color[i:i + len(query)]:
                            break
                        elif query[j] in color[i:i + len(query)] and j == len(query) - 1:
                            colors.append(color)
            return colors

    def searchPlay(self):
        global currColorName
        global currColorHex
        currColorName = "White"
        currColorHex = "#FFFFFF"
        
        def newColor(self):
            global currColorName
            global currColorHex
            nextColor = random.choice(list(self.colorOptions.keys()))
            if nextColor == currColorName:
                newColor(self)
                return
            currColorName = nextColor
            currColorHex = self.colorOptions[currColorName]
            colorFrame.config(bg=currColorHex)   

        def colorClicked(event):
            selected_index = resultView.curselection()
            if selected_index:
                color = resultView.get(selected_index)

                if color == currColorName:
                    newColor(self)
                else:
                    print(f'no the correct color is {currColorName}')
        def returnToMenu():
            self.menu()


        self.master.title("Redy to See Color?")
        for i in self.master.winfo_children():
            i.destroy()
        self.master.geometry("600x400")

        lbl = Label(self.master, text = "What color is this?", font = ("EB Garamond", 25))
        lbl.grid(column=1, row=1)


    

        def checkQuery(event):
            global colorOptions
            query = searchInput.get()
            suggests = []
            if query == "":
                resultView.delete(0, END)
                print('nothing searched')
            else:
                resultView.delete(0, END)
                [suggests.append(i) for i in list(self.colorOptions.keys()) if query.lower() in i.lower() and i not in suggests]
                if len(suggests) < 5:
                    [suggests.append(flip) for flip in self.letterFlips(query) if flip not in suggests]
                elif suggests == []:
                    suggests.append('try another search')
                    print('try another search')
            for suggest in suggests:
                resultView.insert(END, suggest)
        
        searchInput = StringVar()
        textBox = Entry(self.master, textvariable=searchInput)
        textBox.bind('<KeyRelease>', checkQuery)
        textBox.grid(column=1, row=2)

        

        resultView = Listbox(self.master)
        resultView.insert(0, *sorted(list(self.colorOptions.keys())))
        resultView.grid(column = 1, row = 3)
        resultView.bind('')g
        
        colorFrame = Frame(self.master, width=250, height=250)
        colorFrame.grid(column=0, row=1)
        newColor(self)

        returnBtn = Button(self.master, text="Return to Menu", font=("EB Garamond", 14), command=returnToMenu)
        returnBtn.grid(column=0, row=0)
        resultView.bind('<<ListboxSelect>>', colorClicked)





    def play(self):
        global currColorName
        global currColorHex
        currColorName = "White"
        currColorHex = "#FFFFFF"
        
        def newColor(self):
            global currColorName
            global currColorHex
            nextColor = random.choice(list(self.colorOptions.keys()))
            if nextColor == currColorName:
                newColor(self)
                return
            currColorName = nextColor
            currColorHex = self.colorOptions[currColorName]
            colorFrame.config(bg=currColorHex)   

        def enterBtnClicked():
            if colorChoice.get() == currColorName:
                newColor(self)
        def returnToMenu():
            self.menu()

        

        self.master.title("Redy to Learn Color?")
        for i in self.master.winfo_children():
            i.destroy()
        self.master.geometry("600x400")

        lbl = Label(self.master, text = "What color is this?", font = ("EB Garamond", 25))
        lbl.grid(column=1, row=1)

        colorChoice = StringVar(self.master)
        colorChoice.set(list(self.colorOptions.keys())[0])
        colorDrop = OptionMenu(self.master, colorChoice, *list(self.colorOptions.keys()))
        colorDrop.grid(column=1, row=2)

        colorFrame = Frame(self.master, width=250, height=250)
        colorFrame.grid(column=0, row=1)
        newColor(self)


        enterBtn = Button(self.master, text="Enter", font=("EB Garamond", 20), command=enterBtnClicked)
        enterBtn.grid(column=2, row=2)

        returnBtn = Button(self.master, text="Return to Menu", font=("EB Garamond", 14), command=returnToMenu)
        returnBtn.grid(column=0, row=0)

        
        
        





            






# root.geometry("600x400") 
# root.tk.call('tk', 'scaling', 3.0)









root = Tk()
app(root)
root.mainloop()






#colorDict = {"Red":"#FF0000", "Green":"#00FF00", "Blue":"#0000FF", "Yellow":"#FFFF00", "Orange":"#FFA500", "Purple":"#800080", "Pink":"#FFC0CB", "Brown":"#964B00", "Black":"#000000", "White":"#FFFFFF"}
