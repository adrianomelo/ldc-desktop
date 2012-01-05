# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from libs.harddisk.frame_harddisk_module import Ui_FrameHarddiskModule

class GUIHarddiskModule(QtGui.QGroupBox, Ui_FrameHarddiskModule):
    """Estende de 'QtGui.QGroupBox' e 'Ui_FrameHarddiskModule'
    Classe que define um GroupBox para a exibição das informações das partições.
    """

    def __init__(self, parent, deviceFile, filesystem, mountingPoint, size, freeSize):
        """Construtor

        Parâmetros:
        parent -- Frame pai
        deviceFile -- string com o device file
        filesystem -- string com o tipo de sistema de arquivo
        mountingPoint -- string com o ponto de montagem da partição
        size -- int que indica o tamanho da partição
        freeSize -- int que indica o tamanho livre da partição
        """
        QtGui.QGroupBox.__init__(self, parent)
        Ui_FrameHarddiskModule.__init__(self)

        self.setupUi(self)
        deviceFile = self.__check_invalid_values(deviceFile);
        filesystem = self.__check_invalid_values(filesystem);
        mountingPoint = self.__check_invalid_values(mountingPoint);
        freeSize = self.__check_invalid_values(freeSize);

        self.deviceFileLineEdit.setText(QtGui.QApplication.translate("FrameHarddiskModule", deviceFile, None, QtGui.QApplication.UnicodeUTF8))
        self.filesystemLineEdit.setText(QtGui.QApplication.translate("FrameHarddiskModule", filesystem, None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLineEdit.setText(QtGui.QApplication.translate("FrameHarddiskModule", size.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        self.freeSizeLineEdit.setText(QtGui.QApplication.translate("FrameHarddiskModule", freeSize.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        self.mountingPointLineEdit.setText(QtGui.QApplication.translate("FrameHarddiskModule", mountingPoint, None, QtGui.QApplication.UnicodeUTF8))


    def __check_invalid_values(self, value):
        """
        Verifica se há valores inválidos ou irrelevantes em uma lista.
        """
        ret = ""

        if (value):
            if (value != "Other" and value != "NULL" and value != "Unknown"):
                ret = value

        return ret
