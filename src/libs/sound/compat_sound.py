# -*- coding: utf-8 -*-

"""
	RQF11.B : Compatibilidade - Testar a reprodução de um arquivo de audio.
"""

from libs.core.compat_dev import CompatDev
from libs.sound.compat_sound_wizard import SoundWizard

class CompatSound(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do dispositivo.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)
		self.parent = parent

	def compat(self, info):
		"""Executa o teste de compatibilidade do dispositivo como definido no DTR..

		Parametro:
		info_list -- Lista contendo as informacoes detectadas para o dispositivo.
		"""
		self._compat_res = None
		if (info):
			self._compat_res = []
			for i in info:
				a = self.parent.showCustomDialog(SoundWizard, [self, i])
				result = a['result']

				if (result == 0):
					self._compat_res.append((True, u"Placa de som compatível com o Librix."))
				elif (result == 1):
					self._compat_res.append((False, u"Placa de som incorretamente configurada ou incompatível com o Librix"))
				elif (result == 2):
					self._compat_res.append((False, u"O teste de compatibilidade foi interrompido."))
				else:
					self._compat_res.append((False, u"Erro na execução do teste."))


# Testing...

def main(argv):
	test = CompatSound()
	test.runTest(libs.sound.diag_sound.DiagSound)

import sys
if __name__ == "__main__":
	main(sys.argv)