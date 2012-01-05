# -*- coding: utf-8 -*-

"""
Name: harddisk
Status: -1
----INFO----
	device_file = /dev/sdb (-1) : Logical name
	partition_size = 105GB (1) : Partição - Tamanho
	partition_file_type = ext3 (1) : Partição - Sistema de arquivos
	partition_size = 2147MB (2) : Partição - Tamanho
	partition_file_type = linux-swap (2) : Partição - Sistema de arquivos
	partition_size = 16.1GB (3) : Partição - Tamanho
	partition_file_type = ext3 (3) : Partição - Sistema de arquivos
	partition_free_size = 13G (1) : Partição - Tamanho Livre
	partition_mounting_point = /mnt/sdb1 (1) : Partição - Ponto de montagem
	partition_free_size = 1.3G (3) : Partição - Tamanho Livre
	partition_mounting_point = /mnt/sdb3 (3) : Partição - Ponto de montagem
	temperature = NULL (48) : Temperatura
	overall_health_test = NULL (1) : Overall-health self-assessment test

Name: harddisk
Status: -1
----INFO----
	device_file = /dev/sda (-1) : Logical name
	partition_size = 1999MB (1) : Partição - Tamanho
	partition_file_type = linux-swap (1) : Partição - Sistema de arquivos
	partition_size = 18.5GB (2) : Partição - Tamanho
	partition_file_type = ext3 (2) : Partição - Sistema de arquivos
	partition_size = 102GB (3) : Partição - Tamanho
	partition_file_type = ext3 (3) : Partição - Sistema de arquivos
	partition_free_size = 9.6G (3) : Partição - Tamanho Livre
	partition_mounting_point = /home (3) : Partição - Ponto de montagem
	temperature = NULL (49) : Temperatura
	overall_health_test = NULL (1) : Overall-health self-assessment test
"""


class DiagResHarddisk:
	"""Classe básica da biblioteca de HD que define os resultados da parte de diagnóstico."""
	
	__diag_dict = None
	
	__deviceFile = None
	__temperature = None
	__overallHealthTest = None
	
	__partitions = None

	def __init__(self, diag_dict):
		"""Construtor
		
		Parâmetro:
		diag_dict -- dicionário com as informações da etapa de diagnóstico
		"""
		self.__diag_dict = diag_dict
		
		self.__deviceFile = diag_dict['info']['device_file']['value']
		self.__temperature = diag_dict['info']['temperature']['id']
		self.__overallHealthTest = bool(diag_dict['info']['overall_health_test']['id'])
		
		self.__partitions = self.__loadPartitions(diag_dict)

	def __loadPartitions(self, diag_dict):
		"""Para todas as partições cria um DiagResHarddiskPartition com as suas informações.
		Retorna uma lista de 'DiagResHarddiskPartition'
		"""
		ret = None
		partitionsNumber = None
		
		for key, value in diag_dict['info'].items():
			if key.__contains__("part_") and key.__contains__("size") and not key.__contains__("free"):
				if (partitionsNumber):
					partitionsNumber.append(key.split("_")[1])
				else:
					partitionsNumber = [key.split("_")[1]]
		
		partitionsNumber.sort()
		
		if (partitionsNumber):
			ret = []

			for name in partitionsNumber:
				size = diag_dict['info']["part_" + name + "_size"]['value']
				filesystem = diag_dict['info']["part_" + name + "_filesystem"]['value']

				if (diag_dict['info'].has_key("part_" + name + "_mounting_point")):
					mountingPoint = diag_dict['info']["part_" + name + "_mounting_point"]['value']
				else:
					mountingPoint = 'Unknown'
				
				if (diag_dict['info'].has_key("part_" + name + "_free_size")):
					freeSize = diag_dict['info']["part_" + name + "_free_size"]['value']
				else:
					freeSize = 'Unknown'
				
				ret.append(DiagResHarddiskPartition(self.deviceFile + name, size, filesystem, freeSize, mountingPoint))
		
		return ret

	def getDeviceFile(self):
		"""Retorna o divice file do HD"""
		return self.__deviceFile
	
	def getTemperature(self):
		"""Retorna um int com temperatura do HD"""
		return self.__temperature
	
	def getOverallHealthTest(self):
		"""Retorna o 1 ou 0 dependendo do resultado do teste."""
		return self.__overallHealthTest
	
	def getPartitions(self):
		"""Retorna a lista com as partições do tipo 'DiagResHarddiskPartition'."""
		return self.__partitions

	deviceFile = property(getDeviceFile, None, None, None)
	temperature = property(getTemperature, None, None, None)
	overallHealthTest = property(getOverallHealthTest, None, None, None)
	partitions = property(getPartitions, None, None, None)
		
	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações do diagnóstico de HD."""
		ret = "Device file: %s\n\tTemperature: %s\n\tOverall health test: %s" % (self.deviceFile, self.temperature, self.overallHealthTest)
		
		if (self.partitions):
			for part in self.partitions:
				ret = "%s\n%s" % (ret, part.__str__())
		
		return ret
	
	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append((u'Temperatura', str(self.temperature) + u"° C"))
		overallHealth = "Falhou"
		if self.overallHealthTest:
			overallHealth = "OK"            
		diagList.append(('SMART Overall Health Test', overallHealth))
		if (self.partitions):
			for part in self.partitions:
				name, partInfo = part.getReportDiag()
				diagList.append((name, partInfo))
		return diagList

class DiagResHarddiskPartition:
	"""Classe auxiliar de 'DiagResHarddisk' que define as informações de uma partição."""
	
	__deviceFile = None
	__size = None
	__filesystem = None
	__freeSize = None
	__mountingPoint = None
	
	def __init__(self, deviceFile, size, filesystem, freeSize, mountingPoint):
		"""Construtor
		
		Parâmetro:
		deviceFile -- string com o device file do dispositivo
		size -- int que indica o tamanho da partição
		filesystem -- string que indica o tipo de sistema de arquivo
		freeSize -- int que indica o tamanho livre da partição
		mountingPoint -- string que mostra o ponto de montagem
		"""
		self.__deviceFile = deviceFile
		self.__size = size
		self.__filesystem = filesystem
		self.__freeSize = freeSize
		self.__mountingPoint = mountingPoint

	def getDeviceFile(self):
		"""Retorna o device file."""
		return self.__deviceFile

	def getSize(self):
		"""Retorna um int com tamanho da partição."""
		return self.__size
	
	def getFilesystem(self):
		"""Retorna o tipo de sistema de arquivo."""
		return self.__filesystem
	
	def getFreeSize(self):
		"""Retorna um int com tamanho livre da partição."""
		return self.__freeSize
	
	def getMountingPoint(self):
		"""Retorna o ponto de montagem da partição."""
		return self.__mountingPoint
	
	deviceFile = property(getDeviceFile, None, None, None)
	size = property(getSize, None, None, None)
	filesystem = property(getFilesystem, None, None, None)
	freeSize = property(getFreeSize, None, None, None)
	mountingPoint = property(getMountingPoint, None, None, None)
   
	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações de uma partição."""
		
		return "Partition device file: %s\n\tSize:: %s\n\tFree size: %s\n\tFilesystem: %s\n\tMounting point: %s" % (self.deviceFile, self.size, self.freeSize, self.filesystem, self.mountingPoint)
	
	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		diagList.append(('Dispositivo', self.deviceFile))
		diagList.append(('Sistema de Arquivos', self.filesystem))
		diagList.append(('Tamanho', self.size))
		diagList.append((u'Tamanho Disponível', self.freeSize))
		diagList.append(('Ponto de Montagem', self.mountingPoint))
		return 'Volume - %s'%self.deviceFile, diagList

   	