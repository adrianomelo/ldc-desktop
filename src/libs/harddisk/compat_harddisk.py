# -*- coding: utf-8 -*-

"""
	RQF07.B : Compatibilidade - Testar a compatibilidade, executando aplicativo badblocks.
"""

from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command_parms

class CompatHarddisk(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do HD.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info_list):
		"""Executa o teste de compatibilidade como definido na RFQ07.B.'

		Parâmetro:
		info_list -- Lista contendo as informções detectadas para o HD (lista de 'InfoResHarddisk')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		self._compat_res = None

		if (info_list):
			self._compat_res = []

			for info in info_list:
				i, o_str, e_str, ret_code = exec_command_parms([['/sbin/badblocks', '-v', info.deviceFile, '1000000']])

				qtde = e_str.split()[-4]

				if qtde != "trying" and int(qtde) > 0:
					self._compat_res.append((False, u'HD incompatível com o Librix. %d setores defeituosos (bad blocks) encontrados' % int(qtde)))
				else:
					self._compat_res.append((True, u'HD compatível com o Librix.'))

# Testing...

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'CompatDev'"""
	test = CompatHarddisk()
	test.runTest(libs.harddisk.diag_harddisk.DiagHarddisk)

import sys
if __name__ == "__main__":
	main(sys.argv)