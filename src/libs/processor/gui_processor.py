# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.processor.frame_processor import Ui_processorFrame
from libs.processor.frame_processor_cache import Ui_cacheGroupBox

class GUIProcessor (LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de processador.
    """

    name = "Processador" #Atributo que define o nome do dispositivo
    category = "Sistema" #Atributo que define a categoria do dispositivo
    status = None        #Atributo que define o status atual do teste (True/False)

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResProcessor')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DiagResProcessor')
        """

        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_processorFrame() #UI que define os campos da GUI do HD
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)

    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """

        model = self._check_invalid_values(info_res.model)
        vendor = self._check_invalid_values(info_res.vendor)
        clock = self._check_invalid_values(str(info_res.clock) + " MHz")
        socketType = self._check_invalid_values(info_res.socketType)
        nCores = self._check_invalid_values(str(info_res.numberOfCores))
        voltage = self._check_invalid_values(info_res.voltage)
        fsb = self._check_invalid_values(str(info_res.fsb) + " MHz")
        features = self._check_invalid_list(info_res.features)


        ui.modelLineEdit.setText(QtGui.QApplication.translate("processorFrame", model, None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("processorFrame", vendor, None, QtGui.QApplication.UnicodeUTF8))
        ui.clockLineEdit.setText(QtGui.QApplication.translate("processorFrame", clock, None, QtGui.QApplication.UnicodeUTF8))
        ui.typeSocketLineEdit.setText(QtGui.QApplication.translate("processorFrame", socketType, None, QtGui.QApplication.UnicodeUTF8))
        ui.nCoresLineEdit.setText(QtGui.QApplication.translate("processorFrame", nCores, None, QtGui.QApplication.UnicodeUTF8))
        ui.voltageLineEdit.setText(QtGui.QApplication.translate("processorFrame", voltage, None, QtGui.QApplication.UnicodeUTF8))
        ui.fsbLineEdit.setText(QtGui.QApplication.translate("processorFrame", fsb, None, QtGui.QApplication.UnicodeUTF8))
        ui.featuresTextEdit.setText(QtGui.QApplication.translate("processorFrame", features, None, QtGui.QApplication.UnicodeUTF8))
        index = 5 #Posição relativa na tela depois de features

        #Para cada cache cria um QGroupBox e configura com o Ui_cacheGroupBox
        for cache in info_res.caches_list:
            cacheGroupBox = QtGui.QGroupBox()
            ui.frameVerticalLayout.insertWidget(index, cacheGroupBox)
            uiCache = Ui_cacheGroupBox()
            uiCache.setupUi(cacheGroupBox)
            self.__fill_cache(uiCache, cacheGroupBox, cache)
            index = index + 1

        if compat_res[0]: #Dependendo do resultado de compatibilidade mostra as informações de diagnóstico
            ui.diagLabel.setVisible(False)
            ui.diagMsgLineEdit.setVisible(False)
        else:
            ui.compatMsgLineEdit.setText(QtGui.QApplication.translate("processorFrame", "O processador não foi identificado corretamente.", None, QtGui.QApplication.UnicodeUTF8))
            ui.diagMsgLineEdit.setText(QtGui.QApplication.translate("processorFrame", diag_res.model, None, QtGui.QApplication.UnicodeUTF8))


    def __fill_cache (self, uiCache, cacheGroupBox, cache):
        """Preenche as informações da cache

        Parâmetros:
        uiCache -- 'Ui_cacheGroupBox' que define o groupBox para exibir as informações de cache
        cacheGroupBox -- um QGroupBox que irá ser inserido na tela
        cache -- um 'InfoResProcessorCache' com as informações das caches
        """

        name = self._check_invalid_values(cache.name)
        associativity = self._check_invalid_values(cache.associativity)
        size = self._check_invalid_values(str(cache.size)+ " KB")
        operationMode = self._check_invalid_values(cache.operationMode)
        errorCorrectionType = self._check_invalid_values(cache.errorCorrectionType)
        associativity = self._check_invalid_values(cache.associativity)
        supportedSRAMTypes = self._check_invalid_list(cache.supportedSRAMTypes)


        cacheGroupBox.setTitle(QtGui.QApplication.translate("cacheGroupBox", name, None, QtGui.QApplication.UnicodeUTF8))
        uiCache.associativityLineEdit.setText(QtGui.QApplication.translate("cacheGroupBox", associativity, None, QtGui.QApplication.UnicodeUTF8))
        uiCache.sizeLineEdit.setText(QtGui.QApplication.translate("cacheGroupBox", size, None, QtGui.QApplication.UnicodeUTF8))
        uiCache.operationModeLineEdit.setText(QtGui.QApplication.translate("cacheGroupBox", operationMode, None, QtGui.QApplication.UnicodeUTF8))
        supportedSRAMTypes_str = ', '.join(cache.supportedSRAMTypes)
        uiCache.sramTypesLineEdit.setText(QtGui.QApplication.translate("cacheGroupBox", supportedSRAMTypes_str, None, QtGui.QApplication.UnicodeUTF8))
        uiCache.errorCorrectionLineEdit.setText(QtGui.QApplication.translate("cacheGroupBox", errorCorrectionType, None, QtGui.QApplication.UnicodeUTF8))