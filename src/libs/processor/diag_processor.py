# -*- coding: utf-8 -*-

"""
	RQF05.A : Identificar - Fabricante, modelo, clock, caches (tamanho, associatividade, modo de operação, operações SRAM suportadas, tipo de correção de erro), tensão, numero de “cores” (núcleos), “features” (ex: MMX, SSE, HTT, MSR, etc).
	RQF05.C : Diagnóstico - Caso o teste de compatibilidade tenha falhado para este item, informar o nome do processador encontrado através do “dmidecode”.
"""

from libs.core.diag_dev import DiagDev
from libs.processor.info_res_processor import InfoResProcessor
from libs.processor.diag_res_processor import DiagResProcessor

class DiagProcessor(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na biblioteca em C com Python.
	"""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do processador."""
		DiagDev.__init__(self, "libldc_processor.so", ctrl, InfoResProcessor, DiagResProcessor)

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'DiagDev'"""
	test = DiagProcessor()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)
