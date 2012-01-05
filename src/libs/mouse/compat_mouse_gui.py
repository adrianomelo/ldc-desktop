# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from libs.mouse.frame_mouse_compat import Ui_WizardCompatMouse

from libs.mouse.info_res_mouse import InfoResMouse
from libs.mouse.diag_res_mouse import DiagResMouse

class CompatMouseGUI(QtGui.QWizard, Ui_WizardCompatMouse):
	"""Classe que define a Qwizard que realiza o teste de compatibilidade de mouse. Que exibe uma tela para o usuário clicar na tela usando 
	todos os botões e roldanas."""
	
	__info = None

	__numberOfButtons = None #indica quantos boões o mouse possui
	__hasWheel = False #indica se o mouse possui roldana

	__leftClick = False #indica se foi clicado com o botão esquerdo
	__rightClick = False #indica se foi clicado com o botão direito
	__middleClick = False #indica se foi clicado com o botão do meio
	__wheelMove = False #indica se foi utilizda a roldana

	def __init__(self, parent, mouseModel, numberOfButtons, hasWheel):
		"""Construtor que inicializa a QWizard, chamando o construtor da classe pai. 
		Inicializa os atributos que irão indicar o modelo do mouse, o número de botões e se possui roldana com os valores recebidos.
		Também conecta o sinal de mudança de tela com o método wizCore para fazer o tratamento adequado.
		E chama o método __adjusts para fazer os ajustes na tela."""
		QtGui.QWizard.__init__(self, parent)
		Ui_WizardCompatMouse.__init__(self)
		self.setupUi(self)

		self.__mouseModel = mouseModel
		self.__numberOfButtons = numberOfButtons
		self.__hasWheel = hasWheel

		self.__leftFilter = MouseLeftEventFilter()
		self.__rightFilter = MouseRightEventFilter()
		self.__middleFilter = MouseMiddleEventFilter()
		self.__wheelFilter = MouseWheelEventFilter()

		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.__adjusts(mouseModel, numberOfButtons, hasWheel)

	def __adjusts(self, mouseModel, numberOfButtons, hasWheel):
		"""Faz os ajustes iniciais na tela."""
		
		# Instalando filtros para tratar eventos desejados e ignorar outros
		self.scrollVerticalSlider.installEventFilter(self.__wheelFilter)
		self.leftPushButton.installEventFilter(self.__leftFilter)
		self.rightPushButton.installEventFilter(self.__rightFilter)
		self.middlePushButton.installEventFilter(self.__middleFilter)

		# Ocultando botoes desnecessarios
		if (not hasWheel):
			self.scrollVerticalSlider.setVisible(False)

		if (numberOfButtons < 3):
			self.middlePushButton.setVisible(False)

		if (numberOfButtons < 2):
			self.rightPushButton.setVisible(False)

		# Conectando sinais
		self.connect(self.__wheelFilter, QtCore.SIGNAL("mouseWheel!"), self.moveWheel)
		self.connect(self.__leftFilter, QtCore.SIGNAL("mouseLeft!"), self.clickLeft)
		self.connect(self.__rightFilter, QtCore.SIGNAL("mouseRight!"), self.clickRight)
		self.connect(self.__middleFilter, QtCore.SIGNAL("mouseMiddle!"), self.clickMiddle)

		# Definindo texto descritivo
		msgDescription = "Testando mouse \"%s\".<br><br>Clique com os botões indicados para testar o funcionamento do mouse." % mouseModel[1]

		if (hasWheel):
			msgDescription = msgDescription + " Utilize ainda o botão de rolagem para mover a barra vertical."

		msgDescription = msgDescription + " Para finalizar, clique no botão <b>Concluir</b>."

		self.descriptionLabel.setText(QtGui.QApplication.translate("WizardCompatMouse", msgDescription, None, QtGui.QApplication.UnicodeUTF8))

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

		self.leftPushButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.rightPushButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.middlePushButton.setStyleSheet("background-color: rgb(235, 235, 250);")


	def getResult(self):
		return {'leftClick': self.__leftClick, 'rightClick': self.__rightClick, 'middleClick': self.__middleClick, 'wheelMove': self.__wheelMove}

	#indica o resultado do teste de compatibilidade de mouse
	result = property(getResult, None, None, None)

	def moveWheel(self):
		"""Chamado quando foi detectado que houve movimento da roldana."""
		self.__wheelMove = True

	def clickLeft(self):
		"""Chamado quando foi detectado que o botão esquedo foi clicado."""
		self.__leftClick = True
		self.leftPushButton.setEnabled(False)

	def clickRight(self):
		"""Chamado quando foi detectado que o botão direito foi clicado."""
		self.__rightClick = True
		self.rightPushButton.setEnabled(False)

	def clickMiddle(self):
		"""Chamado quando foi detectado que o botão do meio foi clicado."""
		self.__middleClick = True
		self.middlePushButton.setEnabled(False)

class MouseWheelEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de movimento da roldana do mouse."""
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""Método que irá emitir um sinal para o evento de roldana. Esse sinal está conectado com o método moveWheel de CompatMouseGUI"""
		ret = False

		if (event.type() == QtCore.QEvent.Wheel):
			self.emit(QtCore.SIGNAL("mouseWheel!"))
			ret = False
		elif (event.type() == QtCore.QEvent.MouseButtonRelease or \
				event.type() == QtCore.QEvent.MouseButtonPress or \
				event.type() == QtCore.QEvent.MouseButtonDblClick or \
				event.type() == QtCore.QEvent.MouseMove):
			ret = True

		return ret

class MouseLeftEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de clique do botão esquerdo do mouse."""
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""Método que irá emitir um sinal para o de clique do botão esquerdo. Esse sinal está conectado com o método clickLeft de CompatMouseGUI"""
		ret = False

		if (event.type() == QtCore.QEvent.MouseButtonRelease or \
				event.type() == QtCore.QEvent.MouseButtonPress or \
				event.type() == QtCore.QEvent.MouseButtonDblClick):
			if (event.button() == QtCore.Qt.LeftButton):
				self.emit(QtCore.SIGNAL("mouseLeft!"))
				ret = False
			else:
				ret = True

		return ret

class MouseRightEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de clique do botão esquerdo do mouse."""
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""Método que irá emitir um sinal para o clique do botão direito. Esse sinal está conectado com o método clickMiddle de CompatMouseGUI"""
		ret = False

		if (event.type() == QtCore.QEvent.MouseButtonRelease or \
				event.type() == QtCore.QEvent.MouseButtonPress or \
				event.type() == QtCore.QEvent.MouseButtonDblClick):
			if (event.button() == QtCore.Qt.RightButton):
				self.emit(QtCore.SIGNAL("mouseRight!"))
				ret = False
			else:
				ret = True

		return ret

class MouseMiddleEventFilter(QtCore.QObject):
	"""Classe que irá filtrar os eventos de clique do botão esquerdo do mouse."""
	def __init__(self):
		QtCore.QObject.__init__(self)

	def eventFilter(self, object, event):
		"""Método que irá emitir um sinal para o clique do botão do meio. Esse sinal está conectado com o método clickRight de CompatMouseGUI"""
		ret = False

		if (event.type() == QtCore.QEvent.MouseButtonRelease or \
				event.type() == QtCore.QEvent.MouseButtonPress or \
				event.type() == QtCore.QEvent.MouseButtonDblClick):
			if (event.button() == QtCore.Qt.MidButton):
				self.emit(QtCore.SIGNAL("mouseMiddle!"))
				ret = False
			else:
				ret = True

		return ret