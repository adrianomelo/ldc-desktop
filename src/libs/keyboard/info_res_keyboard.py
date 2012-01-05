# -*- coding: utf-8 -*-
		
class InfoResKeyboard:
	"""Classe básica da biblioteca de teclado que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__model = None
	__bus = None
	__deviceFile = None
	__xkbRules = None
	__xkbModel = None
	__xkbLayout = None

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
		self.__xkbRules = info_dict['info']['xkb_rules']['value']
		self.__xkbModel = info_dict['info']['xkb_model']['value']
		self.__xkbLayout = info_dict['info']['xkb_layout']['value']

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

	def getXkbRules(self):
		"""Retorna o as regras do xkb do dispositivo."""
		return self.__xkbRules

	def getXkbModel(self):
		"""Retorna o modelo do xkb do dispositivo."""
		return self.__xkbModel
	
	def getXkbLayout(self):
		"""Retorna o layout do xkb do dispositivo."""
		return self.__xkbLayout

	"""Propriedades que retornam os valores dos atributos"""
	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	bus = property(getBus, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	xkbRules = property(getXkbRules, None, None, None)
	xkbModel = property(getXkbModel, None, None, None)
	xkbLayout = property(getXkbLayout, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Vendor: %s\nModel: %s\nBus: %s\nDevice File: %s\nXKB Rules: %s\nXKB Model: %s\nXKB Layout: %s" % (self.vendor, self.model, self.bus, self.deviceFile, self.xkbRules, self.xkbModel, self.xkbLayout)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Modelo', self.model[1]))
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Barramento', self.bus))
		xkbList = [('Layout', self.xkbLayout), ('Regras', self.xkbRules), ('Modelo', self.xkbModel)]
		infoList.append((u'Configurações XKB', xkbList))
		return infoList
	