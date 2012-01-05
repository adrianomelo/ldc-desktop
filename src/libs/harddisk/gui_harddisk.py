# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.harddisk.frame_harddisk import Ui_HarddiskFrame
from libs.harddisk.frame_harddisk_module import Ui_FrameHarddiskModule
from libs.harddisk.gui_harddisk_module import GUIHarddiskModule

class GUIHarddisk(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de HD.
    """
    
    name = u"Disco Rígido"       #Atributo que define o nome do dispositivo
    category = "Armazenamento"   #Atributo que define a categoria do dispositivo
    status = None                #Atributo que define o status atual do teste (True/False)

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor
        
        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResHarddisks')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResHarddisk')
        """
        
        LDC_Info.__init__(self)
        self.setTitle(self.name)

        self.status = compat_res[0]

        ui = Ui_HarddiskFrame() #UI que define os campos da GUI do HD
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)

    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        
        family = self._check_invalid_values(info_res.modelFamily)
        model = self._check_invalid_values(info_res.model)
        vendor = self._check_invalid_values(info_res.vendor)
        drivers = self._check_invalid_values(", ".join(info_res.drivers))
        bus = self._check_invalid_values(info_res.bus)
        device = self._check_invalid_values(info_res.deviceFile)
        size = self._check_invalid_values(((info_res.size * 1024 * 1024) / 1000000000).__str__() + " GB")
        temperature = self._check_invalid_values(diag_res.temperature.__str__() + "° C")
        
        overall = "Erro"
        if diag_res.overallHealthTest:
            overallHealth = "OK"
                
        ui.familyLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", family, None, QtGui.QApplication.UnicodeUTF8))
        ui.modelLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", model, None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", vendor, None, QtGui.QApplication.UnicodeUTF8))
        ui.driversLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", drivers, None, QtGui.QApplication.UnicodeUTF8))
        ui.busLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", bus, None, QtGui.QApplication.UnicodeUTF8))
        ui.deviceLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", device, None, QtGui.QApplication.UnicodeUTF8))
        ui.sizeLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", size, None, QtGui.QApplication.UnicodeUTF8))
        ui.smartLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", overallHealth, None, QtGui.QApplication.UnicodeUTF8))
        ui.temperatureLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", temperature, None, QtGui.QApplication.UnicodeUTF8))

        self.__fillPartitions(ui, info_res, compat_res, diag_res) #Preenche as informações das partições

        compatMsg = None
        if (compat_res[0]):
            compatMsg = "HD compatível com o Librix."
        else:
            compatMsg = "HD incompatível com o Librix. Ele falhou no teste de badblocks. Consulte seu administrador de sistema."

        ui.compatLineEdit.setText(QtGui.QApplication.translate("HarddiskFrame", compatMsg, None, QtGui.QApplication.UnicodeUTF8))

    def __fillPartitions(self, ui, info_res, compat_res, diag_res):
        """Cria um 'GUIHarddiskModule' com as informações de cada partição e insere na GUI. """
        
        count = 0

        for partition in diag_res.partitions:
            partitionGUI = GUIHarddiskModule(self, partition.deviceFile, partition.filesystem, partition.mountingPoint, partition.size, partition.freeSize)

            ui.partitionsGridLayout.addWidget(partitionGUI, count / 2, count % 2)

            count = count + 1