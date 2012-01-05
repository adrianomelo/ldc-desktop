# -*- coding: utf-8 -*-

"""
	Name: webcam
	Status: 1
		Vendor = Logitech, Inc. (1133) : Vendor
		Product = QuickCam Chat (2348) : Product
	----INFO----
		Model = NULL (-1) : Model
		Driver = usb (-1) : Driver
		Device File = /dev/video0 (-1) : Device File
"""

class InfoResWebcam:
	"""Classe básica da biblioteca de webcam que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__product = None
	__model = None
	__driver = None
	__deviceFile = None

	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict

		self.__vendor = info_dict['vendor']['value']
		self.__product = info_dict['model']['value']
		self.__model = info_dict['info']['model']['value']
		self.__driver = info_dict['info']['driver']['value']
		self.__deviceFile = info_dict['info']['device']['value']
		self.__halUDI = info_dict['info']['hal_udi']['value']

	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getProduct(self):
		"""Retorna a identificação do produto"""
		return self.__product

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model

	def getDriver(self):
		"""Retorna o driver do dispositivo."""
		return self.__driver

	def getDeviceFile(self):
		"""Retorna o identificador do dispositivo no /dev."""
		return self.__deviceFile

	def getHalUDI(self):
		"""Retorna o identificador da camera, segundo o HAL"""
		return self.__halUDI

	vendor = property(getVendor, None, None, None)
	product = property(getProduct, None, None, None)
	model = property(getModel, None, None, None)
	driver = property(getDriver, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	halUDI = property(getHalUDI, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Vendor: %s\nModel: %s\nDriver: %s\nDevice file: %s" % (self.vendor, self.model, self.driver, self.deviceFile)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Produto', self.product))
		infoList.append(('Fabricante', self.vendor))
		infoList.append(('Modelo', self.model))
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Driver', self.driver))
		return infoList
