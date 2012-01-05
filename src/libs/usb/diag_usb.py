# -*- coding: utf-8 -*-

from libs.core.diag_dev import DiagDev
from libs.usb.info_res_usb import InfoResUsb
from libs.usb.diag_res_usb import DiagResUsb

class DiagUsb(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnostico definida na bibliotecas em C com a parte de diagnostico em Python."""

	def __init__ (self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do dispositivo."""
		DiagDev.__init__(self, "libldc_usb.so", ctrl, InfoResUsb, DiagResUsb)

def main(argv):
	test = DiagUsb()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)