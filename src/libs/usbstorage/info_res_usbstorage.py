# -*- coding: utf-8 -*-

from libs.core.attrproperty import attrproperty

class InfoResUsbstorage(object):
	"""Classe básica da biblioteca de armazenamento usb que define os atributos da parte informativa."""

	__info_dict = None
	__part_list = None

	def __init__(self, info_dict):
		"""Construtor

		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict
		self.__fill_part()


	@attrproperty
	def model(self, type):
		"""Retorna o modelo

		Parâmetro:
		type -- pode ser 'id' ou 'value', retornará o 'id' ou o 'value' do modelo
		"""
		if (type is 'id') or (type is 'value'):
			return self.__info_dict['model'][type]
		else:
#			print "ERROR: The variable '%s' was not defined, it should be 'id' or 'value'.!!!"%type
			pass

	@attrproperty
	def vendor(self, type):
		"""Retorna o modelo

		Parâmetro:
		type -- pode ser 'id' ou 'value', retornará o 'id' ou o 'value' do fabricante
		"""
		if (type is 'id') or (type is 'value'):
			return self.__info_dict['vendor'][type]
		else:
#			print "ERROR: The variable '%s' was not defined, it should be 'id' or 'value'.!!!"%type
			pass

	@property
	def device_file(self):
		"""Retorna o device file."""
		return self.__info_dict['info']['device_file']['value']

	@property
	def speed(self):
		"""Retorna um int que indica a velocidade."""
		try:
			return self.__info_dict['info']['speed']['id']
		except:
			return 0

	@property
	def driver(self):
		"""Retorna os drivers."""
		return self.__info_dict['info']['driver']['value']

	@property
	def partition_list(self):
		"""Retorna uma lista de DiagResUsbstoragePartition."""
		return self.__part_list

	@property
	def size (self):
		"""Retorna um int que indica o tamanho do dispositivo."""
		return self.__info_dict['info']['Size']['id']

	def __fill_part(self):
		"""Para todas as partições cria um 'DiagResUsbstoragePartition' com as suas informações.
		Adiciona cada um no atributo '__part_list'
		"""
		partitionsNumber = []

		for key, value in self.__info_dict['info'].items():
			if key.__contains__("partition_") and key.__contains__("size") and not key.__contains__("fileType"):
				partitionsNumber.append(key.split("_")[1])

		partitionsNumber.sort()

		if (partitionsNumber):
			self.__part_list = []
			for name in partitionsNumber:
				size = self.__info_dict['info']["partition_" + name + "_size"]['value']
				filesystem = self.__info_dict['info']["partition_" + name + "_fileType"]['value']
				self.__part_list.append(InfoResUsbstoragePartition(name, self.device_file + name, size, filesystem))

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do dispositivo."""
		ret = "Model: %s\nVendor: %s\nDevice File: %s\nSpeed: %s Mbps\nDrivers: %s\nSize: %s GB"% (self.model.value, self.vendor.value, self.device_file, self.speed, self.driver, self.size)
		for part in self.partition_list:
			ret = "%s\n%s" % (ret, str(part))
		return ret

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model.value))
		infoList.append(('Fabricante', self.vendor.value))
		infoList.append(('Dispositivo', self.device_file))
		infoList.append(('Drivers', self.driver))
		infoList.append(('Tamanho', str(self.size) + " GB"))
		infoList.append(('Velocidade', str(self.speed) + ' Mbps'))
		if self.partition_list:
			for part in self.partition_list:
				name, partInfoList = part.getReportInfo()
				infoList.append((name, partInfoList))
		return infoList

class InfoResUsbstoragePartition:
	"""Classe auxiliar de 'DiagResUsbstorage' que define as informações de uma partição."""

	__id = None
	__device_file = None
	__size = None
	__filesystem = None

	def __init__(self, id, deviceFile, size, filesystem):
		"""Construtor

		Parâmetro:
		id -- número da partição
		deviceFile -- device file do dispositivo
		size -- int que indica o tamanho
		filesystem -- string que indica o tipo de sistema de arquivo
		"""
		self.__id = id
		self.__device_file = deviceFile
		self.setSize(size)
		self.__filesystem = filesystem

	def setSize(self, value):
		"""Atualiza o atributo '__size' com uma string formatada com o tamanho e o tipo (Ex. '2 GB')
		Parâmetro: value -- valor do tamanho em int ou string formatada com o tamanho e tipo
		"""
		if (isinstance(value, str)):
			size_list = value.split('MB')
			if size_list:
				self.__size = size_list[0]
				if (self.__size.isdigit()):
					size_int = int(self.__size)
					if ((size_int/1000) < 1):
						self.__size = str(size_int) + " MB"
					else:
						self.__size = str(size_int/1000) + " GB"
				else:
					self.__size = value
			else:
				self.__size = value


	def getId(self):
		"""Retorna o id da partição"""
		return self.__id

	def getDeviceFile(self):
		"""Retorna o device file do dispositivo"""
		return self.__device_file

	def getSize(self):
		"""Retorna uma string contendo o tamanho e o tipo"""
		return self.__size

	def getFilesystem(self):
		"""Retorna o tipo de sistema de arquivo da partição."""
		return self.__filesystem

	id = property(getId, None, None, None)
	device_file = property(getDeviceFile, None, None, None)
	size = property(getSize, setSize, None, None)
	filesystem = property(getFilesystem, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações de uma partição."""
		return "Partition %s\n\tdevice file: %s\n\tSize:: %s\n\tFilesystem: %s" % (self.id, self.device_file, self.size, self.filesystem)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Dispositivo ', self.device_file))
		infoList.append(('Tamanho', self.size))
		infoList.append(('Sistema de arquivo', self.filesystem))
		return u"Partição - %s"%self.id, infoList


"""
[
	{
		'status': 1,
		'info':
		{
			'device_file': {'id': -1, 'value': '/dev/sdb', 'description': 'Device File'},
			'speed': {'id': 480, 'value': 'NULL', 'description': 'Speed (in Mbps)'},
			'driver': {'id': -1, 'value': 'usb-storage; sd', 'description': 'Driver'},
			'partition_fileType': {'id': 1, 'value': 'fat16', 'description': 'Parti\xe7\xe3o e Sistema de arquivos'},
			'Size': {'id': 2, 'value': 'NULL', 'description': 'Size (in GB)'}
		},
		'model': {'id': 202243, 'value': 'DataTraveler 2.0', 'description': 'Model'},
		'libName': 'pendrive',
		'vendor': {'id': 198993, 'value': 'Kingston', 'description': 'Vendor'}
	}
]
"""
