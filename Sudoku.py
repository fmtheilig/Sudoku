# Sudoku Solver
#
from tkinter import *
class Window( Frame ):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Sudoku Solver!")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Solve!", command=self.client_exit)

        quitButton.place(x=170, y=350)

    def client_exit(self):
        exit()

Board = []
Element = [0, True, True, True, True, True, True, True, True, True]

def NoZeros( num ):
    if num == 0:
        return "   "
    else:
        return " " + str( num ) + " "

def BoxChr( i ):
    return bytes((i,)).decode("cp437")

def BoxLine( i ):
    line = ""
    for x in i:
        line = line + BoxChr( x )
    return line

def SS_Print( char ):
    print( char )
    Label(root, text=char, font=("courier",12)).pack()
    
def Display( Board ):
    tline = BoxLine([201,205,205,205,209,205,205,205,209,205,205,205,203,205,205,205,209,205,205,205,209,205,205,205,203,205,205,205,209,205,205,205,209,205,205,205,187])
    mline = BoxLine([199,196,196,196,197,196,196,196,197,196,196,196,215,196,196,196,197,196,196,196,197,196,196,196,215,196,196,196,197,196,196,196,197,196,196,196,182])
    nline = BoxLine([204,205,205,205,216,205,205,205,216,205,205,205,206,205,205,205,216,205,205,205,216,205,205,205,206,205,205,205,216,205,205,205,216,205,205,205,185])
    bline = BoxLine([200,205,205,205,207,205,205,205,207,205,205,205,202,205,205,205,207,205,205,205,207,205,205,205,202,205,205,205,207,205,205,205,207,205,205,205,188])
    i = 0
    SS_Print( tline )
    char=""
    while ( i < 9 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( mline )
    char = ""
    while ( i < 18 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print(char)
    SS_Print( mline )
    char=""
    while ( i < 27 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print(char)
    SS_Print( nline )
    char=""
    while ( i < 36 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( mline )
    char=""
    while ( i < 45 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( mline )
    char=""
    while ( i < 54 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( nline )
    char=""
    while ( i < 63 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( mline )
    char=""
    while ( i < 72 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( mline )
    char=""
    while ( i < 81 ):
        if i % 3 == 0:
            char=char+BoxChr(186)
        else:
            char=char+BoxChr(179)
        char=char+NoZeros(Board[i][0])
        i += 1
    char=char+BoxChr(186)
    SS_Print( char )
    SS_Print( bline )
    
def Populate( Board ):
    DefBoard = [4,0,6,5,0,0,0,0,0,1,0,5,3,9,0,0,4,0,0,0,0,0,1,4,0,3,6,3,4,0,0,0,0,6,9,0,8,0,0,0,0,0,0,0,4,0,6,2,0,0,0,0,1,7,2,8,0,4,6,0,0,0,0,0,9,0,0,8,5,7,0,3,0,0,0,0,0,2,4,0,1]
    i = 0
    while (i < 81):
        Board.append( [DefBoard[i], True, True, True, True, True, True, True, True, True] )
        i += 1

def Solve( self ):
#    for i in range(0, 81):

    exit()

root = Tk()
root.geometry("400x550")
app = Window( root )

Populate( Board )
Display( Board )
#Solve( Board )
#Display( Board )
