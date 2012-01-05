# -*- coding: utf-8 -*-

class DiagResWireless:
	"""Classe basica da biblioteca de wireless que define os resultados da parte de diagnostico."""

	__diag_dict = None

	__linkStatus = None
	__macAddress = None
	__ipAddress = None
	__netmask = None
	__gateway = None
	__dnsList = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict
		self.__linkStatus = diag_dict['info']['link_up']['id']
		self.__macAddress = diag_dict['info']['mac']['value'].upper()
		self.__ipAddress = diag_dict['info']['ip']['value']
		self.__netmask = diag_dict['info']['netmask']['value']
		self.__gateway = diag_dict['info']['gateway']['value']
		self.__dnsList = self.__fillDnsList(diag_dict['info'])

	def __fillDnsList(self, diag_info):
		result_list = []
		for key in diag_info.keys():
			if ('dns_server' in key):
				result_list.append(diag_info[key]['value'])
		return result_list

	def getLinkStatus(self):
		"""Retorna o se o link está up (1 ou 0)."""
		return self.__linkStatus

	def getMacAddress(self):
		"""Retorna o endereço mac."""
		return self.__macAddress

	def getIpAddress(self):
		"""Retorna o endereço de ip."""
		return self.__ipAddress

	def getNetmask(self):
		"""Retorna a mascara de rede."""
		return self.__netmask

	def getGateway(self):
		"""Retorna o default gateway."""
		return self.__gateway

	def getDnsList(self):
		"""Retorna a lista de dns servers."""
		return self.__dnsList

	linkStatus = property(getLinkStatus, None, None, None)
	macAddress = property(getMacAddress, None, None, None)
	ipAddress = property(getIpAddress, None, None, None)
	netmask = property(getNetmask, None, None, None)
	gateway = property(getGateway, None, None, None)
	dnsList = property(getDnsList, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Link status: %s\nMAC address: %s\nIP Address: %s\nNetmask: %s\nGateway: %s\nDNS: %s" % (self.linkStatus, self.macAddress, self.ipAddress, self.netmask, self.gateway, self.dnsList)

	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		linkStatus = u"Não"
		if (self.linkStatus):
			if (self.ipAddress != None and self.ipAddress != 'None'):
				linkStatus = "Sim"
			else:
				linkStatus = ''
		diagList.append(('Interface configurada', linkStatus))
		diagList.append(('IP', self.ipAddress))
		diagList.append((u'Máscara de rede', self.netmask))
		diagList.append(('MAC', self.macAddress))
		diagList.append(('Gateway', self.gateway))
		diagList.append(('Servidores DNS', ", ".join(self.dnsList)))
		return diagList
