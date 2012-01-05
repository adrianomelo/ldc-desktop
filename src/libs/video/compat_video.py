# -*- coding: utf-8 -*-

"""
	RQF12.B : Compatibilidade - Teste de execução do glxgears.
"""

from libs.core.compat_dev import CompatDev
from libs.video.compat_video_wizard import VideoWizard

class CompatVideo(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do dispositivo.
	"""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, ctrl)

	def compat(self, info):
		"""Executa o teste de compatibilidade do dispositivo como definido no DTR..

		Parametro:
		info_list -- Lista contendo as informacoes detectadas para o dispositivo.
		"""
		self._compat_res = None
		if (info):
			self._compat_res = []

			counter = 0
			for i in info:
				a = self.parent.showCustomDialog(VideoWizard, i, counter)
				result = a['result']

				if (result == 0):
					self._compat_res.append((True, u"Sua placa de vídeo é compatível com o Librix."))
				elif (result == 1):
					self._compat_res.append((False, u"Sua placa de vídeo não é compatível com o Librix ou não está corretamente configurada"))
				elif (result == 2):
					self._compat_res.append((False, u"O teste de compatibilidade foi interrompido."))
				else:
					self._compat_res.append((False, u"Resultado indefinido. Provavelmente algum erro ocorreu na execução do LDC."))

				counter = counter + 1

# Testing...

def main(argv):
	test = CompatVideo()
	test.runTest(libs.video.diag_video.DiagVideo)

import sys
if __name__ == "__main__":
	main(sys.argv)
