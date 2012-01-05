# -*- coding: utf-8 -*-

"""
	RQF07.A	Identificar -Fabricante, produto, modelo, tamanho, device file (logical name) e driver.
	RQF07.C	Diagnóstico - Informar os particionamentos,  o espaço livre e a temperatura dos discos. Caso os discos possuam o recurso “SMART”, executar o teste “overall-health self-assesment”.
"""

from libs.core.diag_dev import DiagDev
from libs.harddisk.info_res_harddisk import InfoResHarddisk
from libs.harddisk.diag_res_harddisk import DiagResHarddisk

class DiagHarddisk(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na bibliotecas em C com a parte de diagnóstico em Python."""

	def __init__ (self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do HD."""
		DiagDev.__init__(self, "libldc_harddisk.so", ctrl, InfoResHarddisk, DiagResHarddisk)

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'DiagDev'"""
	test = DiagHarddisk()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)