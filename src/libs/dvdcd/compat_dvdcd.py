# -*- coding: utf-8 -*-

"""
	RQF08.B : Compatibilidade - Verificar se as mídias suportadas pelo dispositivo foram identificadas.
"""

from libs.core.compat_dev import CompatDev
 
class CompatDVDCD(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do CD/DVD.
	"""
	
	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)
	
	def compat(self, info):
		"""Executa o teste de compatibilidade como definido na RFQ08.B.'

		Parâmetro:
		info_list -- Lista contendo as informções detectadas para o cd/dvd (lista de 'InfoResDVDCD')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		
		self._compat_res = None

		if (info):
			self._compat_res = []
			
			for i in info:
				if len(i.medias) > 0:
					self._compat_res.append((True, u"As mídias suportadas foram identificadas"))
				else:
					self._compat_res.append((False, u"Não foi possível identificar as mídias suportadas"))

# Testing...

def main(argv):
	test = CompatDVDCD()
	test.runTest(libs.dvdcd.diag_dvdcd.DiagDVDCD)

import sys
if __name__ == "__main__":
	main(sys.argv)