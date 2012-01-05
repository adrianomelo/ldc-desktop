# -*- coding: utf-8 -*-

class DiagResUsb:
	"""Classe basica da biblioteca que define os resultados da parte de diagnostico."""
	__diag_dict = None
	__pluggedDevices = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict
		self.__pluggedDevices = diag_dict['info']['plugged_devices']['value']

	def getPluggedDevices(self):
		"""Retorna lista de dispositivos plugados aos barramentos usb."""
		return self.__pluggedDevices

	pluggedDevices = property(getPluggedDevices, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		ret = "Plugged Devices: %s\n" % self.pluggedDevices
		return ret

	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		devices = self.pluggedDevices.split(";")
		resultList = []
		for device in devices:
			if device and device.strip() != '':
				resultList.append(device)
		diagList.append(('Dispositivos Plugados', ', '.join(resultList)))
		return diagList

