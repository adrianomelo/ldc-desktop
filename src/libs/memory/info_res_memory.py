# -*- coding: utf-8 -*-

class InfoResMemory(object):
	"""Classe básica da biblioteca de Memória que define os atributos da parte informativa."""
	__info_dict = None

	__memoryController = None
	__memoryModules = None

	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict

		self.__memoryController = self.__loadController(info_dict)
		self.__memoryModules = self.__loadModules(info_dict)

	def __loadController(self, info_dict):
		"""Método auxiliar que cria um InfoResMemoryController apartir das informações do 'info_dict' passado como parâmetro.
		Retorna um 'InfoResMemoryController'"""
		ret = None

		if (info_dict['info'].has_key('mem_mod_volt')):
			maxMemoryModuleSize = info_dict['info']['max_mem_mod_size']['id']
			maxTotalMemorySize = info_dict['info']['max_total_mem_size']['id']
			memoryModuleVoltage = info_dict['info']['mem_mod_volt']['value']
			supportedTypes = info_dict['info']['sup_types']['value'].split("|")
			supportedTypes.pop(-1)
			supportedSpeeds = info_dict['info']['sup_speeds']['value'].split("|")
			supportedSpeeds.pop(-1)

			ret = InfoResMemoryController(maxMemoryModuleSize, maxTotalMemorySize, memoryModuleVoltage, supportedSpeeds, supportedTypes)

		return ret

	def __loadModules(self, info_dict):
		"""Método auxiliar que cria um InfoResMemoryModule apartir das informações do 'info_dict' passado como parâmetro.
		Retorna um lista de 'InfoResMemoryModule' contendo as informações de cada módulo."""
		ret = None
		modulesName = None

		for key, value in info_dict['info'].items():
			if value['description'].__contains__("Module @ ") and value['description'].__contains__(" type"):
				if (modulesName):
					modulesName.append(key.split("_")[0])
				else:
					modulesName = [key.split("_")[0]]

		if (modulesName):
			modulesName.sort()

			ret = []

			for name in modulesName:
				formFactor = info_dict['info'][name + "_ffactor"]['value']
				partNumber = info_dict['info'][name + "_part"]['value']
				serial = info_dict['info'][name + "_serial"]['value']
				size = info_dict['info'][name + "_size"]['id']
				speed = info_dict['info'][name + "_speed"]['value']
				type = info_dict['info'][name + "_type"]['value']
				vendor = info_dict['info'][name + "_vendor"]['value']

				ret.append(InfoResMemoryModule(name, formFactor, partNumber, serial, size, speed, type, vendor))

		return ret

	@property
	def model(self):
		if (self.__info_dict['model']):
			return self.__info_dict['model']['value']
		else:
			return None

	@property
	def vendor(self):
		if (self.__info_dict['vendor']):
			return self.__info_dict['vendor']['value']
		else:
			return None

	def getMemoryController(self):
		return self.__memoryController

	def getMemoryModules(self):
		return self.__memoryModules

	def __str__(self):
		ret = "Model: %s\nVendor: %s" % (self.model, self.vendor)
		if (self.memoryController):
			ret = "%s\n%s" % (ret, self.memoryController.__str__())

		if (self.memoryModules):
			for mm in self.memoryModules:
				ret = "%s\n%s" % (ret, mm.__str__())

		return ret

	memoryController = property(getMemoryController, None, None, None)
	memoryModules = property(getMemoryModules, None, None, None)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		if (self.memoryController):
			infoList.append((u'Controlador de Memória', self.memoryController.getReportInfo()))
		for module in self.memoryModules:
			name, modinfo = module.getReportInfo()
			infoList.append((name, modinfo))
		return infoList

class InfoResMemoryModule:
	"""Classe auxiliar da biblioteca de Memória que define os atributos dos módulos de memória."""
	__name = None
	__vendor = None
	__type = None
	__size = None
	__speed = None
	__serial = None
	__formFactor = None
	__partNumber = None

	def __init__(self, name, formFactor, partNumber, serial, size, speed, type, vendor):
		self.__name = name
		self.__vendor = vendor
		self.__type = type
		self.__size = size
		self.__speed = speed
		self.__serial = serial
		self.__formFactor = formFactor
		self.__partNumber = partNumber

	def getName(self):
		return self.__name

	def getVendor(self):
		return self.__vendor

	def getType(self):
		return self.__type

	def getSize(self):
		return self.__size

	def getSpeed(self):
		return self.__speed

	def getSerial(self):
		return self.__serial

	def getFormFactor(self):
		return self.__formFactor

	def getPartNumber(self):
		return self.__partNumber

	def __str__(self):
		return "Module Name: %s\n\tVendor: %s\n\tType: %s\n\tSize: %s\n\tSpeed: %s\n\tSerial: %s\n\tForm Factor: %s\n\tPart #: %s" % (self.name, self.vendor, self.type, self.size, self.speed, self.serial, self.formFactor, self.partNumber)

	name = property(getName, None, None, None)
	vendor = property(getVendor, None, None, None)
	type = property(getType, None, None, None)
	size = property(getSize, None, None, None)
	speed = property(getSpeed, None, None, None)
	serial = property(getSerial, None, None, None)
	formFactor = property(getFormFactor, None, None, None)
	partNumber = property(getPartNumber, None, None, None)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Fabricante', self.vendor))
		infoList.append(('Modelo', self.formFactor))
		infoList.append(('Tipo', self.type))
		infoList.append(('Tamanho', str(self.size) + ' MB'))
		infoList.append(('Velocidade', self.speed))
		infoList.append((u'N° de série', self.serial))
		infoList.append((u'Código', self.partNumber))
		return u"Módulo de memória - %s"%self.name, infoList

class InfoResMemoryController:
	"""Classe auxiliar da biblioteca de Memória que define os atributos do controlador de memória."""
	__maxMemoryModuleSize = None
	__maxTotalMemorySize = None
	__memoryModuleVoltage = None
	__supportedSpeeds = None
	__supportedTypes = None

	def __init__(self, maxMemoryModuleSize, maxTotalMemorySize, memoryModuleVoltage, supportedSpeeds, supportedTypes):
		self.__maxMemoryModuleSize = maxMemoryModuleSize
		self.__maxTotalMemorySize = maxTotalMemorySize
		self.__memoryModuleVoltage = memoryModuleVoltage
		self.__supportedSpeeds = supportedSpeeds
		self.__supportedTypes = supportedTypes

	def getMaxMemoryModuleSize(self):
		return self.__maxMemoryModuleSize

	def getMaxTotalMemorySize(self):
		return self.__maxTotalMemorySize

	def getMemoryModuleVoltage(self):
		return self.__memoryModuleVoltage

	def getSupportedSpeeds(self):
		return self.__supportedSpeeds

	def getSupportedTypes(self):
		return self.__supportedTypes

	def __str__(self):
		return "Max. Memory Module Size: %s\nMax. Total Memory Size: %s\nMemory Module Voltage: %s\nSupported Speeds: %s\nSupported Types: %s" % (self.maxMemoryModuleSize, self.maxTotalMemorySize, self.memoryModuleVoltage, self.supportedSpeeds, self.supportedTypes)

	maxMemoryModuleSize = property(getMaxMemoryModuleSize, None, None, None)
	maxTotalMemorySize = property(getMaxTotalMemorySize, None, None, None)
	memoryModuleVoltage = property(getMemoryModuleVoltage, None, None, None)
	supportedSpeeds = property(getSupportedSpeeds, None, None, None)
	supportedTypes = property(getSupportedTypes, None, None, None)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append((u'Maior módulo suportado', str(self.maxMemoryModuleSize) + " MB"))
		infoList.append((u'Memória total máxima', str(self.maxTotalMemorySize) + " MB"))
		infoList.append(('Tipos suportados', ', '.join(self.supportedTypes)))
		infoList.append(('Velocidades suportadas', ', '.join(self.supportedSpeeds)))
		infoList.append((u'Tensão dos módulos', self.memoryModuleVoltage))
		return infoList

""""
{
	'status': 1,
	'info': {
		'mem_mod_volt': {'id': -1, 'value': '3.3 V', 'description': 'Memory Module Voltage (in V)'},
		'max_mem_mod_size': {'id': 1024, 'value': 'NULL', 'description': 'Maximum Memory Module Size (in MB)'},
		'sup_types': {'id': -1, 'value': 'SIMM|DIMM|SDRAM|', 'description': 'Supported Memory Types'},
		'max_total_mem_size': {'id': 4096, 'value': 'NULL', 'description': 'Maximum Total Memory Size (in MB)'},
		'sup_speeds': {'id': -1, 'value': '70 ns|60 ns|50 ns|', 'description': 'Supported Speeds'},

		'DIMM0_part': {'id': -1, 'value': 'PartNum0', 'description': 'Module @ DIMM0 part number'},
		'DIMM0_size': {'id': 512, 'value': 'NULL', 'description': 'Module @ DIMM0 size (in MB)'},
		'DIMM0_type': {'id': -1, 'value': 'SDRAM', 'description': 'Module @ DIMM0 type'},
		'DIMM0_ffactor': {'id': -1, 'value': 'DIMM', 'description': 'Module @ DIMM0 form factor'},
		'DIMM0_speed': {'id': 0, 'value': 'Unknown', 'description': 'Module @ DIMM0 speed'},
		'DIMM0_serial': {'id': -1, 'value': 'SerNum0', 'description': 'Module @ DIMM0 serial number'},
		'DIMM0_vendor': {'id': -1, 'value': 'Manufacturer0', 'description': 'Module @ DIMM0 vendor'},

		'DIMM1_type': {'id': -1, 'value': 'SDRAM', 'description': 'Module @ DIMM1 type'}
		'DIMM1_vendor': {'id': -1, 'value': 'Manufacturer1', 'description': 'Module @ DIMM1 vendor'},
		'DIMM1_ffactor': {'id': -1, 'value': 'DIMM', 'description': 'Module @ DIMM1 form factor'},
		'DIMM1_size': {'id': 256, 'value': 'NULL', 'description': 'Module @ DIMM1 size (in MB)'},
		'DIMM1_speed': {'id': 0, 'value': 'Unknown', 'description': 'Module @ DIMM1 speed'},
		'DIMM1_part': {'id': -1, 'value': 'PartNum1', 'description': 'Module @ DIMM1 part number'},
		'DIMM1_serial': {'id': -1, 'value': 'SerNum1', 'description': 'Module @ DIMM1 serial number'},

		'DIMM2_type': {'id': -1, 'value': 'SDRAM', 'description': 'Module @ DIMM2 type'},
		'DIMM2_vendor': {'id': -1, 'value': 'Manufacturer2', 'description': 'Module @ DIMM2 vendor'},
		'DIMM2_serial': {'id': -1, 'value': 'SerNum2', 'description': 'Module @ DIMM2 serial number'},
		'DIMM2_part': {'id': -1, 'value': 'PartNum2', 'description': 'Module @ DIMM2 part number'},
		'DIMM2_ffactor': {'id': -1, 'value': 'DIMM', 'description': 'Module @ DIMM2 form factor'},
		'DIMM2_speed': {'id': 0, 'value': 'Unknown', 'description': 'Module @ DIMM2 speed'},
		'DIMM2_size': {'id': 256, 'value': 'NULL', 'description': 'Module @ DIMM2 size (in MB)'},

		'DIMM3_vendor': {'id': -1, 'value': 'Manufacturer3', 'description': 'Module @ DIMM3 vendor'},
		'DIMM3_type': {'id': -1, 'value': 'SDRAM', 'description': 'Module @ DIMM3 type'},
		'DIMM3_size': {'id': 128, 'value': 'NULL', 'description': 'Module @ DIMM3 size (in MB)'},
		'DIMM3_part': {'id': -1, 'value': 'PartNum3', 'description': 'Module @ DIMM3 part number'},
		'DIMM3_ffactor': {'id': -1, 'value': 'DIMM', 'description': 'Module @ DIMM3 form factor'},
		'DIMM3_serial': {'id': -1, 'value': 'SerNum3', 'description': 'Module @ DIMM3 serial number'},
		'DIMM3_speed': {'id': 0, 'value': 'Unknown', 'description': 'Module @ DIMM3 speed'},
	},
	'model': None,
	'libName': 'memory',
	'vendor': None
}
"""