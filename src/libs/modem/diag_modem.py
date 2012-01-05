# -*- coding: utf-8 -*-

"""
	RQF15.A : Identificar - Modelo, fabricante e driver.
	RQF15.C : Diagnóstico - Informar se algum dos possíveis drivers foi carregado (ltmodem, sfmodem e hsfmodem). 
"""

from libs.core.diag_dev import DiagDev
from libs.modem.info_res_modem import InfoResModem
from libs.modem.diag_res_modem import DiagResModem

class DiagModem(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na bibliotecas em C com a parte de diagnóstico em modem."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do modem."""
		DiagDev.__init__(self, "libldc_modem.so", ctrl, InfoResModem, DiagResModem)

def main(argv):
	test = DiagModem()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)