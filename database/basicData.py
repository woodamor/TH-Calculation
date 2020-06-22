# -*- coding: UTF-8 -*-
from PyQt5.QtCore import QDate, QFile, QFileInfo, QIODevice, QDataStream

# 桩基基本信息
class PileInfo(object):
    def __init__(self, label = "1#", diameter = 0, top_elev = 0.0, design_load = 0.0):
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

# 缺少计算参数的类