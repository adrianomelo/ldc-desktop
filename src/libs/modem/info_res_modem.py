# -*- coding: utf-8 -*-

"""
	Name: modem
	Status: 1
		vendor = Unknown (270336) : Vendor
		device = AT Modem (262145) : Model
	----INFO----
		dev_file = /dev/ttySHSF0 (-1) : Device file
"""

class InfoResModem:
	"""Classe basica da biblioteca de modem que define os atributos da parte informativa."""
	__info_dict = None
	
	__vendor = None
	__model = None
	__deviceFile = None
	
	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict
		
		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__model = (info_dict['model']['id'], info_dict['model']['value'])
		self.__deviceFile = info_dict['info']['dev_file']['value']
		
	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model
	
	def getDeviceFile(self):
		"""Retorna o device file do dispositivo."""
		return self.__deviceFile

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)	

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Device file: %s\n\tVendor: %s\n\tModel: %s" % (self.deviceFile, self.vendor, self.model)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Modelo', self.model[1]))
		return infoList
	