import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG

class createWindow(QW.QWidget):
    def __init__(self,width, height, title, icon):
        super().__init__()
        self.initializeUI(width, height, title, icon)

    def initializeUI(self, width, height, title, icon):
        self.setGeometry(0 , 0, width, height)
        self.setWindowTitle(title)
        self.setWindowIcon(QG.QIcon(icon))

        #BELOW 3 LINES WILL CENTER THE WINDOW    
        qr = self.frameGeometry()
        qr.moveCenter(QW.QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

        # FONT
        font = QG.QFont('Arial')
        font.setPixelSize(30)

        # CONFIGURE THE LAYOUT
        grid = QW.QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(2)

        

        # EDITOR / TEXT PANEL
        editor = QW.QTextEdit()
        editor.setFont(font)
        grid.addWidget(editor,0,0,1,4)
        
        # BUTTONS
        btn_names = ['AC', '<-', '%', '/',
                     '7' , '8' , '9', '*',
                     '4' , '5' , '6', '-',
                     '1' , '2' , '3', '+',
                     '.' , '0' , '=']

        # i is for Columns and j is for Rows and this type of expression exist in python WTF, it's just awesome no words to say..
        positions = [(i+1, j) for i in range(4) for j in range(4)]
        positions.extend([(5,0),(5,1),(5,2)])

        buttons = []
        for position, btn_name, index in zip(positions, btn_names, range(len(btn_names))):
            # Row = position[0]
            # Column = position[1]
            buttons.append(QW.QPushButton(btn_name))
            buttons[index].setStyleSheet("padding:22%;font:17px;")
            if(position[0]==5 and position[1]==2):
             grid.addWidget(buttons[index],*position,1,2)
            else:
             grid.addWidget(buttons[index],*position)

        # THIS IS SECTION IS CREATED DUE TO A BUG IN PYQT5 fucking gay developers
        def btn_ac(self):
            editor.clear()
            checkInput()
        def btn_idk(self):
            editor.setText(editor.toPlainText()[0:len(editor.toPlainText())-1])
            checkInput()
        def btn_0(self):
            editor.setText(editor.toPlainText()+"0")
            checkInput()
        def btn_1(self):
            editor.setText(editor.toPlainText()+"1")
            checkInput()
        def btn_2(self):
            editor.setText(editor.toPlainText()+"2")
            checkInput()
        def btn_3(self):
            editor.setText(editor.toPlainText()+"3")
            checkInput()
        def btn_4(self):
            editor.setText(editor.toPlainText()+"4")
            checkInput()
        def btn_5(self):
            editor.setText(editor.toPlainText()+"5")
            checkInput()
        def btn_6(self):
            editor.setText(editor.toPlainText()+"6")
            checkInput()
        def btn_7(self):
            editor.setText(editor.toPlainText()+"7")
            checkInput()
        def btn_8(self):
            editor.setText(editor.toPlainText()+"8")
            checkInput()
        def btn_9(self):
            editor.setText(editor.toPlainText()+"9")
            checkInput()
        def btn_mod(self):
            editor.setText(editor.toPlainText()+"%")
            checkInput()
        def btn_add(self):
            editor.setText(editor.toPlainText()+"+")
            checkInput()
        def btn_mul(self):
            editor.setText(editor.toPlainText()+"*")
            checkInput()
        def btn_sub(self):
            editor.setText(editor.toPlainText()+"-")
            checkInput()
        def btn_div(self):
            editor.setText(editor.toPlainText()+"/")
            checkInput()
        def btn_eql(self):
            ans = editor.toPlainText().strip()

            try:
             ans = str(eval(ans))
             editor.clear()
             editor.setText(ans)
             editor.setStyleSheet("color:black;")
            except:
             editor.setStyleSheet("color:red;")
            
        def btn_dot(self):
            editor.setText(editor.toPlainText()+".")  
        
        def checkInput():
            try:
             eval(editor.toPlainText().strip())
             editor.setStyleSheet("color:black;")
            except:
             editor.setStyleSheet("color:red;")


        # ADD EVENTS TO THE BUTTONS
        buttons[0].clicked.connect(btn_ac)
        buttons[0].setShortcut("space")

        buttons[1].clicked.connect(btn_idk)
        buttons[1].setShortcut("backspace")

        buttons[2].clicked.connect(btn_mod)
        buttons[2].setShortcut("shift+5")

        buttons[3].clicked.connect(btn_div)
        buttons[3].setShortcut("/")

        buttons[4].clicked.connect(btn_7)
        buttons[4].setShortcut("7")

        buttons[5].clicked.connect(btn_8)
        buttons[5].setShortcut("8")

        buttons[6].clicked.connect(btn_9)
        buttons[6].setShortcut("9")

        buttons[7].clicked.connect(btn_mul)
        buttons[7].setShortcut("*")

        buttons[8].clicked.connect(btn_4)
        buttons[8].setShortcut("4")

        buttons[9].clicked.connect(btn_5)
        buttons[9].setShortcut("5")

        buttons[10].clicked.connect(btn_6)
        buttons[10].setShortcut("6")

        buttons[11].clicked.connect(btn_sub)
        buttons[11].setShortcut("-")

        buttons[12].clicked.connect(btn_1)
        buttons[12].setShortcut("1")

        buttons[13].clicked.connect(btn_2)
        buttons[13].setShortcut("2")

        buttons[14].clicked.connect(btn_3)
        buttons[14].setShortcut("3")

        buttons[15].clicked.connect(btn_add)
        buttons[15].setShortcut("+")

        buttons[16].clicked.connect(btn_dot)
        buttons[16].setShortcut(".")

        buttons[17].clicked.connect(btn_0)
        buttons[17].setShortcut("0")

        buttons[18].clicked.connect(btn_eql)
        buttons[18].setShortcut("return")




def main():
    App = QW.QApplication(sys.argv)
    main_window = createWindow(300,400,"Calculator","assets/icon.png")
    # ADD YOUR SHIT HERE



    # END OF SHIT 
    main_window.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()