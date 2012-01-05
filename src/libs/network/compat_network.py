# -*- coding: utf-8 -*-

"""
	RQF13.B : Compatibilidade - Verificar se as informações do dispositivo foram obtidas corretamente.
"""

from libs.core.compat_dev import CompatDev

class CompatNetwork(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade de rede.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info):
		"""Executa o teste de compatibilidade como definido na RFQ13.B.'

		Parâmetro:
		info_list -- Lista contendo as informações detectadas para o processador (lista de 'InfoResNetwork')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		
		self._compat_res = None

		if (info):
			self._compat_res = []
			
			for i in info:
				if i.deviceFile and i.model:
					self._compat_res.append((True, u"Sua placa de rede foi corretamente identificada."))
				else:
					self._compat_res.append((False, u"Não foi possível identificar sua placa de rede corretamente."))

# Testing...

def main(argv):
	test = CompatNetwork()
	test.runTest(libs.network.diag_network.DiagNetwork)

import sys
if __name__ == "__main__":
	main(sys.argv)