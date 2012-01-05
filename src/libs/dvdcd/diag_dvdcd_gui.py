# -*- coding: utf-8 -*-

import sys, threading, time
from PyQt4 import QtCore, QtGui

from libs.core.commands_utils import ApplicationExecutor

from libs.dvdcd.frame_dvdcd_burn import Ui_WizardDiagDVDCD

from libs.dvdcd.info_res_dvdcd import InfoResDVDCD
from libs.dvdcd.diag_res_dvdcd import DiagResDVDCD

class DiagDVDCDGUI(QtGui.QWizard, Ui_WizardDiagDVDCD):

	START = 0
	OPEN = 1
	BURN = 2
	READ = 3
	END = 4
	CANCEL = 5
	WRONG = 6
	FAIL = 7
	REINSERT = 8
	ERASED = 9
	FORMATING = 10

	LDC_TEMP_DIR = "/var/tmp/LDC"
	FILE_TO_BURN = "%s/ldc_burn_test.tar" % LDC_TEMP_DIR
	TEMP_MOUNTING_POINT = "%s/mnt" % LDC_TEMP_DIR

	__canceled = False

	__info = None

	__burnStatus = False
	__readStatus = False
	__formatStatus = False

	__currentMedia = (None, False)
	__expectedMedia = (None, False)

	__wrongMedia = False
	__needFormat = False

	def __init__(self, parent, info, expectedMedia):
		"""
		parent - Objeto pai.
		deviceFile - Endereço do dispositivo a ser testado. Ex: /dev/hdc
		expectedMedia - Dicionario que representa o tipo de mídia esperado, no dispositivo, para gravação.
		info - Instancia contendo as informacoes do dispositivo.
		"""

		QtGui.QWizard.__init__(self, parent)
		Ui_WizardDiagDVDCD.__init__(self)
		self.setupUi(self)

		self.__executor = ApplicationExecutor()

		self.__info = info
		self.__deviceFile = info.deviceFile
		self.__expectedMedia = expectedMedia

		self.__backButton = self.button(QtGui.QWizard.BackButton);
		self.__nextButton = self.button(QtGui.QWizard.NextButton);
		self.__cancelButton = self.button(QtGui.QWizard.CancelButton);
		self.__finishButton = self.button(QtGui.QWizard.FinishButton);

		self.__adjusts()

	def getInfo(self):
		"""Retorna a estrutura de informacao sobre o dispositivo."""
		return self.__info

	def getBurnStatus(self):
		"""Retorna o status da gravacao no dispositivo."""
		return self.__burnStatus

	def getReadStatus(self):
		"""Retorna o status da leitura do dispositivo."""
		return self.__readStatus

	def getCurrentMedia(self):
		"""Retorna a midia atual, inserida no CD/DVD."""
		return self.__currentMedia

	def getResult(self):
		"""Retorna o resultado final da execucao do teste."""
		return {'currentMedia': self.__currentMedia, 'burnStatus': self.__burnStatus, 'readStatus': self.__readStatus}

	info = property(getInfo, None, None, None)
	burnStatus = property(getBurnStatus, None, None, None)
	readStatus = property(getReadStatus, None, None, None)
	currentMedia = property(getCurrentMedia, None, None, None)
	result = property(getResult, None, None, None)

	def __adjusts(self):
		"""Redefine as páginas do QWizard, utilizando IDs conhecidos, e realiza pequenos ajustes."""
		for id in self.pageIds():
			self.removePage(id)

		self.setPage(self.START, self.wizardPage_Start)
		self.setPage(self.OPEN, self.wizardPage_Open)
		self.setPage(self.BURN, self.wizardPage_Burn)
		self.setPage(self.READ, self.wizardPage_Read)
		self.setPage(self.END, self.wizardPage_End)
		self.setPage(self.CANCEL, self.wizardPage_Cancel)
		self.setPage(self.WRONG, self.wizardPage_WrongMedia)
		self.setPage(self.FAIL, self.wizardPage_Fail)
		self.setPage(self.REINSERT, self.wizardPage_Reinsert)
		self.setPage(self.ERASED, self.wizardPage_Erased)
		self.setPage(self.FORMATING, self.wizardPage_Format)

		labelsList = [self.label_2, self.label, self.emptyMediaLabel, self.label_4, self.label_5, self.label_3, self.label_7, self.label_10, self.label_14, self.label_11, self.label_6]

		for i in labelsList:
			newText = i.text()
			newText.replace("[???]", "%s" % self.__expectedMedia['Type'])
			newText.replace("MODELO_DO_DISPOSITIVO", "\"%s %s (em %s)\"" % (self.__info.vendor, self.__info.model, self.__info.deviceFile))

			i.setText(QtGui.QApplication.translate("WizardDiagDVDCD", unicode(newText), None, QtGui.QApplication.UnicodeUTF8))

		self.setButtonText(QtGui.QWizard.BackButton, u"Voltar")
		self.setButtonText(QtGui.QWizard.NextButton, u"Avançar")
		self.setButtonText(QtGui.QWizard.CancelButton, u"Cancelar")
		self.setButtonText(QtGui.QWizard.FinishButton, u"Concluir")

		self.__backButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.__nextButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.__cancelButton.setStyleSheet("background-color: rgb(235, 235, 250);")
		self.__finishButton.setStyleSheet("background-color: rgb(235, 235, 250);")

		self.connect(self, QtCore.SIGNAL("currentIdChanged(int)"), self.wizCore)

	def wizCore(self, page_number):
		"""Funcao chamada na transicao entre paginas, que faz o ajuste dos botoes, dependendo
		da pagina destino

		page_number - Pagina destino.
		"""

		if page_number == self.START:
			self.__showButtons(2,0,0,2)
			pass
		elif page_number == self.OPEN:
			self.__showButtons(2,0,0,1)
			pass
		elif page_number == self.BURN:
			self.__showButtons(1,0,0,1)
			pass
		elif page_number == self.READ:
			self.__showButtons(1,0,0,1)
			pass
		elif page_number == self.END:
			self.__showButtons(0,0,2,0)
			pass
		elif page_number == self.CANCEL:
			self.__showButtons(0,0,2,0)
			pass
		elif page_number == self.WRONG:
			self.__showButtons(2,0,0,1)
			pass
		elif page_number == self.FAIL:
			self.__showButtons(0,0,2,0)
			pass
		elif page_number == self.REINSERT:
			self.__showButtons(2,0,0,1)
			pass
		elif page_number == self.ERASED:
			self.__showButtons(2,0,0,1)
			pass
		elif page_number == self.FORMATING:
			self.__showButtons(1,0,0,1)
			pass

	def __showButtons(self, next, back, finish, cancel):
		"""Metodo auxiliar para configuracao da exibicao dos botoes.
		Cada parametro pode ter valor 0, 1 ou 2, correspondendo a
		'oculto', 'desabilitado' e 'habilitado', respectivamente.

		Parametros:
		next - Configuracao para o botao Next.
		back - Configuracao para o botao Back.
		finish - Configuracao para o botao Finish.
		cancel - Configuracao para o botao Cancel.
		"""
		buttons = [QtGui.QWizard.CancelButton, QtGui.QWizard.BackButton, QtGui.QWizard.NextButton, QtGui.QWizard.FinishButton]
		status = [cancel, back, next, finish]

		layout = []

#		print "DEBUG: next = " + str(next)
#		print "DEBUG: back = " + str(back)
#		print "DEBUG: finish = " + str(finish)
#		print "DEBUG: cancel = " + str(cancel)
#		print "DEBUG: cancel, back, next, finish"
#		print "DEBUG: ", buttons

		for i, v in enumerate(buttons):

			visible = False
			enabled = False

#			print "DEBUG:", i, v, status[i]

			if (status[i] == 0):
				visible = False
				enabled = False
			elif (status[i] == 1):
				visible = True
				enabled = False
			elif (status[i] == 2):
				visible = True
				enabled = True
			else:
#				print "DEBUG: wrong showButtons code"
				continue

			self.button(v).setVisible(visible)
			self.button(v).setEnabled(enabled)

#		self.__backButton.setVisible(False)
#		self.__backButton.setEnabled(False)

	def __goToPage(self, page):
		"""Funcao auxiliar para retornar a pagina especificada por page"""

		while (self.hasVisitedPage(page)):
			self.back()

		return page

	def nextId(self):
		"""Redefine o metodo nextId de QWizard para especificar a ordem e condições corretas para a evolução das telas"""
		ret = -1

		cur = self.currentId()

#		print "DEBUG: nextId(%d)" % cur

		if (self.__canceled): # Wizard canceled
			self.__canceled = False
			ret = self.__goToPage(self.CANCEL)

		else:
			if (cur == self.START):
				ret = self.__goToPage(self.OPEN)

			elif (cur in [self.OPEN, self.WRONG]):
				if (self.__wrongMedia):
					ret = self.__goToPage(self.WRONG)
				elif (self.__needFormat):
					ret = self.__goToPage(self.FORMATING)
				else:
					ret = self.__goToPage(self.BURN)

			elif (cur == self.FORMATING):
				if (self.__formatStatus):
					ret = self.__goToPage(self.ERASED)
				else:
					ret = self.__goToPage(self.WRONG)

			elif (cur == self.ERASED):
				ret = self.__goToPage(self.BURN)

			elif (cur == self.BURN):
				if (self.__burnStatus):
					ret = self.__goToPage(self.REINSERT)
				else:
					ret = self.__goToPage(self.FAIL)

			elif (cur == self.REINSERT):
				ret = self.__goToPage(self.READ)

			elif (cur == self.READ):
				if (self.__readStatus):
					ret = self.__goToPage(self.END)
				else:
					ret = self.__goToPage(self.FAIL)

			elif (cur == self.FAIL or cur == self.CANCEL or cur == self.END):
				ret = -1

			else:
#				print "DEBUG : DiagDVDCDGUI : Wrong currentId"
				pass

		return ret

	def runAndWait(self, function, *args):
		"""Funcao que executa outra funcao, passada como parametro, em uma thread separada"""

		eventLoop = QtCore.QEventLoop()
		eventThread = SimpleThread(function, *args)

		self.connect(eventThread, QtCore.SIGNAL("finished()"), eventLoop.quit)

		eventThread.start()
		eventLoop.exec_()

		return eventThread.result

	def validateCurrentPage(self):
		"""
		Método redefinido para especificar se deve-se avançar para a próxima página ou não.
		Este método é executado imediatamente apos o usuário clicar em 'Avançar'.
		"""
		ret = True

		cur = self.currentId()

#		print "DEBUG: validateCurrentPage(%d)" % cur

		if (self.__canceled):
			pass

		elif (cur == self.START):
			pass

		elif (cur == self.OPEN):
			self.__showButtons(1, 0, 0, 1)
#			print "showButtons em OPEN - next e cancel visíveis e desabilitados"

			closed = self.runAndWait(closeTray, self.info.deviceFile)
			closed = (closed == 0)

			if (not closed):
				print "ERRO: Gaveta aberta"
				ret = False

			else:
				self.__needFormat = False
				self.__wrongMedia = False

				self.__currentMedia = self.runAndWait(getMediaInfo, self.info.deviceFile)

				if (self.__currentMedia['Type'] == self.__expectedMedia['Type']):
					if (not self.__currentMedia['Empty']):
						if (self.__currentMedia['Rewritable']):
							self.__needFormat = True
						else:
							self.__wrongMedia = True
				else:
					self.__wrongMedia = True

				if (self.__wrongMedia):
					self.runAndWait(openTray, self.info.deviceFile)

			self.__showButtons(2, 0, 0, 2)
#			print "showButtons em OPEN 2 - next e cancel visíveis e habilitados"

		# Fecha e/ou verifica se a gaveta esta fechada.
		elif (cur == self.REINSERT or cur == self.ERASED):
			self.__showButtons(1, 0, 0, 1)
#			print "showButtons em REINSERT ou ERASED - next e cancel desabilitados"

			closed = self.runAndWait(closeTray, self.info.deviceFile)
			closed = (closed == 0)

			if (not closed):
				print "ERRO: Gaveta aberta"
				ret = False

			self.__showButtons(2, 0, 0, 2)
#			print "showButtons em REINSERT ou ERASED 2 - next e cancel habilitados"

		elif (cur == self.BURN):
			pass

		elif (cur == self.READ):
			pass

		elif (cur == self.WRONG):
			self.__showButtons(1, 0, 0, 1)
#			print "showButtons em WRONG - next e cancel desabilitados"

			closed = self.runAndWait(closeTray, self.info.deviceFile)
			closed = (closed == 0)

			if (not closed):
				print "ERRO: Gaveta aberta"
				ret = False

			else:
				self.__needFormat = False

				self.__wrongMedia = False
				self.__currentMedia = self.__getMediaInfo()

				media = self.__currentMedia

				if (media['Type'] == self.__expectedMedia['Type']):
					if (not media['Empty']):
						if (media['Rewritable']):
							self.__needFormat = True
						else:
							self.__wrongMedia = True
				else:
					self.__wrongMedia = True

				if (self.__wrongMedia):
					self.runAndWait(openTray, self.info.deviceFile)
					ret = False

			self.__showButtons(2, 0, 0, 2)
#			print "showButtons em WRONG - next e cancel habilitados"

		elif (cur == self.CANCEL):
			QtGui.QWizard.reject(self)

		return ret

	def initializePage(self, newId):
		"""
		Método redefinido para especificar a máquina de estados do diagnóstico de DVD/CD.
		Este método é chamado para preparar as páginas, antes da exibição.
		"""

		"""
		Esse metodo é chamado durante a transição entre telas, porém antes de pintar a nova tela.
		Por isso é necessário o uso de QThread e sinais.
		"""

#		print "DEBUG: ------------------------- initializePage(%d) -----------------------" % newId

		# Desabilitar botoes
#		if (newId in [self.OPEN, self.ERASED, self.REINSERT, self.WRONG, self.FORMATING, self.BURN, self.READ]):
#			self.__showButtons(1, 0, 0, 1)
#			print "showButtons em initializePage 1"

		if (newId == self.START):
#			self.__showButtons(2, 0, 0, 2)
#			print "showButtons em initializePage 2"
			pass

		elif (newId in [self.OPEN, self.ERASED, self.REINSERT, self.WRONG]):
			# Abrir gaveta
			self.__cancelButton.setEnabled(False)
			self.__currentSimpleThread = SimpleThread(openTray, self.info.deviceFile)
			self.connect(self.__currentSimpleThread, QtCore.SIGNAL("finished()"), self.__openTrayEnded)
			self.__currentSimpleThread.start()

		elif (newId == self.FORMATING):
			# Formatar
			self.formatProgressLabel.show()
			self.timer = QtCore.QTimer()
			QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateFormatProgressLabel)
			self.timer.start(1000)
			self.__currentSimpleThread = SimpleThread(formatMedia, self.info.deviceFile, self.__currentMedia)
			self.connect(self.__currentSimpleThread, QtCore.SIGNAL("finished()"), self.__formatEnded)
			self.__currentSimpleThread.start()

		elif (newId == self.BURN):
			# Gravar
			self.burnProgressLabel.show()
			self.timer = QtCore.QTimer()
			QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateBurnProgressLabel)
			self.timer.start(1000)
			self.__currentSimpleThread = SimpleThread(burn, self.info.deviceFile, self.LDC_TEMP_DIR, self.FILE_TO_BURN, self.__currentMedia)
			self.connect(self.__currentSimpleThread, QtCore.SIGNAL("finished()"), self.__burnEnded)
			self.__currentSimpleThread.start()

		elif (newId == self.READ):
			# Ler e comparar MD5
			self.readProgressLabel.show()
			self.timer = QtCore.QTimer()
			QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateReadProgressLabel)
			self.timer.start(1000)
			self.__currentSimpleThread = SimpleThread(read, self.info.deviceFile, self.TEMP_MOUNTING_POINT, self.FILE_TO_BURN)
			self.connect(self.__currentSimpleThread, QtCore.SIGNAL("finished()"), self.__readEnded)
			self.__currentSimpleThread.start()

		elif (newId in [self.CANCEL, self.END, self.FAIL]):
			#self.__showButtons(0, 0, 2, 0)
			#print "showButtons em initializePage 3 - finish habilitado"
			pass

	formatCounter = 0
	def updateFormatProgressLabel(self):
		self.formatCounter = self.formatCounter + 1
		self.formatProgressLabel.setText(str(self.formatCounter))

	burnCounter = 0
	def updateBurnProgressLabel(self):
		self.burnCounter = self.burnCounter + 1
		self.burnProgressLabel.setText(str(self.burnCounter))

	readCounter = 0
	def updateReadProgressLabel(self):
		self.readCounter = self.readCounter + 1
		self.readProgressLabel.setText(str(self.readCounter))



	def __openTrayEnded(self):
		"""Metodo executado ao final da abertura da gaveta"""
		if (self.__currentSimpleThread.result != 0):
			print "ERRO: Problema ao abrir gaveta."

		self.__cancelButton.setEnabled(True)
		#self.__showButtons(2, 0, 0, 2)
		#print "showButtons em openTrayEnded - cancel e next habilitados"

	def __closeTrayEnded(self):
		"""Metodo executado ao final do fechamento da gaveta"""
		if (self.__currentSimpleThread.result != 0):
			print "ERRO: Problema ao fechar gaveta."

		#self.__showButtons(2, 0, 0, 2)
		#print "showButtons em closeTrayEnded - cancel e next habilitados"

	def __formatEnded(self):
		"""Metodo executado ao final da formatacao da midia"""
		self.__formatStatus = self.__currentSimpleThread.result

		if (not self.__formatStatus):
			self.__needFormat = False
			self.__wrongMedia = False

		self.timer.stop()
		self.formatProgressLabel.hide()
		self.formatCounter = 0
		self.next()

	def __burnEnded(self):
		"""Metodo executado ao final da gravacao da midia"""
		self.__burnStatus = self.__currentSimpleThread.result
		self.timer.stop()
		self.burnProgressLabel.hide()
		self.burnCounter = 0
		self.next()

	def __readEnded(self):
		"""Metodo executado ao final da leitura dos dados gravados"""
		self.__readStatus = self.__currentSimpleThread.result
		self.timer.stop()
		self.readProgressLabel.hide()
		self.readCounter = 0
		self.next()


def openTray(deviceFile):
	"""Utiliza a aplicação eject para abrir a gaveta do DVD/CD especificado por deviceFile"""

	outputStr, errorStr, returnCode = ApplicationExecutor().executeCommandAndWait(True, None, "cdrecord -eject dev=%s" % deviceFile)
	return returnCode

def closeTray(deviceFile):
	"""Utiliza a aplicação eject para fechar a gaveta do DVD/CD especificado por deviceFile"""

	outputStr, errorStr, returnCode = ApplicationExecutor().executeCommandAndWait(True, None, "cdrecord -load dev=%s" % deviceFile)
	return returnCode

def getMediaInfo(deviceFile):
	"""
	Verifica qual o tipo de mídia inserida no dispositivo deviceFile

	Este método retorna um dicionario com as chaves 'Type', 'Rewritable' e 'Empty',
	onde Type é 'CD', 'DVD' ou None, Rewritable é um booleano, indicando se a mídia é
	regravável e Empty é outro booleano, indicando se a mídia esta vazia.
	"""

	# Current: CD-RW
	# Current: DVD-R sequential recording
	# Current: DVD-RW sequential recording

	mediaType = None
	rewritable = False
	empty = False

	cmd0 = ['cdrecord', '-prcap', 'dev=%s' % deviceFile]
	cmd1 = ['grep', 'Current:']
	cmd2 = ['awk', '{print $2}']

	o_str, e_str, ret_code = ApplicationExecutor().executeCommandAndWait(False, None, cmd0, cmd1, cmd2)

	if (ret_code == 0):
		o_str = o_str.rstrip()

		knownMedia = False

		if (o_str in ['CD-R', 'CD-RW', 'DVD-R', 'DVD+R', 'DVD-RW', 'DVD+RW']):
			knownMedia = True
			rewritable = False

			if (o_str.__contains__("RW")):
				rewritable = True

		else:
			print "ERRO : Tipo de midia desconhecido (%s)" % o_str

		if (knownMedia):
			split_char = "-"

			if (o_str.__contains__("+")):
				split_char = "+"

			mediaType = o_str.split(split_char)[0]

		if (mediaType):
			empty = isEmpty(deviceFile)

	return {'Type': mediaType, 'Rewritable': rewritable, 'Empty': empty}

def isEmpty(deviceFile):
	"""Funcao que verifica se a midia inserida no dispositivo 'deviceFile' esta vazia."""

	cmd0 = ['cdrecord', '-media-info', 'dev=%s' % deviceFile, '2>', '/dev/null']
	cmd1 = ['grep', 'disk status:']
	cmd2 = ['awk', '{print $3}']

	o_str, e_str, ret_code = ApplicationExecutor().executeCommandAndWait(False, None, cmd0, cmd1, cmd2)

	ret = (ret_code == 0) and (o_str.rstrip() == "empty")

	return ret

def formatMedia(deviceFile, media):
	"""Formata a mídia no dispositivo"""

	outputStr = None
	errorStr = None
	returnCode = None

	if (media['Type'] == 'DVD'):
		outputStr, errorStr, returnCode = ApplicationExecutor().executeCommandAndWait(True, None, "dvd+rw-format -force %s" % deviceFile)
	elif (media['Type'] == 'CD'):
		outputStr, errorStr, returnCode = ApplicationExecutor().executeCommandAndWait(True, None, "cdrecord -v gracetime=2 dev=%s blank=fast -force" % deviceFile)
	else:
		print "ERRO : Tipo de midia desconhecido"

	return (returnCode == 0)

def burn(deviceFile, tempDir, fileToBurn, media):
	"""Grava o arquivo fileToBurn na mídia inserida"""

	outputStr = None
	errorStr = None
	returnCode = None

	createBurnFileCmd = __file__.split("/")
	del(createBurnFileCmd[-1])
	createBurnFileCmd.append("create_burn_file.sh")
	createBurnFileCmd = "/".join(createBurnFileCmd)
	createBurnFileCmd = "/bin/sh " + createBurnFileCmd

	executor = ApplicationExecutor()

	outputStr, errorStr, returnCode = executor.executeCommandAndWait(True, None, createBurnFileCmd)

	if (returnCode == 0):
		if (media['Type'] == 'DVD'):
			outputStr, errorStr, returnCode = executor.executeCommandAndWait(True, None, "growisofs -dvd-compat -input-charset=ISO-8859-1 -Z %s -R -J -pad %s" % (deviceFile, fileToBurn))

		elif (media['Type'] == 'CD'):
			outputStr, errorStr, returnCode = executor.executeCommandAndWait(True, None, "mkisofs -r -R -J -l -L -allow-multidot -o %s/ldc_tmp.iso -graft-points %s=%s" % (tempDir, fileToBurn, fileToBurn))
			outputStr, errorStr, returnCode = executor.executeCommandAndWait(True, None, "cdrecord dev=%s -v --eject speed=4" % deviceFile)

		else:
			print "ERRO : Tipo de midia desconhecido"

	return (returnCode == 0)

def read(deviceFile, mountingPoint, fileToBurn):
	"""Lê o MD5 CRC do arquivo local fileToBurn e do arquivo gravado e armazena o resultado da comparação entre eles em __readStatus"""
	executor = ApplicationExecutor()

	result = False

	outputStr, errorStr, returnCode = executor.executeCommandAndWait(True, None, "mount %s %s" % (deviceFile, mountingPoint))

	if (returnCode == 0):
		outputStr1, errorStr1, returnCode1 = executor.executeCommandAndWait(False, None, ['md5sum', "%s" % fileToBurn], ['awk', '{print $1}'])
		outputStr2, errorStr2, returnCode2 = executor.executeCommandAndWait(False, None, ['md5sum', "%s/%s" % (mountingPoint, fileToBurn.split("/")[-1])], ['awk', '{print $1}'])
		outputStr3, errorStr3, returnCode3 = executor.executeCommandAndWait(True, None, "umount %s" % deviceFile)

		originalMD5 = outputStr1.rstrip()
		burnedMD5 = outputStr2.rstrip()

		result = (returnCode1 == 0) and (returnCode2 == 0) and (originalMD5 == burnedMD5)

	return result

class SimpleThread(QtCore.QThread):
	"""Classe auxiliar, para execucao de metodos como threads individuais."""

	def __init__(self, function, *vargs):
		"""Construtor

		Parametros:
			function - Metodo a ser executado.
			vargs - Parametros para a funcao.
		"""
		QtCore.QThread.__init__(self)
		self.__function = function
		self.__vargs = vargs
		self.__result = None

	def run(self):
		"""Reimplementacao do metodo run, definido na classe QThread."""
		self.__result = self.__function(*self.__vargs)

	def getResult(self):
		"""Metodo que retorna o resultado da execucao do metodo passado ao construtor"""
		return self.__result

	result = property(getResult, None, None, None)

if __name__ == "__main__":
	from PyQt4 import QtCore, QtGui
	import sys

	app = QtGui.QApplication(sys.argv)

	gui = DiagDVDCDGUI("/dev/hdb")

	sys.exit(app.exec_())