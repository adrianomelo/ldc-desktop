# -*- coding: utf-8 -*-

"""
	RQF14.A : Identificar - Fabricante, produto, modelo, driver, velocidade nominal e protocolos suportados (802.11 a/b/g/n).
	RQF14.D : Diagnóstico - Informar se o link está ativo (up), informar o endereço de enlace (mac) e as configurações de rede (endereço IP, máscara de rede (netmask), endereço IP do default gateway e endereço do(s) servidor(es) DNS).
"""

from libs.core.diag_dev import DiagDev
from libs.wireless.info_res_wireless import InfoResWireless
from libs.wireless.diag_res_wireless import DiagResWireless

class DiagWireless(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnostico definida na bibliotecas em C com a parte de diagnostico em Python."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do dispositivo."""
		DiagDev.__init__(self, "libldc_wireless.so", ctrl, InfoResWireless, DiagResWireless)

import sys
if __name__ == "__main__":
	def main(argv):
		test = DiagWireless()
		test.runTest()
	main(sys.argv)