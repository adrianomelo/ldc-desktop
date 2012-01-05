# -*- coding: utf-8 -*-

"""
	RQF16.A : Identificar - Fabricante, produto, modelo e driver.
	RQF16.C : Diagnóstico - Informar os drivers que foram carregados via kernel (utilizar kernel 2.6.27 ou superior, presente no Librix Desktop 3.2 ou superior).
"""

from libs.core.diag_dev import DiagDev
from libs.webcam.info_res_webcam import InfoResWebcam
from libs.webcam.diag_res_webcam import DiagResWebcam

class DiagWebcam(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnostico definida na bibliotecas em C com a parte de diagnostico em Python."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do dispositivo."""
		DiagDev.__init__(self, "libldc_webcam.so", ctrl, InfoResWebcam, DiagResWebcam)

def main(argv):
	test = DiagWebcam()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)