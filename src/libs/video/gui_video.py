# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from libs.video.frame_video import Ui_videoFrame
from libs.video.frame_monitor import Ui_monitorFrame
from gui.LDC_Info import LDC_Info

class GUIVideo(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de vídeo.
    """
    name = "Video"
    category = "Multimidia"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResSound)
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagn�stico (lista de 'DaigResSound')
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_videoFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)


    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
#        print "DEBUG:", info_res
        ui.productLineEdit.setText(QtGui.QApplication.translate("videoFrame",self._check_invalid_values(info_res.model[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("videoFrame", self._check_invalid_values(info_res.vendor[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.driverModulesLineEdit.setText(QtGui.QApplication.translate("videoFrame", self._check_invalid_values(info_res.module), None, QtGui.QApplication.UnicodeUTF8))
        mod3D = "Não"
        if info_res.module3D == 1:
            mod3D = "Sim"
        ui.Module3DLineEdit.setText(QtGui.QApplication.translate("videoFrame", mod3D, None, QtGui.QApplication.UnicodeUTF8))
        extDr = ""
        if info_res.moduleExtensions:
            if (info_res.moduleExtensions[-1] == ""):
            	info_res.moduleExtensions.pop(-1)
            extDr = ", ".join(info_res.moduleExtensions)
        ui.extDriverLineEdit.setText(QtGui.QApplication.translate("videoFrame", extDr, None, QtGui.QApplication.UnicodeUTF8))

        #Não tem compatibilidade ainda
        ui.compatGroupBox.setVisible(True)
        ui.compatMsgLineEdit.setText(QtGui.QApplication.translate("videoFrame", compat_res[1], None, QtGui.QApplication.UnicodeUTF8))

        index = 4 #Posição relativa na tela para inserir as informações de particionamento
        #Para cada partição cria um QGroupBox e configura com o Ui_partGroupBox
#        for diag in diag_res:
        monitorGroupBox = QtGui.QGroupBox()
        ui.frameVerticalLayout.insertWidget(index, monitorGroupBox)
        uiMonitor = Ui_monitorFrame()
        uiMonitor.setupUi(monitorGroupBox)
        self.__fill_monitor(uiMonitor, monitorGroupBox, diag_res)


    def __fill_monitor (self, uiMonitor, monitorGroupBox, monitor_res):
        """Preenche as informações do monitor passada como parâmetro

        Parâmetros:
        uiPart -- 'Ui_partGroupBox' que define o groupBox para exibir as informações do monitor
        partGroupBox -- um QGroupBox que irá ser inserido na tela
        monitor_res -- um 'DiagResVideo' com as informações do monitor
        """
        uiMonitor.vendorLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.vendor[1]), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.modelLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.model[1]), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.currentResLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.currentResolution), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.maxResLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.maximumResolution), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.sizeScreenLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.screenSize), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.vSyncLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.vsyncRange), None, QtGui.QApplication.UnicodeUTF8))
        uiMonitor.hSyncLineEdit.setText(QtGui.QApplication.translate("monitorFrame", self._check_invalid_values(monitor_res.hsyncRange), None, QtGui.QApplication.UnicodeUTF8))




