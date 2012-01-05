# -*- coding: utf-8 -*-

"""
	Name: harddisk
	Status: -1
		vendor = Maxtor (-1) : Vendor
		device = Maxtor 6B120M0 (-1) : Model
	----INFO----
		bus = IDE (-1) : Bus type
		device_file = /dev/sdb (-1) : Device file
		size = NULL (117246) : Size (in MB)
		drivers = ata_piix|sd (-1) : Device drivers
		model_family = Maxtor DiamondMax 10 family (ATA/133 and SATA/150) (-1) : Model family

	Name: harddisk
	Status: -1
		vendor = Maxtor (-1) : Vendor
		device = Maxtor 6B120M0 (-1) : Model
	----INFO----
		bus = IDE (-1) : Bus type
		device_file = /dev/sda (-1) : Device file
		size = NULL (117246) : Size (in MB)
		drivers = ata_piix|sd (-1) : Device drivers
		model_family = Maxtor DiamondMax 10 family (ATA/133 and SATA/150) (-1) : Model family
"""

class InfoResHarddisk(object):
	"""Classe básica da biblioteca de HD que define os atributos da parte informativa."""
	
	__info_dict = None
	
	__vendor = None
	__model = None
	__bus = None
	__deviceFile = None
	__size = None
	__drivers = None
	__modelFamily = None

	def __init__(self, info_dict):
		"""Construtor
		
		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict
		
		self.__vendor = info_dict['vendor']['value']
		self.__model = info_dict['model']['value']
		self.__bus = info_dict['info']['bus']['value']
		self.__deviceFile = info_dict['info']['device_file']['value']
		self.__size = info_dict['info']['size']['id']
		self.__drivers = info_dict['info']['drivers']['value'].split("|")
		self.__modelFamily = info_dict['info']['model_family']['value']

	def getVendor(self):
		"""Retorna o fabricante"""
		return self.__vendor
	
	def getModel(self):
		"""Retorna o modelo"""
		return self.__model
	
	def getBus(self):
		"""Retorna o bus"""
		return self.__bus
	
	def getDeviceFile(self):
		"""Retorna o device file do dispositivo"""
		return self.__deviceFile
	
	def getSize(self):
		"""Retorna o tamanho do HD"""
		return self.__size
	
	def getDrivers(self):
		"""Retorna uma lista com os drivers configurados para o dispositivo."""
		return self.__drivers
	
	def getModelFamily(self):
		"""Retorna a família do modelo"""
		return self.__modelFamily

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	bus = property(getBus, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	size = property(getSize, None, None, None)
	drivers = property(getDrivers, None, None, None)
	modelFamily = property(getModelFamily, None, None, None)
	
	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do dispositivo."""
		return "Model: %s\nVendor: %s\nDevice File: %s\nBus: %s\nDrivers: %s\nModel Family: %s\nSize: %s" % (self.model, self.vendor, self.deviceFile, self.bus, self.drivers, self.modelFamily, self.size)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append((u'Família', self.modelFamily))
		infoList.append(('Modelo', self.model))
		infoList.append(('Fabricante', self.vendor))
		size = ((self.size * 1024 * 1024) / 1000000000)
		infoList.append(('Capacidade', str(size) + " GB"))
		infoList.append(('Barramento', self.bus))
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Drivers', ", ".join(self.drivers)))
		return infoList
