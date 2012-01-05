# -*- coding: utf-8 -*-

"""
	FALTANDO MODELO DE DADOS PARA FAZER ISSO AQUI. ATUALMENTE TA IGUAL A NETWORK
"""

class InfoResWireless:
	"""Classe básica da biblioteca de adaptador de rede sem fio que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__model = None
	__driver = None
	__deviceFile = None
	__channels = None
	__encryption_modes = None
	__authentication_modes = None
	__wifimode = None

	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict

		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__model = (info_dict['model']['id'], info_dict['model']['value'])
		self.__driver = info_dict['info']['driver']['value']
		self.__deviceFile = info_dict['info']['device_file']['value']
		self.__channels = ''
		if info_dict['info'].has_key('channels'):
			self.__channels = info_dict['info']['channels']['value']
		self.__encryption_modes = ''
		if info_dict['info'].has_key('encryption_modes'):
			self.__encryption_modes = info_dict['info']['encryption_modes']['value']
		self.__authentication_modes = ''
		if info_dict['info'].has_key('authentication_modes'):
			self.__authentication_modes = info_dict['info']['authentication_modes']['value']
		self.__wifimode = ''
		if info_dict['info'].has_key('wifimode'):
			self.__wifimode = info_dict['info']['wifimode']['value']

	def getWifimode(self):
		""" Retorna os modos de operação wifi a/b/g/n suportados."""
		return self.__wifimode

	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model

	def getDriver(self):
		"""Retorna o driver do dispositivo."""
		return self.__driver

	def getDeviceFile(self):
		"""Retorna o identificador do dispositivo no /dev."""
		return self.__deviceFile

	def getChannels(self):
		"""Retorna os canais suportados pelo dispositivo."""
		return self.__channels

	def getEncryption_modes(self):
		"""Retorna os modos de endriptação suportados pelo dispositivo."""
		return self.__encryption_modes

	def getAuthentication_modes(self):
		"""Retorna os modos de autenticação suportados pelo dispositivo."""
		return self.__authentication_modes

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	driver = property(getDriver, None, None, None)
	deviceFile = property(getDeviceFile, None, None, None)
	channels = property(getChannels, None, None, None)
	encryption_modes = property(getEncryption_modes, None, None, None)
	authentication_modes = property(getAuthentication_modes, None, None, None)
	wifimode = property(getWifimode, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Vendor: %s\nModel: %s\nDriver: %s\nDevice file: %s\n" % (self.vendor, self.model, self.driver, self.deviceFile)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model[1]))
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append(('Dispositivo', self.deviceFile))
		modeList = []
		modes = self.wifimode.strip()
		modes.strip("802.11")
		if modes != 'Unknown':
			if modes.count('a') > 0:
				modeList.append("802.11a - 54 Mbps")
			if modes.count('b') > 0:
				modeList.append("802.11b - 11 Mbps")
			if modes.count('g') > 0:
				modeList.append("802.11g - 54 Mbps")
			if modes.count('n') > 0:
				modeList.append("802.11n - 128 Mbps")
		infoList.append(('Modos 802.11', ', '.join(modeList)))
		encryptionList = self.encryption_modes.split(' ')
		infoList.append(('Criptografia', ', '.join(encryptionList)))
		authenticationList= self.authentication_modes.split(' ')
		infoList.append((u'Autenticação', ', '.join(authenticationList)))
		infoList.append(('Drivers', self.driver))
		return infoList

