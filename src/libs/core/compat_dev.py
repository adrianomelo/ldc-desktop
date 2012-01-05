# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

class CompatDev(QtCore.QObject):
	"""
	Classe base para os módulos de compatibilidade, de onde herdam todas
	as outras, específicas de cada dispositivo.
	
	"""

	_compat_res = None

	def __init__(self, parent):
		"""
			parent - objeto pai
			
		"""
		
		QtCore.QObject.__init__(self)
		self.parent = parent
		pass

	def compat(self, info_list):
		"""
		Retorna uma lista de tuplas Python, com os resultados da execução dos testes de compatibilidade.
		Este método retorna um stub e deve ser redefinido, nas subclasses.
		
		"""
		
		result = None

		if (info_list):
			result = []

			for info in info_list:
				result.append((False, 'Stub'))

		self._compat_res = result

	def getCompatResults(self):
		return self._compat_res

	def runTest(self, diagClass):
		"""
		Executa as funções de informativo, diagnóstico e compatibilidade, imprimindo o resultado de cada uma delas.
		
		"""
		
		test_info = diagClass()

		test_info.info()

		info_res = test_info.getInfoResults()

		self.compat(info_res)

		compat_list = self.getCompatResults()

		print "--- INFO ---"
		if (info_res):
			for i in info_res:
				print i
		else:
			print None

		print "--- COMPAT ---"
		if (compat_list):
			for i in compat_list:
				print i
		else:
			print None
