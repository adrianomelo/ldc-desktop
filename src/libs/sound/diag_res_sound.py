# -*- coding: utf-8 -*-

class DiagResSound:
	"""Classe basica da biblioteca que define os resultados da parte de diagnostico."""
	__diag_dict = None

	__alsaMute = None
	__alsaVolume = None

	def __init__(self, diag_dict):
		"""Construtor

		Parametro:
		diag_dict -- dicionario com as informacoes da etapa de diagnostico
		"""
		self.__diag_dict = diag_dict

		self.__alsaMute = diag_dict['info']['mute_unmute_test']['id']
		self.__alsaVolume = diag_dict['info']['volume_test']['id']

	def getAlsaMute(self):
		"""Retorna informação indicando se o teste de diagnóstico conseguiu alterar o estado do som para mudo/não-mudo."""
		return self.__alsaMute

	def getAlsaVolume(self):
		"""Retorna informação indicando se o teste de diagnóstico conseguiu alterar o volume do dispositivo de som."""
		return self.__alsaVolume

	alsaMute = property(getAlsaMute, None, None, None)
	alsaVolume = property(getAlsaVolume, None, None, None)

	def __str__(self):
		"""Retorna uma string formatada contendo as informacoes de diagnostico do dispositivo"""
		return "Alsa mutable: %s\nAlsa volume adjustable: %s" % (self.alsaMute, self.alsaVolume)

	def getReportDiag(self):
		"""Método que retorna as informações no formato de tuplas para o pdf"""
		diagList = []
		vol = u'Não passou'
		if self.alsaVolume:
			vol = 'Passou'
		diagList.append((u'Teste de aumentar/diminuir volume', vol))
		mute = u'Não passou'
		if self.alsaMute:
			mute = 'Passou'
		diagList.append((u'Teste de habilitar/desabilitar a placa de som', mute))
		return diagList