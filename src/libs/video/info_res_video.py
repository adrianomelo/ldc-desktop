# -*- coding: utf-8 -*-

"""
	Name: videocard
	Status: 1
		vendor = Intel Corporation (98438) : Vendor
		device = Intel 82915G Integrated Graphics Controller (75650) : Model
	----INFO----

	Name: videocard
	Status: 1
		vendor = Intel Corporation (98438) : Vendor
		device = Intel 915 G (75138) : Model
	----INFO----
		xf86_module_name = intel (-1) : XFree86 Server Module
		xf86_module_3d = NULL (0) : XFree86 Server Module 3D Support
		xf86_module_name = intel (-1) : XFree86 Server Module
		xf86_module_3d = NULL (1) : XFree86 Server Module 3D Support
		xf86_module_ext = dri| (-1) : XFree86 Server Module Extensions

	Name: framebuffer
	Status: 1
		vendor = Intel Corporation (0) : Vendor
		device = Intel(r)Grantsdale-G Graphics Controller (0) : Model
	----INFO----
		mem_size = NULL (8060928) : Video Memory Size (in bytes)
		sup_mode = 1920x1440 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1920x1440 (16 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1600x1200 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1600x1200 (16 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1600x1200 (24 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1280x1024 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1280x1024 (16 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1280x1024 (24 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1024x768 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1024x768 (16 bits) (-1) : Supported Mode/Resolution
		sup_mode = 1024x768 (24 bits) (-1) : Supported Mode/Resolution
		sup_mode = 640x480 (24 bits) (-1) : Supported Mode/Resolution
		sup_mode = 800x600 (16 bits) (-1) : Supported Mode/Resolution
		sup_mode = 800x600 (24 bits) (-1) : Supported Mode/Resolution
		sup_mode = 640x480 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 800x600 (8 bits) (-1) : Supported Mode/Resolution
		sup_mode = 640x480 (16 bits) (-1) : Supported Mode/Resolution
"""

class InfoResVideo:
	"""Classe básica da biblioteca de vídeo que define os atributos da parte informativa."""
	__info_dict = None

	__vendor = None
	__model = None

	__module = None
	__module3D = None
	__moduleExtensions = None

	__memorySize = None
	__supportedModes = None

	__monitor = None

	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict

		#print "DEBUG:", "info = " + str(info_dict)

		self.__vendor = (info_dict['vendor']['id'], info_dict['vendor']['value'])
		self.__model = (info_dict['model']['id'], info_dict['model']['value'])
		self.__module = ''
		if info_dict['info'].has_key('xf86_module_name'):
			self.__module = info_dict['info']['xf86_module_name']['value']
		self.__module3D = 0
		if info_dict['info'].has_key('xf86_module_3d'):
			self.__module3D = info_dict['info']['xf86_module_3d']['id']
		self.__moduleExtensions = []
		if info_dict['info'].has_key('xf86_module_ext'):
			self.__moduleExtensions = info_dict['info']['xf86_module_ext']['value'].strip().split('|')


	def getVendor(self):
		"""Retorna o fabricante do dispositivo."""
		return self.__vendor

	def getModel(self):
		"""Retorna o modelo do dispositivo."""
		return self.__model

	def getModule(self):
		"""Retorna o módulo do dispositivo."""
		return self.__module

	def getModule3D(self):
		"""Retorna o módulo 3d do dispositivo."""
		return self.__module3D

	def getModuleExtensions(self):
		"""Retorna as extensões dos módulos do dispositivo."""
		return self.__moduleExtensions

	def getMemorySize(self):
		"""Retorna o tamanho da memória."""
		return self.__memorySize

	def getSupportedModes(self):
		"""Retorna os modos suportados."""
		return self.__supportedModes

	def getMonitor(self):
		"""Retorna informações sobre o monitor conectado."""
		return self.__monitor

	vendor = property(getVendor, None, None, None)
	model = property(getModel, None, None, None)
	module = property(getModule, None, None, None)
	module3D = property(getModule3D, None, None, None)
	moduleExtensions = property(getModuleExtensions, None, None, None)
	memorySize = property(getMemorySize, None, None, None)
	supportedModes = property(getSupportedModes, None, None, None)
	monitor = property(getMonitor, None, None, None)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model[1]))
		infoList.append(('Fabricante', self.vendor[1]))
		infoList.append((u'Módulos do driver', self.module))
		mod3D = u"Não"
		if self.module3D:
			mod3D = "Sim"
		infoList.append((u'Possui módulo 3D', mod3D))
		extDr = ""
		if self.moduleExtensions:
			self.moduleExtensions.pop(-1)
			extDr = ", ".join(self.moduleExtensions)
		infoList.append((u'Extensões do driver', extDr))
		return infoList

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "Vendor: %s\nModel: %s\nModule: %s\n3D Module: %s\nModule Extensions: %s" % (self.vendor, self.model, self.module, self.module3D, ", ".join(self.moduleExtensions))
#		return "Vendor: %s\nModel: %s\nModule: %s\n3D Module: %s\nModule Extensions: %s\nMemory Size: %s\nSupported Modes: %s" % (self.vendor, self.model, self.module, self.module3D, self.moduleExtensions, self.memorySize, ", ".join(self.supportedModes))
