# -*- coding: utf-8 -*-

from libs.binding.libldc_python import libldc_python

class DiagDev:
	"""
	Classe base para os módulos de informação/diagnóstico, de onde herdam todas
	as outras, específicas de cada dispositivo.
	
	"""

	_lib_name = None
	_lib_bind = None

	_info_res_class = None
	_diag_res_class = None

	_info_tuple = None
	_diag_tuple = None

	def __init__ (self, libName, ctrl, infoResClass, diagResClass):
		"""
			libName - Nome representativo da biblioteca C. Ex.: libldc_mouse.so
			infoResClass - Classe que encapsula os resultados informativos.
			diagResClass - Classe que encapsula os resultados de diagnóstico.
			
		"""
		
		self._lib_name = libName
		self._ctrl = ctrl
		self._info_res_class = infoResClass
		self._diag_res_class = diagResClass
		
		self._lib_bind = libldc_python(libName)		

	def info(self):
		"""Chama a função info, definida na biblioteca C, e armazena o resultado num atributo."""
		self._info_tuple = self._lib_bind.info(1)

	def diag(self, info):
		"""Chama a função diag, definida na biblioteca C, e armazena o resultado num atributo."""
		self._diag_tuple = self._lib_bind.diag(1, info)

	def getLDCInfo(self):
		"""Retorna a estrutura de dados em C resultante da execução da função info"""
		return self._info_tuple[0]
	
	def getLDCDiag(self):
		"""Retorna a estrutura de dados em C resultante da execução da função diag"""
		return self._diag_tuple[0]

	def getInfoResults(self):
		"""
		Retorna uma lista python dos resultados da execução da função info,
		encapsulados, cada um, pela classe infoResClass, passada ao construtor.
		Este método retorna um stub, se nenhuma classe de resultado de informativo
		foi definida.
		
		"""
		
		ret = None
		
		if (self._info_tuple):
			if (self._info_res_class):
				ret = []
				
				for i in self._info_tuple[1]:
					ret.append(self._info_res_class(i))
			else:
				print "STUB: InfoRes Class is 'None'"

		return ret
	
	def getDiagResults(self):
		"""
		Retorna uma lista python dos resultados da execução da função diag,
		encapsulados, cada um, pela classe diagResClass, passada ao construtor.
		Este método retorna um stub, se nenhuma classe de resultado de diagnóstico
		foi definida.
		
		"""
		
		ret = None

		if (self._diag_tuple):
			if (self._diag_res_class):
				ret = []
				
				for i in self._diag_tuple[1]:
					ret.append(self._diag_res_class(i))
			else:
				ret = [(False, 'Stub : No DiagRes Class')]
		else:
			ret = ['Stub : No C level diag result. (Python only??)']
		
		return ret
	
	def runTest(self):
		"""
		Executa as funções de informativo e diagnóstico e imprime o resultado de
		cada uma delas.
		
		"""
		
		self.info()
		self.diag(self.getLDCInfo())
		
		print "--- INFO ---"
		info_res = self.getInfoResults() 
		if (info_res):
			for i in info_res:
				print i
		else:
			print None

		print "--- DIAG ---"
		diag_res = self.getDiagResults() 
		if (diag_res):
			for i in diag_res:
				print i
		else:
			print None