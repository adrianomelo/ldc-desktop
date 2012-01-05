# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from libs.keyboard.frame_keyboard_compat import Ui_WizardCompatKeyboard

from libs.keyboard.info_res_keyboard import InfoResKeyboard
from libs.keyboard.diag_res_keyboard import DiagResKeyboard

class CompatKeyboardGUI(QtGui.QWizard, Ui_WizardCompatKeyboard):
	"""Classe que define a Qwizard que realiza o teste de compatibilidade de teclado. Que exibe uma tela para o usuário digitar uma mensagem."""
	
	__info = None

	def __init__(self, parent, pangram):
		"""Construtor que inicializa a QWizard, chamando o construtor da classe pai. 
		Inicializa a variável __pangram com a mensagem de panagrama recebida como parâmetro
		Também conecta o sinal de mudança de tela com o método wizCore para fazer o tratamento adequado.
		E chama o método __adjusts para fazer os ajustes na tela."""
		QtGui.QWizard.__init__(self, parent)
		Ui_WizardCompatKeyboard.__init__(self)
		self.setupUi(self)
		self.setPixmap(3, QtGui.QPixmap(":/ldc_wizard_bckg/ldc_wizard_bckg.png"))

		self.__pangram = pangram

		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.__adjusts()

	def __adjusts(self):
		"""Faz os ajustes iniciais na tela."""
		self.panagramLabel.setText(QtGui.QApplication.translate("WizardCompatKeyboard", self.__pangram, None, QtGui.QApplication.UnicodeUTF8))

		self.backButton = self.button(QtGui.QWizard.BackButton);
		self.nextButton = self.button(QtGui.QWizard.NextButton);
		self.cancelButton = self.button(QtGui.QWizard.CancelButton);
		self.finishButton = self.button(QtGui.QWizard.FinishButton);

	def wizCore(self, newId):
		"""Método que irá ser chamado quando ocorrer o sinal currentIdChanged(int), que indica que a tela do wizard foi mofificada.
		Serão feitos os ajustes necessários."""
		self.backButton.setText(u"Voltar")
		self.nextButton.setText(u"Avançar")
		self.cancelButton.setText(u"Cancelar")
		self.finishButton.setText(u"Concluir")

		self.backButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.nextButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.cancelButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.finishButton.setStyleSheet("background-color: rgb(235, 235, 250);")

	def getResult(self):
		return {'typed': self.typeLineEdit.text()}

	result = property(getResult, None, None, None)

import ldc_resources_rc