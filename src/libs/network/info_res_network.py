# -*- coding: utf-8 -*-

"""
	Name: network
	Status: 1
	        vendor = Intel Corporation (98438) : Vendor
	        device = 82557/8/9/0/1 Ethernet Pro 100 (70185) : Model
	----INFO----
	        driver = e100 (-1) : Netcard Driver
	        device_file = /dev/eth0 (-1) : Netcard Device File
	        speed = 10/100 (-1) : Netcard Speed
	        link_state = NULL (1) : Netcard Link State
	
	Name: network
	Status: 1
	        vendor = Intel Corporation (98438) : Vendor
	        device = 82540EM Gigabit Ethernet Controller (69646) : Model
	----INFO----
	        driver = e1000 (-1) : Netcard Driver
	        device_file = /dev/eth1 (-1) : Netcard Device File
	        speed = 100/1000 (-1) : Netcard Speed
	        link_state = NULL (0) : Netcard Link State
"""

class InfoResNetwork:
	"""Classe básica da biblioteca de rede que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__model = None
	__driver = None
	__deviceFile = None
	__speed = None
	__linkState = None
	
	def __init__(self, info_dict):
		"""Construtor
		
		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict
		
		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__model = (info_dict['model']['id'], info_dict['model']['value'])
		self.__driver = info_dict['info']['driver']['value']
		self.__deviceFile = info_dict['info']['device_file']['value']
		self.__speed = info_dict['info']['speed']['value']
		self.__linkState = bool(info_dict['info']['link_state']['id'])

	def getVendor(self):
		"""Retorna o fabricante."""
		return self.__vendor

	def getModel(self):
		"""Retorna o modelo."""
		return self.__model

	def getDriver(self):
		"""Retorna o driver."""
		return self.__driver

	def getDeviceFile(self):
		"""Retorna o device file."""
		return self.__deviceFile

	def getSpeed(self):
		"""Retorna a velocidade."""
		return self.__speed

	def getLinkState(self):
		"""Retorna o estado do link."""
		return self.__linkState
	
	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	driver = property(getDriver, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	speed = property(getSpeed, None, None, None)
	linkState = property(getLinkState, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações da rede."""
		return "Vendor: %s\nModel: %s\nDriver: %s\nDevice file: %s\nSpeed: %s\nLink state: %s" % (self.vendor, self.model, self.driver, self.deviceFile, self.speed, self.linkState)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model[1]))
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Speed', self.speed))
		infoList.append(('Drivers', self.driver))
		infoList.append(('Dispositivo', self.deviceFile))
		linkDetec = u"Não"
		if (self.linkState):
			linkDetec = "Sim"
		infoList.append(('Link ativo', linkDetec))
		return infoList
	
	
	