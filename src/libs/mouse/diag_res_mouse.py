# -*- coding: utf-8 -*-

class DiagResMouse:
	"""Classe basica da biblioteca de wireless que define os resultados da parte de diagnostico."""
	__diag_dict = None

	__plugged = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict
		
		self.__plugged = diag_dict['actionDetected']

	def getPlugged(self):
		"""Indica se o mouse está plugado."""
		return self.__plugged

	plugged = property(getPlugged, None, None, None)
	
	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Plugged: %s" % (self.plugged)
	
	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		if (not self.plugged):
			msg = u"Seu mouse parece não estar conectado. Verifique a conexão e tente novamente."
			diagList.append((u'Mouse desconectado', msg))
		return diagList