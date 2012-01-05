# -*- coding: utf-8 -*-

class InfoResUsb(object):
	"""Classe básica da biblioteca de USB que define os atributos da parte informativa."""
	__info_dict = None

	__usb_total = None
	__low_speed_total = None
	__full_speed_total = None
	__high_speed_total = None
	__ohci_total = None
	__uhci_total = None
	__ehci_total = None

	def __init__(self, info_dict):
		"""Construtor

		Parametro:
		info_dict -- dicionario com as informacoes da etapa de identificacao.
		"""
		self.__info_dict = info_dict

		self.__usb_total = info_dict['info']['usb_total']['id']
		self.__low_speed_total = info_dict['info']['low_speed_total']['id']
		self.__full_speed_total = info_dict['info']['full_speed_total']['id']
		self.__high_speed_total = info_dict['info']['high_speed_total']['id']
		self.__ohci_total = info_dict['info']['ohci_total']['id']
		self.__uhci_total = info_dict['info']['uhci_total']['id']
		self.__ehci_total = info_dict['info']['ehci_total']['id']

	def getUsb_total(self):
		"""Retorna número total de hubs USB."""
		return self.__usb_total

	def getLow_speed_total(self):
		"""Retorna número total de hubs USB low speed."""
		return self.__low_speed_total

	def getFull_speed_total(self):
		"""Retorna número total de hubs USB full speed."""
		return self.__full_speed_total

	def getHigh_speed_total(self):
		"""Retorna número total de hubs USB high speed."""
		return self.__high_speed_total

	def getOhci_total(self):
		"""Retorna o número de hubs USB usando OHCI."""
		return self.__ohci_total

	def getUhci_total(self):
	    """Retorna o número de hubs USB usando UHCI."""
	    return self.__uhci_total

	def getEhci_total(self):
		"""Retorna o número de hubs USB usando EHCI."""
		return self.__ehci_total

	usb_total = property(getUsb_total, None, None, None)
	low_speed_total = property(getLow_speed_total, None, None, None)
	full_speed_total = property(getFull_speed_total, None, None, None)
	high_speed_total = property(getHigh_speed_total, None, None, None)
	ohci_total = property(getOhci_total, None, None, None)
	uhci_total = property(getUhci_total, None, None, None)
	ehci_total = property(getEhci_total, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informacoes do dispositivo"""
		return "USB Total: %i\n1.0: %i\n1.1: %i\n2.0: %i\nOHCI: %i\nUHCI: %i\nEHCI: %i" % (self.usb_total, self.low_speed_total, self.full_speed_total, self.high_speed_total, self.ohci_total, self.uhci_total, self.ehci_total)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append((u'Número de HUBs USB', str(self.usb_total)))
		infoList.append(('1.0 - Low Speed', str(self.low_speed_total)))
		infoList.append(('1.1 - Full Speed', str(self.full_speed_total)))
		infoList.append(('2.0 - Hi Speed', str(self.high_speed_total)))
		hostList = [('OHCI', str(self.ohci_total)), ('UHCI', str(self.uhci_total)), ('EHCI', str(self.ehci_total))]
		infoList.append(('Host Controller Interfaces', hostList))
		return infoList
