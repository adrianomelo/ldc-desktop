# -*- coding: utf-8 -*-

import sys, os, time, threading, subprocess
from PyQt4 import QtCore, QtGui

from libs.sound.frame_sound_wizard import Ui_Wizard

from libs.sound.info_res_sound import InfoResSound
from libs.sound.diag_res_sound import DiagResSound

class SoundWizard(QtGui.QWizard, Ui_Wizard):
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
		self.deviceID = info[1].deviceID

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
		self.setPage(self.PLAY, self.soundplay)
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
		msg = "Placa de som compatível com o Librix Desktop. \n\nClique no botão <b>Concluir</b>."
		self.successLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
		self.successLabel.setTextFormat(QtCore.Qt.RichText)
		self.RESULT = self.SUCCESS
		self.next()
		pass

	def noClicked(self):
		"""Configura as mensagens em caso de falha e prossegue com o teste."""
		msg = "Falha no teste de som. \n\nSua placa de som não está corretamente configurada ou é incompatível com o Librix."
		self.successLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
		self.RESULT = self.FAIL
		self.next()
		pass

	def setInterrupted(self):
		"""Configura as mensagens em caso de interrupção do teste."""
		self.RESULT = self.INTERRUPTED

	def playOnThread(self):
		"""Função que delega a execução da função play() a uma nova thread."""
		a = threading.Thread(target=self.play)
		a.start()
		a.join()
		self.next()

	def play(self):
		"""Função que executa o programa usado para aceitação do teste de compatibilidade."""
		self.playButton.setEnabled(False)
		self.nextButton.setEnabled(False)
		i, o_str, e_str = os.popen3('alsaplayer -i text -d hw:%i libs/sound/Bass.wav' % int(self.deviceID))
		time.sleep(4)
		os.system('alsaplayer --stop')
		os.system('alsaplayer --quit')
		self.playButton.setEnabled(True)
		self.nextButton.setEnabled(True)



if __name__ == "__main__":
	from PyQt4 import QtCore, QtGui
	import sys

	app = QtGui.QApplication(sys.argv)

	gui = SoundWizard("/dev/audio")

	sys.exit(app.exec_())