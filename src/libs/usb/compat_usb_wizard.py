# -*- coding: utf-8 -*-

import sys, os, time, threading
from PyQt4 import QtCore, QtGui

from libs.core.commands_utils import prepare_command, exec_command_parms, exec_command

from libs.usb.frame_usb_wizard import Ui_Wizard

from libs.usb.info_res_usb import InfoResUsb
from libs.usb.diag_res_usb import DiagResUsb

class UsbWizard(QtGui.QWizard, Ui_Wizard):
	"""Classe que define a Qwizard que realiza o teste de compatibilidade do dispositivo."""

	__canceled = False

	START = 0
	NUMBER = 1
	INSERT = 2
	MESSAGE = 3
	END = 4

	NUMBER_OF_PORTS = -1
	REMAINING_PORTS = -1
	SUCCESSFUL_PORTS = 0
	FAILED_PORTS = 0

	SUCCESS = 0
	FAIL = 1
	INTERRUPTED = 2
	RESULT = -1

	visited_ports = []
	internal_ports = []

	def __init__(self, parent, info):
		"""Construtor que inicializa a QWizard, chamando o construtor da classe pai.
		Conecta os sinais necessarios e chama __adjusts() para fazer os ajustes na tela."""
		QtGui.QWizard.__init__(self, parent)
		Ui_Wizard.__init__(self)
		self.setupUi(self)

		self.__adjusts()
		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)
		self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.setInterrupted)

	def __adjusts(self):
		"""Faz os ajustes iniciais na tela."""
		for id in self.pageIds():
			self.removePage(id)

		self.numberWarningLabel.hide()
		self.insertWarningLabel.hide()

		self.setPage(self.START, self.start)
		self.setPage(self.NUMBER, self.number)
		self.setPage(self.INSERT, self.insert)
		self.setPage(self.MESSAGE, self.message)
		self.setPage(self.END, self.end)

		self.backButton = self.button(QtGui.QWizard.BackButton);
		self.nextButton = self.button(QtGui.QWizard.NextButton);
		self.cancelButton = self.button(QtGui.QWizard.CancelButton);
		self.finishButton = self.button(QtGui.QWizard.FinishButton);

		self.backButton.setText(u"Voltar")
		self.nextButton.setText(u"Avançar")
		self.cancelButton.setText(u"Cancelar")
		self.finishButton.setText(u"Concluir")

	def wizCore(self, newId):
		"""Metodo que ira ser chamado quando ocorrer o sinal currentIdChanged(int), que indica que a tela do wizard foi mofificada.
		Serao feitos os ajustes necessarios."""
		self.backButton.setText(u"Voltar")
		self.nextButton.setText(u"Avançar")
		self.cancelButton.setText(u"Cancelar")
		self.finishButton.setText(u"Concluir")

		if (newId == self.START):
			self.visited_ports = []
			self.internal_ports = []
		elif (newId == self.NUMBER):
			pass
		elif (newId == self.INSERT):
			pass
		elif (newId == self.MESSAGE):
			self.REMAINING_PORTS = self.REMAINING_PORTS - 1
			pass
		elif (newId == self.END):
			end = "Portas testadas: %i \n \n Portas detectadas: %i \n Portas não detectadas: %i" % (self.NUMBER_OF_PORTS, self.SUCCESSFUL_PORTS, self.FAILED_PORTS)
			self.RESULT = end
			self.endLabel.setText(QtGui.QApplication.translate("Wizard", end, None, QtGui.QApplication.UnicodeUTF8))
			pass
		else:
			pass

	def validateCurrentPage(self):
		"""
		Função chamada por QWizard quando o usuario clica em Next ou Finish.
		Usada para validar a pagina atual.
		Se retornar True, a proxima pagina eh exibida; se retornar False, permanece na pagina atual.
		"""
		cur = self.currentId()
		ret = True

		if (not self.__canceled):
			if (cur == self.NUMBER):
				n = self.numberLineEdit.text()
				if (unicode(n).isdigit()):
					self.NUMBER_OF_PORTS = int(n)
					self.REMAINING_PORTS = int(n)
					self.numberWarningLabel.hide()
					ret = True

					# ls /sys/bus/usb/devices/ --dired --ignore=usb* --ignore=*:* | grep - | sed :a;$!N;s/\\n/;/g;ta 
#					cmd = [['ls', '/sys/bus/usb/devices/', '--dired', '--ignore=usb*', '--ignore=*:*'], ['grep', '-'], ['sed', ':a;$!N;s/\\n/;/g;ta']]
					cmd = [['ls', '/sys/bus/usb/devices/', '--dired', '--ignore=usb*', '--ignore=*:*']]
					i, o_str, e_str, returncode = exec_command_parms(cmd)
					internal_devices = o_str.strip()
#					print "DEBUG: strip ", internal_devices
					if internal_devices:
						internal_devices = internal_devices.split()
					self.internal_ports = internal_devices
#					print "DEBUG: internal ports ", self.internal_ports

				else:
					self.numberWarningLabel.show()
					self.numberLineEdit.setFocus()
					ret = False
			elif (cur == self.INSERT):
				time.sleep(1) #tempo para o SO reconhecer o device
#				cmd = [['ls', '/sys/bus/usb/devices/', '--dired', '--ignore=usb*', '--ignore=*:*'], ['grep', '-'], ['sed', ':a;$!N;s/\\n/;/g;ta']]#, ["sed", ':a;$!N;s/\\n/; /g;ta']]
				cmd = [['ls', '/sys/bus/usb/devices/', '--dired', '--ignore=usb*', '--ignore=*:*']]
				i, o_str, e_str, returncode = exec_command_parms(cmd)
				port = o_str.strip()
				ports = []
				if port:
					ports = port.split()
#				print "DEBUG: ports ", ports

				def list_sub(a, b):
					c = []
					for i in a:
						if i not in b:
							c.append(i)
					return c

				non_internal_ports = list_sub(ports, self.internal_ports)
#				print "DEBUG: non_internal_ports ", non_internal_ports
				if len(non_internal_ports) == 0:
#					print "DEBUG: Nenhuma porta nova foi reconhecida"
					msg = "Não foi possível reconhecer a porta onde o pen drive está inserido. \n\n\n Pressione <b>Avançar</b> para continuar."
					self.messageLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
					self.messageLabel.setTextFormat(QtCore.Qt.RichText)
					self.FAILED_PORTS = self.FAILED_PORTS + 1
					self.insertWarningLabel.setVisible(False)
					ret = True
					#failed ports + 1
				else:
					non_visited_ports = list_sub(non_internal_ports, self.visited_ports)
#					print "DEBUG: non_visited_ports", non_visited_ports
					if len(non_visited_ports) == 0:
#						print "DEBUG: Porta já testada"
						self.insertWarningLabel.setVisible(True)
						ret = False
					else:
						if len(non_visited_ports) == 1:
							port = non_visited_ports[0]

							self.visited_ports.append(port)
							self.SUCCESSFUL_PORTS = self.SUCCESSFUL_PORTS + 1

							msg = "Teste realizado com sucesso. \n\nPressione <b>Avançar</b> para continuar."
							self.messageLabel.setText(QtGui.QApplication.translate("Wizard", msg, None, QtGui.QApplication.UnicodeUTF8))
							self.messageLabel.setTextFormat(QtCore.Qt.RichText)
							self.insertWarningLabel.setVisible(False)
							ret = True
						else:
#							print "DEBUG: Comportamento indesejado"
							pass

#				print "DEBUG:", port, self.visited_ports, self.internal_ports

			elif (cur == self.MESSAGE):
				if (self.REMAINING_PORTS > 0):
					self.back()
					self.back()
			else:
				pass

		return ret

	def nextId(self):
		"""Função de QWizard que define a proxima pagina a ser exibida quando o usuario clica no botao Next(Avancar)."""
		ret = -1
		cur = self.currentId()

		if (cur == self.NUMBER and self.NUMBER_OF_PORTS < 1):
			ret = self.END
		elif (cur == self.MESSAGE and self.REMAINING_PORTS > 0):
			ret = self.INSERT
		elif (cur == self.END):
			ret = -1
		else:
			ret = cur + 1

		return ret

	def setInterrupted(self):
		"""Configura as mensagens em caso de interrupção do teste."""
		self.__canceled = True
		self.RESULT = "O teste foi interrompido pelo usuário."

	def testOnThread(self):
		"""Função que delega a execução da função play() a uma nova thread."""
		threading.Thread(target=self.test).start()

	def test(self):
		"""Função que executa o programa usado para aceitação do teste de compatibilidade."""
#		print "DEBUG: teste"
		pass

if __name__ == "__main__":
	from PyQt4 import QtCore, QtGui
	import sys

	app = QtGui.QApplication(sys.argv)

	gui = SoundWizard("/dev/audio")

	sys.exit(app.exec_())