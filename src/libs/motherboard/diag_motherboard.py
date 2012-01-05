# -*- coding: utf-8 -*-

"""
	RQF04.A : Identificar - Fabricante, produto, versão, serial, chipset (modelo e driver module), informações da BIOS (vendedor, versão, data).
	RQF04.C : Diagnóstico - Caso algum dispositivo não tenha sido identificado corretamente no teste de compatibilidade (identificado como “unknown”), sugerir a atualização do arquivo de definições pciids.
"""

from libs.core.diag_dev import DiagDev
from libs.motherboard.info_res_motherboard import InfoResMotherboard
from libs.motherboard.diag_res_motherboard import DiagResMotherboard

class DiagMotherboard(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na bibliotecas em C com a parte de diagnóstico em Python."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca da placa mãe."""
		DiagDev.__init__(self, "libldc_motherboard.so", ctrl, InfoResMotherboard, DiagResMotherboard)

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'DiagDev'"""
	test = DiagMotherboard()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)