# -*- coding: utf-8 -*-

class DiagResMemory(object):
	"""Classe básica da biblioteca de Memória que define os resultados da parte de diagnóstico."""
	__diag_dict = None

	__dmiDecodeSize = None
	__procMemInfoSize = None

	def __init__(self, diag_dict):
		"""Construtor
		
		Parâmetro:
		diag_dict -- dicionário com as informações da etapa de diagnóstico
		"""
		self.__diag_dict = diag_dict
		
		self.__calculateSizes(diag_dict)

	def getDmiDecodeSize(self):
		"""Retorna o tamanho de memória detectado pele dmidecode."""
		return self.__dmiDecodeSize

	def getProcMemInfoSize(self):
		"""Retorna o tamanho de memória usando o /proc."""
		return self.__procMemInfoSize

	def getStatus(self):
		"""Retorna o status."""
		if (self.__diag_dict['status'] == 1):
			return True
		else:
			return False

	dmiDecodeSize = property(getDmiDecodeSize, None, None, None)
	procMemInfoSize = property(getProcMemInfoSize, None, None, None)
	status = property(getStatus, None, None, None)

	def __calculateSizes(self, info_dict):
		"""Calcula o tamanho da memória para o dmidecode e proc somando os valores contidos no 'info'"""
		totalDMI = 0
		totalProc = 0
		
		for key, value in info_dict['info'].items():
			if value['description'].__contains__("Module @ "):
				totalDMI += int(value['id'])
			elif value['description'].__contains__("meminfo"):
				totalProc += int(value['id'])
		
		self.__dmiDecodeSize = totalDMI * 1000
		self.__procMemInfoSize = totalProc

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "DMIDecode: %d\nProcMemInfo: %d\nResult: %s" % (self.dmiDecodeSize, self.procMemInfoSize, self.status)
	
	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append((u'Memória total informada pelo Librix', str(self.procMemInfoSize / 1024) + " MB"))
		diagList.append((u'Memória total informada pela BIOS', str(self.dmiDecodeSize / 1024) + " MB"))
		return diagList
	