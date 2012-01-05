# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.memory.frame_memory import Ui_FrameMemory
from libs.memory.gui_memory_module import GUIMemoryModule

from libs.memory.info_res_memory import InfoResMemory
from libs.memory.info_res_memory import InfoResMemoryController
from libs.memory.info_res_memory import InfoResMemoryModule

class GUIMemory(LDC_Info, Ui_FrameMemory):
	"""Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de memória.
    """
	name = u"Memória"
	category = "Sistema"
	status = None
	ui = Ui_FrameMemory()

	def __init__(self, info_res, compat_res, diag_res):
		"""Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResMemory')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResMemory')
        """
		LDC_Info.__init__(self)

		self.ui.setupUi(self.frame)

		self.setTitle(self.name)
		self.status = compat_res[0]

		self.__fill_frame(info_res, compat_res, diag_res)

	def __fill_frame(self, info_res, compat_res, diag_res):
		"""Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico."""

		controller = info_res.memoryController

		if (controller):
			maxMemoryModuleSize = self._check_invalid_values(controller.maxMemoryModuleSize)
			memoryModuleVoltage = self._check_invalid_values(controller.memoryModuleVoltage)
			maxTotalMemorySize = self._check_invalid_values(controller.maxTotalMemorySize)
			supportedSpeeds = self._check_invalid_list(controller.supportedSpeeds)
			supportedTypes = self._check_invalid_list(controller.supportedTypes)

			self.ui.maxModSizeLineEdit.setText(QtGui.QApplication.translate("FrameMemory", "%d MB" % maxMemoryModuleSize, None, QtGui.QApplication.UnicodeUTF8))
			self.ui.voltageLineEdit.setText(QtGui.QApplication.translate("FrameMemory", memoryModuleVoltage, None, QtGui.QApplication.UnicodeUTF8))
			self.ui.maxTotalMemLineEdit.setText(QtGui.QApplication.translate("FrameMemory", "%d MB" % maxTotalMemorySize, None, QtGui.QApplication.UnicodeUTF8))
			self.ui.supSpeedsLineEdit.setText(QtGui.QApplication.translate("FrameMemory", supportedSpeeds, None, QtGui.QApplication.UnicodeUTF8))
			self.ui.supTypesLineEdit.setText(QtGui.QApplication.translate("FrameMemory", supportedTypes, None, QtGui.QApplication.UnicodeUTF8))

		else:
			self.ui.controllerGroupBox.hide()

		self.__fillModules(info_res, compat_res, diag_res)

		compatMsg = None
		if (compat_res[0]):
			compatMsg = "Memória compatível com o Librix"
		else:
			self.ui.compatTextEdit.setMaximumSize(QtCore.QSize(16777215, 90))
			compatMsg = "Foi detectado um erro de acesso à memória."

			if (not diag_res.status):
				compatMsg = "%s A memória total informada pelo Librix é diferente da que foi informada pela BIOS:\n\tLibrix: %s MB\n\tBIOS: %s MB" % (compatMsg, diag_res.procMemInfoSize / 1024, diag_res.dmiDecodeSize / 1024)

		self.ui.compatTextEdit.setPlainText(QtGui.QApplication.translate("FrameMemory", compatMsg, None, QtGui.QApplication.UnicodeUTF8))

	def __fillModules(self, info_res, compat_res, diag_res):
		"""Cria um 'GUIMemoryModule' com as informações de cada módulo de memória e insere na GUI. """

		count = 0

		for module in info_res.memoryModules:
			vendor = self._check_invalid_values(module.vendor)
			formFactor = self._check_invalid_values(module.formFactor)
			type = self._check_invalid_values(module.type)
			size = self._check_invalid_values(module.size)
			speed = self._check_invalid_values(module.speed)
			serial = self._check_invalid_values(module.serial)
			partNumber = self._check_invalid_values(module.partNumber)

			moduleGUI = GUIMemoryModule(self, vendor, formFactor, type, size, speed, serial, partNumber)

			self.ui.modulesGridLayout.addWidget(moduleGUI, count / 2, count % 2)

			count = count + 1
