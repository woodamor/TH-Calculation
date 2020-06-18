import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_MainWinSignalSlog01 import Ui_Form  # 使用vscode生成的调用方法
# from MainWinSignalSlog01 import Ui_Form  # 使用pycharm生成的调用方法
 
class MyMainWindow(QMainWindow,Ui_Form):
    def __init__(self,parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
