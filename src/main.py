import os, sys
from PyQt4 import QtCore, QtGui
from gui.LDC_Main import LDC_Main

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)

#    main = LDC_Main()
    main = LDC_Main(app)
    main.selectTests()
    main.show()

    sys.exit(app.exec_())