# -*- coding: utf-8 -*-

"""
	RQF06.A	Identificar - Controlador: velocidades suportadas, tipos de módulos suportados, tensão dos módulos, tamanho máximo de cada módulo, tamanho total máximo e espaço de endereçamento.
	RQF06.B	Identificar - Módulos: Tamanho, modelo (SDRAM, DRAM, SGRAM, etc), tipo (DIMM, SIMM, etc), velocidade, localização (DIMM0, DIMM1, etc).
	RQF06.D	Diagnóstico - Informar o tamanho da memória obtido através do "/proc" e o tamanho obtido através do “dmidecode” (a diferença entre os dois valores, provavelmente, será a memória alocada para vídeo).
"""

from libs.core.diag_dev import DiagDev
from libs.memory.info_res_memory import InfoResMemory
from libs.memory.diag_res_memory import DiagResMemory

class DiagMemory(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnóstico definida na bibliotecas em C com a parte de diagnóstico em Python."""

	def __init__ (self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca de memória."""
		DiagDev.__init__(self, "libldc_memory.so", ctrl, InfoResMemory, DiagResMemory)

def main(argv):
	test = DiagMemory()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)