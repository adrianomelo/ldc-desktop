# -*- coding: utf-8 -*-

class DiagResVideo:
	"""Classe basica da biblioteca que define os resultados da parte de diagnostico."""
	__diag_dict = None

	__vendor = None
	__model = None
	__screenSize = None
	__currentResolution = None
	__maximumResolution = None
	__vsyncRange = None
	__hsyncRange = None
	__supportedResolutions = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict
		try:
			self.__vendor = (diag_dict['info']['vendor']['id'], diag_dict['info']['vendor']['value'])
		except:
			self.__vendor = (-1, "")

		try:
			self.__model = (diag_dict['info']['model']['id'], diag_dict['info']['model']['value'])
		except:
			self.__model = (-1, "")

		try:
			self.__screenSize = diag_dict['info']['screen_size']['value']
		except:
			self.__screenSize = ""

		try:
			self.__currentResolution = diag_dict['info']['cur_resolution']['value']
		except:
			self.__currentResolution = ""

		try:
			self.__maximumResolution = diag_dict['info']['max_resolution']['value']
		except:
			self.__maximumResolution = ""

		try:
			self.__vsyncRange = diag_dict['info']['vsync_range']['value']
			self.__hsyncRange = diag_dict['info']['hsync_range']['value']
		except:
			self.__vsyncRange = ""
			self.__hsyncRange = ""


	def getVendor(self):
		"""Retorna fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		"""Retorna modelo do dispositivo."""
		return self.__model

	def getScreenSize(self):
		"""Retorna tamanho da tela."""
		return self.__screenSize

	def getCurrentResolution(self):
		"""Retorna resolução atual."""
		return self.__currentResolution

	def getMaximumResolution(self):
		"""Retorna resolução máxima."""
		return self.__maximumResolution

	def getVsyncRange(self):
		"""Retorna faixa de sincronização vertical."""
		return self.__vsyncRange

	def getHsyncRange(self):
		"""Retorna faixa de sincronização horizontal."""
		return self.__hsyncRange

	def getSupportedResolutions(self):
		"""Retorna resoluções suportadas."""
		return self.__supportedResolutions

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	screenSize = property(getScreenSize, None, None, None)
	currentResolution = property(getCurrentResolution, None, None, None)
	maximumResolution = property(getMaximumResolution, None, None, None)
	vsyncRange = property(getVsyncRange, None, None, None)
	hsyncRange = property(getHsyncRange, None, None, None)
	supportedResolutions = property(getSupportedResolutions, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Vendor: %s\nModel: %s\nScreen Size: %s\nCurrent Resolution: %s\nMaximum Resolution: %s\nVertical Sync Range: %s\nHorizontal Sync Range: %s" % (self.vendor, self.model, self.screenSize, self.currentResolution, self.maximumResolution, self.vsyncRange, self.hsyncRange)

	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append(('Fabricante', self.vendor[1]))
		diagList.append(('Modelo', self.model[1]))
		diagList.append(('Tamanho', self.screenSize))
		diagList.append((u'Resolução atual', self.currentResolution))
		diagList.append((u'Resolução máxima', self.maximumResolution))
		diagList.append((u'Taxa de sincronização vertical', self.vsyncRange))
		diagList.append((u'Taxa de sincronização horizontal', self.hsyncRange))
		return diagList

