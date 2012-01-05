# -*- coding: utf-8 -*-
import os, sys, time, shutil
from PyQt4 import QtCore, QtGui
from gui.pyui.LDC_Main_Window import Ui_LDC_Main_Window

from gui.LDC_Selection_Frame import LDC_Selection_Frame
from gui.LDC_Result_Frame import LDC_Result_Frame, DeviceNotFound
from gui.LDC_Executor import LDC_Executor

from gui.widgets.messagebox.LDC_MessageBox import LDC_MessageBox
from gui.widgets.inputdialog.LDC_InputDialog import LDC_InputDialog

from libs.core.pdf_report import PdfReport


class LDC_Main(QtGui.QMainWindow, Ui_LDC_Main_Window):
	"""
	Classe principal do programa.
	Define funções principais e variáveis acessadas por várias etapas do processo, desde seleção dos testes até exibição de resultados.
	Controla o fluxo de execução do LDC e coordena a exibição de telas.
	Representa a thread da interface gráfica.
	"""

	def __init__(self, app):
		"""
		Construtor da classe.
		"""
		QtGui.QMainWindow.__init__(self)
		Ui_LDC_Main_Window.__init__(self)
		self.setupUi(self)
		self.app = app

		self.wait = QtCore.QWaitCondition()
		self.waitMutex = QtCore.QMutex()
		self.waitCounter = 0
		self.answer = {}

		self.logger = []

	def getWait(self):
		"""
		"""
		return self.wait

	def getWaitMutex(self):
		"""
		"""
		return self.waitMutex

	def getWaitCounter(self):
		"""
		"""
		return self.waitCounter

	def selectTests(self):
		"""
		Rotina que exibe a tela de seleção após chamar as funções de carregamento de plugis/bibliotecas e geração de itens selecionáveis LDCCheckBox.
		"""
		self.selectionFrame = LDC_Selection_Frame()
		self.librariesList = self.selectionFrame.loadLibraries()
		self.selectionFrame.generateList(self.librariesList)
		QtCore.QObject.connect(self.selectionFrame.pushButton, QtCore.SIGNAL("clicked()"), self.tryExecuteTests)
		self.setCentralWidget(self.selectionFrame)

	def tryExecuteTests(self):
		"""
		Verifica se testes foram selecionados e prossegue para a execução destes.
		Se nenhum teste foi selecionado, uma mensagem é exibida e o usuário permanece na tela de seleção.
		"""
		chosen_libraries = self.selectionFrame.getChosen()
		#print "DEBUG:", chosen_libraries
		if (chosen_libraries == []):
				dialog = LDC_MessageBox(self)
				dialog.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
				dialog.buttonBox.setCenterButtons(True)
				dialog.setMessage("Nenhum teste foi selecionado. Favor selecionar os dispositivos a diagnosticar antes de prosseguir.")
				result = dialog.exec_()
				self.wakePopupWait()
		else:
				self.executeTests()

	def createReport(self):
			"""
			Método que cria o relatório em pdf com as informações contidas em 'self.logger', salva o relatório se o
			usuário deseja e chama o método que mostra o relatório gerado.
			"""
			pdf = PdfReport(self.logger)
			filename = pdf.dump()
			openPath = filename
			self.showMessageBox(u'Você deseja salvar o relatório?') #Melhorar MessageBox

			if self.answer['code']: #Salvar relatório
					fileSavePath = QtGui.QFileDialog.getSaveFileName(self, u'Salvar relatório', filename, ('*.pdf'))
					if fileSavePath:
							shutil.move(filename, fileSavePath)
							openPath = str(fileSavePath)

			pdf.showReport(openPath)

	def executeTests(self):
		"""
		Cria um frame de resultados e cria uma thread independente da interface gráfica para a execução dos resultados.
		Enquanto os testes são executados, um label é exibido sobre a tela de seleção.
		Ao final de cada teste o resultado é inserido no frame de resultados.
		Ao final de todos os testes, a tela de resultados é exibida.
		"""
		self.resultFrame = LDC_Result_Frame()
		self.logger = []
		chosen_libraries = self.selectionFrame.getChosen()
		executor = LDC_Executor(self, chosen_libraries)
		QtCore.QObject.connect(self.resultFrame.pushButton, QtCore.SIGNAL("clicked()"), self.createReport)
		QtCore.QObject.connect(self.resultFrame.pushButton_2, QtCore.SIGNAL("clicked()"), self.selectTests)
		QtCore.QObject.connect(executor, QtCore.SIGNAL("exec_addResult(PyQt_PyObject)"), self.addResult)

		executor.start()
		label = self.createLoadingLabel()

		while executor.isRunning():
				label.setText("Carregando")
				label.update()
				self.app.processEvents()
				time.sleep(0.4)

				label.setText("Carregando.")
				label.update()
				self.app.processEvents()
				time.sleep(0.4)

				label.setText("Carregando..")
				label.update()
				self.app.processEvents()
				time.sleep(0.4)

				label.setText("Carregando...")
				label.update()
				self.app.processEvents()
				time.sleep(0.4)


		executor.terminate()
		executor.wait()

		label.hide()

		self.setCentralWidget(self.resultFrame)


	def addResult(self, list):
		"""
		Adiciona o resultado de um teste de tela de resultados.
		"""
		name = list[0]
		category = list[1]
		resultclass = list[2]
		icon = list[3]
		resultdict = list[4]
		reportRes = list[5]
		self.logger.append(reportRes)
		if resultdict['info'] == None:
				result = DeviceNotFound(name)
		else:
				result = resultclass(resultdict['info'], resultdict['compat'], resultdict['diag'])

		self.resultFrame.addResult(name, category, result, icon)

	def createLoadingLabel(self):
		"""
		Cria label para exibição enquanto os testes dos plugins são excutados.
		"""
		frame = QtGui.QFrame(self)
		frame.setGeometry(10, 10, 780, 580)
		frame.setStyleSheet("background-color: rgba(255, 255, 255, 175);\n color: rgb(57, 93, 118);\n font: 32pt \"Sans Serif\";")
		label = QtGui.QLabel(frame)
		label.setText("Carregando")
		label.setGeometry(240, 100, 300, 50)
		label.setAlignment(QtCore.Qt.AlignLeft)
		label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n color: rgb(57, 93, 118); font: 32pt \"Sans Serif\";")
		frame.show()
		frame.raise_()
		return label

	def showMessageBox(self, message):
		"""
		Exibe uma caixa de diálogo com uma mensagem message e armazena o resultado em self.answer['code'].
		"""
		dialog = LDC_MessageBox(self)
		dialog.setMessage(message)
		result = dialog.exec_()
		self.answer['code'] = result
		#print "DEBUG:", self.answer
		self.wakePopupWait()

	def showInputDialog(self, message):
		"""
		Exibe uma caixa de diálogo com uma mensagem e armazena o resultado em self.answer['code'] e o valor inserido pelo usuário em self.answer['result'].
		"""
		dialog = LDC_InputDialog(self)
		dialog.setMessage(message)
		result = dialog.exec_()
		self.answer['code'] = result
		self.answer['result'] = dialog.inputBox.text()
		self.wakePopupWait()

	def showCustomDialog(self, customDialogClass, *params):
		"""
		Exibe uma caixa de diálogo definida pelo usuário.
		Armazena os resultados da execução em self.answer['code'] e self.answer['result'];
		"""
		pos_x = self.x() + 40
		pos_y = self.y() + 40

		dialog = customDialogClass(self, *params)
		dialog.move(pos_x, pos_y)

		try:
				dialog.setPixmap(3, QtGui.QPixmap(":/ldc_wizard_bckg/ldc_wizard_bckg.png"))
		except:
				#print "DEBUG: customDialog is not a QWizard!"
				pass

		result = dialog.exec_()
		self.answer['code'] = result
		try:
				self.answer['result'] = dialog.RESULT
		except:
				self.answer['result'] = dialog.result
		self.wakePopupWait()
		pass

	def wakePopupWait(self):
		"""
		Função usada para sincronização de threads.
		Espera até que não existam threads pendentes antes de retornar.
		"""
		self.waitMutex.lock();

		# Sleep until there are no busy worker threads
		while (self.waitCounter > 0):
				self.waitMutex.unlock()
				sleep(1)
				self.waitMutex.lock()

		self.waitMutex.unlock()

		self.wait.wakeAll()