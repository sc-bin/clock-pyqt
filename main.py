import sys
from PyQt5 import QtWidgets
import page

class my_page(page.Ui_MainWindow):
    pass

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = my_page()
ui.setupUi(window)


window.show()
sys.exit(app.exec_())
