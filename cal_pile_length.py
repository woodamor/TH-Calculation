# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtCore import QDate, QFile, QFileInfo, QIODevice, QDataStream
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.mainFrame import Ui_MainWindow
from database.borehole import Borhole

class BasicInfo(object):
    def __init__(self, label = "", diameter = 0, top_elev = 0.0, design_load = 0.0):
        self.__fname = label
        self.label = label
        self.diameter = diameter
        self.top_elev = top_elev
        self.design_load = design_load
    
    def save_datastream(self, fname):
        error = None
        fh = None
        try:
            fh = QFile(fname)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            
            stream = QDataStream(fh)
            stream.writeQString(self.label)
            stream.writeInt32(self.diameter)
            stream.writeDouble(self.top_elev)
            stream.writeDouble(self.design_load)
            stream.setVersion(QDataStream.Qt_5_12)
        except EnvironmentError as e:
            error = "Failed to save:{0}".format(e)
        
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print(error)
            self.__dirty = False
            print("save to {0}".format(QFileInfo(fname).fileName))

    def load_datastream(self, fname):
        error = None
        fh = None

        try:
            fh = QFile(fname)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError(str(fh.errorString()))

            stream = QDataStream(fh)
            while not stream.atEnd():
                self.label = stream.readQString()
                self.diameter = stream.readInt32()
                self.top_elev = stream.readDouble()
                self.design_load = stream.readDouble()
        except EnvironmentError as e:
            error = "Failed to load:{0}".format(e)
        
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print(error)
            self.__dirty = False
            print("load data from{0}".format(QFileInfo(fname).fileName()))


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)

        self.basicInfo = BasicInfo()

        self.push_btn_save.clicked.connect(self.save_data)
        self.push_btn_load.clicked.connect(self.load_data)

    def load_data(self):
        self.basicInfo.load_datastream("save_data")
        self.textEdit_pile_label.setText(self.basicInfo.label)
        self.textEdit_pile_diameter.setText(str(self.basicInfo.diameter))
        self.textEdit_pile_top_elev.setText(str(self.basicInfo.top_elev))
        self.textEdit_design_load.setText(str(self.basicInfo.design_load))

    def save_data(self):
        self.basicInfo
        self.basicInfo.label = 	self.textEdit_pile_label.toPlainText()
        self.basicInfo.diameter = int(self.textEdit_pile_diameter.toPlainText())
        self.basicInfo.top_elev = float(self.textEdit_pile_top_elev.toPlainText())
        self.basicInfo.design_load = float(self.textEdit_design_load.toPlainText())

        self.basicInfo.save_datastream("save_data")


if __name__ == '__main__':
    path = 'text_qstream_save'
    app = QApplication(sys.argv)
    myWin = MyMainForm()   

    # basic_info = BasicInfo("1#_qstream_test", 1500, 32.123, 3500.5)
    # myWin.basicInfo = basic_info

    myWin.show()
    sys.exit(app.exec_())
