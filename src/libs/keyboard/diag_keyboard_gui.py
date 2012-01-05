# -*- coding: utf-8 -*-

import sys, time, threading
from PyQt4 import QtCore, QtGui

from libs.keyboard.frame_keyboard_diag import Ui_WizardDiagKeyboard

from libs.keyboard.info_res_keyboard import InfoResKeyboard
from libs.keyboard.diag_res_keyboard import DiagResKeyboard

class DiagKeyboardGUI(QtGui.QWizard, Ui_WizardDiagKeyboard):
	"""Classe que define a Qwizard que realiza o teste de diagnóstico de teclado. Que exibe uma tela para o usuário pressionar uma tecla
	para indicar que o teclado está plugado."""
	__info = None

	__keyPressed = False

	__maxCount = 10

	def __init__(self, parent):
		"""
		Construtor que inicializa a QWizard, chamando o construtor da classe pai. Cria uma instância
		de KeyboardEventFilter, e da Thread para ficar atualizando a mensagem de contagem regressiva.
		Também conecta o sinal de mudança de tela com o método wizCore para fazer o tratamento adequado.
		E chama o método __adjusts para fazer os ajustes na tela."""
		
		QtGui.QWizard.__init__(self, parent)
		Ui_WizardDiagKeyboard.__init__(self)
		self.setupUi(self)

		self.__myEventFilter = KeyboardEventFilter()

		self.countdownThread = threading.Thread(target = self.updateCountdown, name = "Countdown Thread")
		self.countdownThread.start()

		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.__adjusts()

	def __adjusts(self):
		"""Faz os ajustes iniciais na tela. Conecta todos os eventos de teclado com o método keyboardPlugged. 
		Conecta a sinal "countdownTimeOut!" com o método self.timeout.
		Incializa as variáveis correspondentes aos botões."""
		listeners = [self]
		listeners = listeners + self.children()

		for elem in listeners:
			elem.installEventFilter(self.__myEventFilter)

		self.connect(self.__myEventFilter, QtCore.SIGNAL("keyPressed(QKeyEvent)"), self.keyboardPlugged)
		self.connect(self.__myEventFilter, QtCore.SIGNAL("keyReleased(QKeyEvent)"), self.keyboardPlugged)
		self.connect(self, QtCore.SIGNAL("countdownTimeOut!"), self.timeout)

		self.backButton = self.button(QtGui.QWizard.BackButton)
		self.nextButton = self.button(QtGui.QWizard.NextButton)
		self.cancelButton = self.button(QtGui.QWizard.CancelButton)
		self.finishButton = self.button(QtGui.QWizard.FinishButton)
		
		self.backButton.installEventFilter(self.__myEventFilter)
		self.nextButton.installEventFilter(self.__myEventFilter)
		self.cancelButton.installEventFilter(self.__myEventFilter)
		self.finishButton.installEventFilter(self.__myEventFilter)

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
		return {'keyPressed': self.__keyPressed}

	result = property(getResult, None, None, None)

	def updateCountdown(self):
		"""Método que fica atualizando o label de contagem regressiva. Ao terminar emite o sinal "countdownTimeOut!" que irá chamar o método
		self.timeout."""
		while (self.__maxCount > -1):
			self.countdownLabel.setText(QtGui.QApplication.translate("WizardDiagKeyboard", "%d" % self.__maxCount, None, QtGui.QApplication.UnicodeUTF8))
			self.__maxCount = self.__maxCount - 1
			time.sleep(1)

		self.emit(QtCore.SIGNAL("countdownTimeOut!"))

	def timeout(self):
		"""Método chamado pelo sinal "countdownTimeOut!", que irá atualizar o resultado da wizard indicando que não foi	recebido nenhum evento 
		de teclado."""
		self.reject()

	def keyboardPlugged(self, event):
		"""Método chamado por qualquer evento do teclado. Será atualizada a variável indicando que o teclado está plugado."""
		self.__keyPressed = True
		self.accept()

class KeyboardEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de teclado."""
	
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""M￩todo que irá emitir um sinal para cada evento de teclado. Esse sinal está conectado com o método keyboardPlugged de DiagKeyboardGUI"""
		if (event.type() == QtCore.QEvent.KeyPress):
			self.emit(QtCore.SIGNAL("keyPressed(QKeyEvent)"), event)
		elif (event.type() == QtCore.QEvent.KeyRelease):
			self.emit(QtCore.SIGNAL("keyReleased(QKeyEvent)"), event)

		return False