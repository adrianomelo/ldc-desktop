# -*- coding: utf-8 -*-

from PyQt4 import QtCore

class CtrlDev(QtCore.QObject):
	"""
	Classe base para os módulos de controle, de onde herdam todas as outras,
	específicas de cada dispositivo.

	_name - Nome do dispositivo relativo a essa classe
	_category - Categoria do dispositivo relacionado a essa classe

	_diag - Instancia da classe de diagnóstivo/informativo (DiagDev) do dispositivo.
	_compat - Instancia da classe de compatibilidade (CompatDev) do dispositivo.

	_guiClass - Classe utilizada para representar os resultados do dispositivo, na GUI.

	_infoRes - Resultados encapsulados do informativo.
	_compatRes - Resultados encapsulados do teste de compatibilidade.
	_diagRes - Resultados encapsulados do teste de diagnóstico.
	_guiRes - Lista de instâncias de _guiClass, representando os resultados obtidos.

	"""
	_name = None
	_category = None

	_diag = None
	_compat = None

	_guiClass = None

	_infoRes = None
	_compatRes = None
	_diagRes = None
	_guiRes = None

	def __init__(self, parent):
		QtCore.QObject.__init__(self)
		self.parent = parent

	def execute_lib(self):
		"""
		Este método deve ser redefinido, nas subclasses, para refletir o
		comportamento esperado do dispositivo específico.

		"""
		pass

	def getCompat(self):
	    return self._compat

	def getName(self):
	    return self._name

	def getCategory(self):
	    return self._category

	def getGuiClass(self):
	    return self._guiClass

	def getInfoRes(self):
	    return self._infoRes

	def getCompatRes(self):
	    return self._compatRes

	def getDiagRes(self):
	    return self._diagRes

	def getGUIRes(self):
		"""
		Retorna a lista das instâncias da GUI, preenchidas com os respectivos
		resultados a serem apresentados.

		"""
		return self._guiRes

	def _callInfo(self):
		"""Executa a função de informativo e armazena o resultado encapsulado internamente"""
		self._diag.info()
		self._infoRes = self._diag.getInfoResults()

	def _callCompat(self):
		"""Executa a função de compatibilidade e armazena o resultado encapsulado internamente"""
		self._compat.compat(self._infoRes)
		self._compatRes = self._compat.getCompatResults()

	def _callDiag(self):
		"""Executa a função de diagnóstico e armazena o resultado encapsulado internamente"""
		self._diag.diag(self._diag.getLDCInfo())
		self._diagRes = self._diag.getDiagResults()

	def _createGUIs(self):
		"""
		Instancia a classe de GUI do dispositivo para cada um dos resultados
		do informativo, armazenando-as internamente.

		"""

		self._guiRes = []

		if self._infoRes:
			for index in range(0, len(self._infoRes)):
				diag = None

				if (self._diagRes):
					diag = self._diagRes[index]

				frame = self._guiClass(self._infoRes[index], self._compatRes[index], diag)
				self._guiRes.append(frame)
		else:
			#FIXME: Solução para resolver o problema de usb storage inexistente. Precisa ser melhorada!
			diag = None
			compat = None
			if (self._diagRes):
				diag = self._diagRes[0]
			if (self._compatRes):
				compat = self._compatRes[0]
			frame = self._guiClass(None, compat, diag)
			self._guiRes.append(frame)

	def print_test(self):
		"""
		Imprime os resultados obtidos a partir das execuções das funções
		callInfo, callDiag e callCompat.

		"""

		print "--- INFO ---"
		if (self._infoRes):
			for i in self._infoRes:
				print i
		else:
			print None

		print "--- COMPAT ---"
		if (self._compatRes):
			for i in self._compatRes:
				print i
		else:
			print None

		print "--- DIAG ---"
		if (self._diagRes):
			for i in self._diagRes:
				print i
		else:
			print None

	def gui_test(self):
		self._createGUIs()
		
		"""Exibe cada uma das GUI criadas"""
		for frame in self._guiRes:
			frame.show()
			
	def getReportInfo(self, name, category, icon):
		"""Cria a estrutura necessária para gerar o relatório em pdf a apartir dos dados de info, diag e compat.
		Retorna um lista de dicionario no formato
		  { 'category': 'nome da categoria', 
            'name': 'nome do dispositivo', 
            'icon': 'nome do arquivo da imagem do ícone',
            'info': [('Modelo', 'x'), ..., ('Vendor', 'y')] -- lista de tuplas contendo o resultado de info(), 
            'compat': (True/False, 'msg') -- resultado do teste de compatibilidade,
            'diag': [('Dispositivo', 'x'), ..., ('Tamanho', 'y')] -- lista de tuplas contendo o resultado de diag()
          }
		"""
		reportInfoList = []

		if self._infoRes and self._infoRes[0]:
			for index in range(0, len(self._infoRes)):
				diag = None
				info = None
				compat = None

				if (self._diagRes):
					diag = self._diagRes[index].getReportDiag()
				if (self._infoRes):
					info = self._infoRes[index].getReportInfo()		
				if (self._compatRes):
					compat = self._compatRes[index]		

				reportInfo = { 'category': category,
					  		   'name': name,
					  		   'icon': icon,
					  		   'info': info,
					  		   'compat': self._compatRes[index],
					  		   'diag': diag
					  		}
				reportInfoList.append(reportInfo)
		else:
			#FIXME: Solução para resolver o problema de usb storage inexistente. Precisa ser melhorada!
			diag = None
			compat = None
					
			if (self._diagRes and self._diagRes[0]):
				diag = self._diagRes[0].getReportDiag()
			if (self._compatRes and self._compatRes[0]):
				compat = self._compatRes[0]
			else:
				compat = (False, 'Nenhum dispositivo deste tipo foi encontrado.')
				
			reportInfo = { 'category': category,
				  		   'name': name,
				  			'info': None,
				  			'compat': compat,
				  			'diag': diag,
				  			'icon': icon
				  		}
			reportInfoList.append(reportInfo)	
		
		return reportInfoList	


	guiRes = property(getGUIRes, None, None, None)
	guiClass = property(getGuiClass, None, None, None)
	infoRes = property(getInfoRes, None, None, None)
	compatRes = property(getCompatRes, None, None, None)
	diagRes = property(getDiagRes, None, None, None)
	name = property(getName, None, None, None)
	category = property(getCategory, None, None, None)
	compat = property(getCompat, None, None, None)

	def waitUser(self):
		"""Chama o método waitUser da classe pai."""
		self.parent.waitUser()
		pass

	def waitUserFree(self):
		"""Chama o método waitUserFree da classe pai."""
		self.parent.waitUserFree()
		pass


	def showMessageBox(self, message):
		"""Emite o sinal para exibir uma MessageBox com a mensagem passada como parâmetro e fica esperando ela ser finalizada. 
		Retorna o resultado da MessageBox, inteiro indicando se foi clicado no botão 'OK' ou 'Cancelar'"""
		self.emit(QtCore.SIGNAL("showMessageBox(QString)"), message)
		self.waitUser()

		self.result = self.parent.parent.answer['code']
		self.waitUserFree()
		return self.result

	def showInputDialog(self, message):
		"""Emite o sinal para exibir um InputDialog com a mensagem passada como parâmetro e fica esperando ele ser finalizada. 
		Retorna o resultado do InputDialog, a resposta enviada pelo usuário"""
		self.emit(QtCore.SIGNAL("showInputDialog(QString)"), message)
		self.waitUser()

		self.result = self.parent.parent.answer
		self.waitUserFree()
		return self.result

	def showCustomDialog(self, customDialogClass, *params):
		"""Emite o sinal para exibir uma Dialog customizada, para isso recebe como parâmetros a customDialogClass e uma lista de parâmetros 
		para a sua inicialização."""
		self.emit(QtCore.SIGNAL("showCustomDialog!"), customDialogClass, *params)
		self.waitUser()

		self.result = self.parent.parent.answer
		self.waitUserFree()
		return self.result