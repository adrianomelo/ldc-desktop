# -*- coding: utf-8 -*-

class DiagResProcessor(object):
	"""Classe básica da biblioteca de processador que define os resultados da parte de diagnóstico."""
	
	__diag_dict = None

	def __init__(self, diag_dict):
		"""Construtor
		
		Parâmetro:
		diag_dict -- dicionário com as informações da etapa de diagnóstico
		"""
		self.__diag_dict = diag_dict

	@property
	def model(self):
		"""Retorna o modelo."""
		return self.__diag_dict['info']['version']['value'].rstrip()

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do diagnóstico de processador."""
		return "Model: %s" % (self.model)
	
	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append(('Dminame', self.model))
		return diagList
