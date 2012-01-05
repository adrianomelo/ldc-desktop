# -*- coding: utf-8 -*-

import sys, os, time, threading
from PyQt4 import QtCore, QtGui

from libs.core.commands_utils import prepare_command, exec_command_parms, exec_command,  ApplicationExecutor

from libs.webcam.frame_webcam_wizard import Ui_Wizard

from libs.webcam.info_res_webcam import InfoResWebcam
from libs.webcam.diag_res_webcam import DiagResWebcam

class WebcamWizard(QtGui.QWizard, Ui_Wizard):
	"""Classe que define a Qwizard que realiza o teste de compatibilidade do dispositivo."""

	START = 0
	PLAY = 1
	YESORNO = 2
	END = 3

	SUCCESS = 0
	FAIL = 1
	INTERRUPTED = 2
	RESULT = -1

	def __init__(self, parent, info):
		"""Construtor que inicializa a QWizard, chamando o construtor da classe pai.
		Conecta os sinais necessarios e chama __adjusts() para fazer os ajustes na tela."""
		QtGui.QWizard.__init__(self, parent)
		Ui_Wizard.__init__(self)
		self.setupUi(self)

		self.__halUDI = info.halUDI

		self.__adjusts()
		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.connect(self.playButton, QtCore.SIGNAL("clicked()"), self.playOnThread)
		self.connect(self.yesButton, QtCore.SIGNAL("clicked()"), self.yesClicked)
		self.connect(self.noButton, QtCore.SIGNAL("clicked()"), self.noClicked)
		self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.setInterrupted)


	def __adjusts(self):
		"""Faz os ajustes iniciais na tela."""
		for id in self.pageIds():
			self.removePage(id)

		self.setPage(self.START, self.start)
		self.setPage(self.PLAY, self.webcamplay)
		self.setPage(self.YESORNO, self.yesorno)
		self.setPage(self.END, self.success)

		self.backButton = self.button(QtGui.QWizard.BackButton);
		self.nextButton = self.button(QtGui.QWizard.NextButton);
		self.cancelButton = self.button(QtGui.QWizard.CancelButton);
		self.finishButton = self.button(QtGui.QWizard.FinishButton);


	def wizCore(self, newId):
		"""Metodo que ira ser chamado quando ocorrer o sinal currentIdChanged(int), que indica que a tela do wizard foi mofificada.
		Serao feitos os ajustes necessarios."""
#		print "DEBUG: Current: %s" % newId
		self.backButton.setText(u"Voltar")
		self.nextButton.setText(u"Avançar")
		self.cancelButton.setText(u"Cancelar")
		self.finishButton.setText(u"Concluir")

		self.backButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.nextButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.cancelButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.finishButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.playButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.yesButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.noButton.setStyleSheet("background-color: rgb(235, 235, 250);")

		if (newId == self.START):
			self.cancelButton.show()
			self.nextButton.show()
			self.backButton.hide()
			pass
		elif (newId == self.PLAY):
			self.cancelButton.show()
			self.nextButton.setEnabled(False)
			self.backButton.show()
			pass
		elif (newId == self.YESORNO):
			self.cancelButton.show()
			self.nextButton.setEnabled(False)
			self.backButton.show()
			pass
		elif (newId == self.END):
			self.cancelButton.hide()
			self.setResult(self.RESULT)
			pass
		else:
			pass

	def yesClicked(self):
		"""Configura as mensagens em caso de sucesso e prossegue com o teste."""
		msg = "Webcam compatível com o Librix Desktop. \n\nClique no botão <b>Concluir</b>."
		self.successLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
		self.successLabel.setTextFormat(QtCore.Qt.RichText)
		self.RESULT = self.SUCCESS
		self.next()
		pass

	def noClicked(self):
		"""Configura as mensagens em caso de falha e prossegue com o teste."""
		msg = "Falha no teste de webcam. \n\nSua webcam não está corretamente configurada ou é incompatível com o Librix."
		self.successLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
		self.RESULT = self.FAIL
		self.next()
		pass

	def setInterrupted(self):
		"""Configura as mensagens em caso de interrupção do teste."""
		self.RESULT = self.INTERRUPTED

	def playOnThread(self):
		"""Função que delega a execução da função play() a uma nova thread."""
		self.nextButton.setEnabled(False)
		self.playButton.setEnabled(False)
		self.playButton.update()

		a = threading.Thread(target=self.play)
		a.start()
		a.join()

		self.nextButton.setEnabled(True)
		self.playButton.setEnabled(True)
		self.next()

	def play(self):
		"""Função que executa o programa usado para aceitação do teste de compatibilidade."""

		application = "cheese -d %s" % self.__halUDI

		i, o_str, e_str = os.popen3(application)

		time.sleep(10)

		os.system('killall cheese')