# -*- coding: utf-8 -*-

import sys, time, threading
from PyQt4 import QtCore, QtGui

from libs.mouse.frame_mouse_diag import Ui_WizardDiagMouse

from libs.mouse.info_res_mouse import InfoResMouse
from libs.mouse.diag_res_mouse import DiagResMouse

class DiagMouseGUI(QtGui.QWizard, Ui_WizardDiagMouse):
	"""Classe que define a Qwizard que realiza o teste de diagnóstico de Mouse. Que exibe uma tela para o usuário realizar um evento de mouse
	para indicar que este está plugado."""
	__info = None

	__actionDetected = False

	__maxCount = 10

	def __init__(self, parent):
		"""
		Construtor que inicializa a QWizard, chamando o construtor da classe pai. Cria uma instância
		de MouseEvenFilter, e da Thread para ficar atualizando a mensagem de contagem regressiva.
		Também conecta o sinal de mudança de tela com o método wizCore para fazer o tratamento adequado."""
		QtGui.QWizard.__init__(self, parent)
		Ui_WizardDiagMouse.__init__(self)
		self.setupUi(self)

		self.__myEventFilter = MouseEventFilter()

		self.countdownThread = threading.Thread(target = self.updateCountdown, name = "Countdown Thread")
		self.countdownThread.start()

		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.__adjusts()

	def __adjusts(self):
		"""Faz os ajustes iniciais na tela. Conecta todos os eventos de mouse com o método self.mousePlugged. 
		Conecta a sinal "countdownTimeOut!" com o método self.timeout.
		Incializa as variáveis correspondentes aos botões."""
		listeners = [self]
		listeners = listeners + self.children()

		for elem in listeners:
			elem.setMouseTracking(True)
			elem.installEventFilter(self.__myEventFilter)

		self.connect(self.__myEventFilter, QtCore.SIGNAL("mouseDoubleClicked(QMouseEvent)"), self.mousePlugged)
		self.connect(self.__myEventFilter, QtCore.SIGNAL("mouseMoved(QMouseEvent)"), self.mousePlugged)
		self.connect(self.__myEventFilter, QtCore.SIGNAL("mousePressed(QMouseEvent)"), self.mousePlugged)
		self.connect(self.__myEventFilter, QtCore.SIGNAL("mouseReleased(QMouseEvent)"), self.mousePlugged)
		self.connect(self.__myEventFilter, QtCore.SIGNAL("mouseWheel(QWheelEvent)"), self.mousePlugged)
		
		self.connect(self, QtCore.SIGNAL("countdownTimeOut!"), self.timeout)

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
		return {'actionDetected': self.__actionDetected}

	result = property(getResult, None, None, None)

	def updateCountdown(self):
		"""Método que fica atualizando o label de contagem regressiva. Ao terminar emite o sinal "countdownTimeOut!" que irá chamar o método
		self.timeout."""
		while (self.__maxCount > -1):
			self.countdownLabel.setText(QtGui.QApplication.translate("WizardDiagMouse", "%d" % self.__maxCount, None, QtGui.QApplication.UnicodeUTF8))
			self.__maxCount = self.__maxCount - 1
			time.sleep(1)

		self.emit(QtCore.SIGNAL("countdownTimeOut!"))

	def timeout(self):
		"""Método chamado pelo sinal "countdownTimeOut!", que irá fazer os ajustes finais e atualizar o resultado da wizard indicando que não foi
		recebido nenhum evento de mouse."""
		self.releaseMouse()
		self.reject()

	def mousePlugged(self, event):
		"""Método chamado por qualquer evento de mouse. Será atualizada a variável indicando que o mouse está plugado."""
		self.__actionDetected = True
		self.accept()

class MouseEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de mouse."""
	
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""Método que irá emitir um sinal para cada evento de mouse. Esse sinal está conectado com o método mousePlugged de DiagMouseGUI"""
		if (event.type() == QtCore.QEvent.MouseMove):
			self.emit(QtCore.SIGNAL("mouseMoved(QMouseEvent)"), event)
		elif (event.type() == QtCore.QEvent.MouseButtonPress):
			self.emit(QtCore.SIGNAL("mousePressed(QMouseEvent)"), event)
		elif (event.type() == QtCore.QEvent.MouseButtonRelease):
			self.emit(QtCore.SIGNAL("mouseReleased(QMouseEvent)"), event)
		elif (event.type() == QtCore.QEvent.MouseButtonDblClick):
			self.emit(QtCore.SIGNAL("mouseDoubleClicked(QMouseEvent)"), event)
		elif (event.type() == QtCore.QEvent.Wheel):
			self.emit(QtCore.SIGNAL("mouseWheel(QWheelEvent)"), event)
		elif (event.type() == QtCore.QEvent.MouseTrackingChange):
			self.emit(QtCore.SIGNAL("mouseTrackingChanged(QMouseEvent)"), event)

		return False