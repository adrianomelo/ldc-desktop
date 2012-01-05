# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from libs.memory.frame_memory_module import Ui_FrameMemoryModule

class GUIMemoryModule(QtGui.QGroupBox, Ui_FrameMemoryModule):
	"""Classe que define um GroupBox para a exibição das informações dos módulos de memória."""

	def __init__(self, parent, vendor, formFactor, type, size, speed, serial, partNumber):
		"""Construtor que recebe como parâmetro as informações do módulo de memória"""
		QtGui.QGroupBox.__init__(self, parent)
		Ui_FrameMemoryModule.__init__(self)

		self.setupUi(self)

		vendor = self.__check_invalid_values(vendor)
		formFactor = self.__check_invalid_values(formFactor)
		type = self.__check_invalid_values(type)
		size = self.__check_invalid_values(size)
		speed = self.__check_invalid_values(speed)
		serial = self.__check_invalid_values(serial)
		partNumber = self.__check_invalid_values(partNumber)

		self.vendorLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", vendor, None, QtGui.QApplication.UnicodeUTF8))
		self.formFactorLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", formFactor, None, QtGui.QApplication.UnicodeUTF8))
		self.typeLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", type, None, QtGui.QApplication.UnicodeUTF8))
		self.sizeLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", "%s MB" % size, None, QtGui.QApplication.UnicodeUTF8))
		self.speedLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", speed, None, QtGui.QApplication.UnicodeUTF8))
		self.serialLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", serial, None, QtGui.QApplication.UnicodeUTF8))
		self.partLineEdit.setText(QtGui.QApplication.translate("FrameMemoryModule", partNumber, None, QtGui.QApplication.UnicodeUTF8))

	def __check_invalid_values(self, value):
		"""Verifica os valores e caso sejam inválidos substitui por pela string vazia"""
		ret = ""

		if (value):
			if (value != "Other" and value != "NULL" and value != "Unknown" and value != "None"):
				ret = value

		return ret

	def __check_invalid_list(self, list):
		"""Verifica os valores da lista e caso sejam inválidos serão removidos.
		Retorna um string com os valores da lista separados por virgula."""
		ret = ""

		if (list):
			ret = []

			for i in list:
				item = self.__check_invalid_values(i)

				if (item):
					ret.append(item)

			if (not ret):
				ret = ""

		return ", ".join(ret)