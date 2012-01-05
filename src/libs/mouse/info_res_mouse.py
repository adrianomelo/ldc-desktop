# -*- coding: utf-8 -*-

"""
	Name: mouse
	Status: 1
	        vendor = NULL (1) : Vendor
	        device = Macintosh mouse button emulation (1) : Model
	----INFO----
	        bus = ADB (135) : Bus type
	        device = /dev/input/mice (-1) : Device file
	        buttons = NULL (3) : # of buttons
	        wheels = NULL (0) : Has wheels
	        gpm = exps2 (-1) : GPM protocol
	        xf86 = explorerps/2 (-1) : XFree86 protocol
	
	Name: mouse
	Status: 1
	        vendor = NULL (2) : Vendor
	        device = ImPS/2 Generic Wheel Mouse (5) : Model
	----INFO----
	        bus = PS/2 (128) : Bus type
	        device = /dev/input/mice (-1) : Device file
	        buttons = NULL (3) : # of buttons
	        wheels = NULL (1) : Has wheels
	        gpm = exps2 (-1) : GPM protocol
	        xf86 = explorerps/2 (-1) : XFree86 protocol
"""

class InfoResMouse:
	"""Classe basica da biblioteca de mouse que define os atributos da parte informativa."""
	
	__info_dict = None

	__vendor = None
	__model = None
	__bus = None
	__deviceFile = None
	__numberOfButtons = None
	__hasWheel = None
	__gpmProtocol = None
	__xf86Protocol = None
	
	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict
		
		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__model = (info_dict['model']['id'], info_dict['model']['value'])
		self.__bus = info_dict['info']['bus']['value']
		self.__deviceFile = info_dict['info']['device']['value']
		self.__numberOfButtons = info_dict['info']['buttons']['id']
		self.__hasWheel = bool(info_dict['info']['wheels']['id'])
		self.__gpmProtocol = info_dict['info']['gpm']['value']
		self.__xf86Protocol = info_dict['info']['xf86']['value']

	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model

	def getBus(self):
		"""Retorna o bus do dispositivo."""
		return self.__bus

	def getDeviceFile(self):
		"""Retorna o device file do dispositivo."""
		return self.__deviceFile

	def getNumberOfButtons(self):
		"""Retorna o numero de botões do dispositivo."""
		return self.__numberOfButtons

	def getHasWheel(self):
		"""Retorna um int indicando se o dispositivo possui roldana."""
		return self.__hasWheel

	def getGpmProtocol(self):
		"""Retorna o protocolo gpm do dispositivo."""
		return self.__gpmProtocol

	def getXf86Protocol(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__xf86Protocol

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	bus = property(getBus, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	numberOfButtons = property(getNumberOfButtons, None, None, None)
	hasWheel = property(getHasWheel, None, None, None)
	gpmProtocol = property(getGpmProtocol, None, None, None)
	xf86Protocol = property(getXf86Protocol, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Vendor: %s\nModel: %s\nBus: %s\nDevice File: %s\nNumber of buttons: %s\nHas wheel: %s\nGPM protocol: %s\nXFree86 Protocol: %s" % (self.vendor, self.model, self.bus, self.deviceFile, self.numberOfButtons, self.hasWheel, self.gpmProtocol, self.xf86Protocol)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Modelo', self.model[1]))
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Barramento', self.bus))
		infoList.append((u'Número de botões', str(self.numberOfButtons)))
		if (self.hasWheel == True):
			wheel = "Presente"
		elif (self.hasWheel == False):
			wheel = "Ausente"
		infoList.append(('Roldana', wheel))
		protocolList = [('GPM', self.gpmProtocol), ('XF86', self.xf86Protocol)]
		infoList.append(('Protocolos', protocolList))
		return infoList
	
