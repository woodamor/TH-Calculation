# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.mainFrame import Ui_MainWindow
from database.borehole import Borhole
from database.basicData import PileInfo


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)

        self.PileInfo = PileInfo()

        self.push_btn_save.clicked.connect(self.save_data_from_ui)
        self.push_btn_load.clicked.connect(self.load_data_to_ui)

    def load_data_to_ui(self):
        self.load_pile_info()

    def save_data_from_ui(self):
        self.save_pile_info()

    def load_pile_info(self):
        self.PileInfo.load_datastream("save_data")
        self.textEdit_pile_label.setText(self.PileInfo.label)
        self.textEdit_pile_diameter.setText(str(self.PileInfo.diameter))
        self.textEdit_pile_top_elev.setText(str(self.PileInfo.top_elev))
        self.textEdit_design_load.setText(str(self.PileInfo.design_load))

    def save_pile_info(self):
        self.PileInfo.label = 	self.textEdit_pile_label.toPlainText()
        if(self.textEdit_pile_diameter.toPlainText()):
            self.PileInfo.diameter = int(self.textEdit_pile_diameter.toPlainText())
        
        if(self.textEdit_pile_top_elev.toPlainText()):
            self.PileInfo.top_elev = float(self.textEdit_pile_top_elev.toPlainText())

        if(self.textEdit_design_load.toPlainText()):
            self.PileInfo.design_load = float(self.textEdit_design_load.toPlainText())

        self.PileInfo.save_datastream("save_data")

if __name__ == '__main__':
    path = 'text_qstream_save'
    app = QApplication(sys.argv)
    myWin = MyMainForm()   

    # basic_info = PileInfo("1#_qstream_test", 1500, 32.123, 3500.5)
    # myWin.PileInfo = basic_info

    myWin.show()
    sys.exit(app.exec_())
