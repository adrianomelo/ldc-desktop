# -*- coding: utf-8 -*-

"""
	RQF05.B	: Compatibilidade - Identificar o processador através da informação do “/proc/cpuinfo”. O processador é dito incompatível se apenas a informação sobre a arquitetura estiver disponível.
"""

from libs.core.compat_dev import CompatDev

class CompatProcessor(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do processador.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	#FIXME: Revisar o conceito do teste. Nao foi levado em conta a arquitetura do processador
	def compat(self, info_list):
		"""Executa o teste de compatibilidade como definido na RFQ05.B.'

		Parâmetro:
		info_list -- Lista contendo as informções detectadas para o processador (lista de 'InfoResProcessor')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		self._compat_res = None

		cpuinfo_file = open('/proc/cpuinfo', 'r')
		cpuinfo_str = cpuinfo_file.read()
		cpuinfo_list = cpuinfo_str.strip().split('\n\n')

		if (cpuinfo_list):
			self._compat_res = []

			for cpuinfo in cpuinfo_list:
				result = False
				msg = u"O processador não foi identificado corretamente."

				info_list = cpuinfo.splitlines()

				for info in info_list:
					if 'model name' in info:
						result = True
						msg = u"O processador foi identificado corretamente."
						#msg = info.split(':')[1].strip()

				self._compat_res.append((result, msg))

		return self._compat_res

	def get_uname(self, type):
		"""Retorna o resultado do uname.
		Parâmetro: type -- tipo passado para o comando uname.
		"""
		i, o_str, e_str, ret_code = exec_command('uname -%s'%type)
		return o_str

# Testing...

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'CompatDev'"""
	test = CompatProcessor()
	test.runTest(libs.processor.diag_processor.DiagProcessor)

import sys
if __name__ == "__main__":
	main(sys.argv)