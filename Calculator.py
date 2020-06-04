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
            buttons[index].setStyleSheet("padding:22%;")
            if(position[0]==5 and position[1]==2):
             grid.addWidget(buttons[index],*position,1,2)
            else:
             grid.addWidget(buttons[index],*position)

        # THIS IS SECTION IS CREATED DUE TO A BUG IN PYQT5 fucking gay developers
        def btn_ac(self):
            editor.clear()
        def btn_idk(self):
            print("Pressed idk")
        def btn_0(self):
            print("Pressed 0")
            editor.setText(editor.toPlainText()+"0")
        def btn_1(self):
            print("Pressed 1")
            editor.setText(editor.toPlainText()+"1")
        def btn_2(self):
            print("Pressed 2")
            editor.setText(editor.toPlainText()+"2")
        def btn_3(self):
            print("Pressed 3")
            editor.setText(editor.toPlainText()+"3")
        def btn_4(self):
            print("Pressed 4")
            editor.setText(editor.toPlainText()+"4")
        def btn_5(self):
            print("Pressed 5")
            editor.setText(editor.toPlainText()+"5")
        def btn_6(self):
            print("Pressed 6")
            editor.setText(editor.toPlainText()+"6")
        def btn_7(self):
            print("Pressed 7")
            editor.setText(editor.toPlainText()+"7")
        def btn_8(self):
            print("Pressed 8")
            editor.setText(editor.toPlainText()+"8")
        def btn_9(self):
            print("Pressed 9")
            editor.setText(editor.toPlainText()+"9")
        def btn_mod(self):
            print("Pressed mod")
            editor.setText(editor.toPlainText()+"%")
        def btn_add(self):
            print("Pressed add")
            editor.setText(editor.toPlainText()+"+")
        def btn_mul(self):
            print("Pressed mul")
            editor.setText(editor.toPlainText()+"*")
        def btn_sub(self):
            print("Pressed sub")
            editor.setText(editor.toPlainText()+"-")
        def btn_div(self):
            print("Pressed div")
            editor.setText(editor.toPlainText()+"/")
        def btn_eql(self):
            print("Pressed eql")
            ans = editor.toPlainText().strip()
            try:
             ans = str(eval(ans))
             editor.clear()
             editor.setText(ans)
            except:
             print("Error Occured")

            
        def btn_dot(self):
            print("Pressed dot")
            editor.setText(editor.toPlainText()+".")  

        # ADD EVENTS TO THE BUTTONS
        buttons[0].clicked.connect(btn_ac)
        buttons[1].clicked.connect(btn_idk)
        buttons[2].clicked.connect(btn_mod)
        buttons[3].clicked.connect(btn_div)
        buttons[4].clicked.connect(btn_7)
        buttons[5].clicked.connect(btn_8)
        buttons[6].clicked.connect(btn_9)
        buttons[7].clicked.connect(btn_mul)
        buttons[8].clicked.connect(btn_4)
        buttons[9].clicked.connect(btn_5)
        buttons[10].clicked.connect(btn_6)
        buttons[11].clicked.connect(btn_sub)
        buttons[12].clicked.connect(btn_1)
        buttons[13].clicked.connect(btn_2)
        buttons[14].clicked.connect(btn_3)
        buttons[15].clicked.connect(btn_add)
        buttons[16].clicked.connect(btn_dot)
        buttons[17].clicked.connect(btn_0)
        buttons[18].clicked.connect(btn_eql)




def main():
    App = QW.QApplication(sys.argv)
    main_window = createWindow(300,400,"Calculator",None)
    # ADD YOUR SHIT HERE




    # END OF SHIT 
    main_window.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()