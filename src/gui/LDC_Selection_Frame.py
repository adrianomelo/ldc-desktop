# -*- coding: utf-8 -*-
import os, sys, traceback
from PyQt4 import QtCore, QtGui
from gui.pyui.LDC_Selection_Frame_pyui import Ui_LDC_Selection_Frame

class LDC_Selection_Frame(QtGui.QFrame, Ui_LDC_Selection_Frame):
	"""
	Classe responsável pela exibição e funções básicas da tela de seleção
	de testes a diagnosticar.
	"""


	def __init__(self):
		"""
		Construtor da classe.
		"""

		QtGui.QFrame.__init__(self)
		Ui_LDC_Selection_Frame.__init__(self)
		self.setupUi(self)
		QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked()"), self.selectAll)

	def loadLibraries(self):
		"""
		Método responsável pelo carregamento das bibliotecas disponíveis.
		"""

		libraries_list = []
		cwd = os.getcwd()
		sourcePath = cwd
		libsPath = os.path.join(sourcePath, "libs")

		for root, dirs, filesnames in os.walk(libsPath):
		    for dir in dirs:
		        if dir != ".svn" and dir != "core" and dir != "binding":
		            try:
		                path = "/".join([cwd, "libs", dir, "cfg.ldc"])
		                file = QtCore.QFile(path)
		                if (file.open(QtCore.QIODevice.ReadOnly)):
		                    folder, controller, ctrl_class, name, category, icon = self.parseCfgFile(file)

		                    importString = "from libs." + folder + "." + controller + " import " + ctrl_class
		                    exec importString

		                    libraries_list.append({'folder':folder, 'controller':controller, 'ctrl_class':ctrl_class, 'name':name, 'category':category, 'icon':icon})
		                    file.close()
		            except:
		                 print "Failed to load library: " + dir.lower().capitalize()
		                 traceback.print_exc()
		    break #TODO Fix-ugly

		libraries_list.sort(compareLibs)

		return libraries_list

	def parseCfgFile(self, file):
		"""
		Extrai as informações do arquivo de configuração de cada plugin.
		"""

		folder = file.readLine().__str__().replace("folder=\"", "").replace("\"\n", "")
		controller = file.readLine().__str__().replace("controller=\"", "").replace("\"\n", "")
		ctrl_class = file.readLine().__str__().replace("class=\"", "").replace("\"\n", "")
		name = file.readLine().__str__().replace("name=\"", "").replace("\"\n", "")
		category = file.readLine().__str__().replace("category=\"", "").replace("\"\n", "")
		icon = file.readLine().__str__().replace("icon=\"", "").replace("\"\n", "")
		#print "DEBUG:", folder, controller, ctrl_class, name, category, icon
		return folder, controller, ctrl_class, name, category, icon

	def generateList(self, libraries_list):
		"""
		Gera a lista de "checkboxes" para a interface gráfica.
		Em vez de QCheckBox de QT, usa LDCCheckBox para armazenar informações de configuração de cada biblioteca.
		"""

		for library in libraries_list:
		    choice = LDCCheckBox(library)
		    count = self.gridLayout.count()
		    self.gridLayout.addWidget(choice, count / 3, count % 3)
		#self.verticalLayout.addStretch()

	def getChosen(self):
		"""
		Lista e retorna os dispositivos selecionados na tela de seleção.
		"""

		count = self.gridLayout.count()
		chosen = []

		for i in range(0, count):
		    checkBox = self.gridLayout.itemAt(i).widget()
		    name = checkBox.objectName().__str__()
		    if checkBox.checkState() == 2:
		        chosen.append(checkBox.dict)

		return chosen

	def selectAll(self):
		"""
		Função que seleciona iterativamente todos os dispositivos listados na tela de selação.
		Disparada quando a caixa Todos da tela de seleção é clicada.
		"""

		state = self.checkBox.checkState()
		count = self.gridLayout.count()
		for i in range(0,count):
		    checkbox = self.gridLayout.itemAt(i).widget()
		    checkbox.setCheckState(state)



class LDCCheckBox(QtGui.QCheckBox):
	"""
	Alternativa à implementação de QCheckBox para armazenar
	informações relativas à biblioteca correspondente dentro
	do objeto selecionável.
	"""

	def __init__(self, dict):
		"""
		Construtor da classe LDCCheckBox
		"""
		self.dict = dict
		self.name = QtGui.QApplication.translate("LDC_Info", dict['name'], None, QtGui.QApplication.UnicodeUTF8)
		QtGui.QCheckBox.__init__(self, self.name)



def compareLibs(a, b):
	"""
	Função usada como critério para ordenação de listas de
	bibliotecas através da função sort().

	Passando essa função como parâmetro para a chamada de sort()
	de uma lista de bibliotecas, o resultado será a ordenação da
	lista baseada nos nomes dessas bibliotecas.
	"""
	result = -1
	an = a["name"]
	bn = b["name"]

	if (an > bn):
		result = 1
	elif (an == bn):
		result = 0
	
	return result









