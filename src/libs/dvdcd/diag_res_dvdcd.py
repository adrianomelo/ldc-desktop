# -*- coding: utf-8 -*-

class DiagResDVDCD:
	"""Classe utilizada para representar o resultado de um diagnóstico de DVD/CD"""

	__burnerType = None
	__testedMediaType = None
	__burnSuccess = False
	__readSuccess = False
	__deviceFile = None

	def __init__(self, diagDict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__deviceFile = diagDict['deviceFile']
		self.__burnerType = diagDict['burnerType']
		self.__testedMediaType = diagDict['testedMediaType']
		self.__burnSuccess = diagDict['burnSuccess']
		self.__readSuccess = diagDict['readSuccess']

	def getBurnerType(self):
		"""Retorna o tipo de gravador."""
		return self.__burnerType

	burnerType = property(getBurnerType, None, None, None)

	def getTestedMediaType(self):
		"""Retorna o tipo de mídia testada."""
		return self.__testedMediaType

	testedMediaType = property(getTestedMediaType, None, None, None)

	def getBurnSuccess(self):
		"""Retorna um bool indicando se foi gravado com sucesso."""
		return self.__burnSuccess

	burnSuccess = property(getBurnSuccess, None, None, None)

	def getReadSucess(self):
		"""Retorna um bool indicando se o teste de leitura foi ok."""
		return self.__readSuccess

	readSuccess = property(getReadSucess, None, None, None)

	def getDeviceFile(self):
		"""Retorna o device file do dispositivo."""
		return self.__deviceFile

	deviceFile = property(getDeviceFile, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Device file: %s\nBurner type: %s\nUsed media: %s\nBurned: %s\nReaded: %s" % (self.deviceFile, self.burnerType, self.testedMediaType, self.burnSuccess, self.readSucess)

	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		burnTest = None
		burnDetails = None

		if (self.burnerType == None):
			burnTest = u"Não realizado."
			burnDetails = u"O teste não foi realizado pois esse dispositivo não é um gravador."
		elif (self.testedMediaType == None):
			burnTest = u"Não realizado."
			burnDetails = u"O teste foi cancelado pelo usuário."
		elif (not self.burnSuccess):
			burnTest = u"Falha na gravação."
			burnDetails = u"Houve um erro ao tentar gravar um arquivo na mídia. Isso pode indicar uma falha de hardware ou um defeito na mídia. Em caso de falha de hardware, o drive de CD/DVD deve ser substituído."
		elif (not self.readSuccess):
			burnTest = u"Falha na leitura."
			burnDetails = u"Houve um erro ao ler o arquivo que foi gravado. Isso pode indicar uma falha de hardware, um erro na gravação ou um defeito na mídia. Caso suspeite de mídia defeituosa, o teste pode ser executado novamente, com outra mídia, para verificar essa possibilidade. A falha de gravação não decorrente de mídia defeituosa pode indicar um problema no hardware, sendo necessária sua substituição."
		elif (self.burnSuccess and self.readSuccess):
			burnTest = u"Teste realizado com sucesso."
			rewritable = "R"
			if (self.testedMediaType['Rewritable']):
				rewritable = "RW"
			burnDetails = u"A gravação e leitura foram executadas e verificadas com sucesso, utilizando uma mídia do tipo %s-%s" % (self.testedMediaType['Type'], rewritable)

		diagList.append((u'Teste de gravação', burnTest))
		diagList.append((u'Detalhes do teste de gravação', burnDetails))

		return diagList
