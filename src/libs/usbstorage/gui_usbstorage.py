# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.usbstorage.frame_usbstorage import Ui_usbstorageFrame
from libs.usbstorage.frame_usbstorage_part import Ui_partGroupBox


class GUIUsbstorage (LDC_Info):
		"""Estende a classe 'LDC_Info'.
		Classe que define a interface gráfica com os resultados para o teste de armazenamento usb.
		"""

		name = "Armazenamento USB"
		category = "Armazenamento"
		status = None

		def __init__(self, info_res, compat_res, diag_res):
				"""Construtor

				Parâmetros:
				info_res -- lista com os resultados informativos (lista de 'InfoResUsbstorage')
				compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
				diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResUsbstorage')
				"""
				LDC_Info.__init__(self)
				self.setTitle(self.name)

				if info_res:
						self.status = compat_res[0] #compat result
						ui = Ui_usbstorageFrame()
						ui.setupUi(self.frame)
						self.__fill_frame(ui, info_res, compat_res, diag_res)
				else:
						self.__labelError(compat_res)


		def __fill_frame(self, ui, info_res, compat_res, diag_res):
				"""Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
				ui.modelLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", self._check_invalid_values(info_res.model.value), None, QtGui.QApplication.UnicodeUTF8))
				ui.vendorLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", self._check_invalid_values(info_res.vendor.value), None, QtGui.QApplication.UnicodeUTF8))
				ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", self._check_invalid_values(info_res.device_file), None, QtGui.QApplication.UnicodeUTF8))
				ui.driversLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", self._check_invalid_values(info_res.driver), None, QtGui.QApplication.UnicodeUTF8))
				if info_res.size > 0:
					ui.sizeLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", str(info_res.size) + ' GB', None, QtGui.QApplication.UnicodeUTF8))
				if info_res.speed > 0:
					ui.speedLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", str(info_res.speed) + ' Mbps', None, QtGui.QApplication.UnicodeUTF8))
				else:
					ui.speedLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", '', None, QtGui.QApplication.UnicodeUTF8))

				index = 3 #Posição relativa na tela para inserir as informações de particionamento
				#Para cada partição cria um QGroupBox e configura com o Ui_partGroupBox
				if info_res.partition_list:
					for part in info_res.partition_list:
							partGroupBox = QtGui.QGroupBox()
							ui.frameVerticalLayout.insertWidget(index, partGroupBox)
							uiPart = Ui_partGroupBox()
							uiPart.setupUi(partGroupBox)
							self.__fill_cache(uiPart, partGroupBox, part)
							index = index + 1

				#Dependendo do resultado de compatibilidade mostra as informações de diagnóstico
				if compat_res[0]:
						ui.diagMountLabel.setVisible(False)
						ui.diagMountLineEdit.setVisible(False)
						ui.diagPartLabel.setVisible(False)
						ui.diagPartLineEdit.setVisible(False)
						ui.diagFsckLabel.setVisible(False)
						ui.diagFsckLineEdit.setVisible(False)
				else:
						ui.compatMsgLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", u"Dispositivo de armazenamento incompatível com o Librix. " + compat_res[1], None, QtGui.QApplication.UnicodeUTF8))
						if not diag_res.part_check:
								ui.diagMountLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", "Particionamento não identificado corretamente.", None, QtGui.QApplication.UnicodeUTF8))
						if not diag_res.mount_test:
								ui.diagPartLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", "Problema na montagem do dispositivo.", None, QtGui.QApplication.UnicodeUTF8))
						if not diag_res.fsck_test:
								ui.diagFsckLineEdit.setText(QtGui.QApplication.translate("usbstorageFrame", "Falha na verificação de erro (fsck).", None, QtGui.QApplication.UnicodeUTF8))


		def __fill_cache (self, uiPart, partGroupBox, part):
				"""Preenche as informações da partição passada como parâmetro

				Parâmetros:
				uiPart -- 'Ui_partGroupBox' que define o groupBox para exibir as informações de cache
				partGroupBox -- um QGroupBox que irá ser inserido na tela
				part -- um 'InfoResUsbstoragePartition' com as informações das partições
				"""
				partGroupBox.setTitle(QtGui.QApplication.translate("partGroupBox", "Partição %s"%part.id, None, QtGui.QApplication.UnicodeUTF8))
				uiPart.deviceFileLineEdit.setText(QtGui.QApplication.translate("partGroupBox", part.device_file, None, QtGui.QApplication.UnicodeUTF8))
				uiPart.sizeLineEdit.setText(QtGui.QApplication.translate("partGroupBox", part.size, None, QtGui.QApplication.UnicodeUTF8))
				uiPart.fileSytemLineEdit.setText(QtGui.QApplication.translate("partGroupBox", part.filesystem, None, QtGui.QApplication.UnicodeUTF8))

		def __labelError(self, compat_res):
				"""Insere uma mensagem indicando que não foi encontrado nenhum dispositivo de armazenamento"""
				label = QtGui.QLabel(u"Não foi detectado nenhum dispositivo de armazenamento.")
				verticalLayout = QtGui.QVBoxLayout(self.frame)
				verticalLayout.addWidget(label)

