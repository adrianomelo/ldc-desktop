# -*- coding: utf-8 -*-

"""
	RQF16.B : Compatibilidade -  Verificar se o device /dev/video0 foi criado.
"""

from PyQt4 import QtCore

from libs.core.commands_utils import exec_command_parms, exec_command

from libs.core.compat_dev import CompatDev
from libs.webcam.compat_webcam_wizard import WebcamWizard

class CompatWebcam(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do dispositivo.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, infoList):
		"""Executa o teste de compatibilidade do dispositivo como definido no DTR..

		Parametro:
		info_list -- Lista contendo as informacoes detectadas para o dispositivo.
		"""
		self._compat_res = []

		for info in infoList:
			i, o_str, e_str, retCode = exec_command('ls %s' % info.deviceFile)

			if (retCode == 0 and o_str.__contains__(info.deviceFile)):
				result = self.parent.showCustomDialog(WebcamWizard, info)['result']

				if (result == 0):
					self._compat_res.append((True, u"Sua webcam é compatível com o Librix."))
				elif (result == 1):
					self._compat_res.append((False, u"Sua webcam não é compatível com o Librix ou não está corretamente configurada"))
				elif (result == 2):
					self._compat_res.append((False, u"O teste de compatibilidade foi interrompido."))
				else:
					self._compat_res.append((False, u"Resultado indefinido. Provavelmente algum erro ocorreu na execução do LDC."))
			else:
				self._compat_res.append((False, u'Nenhum dispositivo foi encontrado.'))

# Testing...

def main(argv):
	test = CompatWebcam()
	test.runTest(libs.webcam.diag_webcam.DiagWebcam)

import sys
if __name__ == "__main__":
	main(sys.argv)