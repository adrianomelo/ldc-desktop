# -*- coding: utf-8 -*-

"""
	RQF10.A	Identificar – Modelo, fabricante, tamanho total, velocidade, driver, device file, sistema de arquivo, 
	                      partições. 
	RQF10.C	Diagnóstico – Verificar montagem.
	RQF10.D	Diagnóstico – Verificar particionamento.
	RQF10.E	Diagnóstico – Se o sistema de arquivos permitir, executar o comando “fsck” correspondente.
"""

from libs.core.diag_dev import DiagDev
from libs.usbstorage.info_res_usbstorage import InfoResUsbstorage
from libs.usbstorage.diag_res_usbstorage import DiagResUsbstorage

class DiagUsbstorage(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na biblioteca em C com Python.
	"""

	def __init__ (self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca de armazenamento usb."""
		DiagDev.__init__(self, "libldc_usbstorage.so", ctrl, InfoResUsbstorage, DiagResUsbstorage)
		
def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'DiagDev'"""
	test = DiagUsbstorage()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)


