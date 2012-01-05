# -*- coding: utf-8 -*-

"""
	RQF11.A : Identificar - Fabricante, produto, modelo e driver.
	RQF11.C : Diagnóstico - Utilizar o pacote alsa para aumentar/diminuir o volume e habilitar/desabilitar a placa de som. Informar o resultado obtido através da utilização do pacote alsa. Caso haja algum problema, sugerir ao usuário que execute o teste de compatibilidade, e solicitar que ele cheque as caixas de som.
"""

from libs.core.diag_dev import DiagDev
from libs.sound.info_res_sound import InfoResSound
from libs.sound.diag_res_sound import DiagResSound

class DiagSound(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnostico definida na bibliotecas em C com a parte de diagnostico em Python."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do dispositivo."""
		DiagDev.__init__(self, "libldc_sound.so", ctrl, InfoResSound, DiagResSound)

def main(argv):
	test = DiagSound()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)
