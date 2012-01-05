# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.dvdcd.frame_dvdcd import Ui_FrameDVDCD

class GUIDVDCD(LDC_Info):
	"""Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de CD/DVD.
    """

	name = u"CD/DVD"
	category = "Armazenamento"
	status = None

	ui = Ui_FrameDVDCD()

	def __init__(self, info_res, compat_res, diag_res):
		"""Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResDVDCD')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResDVDCD')
        """

		LDC_Info.__init__(self)
		self.setTitle(self.name)

		self.status = compat_res[0]

		self.ui.setupUi(self.frame)
		self.__fill_frame(info_res, compat_res, diag_res)

	def __fill_frame(self, info_res, compat_res, diag_res):
		"""Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico."""
		
		self.ui.modelLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", info_res.model, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.vendorLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", info_res.vendor, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", info_res.deviceFile, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.driversLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", ", ".join(info_res.drivers), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.burnPushButton.hide()

		self.__fill_medias(info_res, compat_res, diag_res)
		self.__fill_burn(info_res, compat_res, diag_res)
		self.__fill_compat(info_res, compat_res, diag_res)

	def __fill_medias(self, info_res, compat_res, diag_res):
		"""Preenche as informações das midias suportadas.
		
		Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResDVDCD')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResDVDCD')
		"""
		        
		medias = "Não informado"

		if (info_res.medias):
			medias = ", ".join(info_res.medias)

		self.ui.mediasLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", medias, None, QtGui.QApplication.UnicodeUTF8))

	def __fill_burn(self, info_res, compat_res, diag_res):
		"""Preenche as informações do status do teste de gravacao.
		
		Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResDVDCD')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResDVDCD')
		"""
		
		burnTest = None
		burnDetails = None

		if (diag_res.burnerType == None):
			burnTest = "Não realizado."
			burnDetails = "O teste não foi realizado pois esse dispositivo não é um gravador."
		elif (diag_res.testedMediaType == None):
			burnTest = "Não realizado."
			burnDetails = "O teste foi cancelado pelo usuário."
		elif (not diag_res.burnSuccess):
			burnTest = "Falha na gravação."
			burnDetails = "Houve um erro ao tentar gravar um arquivo na mídia. Isso pode indicar uma falha de hardware ou um defeito na mídia. Em caso de falha de hardware, o drive de CD/DVD deve ser substituído."
		elif (not diag_res.readSuccess):
			burnTest = "Falha na leitura."
			burnDetails = "Houve um erro ao ler o arquivo que foi gravado. Isso pode indicar uma falha de hardware, um erro na gravação ou um defeito na mídia. Caso suspeite de mídia defeituosa, o teste pode ser executado novamente, com outra mídia, para verificar essa possibilidade. A falha de gravação não decorrente de mídia defeituosa pode indicar um problema no hardware, sendo necessária sua substituição"
		elif (diag_res.burnSuccess and diag_res.readSuccess):
			burnTest = "Teste realizado com sucesso."

			rewritable = "R"

			if (diag_res.testedMediaType['Rewritable']):
				rewritable = "RW"

			burnDetails = "A gravação e leitura foram executadas e verificadas com sucesso, utilizando uma mídia do tipo %s-%s" % (diag_res.testedMediaType['Type'], rewritable)


		self.ui.burnLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", burnTest, None, QtGui.QApplication.UnicodeUTF8))

	def __fill_compat(self, info_res, compat_res, diag_res):
		"""Atualiza a mensagem de compatibilidade e diagnóstico a partir dos seus resultados."""
		compatMsg = None
		if (compat_res[0]):
			compatMsg = "Seu dispositivo é compatível com o Librix."
		else:
			compatMsg = "Não foi possível identificar corretamente todas as funcionalidades do seu dispositivo."

		self.ui.compatLineEdit.setText(QtGui.QApplication.translate("FrameDVDCD", compatMsg, None, QtGui.QApplication.UnicodeUTF8))