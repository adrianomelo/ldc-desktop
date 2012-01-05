# -*- coding: utf-8 -*-

"""
	RQF13.A : Identificar - Produto, fabricante, driver, device file e velocidade.
	RQF13.C : Diagnóstico - Informar se o link está ativo (up), informar o endereço de enlace (mac) e as configurações de rede (endereço IP, máscara de rede (netmask), endereço IP do default gateway e endereço do(s) servidor(es) DNS).
"""

from libs.core.diag_dev import DiagDev
from libs.network.info_res_network import InfoResNetwork
from libs.network.diag_res_network import DiagResNetwork

class DiagNetwork(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na biblioteca em C com Python.
	"""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca de rede."""
		DiagDev.__init__(self, "libldc_network.so", ctrl, InfoResNetwork, DiagResNetwork)

def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'DiagDev'"""
	test = DiagNetwork()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)