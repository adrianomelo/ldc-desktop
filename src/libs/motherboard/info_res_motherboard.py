# -*- coding: utf-8 -*-

from libs.core.attrproperty import attrproperty

class InfoResMotherboard(object):
	"""Classe básica da biblioteca da placa mãe que define os atributos da parte informativa."""

	__info_dict = None #Dicionário com as informações da etapa de identificação

	def __init__(self, info_dict):
		"""Construtor

		Parâmetro:
		info_dict -- dicionário com as informações da etapa de identificação
		"""
		self.__info_dict = info_dict

	@property
	def model(self):
		"""Retorna o modelo"""
		return self.__info_dict['model']['value']

	@property
	def vendor(self):
		"""Retorna o fabricante"""
		return self.__info_dict['vendor']['value']

	@property
	def version(self):
		"""Retorna a versão"""
		try:
			s = self.__info_dict['info']['version']['value']
		except:
			s = "Unknown"
		return s

	@property
	def serial(self):
		"""Retorna o serial"""
		try:
			s = self.__info_dict['info']['serial']['value']
		except:
			s = "Unknown"
		return s

	@property
	def bios_vendor(self):
		"""Retorna o fabricante da BIOS"""
		return self.__info_dict['info']['bios_vendor']['value']

	@property
	def bios_date(self):
		"""Retorna a data da BIOS"""
		return self.__info_dict['info']['bios_date']['value']

	@property
	def bios_version(self):
		"""Retorna a versão da BIOS"""
		return self.__info_dict['info']['bios_version']['value']

	@attrproperty
	def chipset_device(self, type):
		"""Retorna o modelo do chipset

		Parâmetro:
		type -- pode ser 'id' ou 'value', retornará o 'id' ou o 'value' do modelo do chipset
		"""
		if (type is 'id') or (type is 'value'):
			return self.__info_dict['info']['chipset_device'][type]
		else:
#			print "DEBUG: The variable '%s' was not defined, it should be 'id' or 'value'.!!!"%type
			pass

	@attrproperty
	def chipset_vendor(self, type):
		"""Retorna o modelo do chipset

		Parâmetro:
		type -- pode ser 'id' ou 'value', retornará o 'id' ou o 'value' do modelo do chipset
		"""
		if (type is 'id') or (type is 'value'):
			return self.__info_dict['info']['chipset_vendor'][type]
#		else:
##			print "ERROR: The variable '%s' was not defined, it should be 'id' or 'value'.!!!"%type
#			pass

	@property
	def chipset_driver_modules(self):
		"""Retorna os driver modules em forma de string separados por ';'
		"""
		return self.__info_dict['info']['chipset_driver_modules']['value']

	def __str__(self):
		"""Retorna uma string formatada contendo todas as informações da placa mãe
		"""
		return "Model: %s\nVendor: %s\nVersion: %s\nSerial: %s\nBios Vendor: %s\nBios Date: %s\nBios Version: %s\nChipset Device (ID, Name): (%s, %s)\nChipset Vendor (ID, Name): (%s, %s)\nChipset Driver Modules: %s" % (self.model, self.vendor, self.version, self.serial, self.bios_vendor, self.bios_date, self.bios_version, self.chipset_device.id, self.chipset_device.value, self.chipset_vendor.id, self.chipset_vendor.value, self.chipset_driver_modules)

	def getReportInfo(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		infoList = []
		infoList.append(('Modelo', self.model))
		infoList.append(('Fabricante', self.vendor))
		infoList.append((u'Versão', self.version))
		if not 'SERIAL' in self.serial.upper():
			infoList.append(('Serial', self.serial))

		biosList = []
		biosList.append(('Fabricante', self.bios_vendor))
		biosList.append(('Data', self.bios_date))
		biosList.append((u'Versão', self.bios_version))
		infoList.append(('Bios', biosList))

		chipsetList = []
		chipsetList.append(('Modelo', self.chipset_device.value))
		chipsetList.append(('Fabricante', self.chipset_vendor.value))
		chipsetList.append(('Driver Modules', self.chipset_driver_modules))
		infoList.append(('Chipset', chipsetList))
		return infoList


		"""
		[{'status': 1,

		'info': {
			-- 'bios_vendor': {'id': -1, 'value': 'Itautec ST 2141,LTD', 'description': 'BIOS - Vendor'},
			-- 'version': {'id': -1, 'value': 'PCB 1.1', 'description': 'Version'},
			-- 'bios_date': {'id': -1, 'value': '05/19/2006', 'description': 'BIOS - Date'},
			-- 'chipset_device': {'id': 67169, 'value': '661FX/M661FX/M661MX Host', 'description': 'Chipset - Device'},
			-- 'bios_version': {'id': -1, 'value': '6.00 PG', 'description': 'BIOS - Version'},
			-- 'chipset_vendor': {'id': 69689, 'value': 'Silicon Integrated Systems Corp.', 'description': 'Chipset - Vendor'},
			-- 'serial': {'id': -1, 'value': 'Serial', 'description': 'Serial'},
			'chipset_driver_modules': {'id': -1, 'value': 'sis_agp', 'description': 'Chipset - Driver Modules'}
		},

		-- 'model': {'id': -1, 'value': 'ST 2141', 'description': 'Model'},
		'libName': 'motherboard',
		-- 'vendor': {'id': -1, 'value': 'Itautec Philco S.A.', 'description': 'Vendor'}}]

		"""




