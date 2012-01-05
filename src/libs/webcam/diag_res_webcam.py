# -*- coding: utf-8 -*-
class DiagResWebcam:
	"""Classe basica da biblioteca que define os resultados da parte de diagnostico."""
	__diag_dict = None

	__status = None
	__drivers = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict
		self.__status = (diag_dict['status'] == 1)

		if (diag_dict['info']):
			self.__drivers = []

			for key in diag_dict['info'].keys():
				if key.__contains__("driver_mod"):
					self.__drivers.append(diag_dict['info'][key]['value'])

	def getStatus(self):
		"""Retorna estado do diagnostico."""
		return self.__status

	def getDrivers(self):
		"""Retorna lisa de drivers carregados."""
		if self.__drivers == None:
			return ""
		else:
			return self.__drivers

	status = property(getStatus, None, None, None)
	drivers = property(getDrivers, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Result: %s\nDrivers: %s" % (self.status, ", ".join(self.drivers))


	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append((u'Drivers carregados pelo Sistema', ", ".join(self.drivers)))
		return diagList
