# -*- coding: utf-8 -*-

class InfoResDVDCD:
	"""Classe básica da biblioteca de CD/DVD que define os atributos da parte informativa."""
	__info_dict = None
	
	__deviceFile = None
	__model = None
	__vendor = None
	__drivers = None
	__medias = None

	def __init__(self, info_dict):
		"""Construtor
		
		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict
		
		self.__model = info_dict['model']['value']
		self.__vendor = info_dict['vendor']['value']
		self.__deviceFile = info_dict['info']['device']['value']
		self.__medias = info_dict['info']['medias']['value'].split("|")
		self.__drivers = info_dict['info']['drivers']['value'].split("|")
		
		self.__medias.remove('')
	
	def getDeviceFile(self):
		"""Retorna o device file."""
		return self.__deviceFile

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model

	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getDrivers(self):
		"""Retorna os drivers carregados para o dispositivo."""
		return self.__drivers

	def getMedias(self):
		"""Retorna as midias suportadas pelo dispositivo."""
		return self.__medias

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do dispositivo."""
		return "Model: %s\nVendor: %s\nDevice File: %s\nDrivers: %s\nMedias: %s" % (self.model, self.vendor, self.deviceFile, self.drivers, self.medias)

	deviceFile = property(getDeviceFile, None, None, None)
	model = property(getModel, None, None, None)
	vendor = property(getVendor, None, None, None)
	drivers = property(getDrivers, None, None, None)
	medias = property(getMedias, None, None, None)
	
	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Fabricante', self.vendor))
		infoList.append(('Modelo', self.model))
		infoList.append(('Dispositivo', self.deviceFile))
		infoList.append(('Drivers', ", ".join(self.drivers)))
		if (self.medias):
			infoList.append((u'Mídias suportadas', ", ".join(self.medias)))
		return infoList