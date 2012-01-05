# -*- coding: utf-8 -*-

class InfoResProcessor(object):
	"""Classe básica da biblioteca de processador que define os atributos da parte informativa."""
	__info_dict = None
	__caches_list = None

	def __init__(self, info_dict):
		"""Construtor

		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict
		self.__caches_list = self.__loadCaches(info_dict)

	def getModel(self):
		"""Retorna o modelo."""
		return self.__info_dict['model']['value']

	def getVendor(self):
		"""Retorna o fabricante."""
		return self.__info_dict['vendor']['value']

	def getClock(self):
		"""Retorna um int que indica o clock."""
		return self.__info_dict['info']['clock']['id']

	def getFsb(self):
		"""Retorna um int que indica o FSB."""
		return self.__info_dict['info']['fsb_clock']['id']

	def getVoltage(self):
		"""Retorna a voltagem."""
		return self.__info_dict['info']['voltage']['value']

	def getSocketType(self):
		"""Retorna o tipo de socket."""
		return self.__info_dict['info']['socket_type']['value']

	def getNumberOfCores(self):
		"""Retorna o número de núcleos."""
		return self.__info_dict['info']['n_cores']['id']

	def getStartAddress(self):
		"""Retorna o endereço do início."""
		return self.__info_dict['info']['start_addr']['value']

	def getEndAddress(self):
		"""Retorna o endereço do fim."""
		return self.__info_dict['info']['end_addr']['value']

	def getFeatures(self):
		"""Retorna as features do processador na forma de lista"""
		return self.__info_dict['info']['features']['value'].split("|")

	def getCaches_list(self):
		"""Retorna a lista de 'InfoResProcessorCache'"""
		return self.__caches_list

	startAddress = property(getStartAddress, None, None, None)
	endAddress = property(getEndAddress, None, None, None)
	model = property(getModel, None, None, None)
	vendor = property(getVendor, None, None, None)
	clock = property(getClock, None, None, None)
	fsb = property(getFsb, None, None, None)
	voltage = property(getVoltage, None, None, None)
	socketType = property(getSocketType, None, None, None)
	caches_list = property(getCaches_list, None, None, None)
	numberOfCores = property(getNumberOfCores, None, None, None)
	features = property(getFeatures, None, None, None)

	def __loadCaches(self, info_dict):
		"""Para todas as caches cria um 'InfoResProcessorCache' com as suas informações.
		Retorna uma lista de 'InfoResProcessorCache'
		"""
		ret = None
		cachesName = None

		for key, value in info_dict['info'].items():
			if value['description'].__contains__("Cache") and value['description'].__contains__("size"):
				if (cachesName):
					cachesName.append(key.split("_siz")[0])
				else:
					cachesName = [key.split("_siz")[0]]

		cachesName.sort()

		if (cachesName):
			ret = []
			for name in cachesName:
				associativity = info_dict['info'][name + "_associativity"]['value']
				size = info_dict['info'][name + "_size"]['id']
				supportedSRAMTypes = info_dict['info'][name + "_sup_sram_types"]['value'].split("|")
				supportedSRAMTypes.pop(-1)
				operationMode = info_dict['info'][name + "_opmode"]['value']
				errorCorrectionType = info_dict['info'][name + "_err_correction_type"]['value']

				ret.append(InfoResProcessorCache(name, associativity, size, supportedSRAMTypes, operationMode, errorCorrectionType))

		return ret

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do processador."""

		ret = "Model: %s\n\tVendor: %s\n\tClock: %s\n\tFSB: %s\n\tNo Cores: %s\n\tVoltage: %s\n\tSocket Type: %s\n\tFeatures: %s" % (self.model, self.vendor, self.clock, self.fsb, self.numberOfCores, self.voltage, self.socketType, self.features)
		for cache in self.__caches_list:
			ret = "%s\n%s" % (ret, cache.__str__())

		return ret

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model))
		infoList.append(('Fabricante', self.vendor))
		infoList.append(('Clock', str(self.clock) + " MHz"))
		infoList.append(('Tipo de socket', self.socketType))
		infoList.append((u'Nº de núcleos', str(self.numberOfCores)))
		infoList.append(('Voltagem', self.voltage))
		infoList.append(('FSB', str(self.fsb) + " MHz"))
		infoList.append(('Features', ", ".join(self.features)))
		for cache in self.caches_list:
			name, cacheinfo = cache.getReportInfo()
			infoList.append((name, cacheinfo))
		return infoList

class InfoResProcessorCache(object):
	"""Classe auxiliar de 'InfoResProcessor' que define as informações de uma cache."""

	__name = None
	__associativity = None
	__size = None
	__supportedSRAMTypes = None
	__operationMode = None
	__errorCorrectionType = None

 	def __init__(self, name, associativity, size, supportedSRAMTypes, operationMode, errorCorrectionType):
		"""Construtor

		Parâmetros:
		name -- string com o nome da cache
		associativity -- string que indica o tipo de associatividade
		size -- int que indica o tamanho da cache
		supportedSRAMTypes -- string que indica o tipo de SRAM suportado
		operationMode -- string que indica o modo de operação
		errorCorrectionType -- string que mostra o tipo de correção de erro
		"""
		self.__name = name
		self.__associativity = associativity
		self.__size = size
		self.__supportedSRAMTypes = supportedSRAMTypes
		self.__operationMode = operationMode
		self.__errorCorrectionType = errorCorrectionType

	def getName(self):
		"""Retorna o nome da cache."""
		return self.__name

	def getAssociativity(self):
		"""Retorna o tipo de associatividade."""
		return self.__associativity

	def getSize(self):
		"""Retorna int que indica o tamanho da cache."""
		return self.__size

	def getSupportedSRAMTypes(self):
		"""Retorna o tipo de SRAM suportado."""
		return self.__supportedSRAMTypes

	def getOperationMode(self):
		"""Retorna o modo de operação."""
		return self.__operationMode

	def getErrorCorrectionType(self):
		"""Retorna o tipo de correção de erro."""
		return self.__errorCorrectionType

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações de uma cache."""
		return "Cache Name: %s\n\tAssociativity: %s\n\tSize: %s\n\tSupported SRAM Types: %s\n\tOperation Mode: %s\n\tError Correction Type: %s" % (self.name, self.associativity, self.size, self.supportedSRAMTypes, self.operationMode, self.errorCorrectionType)

	name = property(getName, None, None, None)
	associativity = property(getAssociativity, None, None, None)
	size = property(getSize, None, None, None)
	supportedSRAMTypes = property(getSupportedSRAMTypes, None, None, None)
	operationMode = property(getOperationMode, None, None, None)
	errorCorrectionType = property(getErrorCorrectionType, None, None, None)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Associatividade', self.associativity))
		infoList.append(('Size', str(self.size)+ " KB"))
		infoList.append((u'Modo de operação', self.operationMode))
		infoList.append((u'Tipos de SRAM suportados', ", ".join(self.supportedSRAMTypes)))
		infoList.append((u'Tipo de correção de erro', self.errorCorrectionType))
		return self.name, infoList


"""
	[
	{
		'status': 1,
		'info': {
		   'clock': {'id': 3066, 'value': 'NULL', 'description': 'Clock'},
			'n_cores': {'id': 2, 'value': 'NULL', 'description': '# de n\xfacleos'},
			'voltage': {'id': -1, 'value': '0.0 V', 'description': 'Voltage'},
			'socket_type': {'id': -1, 'value': 'Socket 775', 'description': 'Socket Type'},

			'Internal Cache_associtivity': {'id': -1, 'value': 'Unknown', 'description': 'Internal Cache associativity'},
			'Internal Cache_size': {'id': 32, 'value': 'NULL', 'description': 'Internal Cache size (in KB)'},
			'Internal Cache_sup_sram_types': {'id': -1, 'value': 'Synchronous|', 'description': 'Internal Cache supported SRAM types'}
			'Internal Cache_opmode': {'id': -1, 'value': 'Write Back', 'description': 'Internal Cache operational mode'},
			'Internal Cache_err_correction_type': {'id': -1, 'value': 'Unknown', 'description': 'Internal Cache error correction type'},

			'External Cache_associtivity': {'id': -1, 'value': 'Unknown', 'description': 'External Cache associativity'},
			'External Cache_size': {'id': 1024, 'value': 'NULL', 'description': 'External Cache size (in KB)'},
			'External Cache_sup_sram_types': {'id': -1, 'value': 'Synchronous|', 'description': 'External Cache supported SRAM types'},
			'External Cache_opmode': {'id': -1, 'value': 'Write Back', 'description': 'External Cache operational mode'},
			'External Cache_err_correction_type': {'id': -1, 'value': 'Unknown', 'description': 'External Cache error correction type'},
		  },

		'model': {'id': -1, 'value': 'Intel(R) Pentium(R) 4 CPU 3.06GHz', 'description': 'Model'},
		'libName': 'processor',
		'vendor': {'id': -1, 'value': 'GenuineIntel', 'description': 'Vendor'}
	},

	{
		'status': 1,
		'info': {
			'clock': {'id': 3066, 'value': 'NULL', 'description': 'Clock'},
			'n_cores': {'id': 2, 'value': 'NULL', 'description': '# de n\xfacleos'},
			'voltage': {'id': -1, 'value': '0.0 V', 'description': 'Voltage'},
			'socket_type': {'id': -1, 'value': 'Socket 775', 'description': 'Socket Type'},

			'Internal Cache_associtivity': {'id': -1, 'value': 'Unknown', 'description': 'Internal Cache associativity'},
			'Internal Cache_size': {'id': 32, 'value': 'NULL', 'description': 'Internal Cache size (in KB)'},
			'Internal Cache_sup_sram_types': {'id': -1, 'value': 'Synchronous|', 'description': 'Internal Cache supported SRAM types'}
			'Internal Cache_opmode': {'id': -1, 'value': 'Write Back', 'description': 'Internal Cache operational mode'},
			'Internal Cache_err_correction_type': {'id': -1, 'value': 'Unknown', 'description': 'Internal Cache error correction type'},

			'External Cache_associtivity': {'id': -1, 'value': 'Unknown', 'description': 'External Cache associativity'},
			'External Cache_size': {'id': 1024, 'value': 'NULL', 'description': 'External Cache size (in KB)'},
			'External Cache_sup_sram_types': {'id': -1, 'value': 'Synchronous|', 'description': 'External Cache supported SRAM types'},
			'External Cache_opmode': {'id': -1, 'value': 'Write Back', 'description': 'External Cache operational mode'},
			'External Cache_err_correction_type': {'id': -1, 'value': 'Unknown', 'description': 'External Cache error correction type'},

		},
		'model': {'id': -1, 'value': 'Intel(R) Pentium(R) 4 CPU 3.06GHz', 'description': 'Model'},
		'libName': 'processor',
		'vendor': {'id': -1, 'value': 'GenuineIntel', 'description': 'Vendor'}
	}
	]

	"""
