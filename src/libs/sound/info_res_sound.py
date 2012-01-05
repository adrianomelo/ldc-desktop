# -*- coding: utf-8 -*-

"""
Name: sound
Status: 1
	vendor = Intel Corporation (98438) : Vendor
	device = 82801FB/FBM/FR/FW/FRW (ICH6 Family) High Definition Audio Controller (75368) : Device
----INFO----
	model = Intel 82801FB/FBM/FR/FW/FRW (ICH6 Family) High Definition Audio Controller (-1) : Model
	driver_modules = snd_hda_intel (-1) : Driver Modules
"""

class InfoResSound:
	"""Classe básica da biblioteca de som que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__product = None
	__drivers = None
	__driverActive = None
	__deviceID = None
	__model = None

	def __init__(self, info_dict):
		"""Construtor

		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação.
		"""
		self.__info_dict = info_dict

		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__product = (info_dict['model']['id'], info_dict['model']['value'])
		self.__model = info_dict['info']['model']['value']
		self.__drivers = info_dict['info']['driver_modules']['value']
		self.__driverActive = info_dict['info']['driver_active']['id']
		if info_dict['info'].has_key('device_id'):
			self.__deviceID = info_dict['info']['device_id']['value']
		else:
			self.__deviceID = '-1'

	def getProduct(self):
		""" Retorna o nome do produto."""
		return self.__product

	def getDriverActive(self):
		"""Retorna se o driver está ativo ou não."""
		result = 1
		if self.__driverActive != 1:
			result = 0
		return result

	def getDeviceID(self):
		""" Retorna o identificador do dispositivo.
		"""
		return self.__deviceID

	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		""" Retorna o modelo do dispositivo."""
		return self.__model

	def getDrivers(self):
		""" Retorna os drivers do dispositivo. """
		return self.__drivers

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	drivers = property(getDrivers, None, None, None)
	driverActive = property(getDriverActive, None, None, None)
	deviceID = property(getDeviceID, None, None, None)
	product = property(getProduct, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do dispositivo."""
		return "Vendor: %s\nDevice: %s\nModel: %s\nDevice ID: %s\nDriver Modules: %s\nDriver Active: %s" % (self.vendor, self.product, self.model, self.deviceID, self.drivers, self.driverActive)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf."""
		infoList = []
		infoList.append(('Produto', self.product[1]))
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Modelo', self.model))
		infoList.append((u'N° da placa', str(self.deviceID)))
		driverActive = u'Não'
		if self.driverActive:
			driverActive = 'Sim'
		infoList.append((u'Driver Ativo', driverActive))
		infoList.append(('Modulos do driver', self.drivers))
		return infoList



