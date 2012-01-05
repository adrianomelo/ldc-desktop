# -*- coding: utf-8 -*-

from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command_parms
from libs.usb.compat_usb_wizard import UsbWizard
#from libs.usb.dbusobject import *

class CompatUsb(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do dispositivo.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info_list):
		"""Executa o teste de compatibilidade do dispositivo como definido no DTR..

		Parametro:
		info_list -- Lista contendo as informacoes detectadas para o dispositivo.
		"""
		self._compat_res = []

		for i in info_list:
			a = self.parent.showCustomDialog(UsbWizard, [self, i])
			code = a['code']
			result = a['result']
			self._compat_res.append((code, result))


#		dialog_result = self.parent.showInputDialog("Quantas portas USB seu computador possui?")
#		nPortas = dialog_result['result']
#		while nPortas == None or not unicode(nPortas).isdigit():
#			dialog_result = self.parent.showInputDialog("Quantas portas USB seu computador possui? <br> Apenas números são suportados!")
#			nPortas = dialog_result['result']
#
#		nPortas = int(nPortas)
#		print nPortas
#
#		if nPortas > 0:
#			for i in range(0, nPortas):
#				pass
#
#		try:
#			self._compat_res.append((True, "Great Success!"))
#		except:
#			self._compat_res.append((False, "fail"))

# Testing...

def main(argv):
	test = CompatUsb()
	test.runTest(libs.usb.diag_usb.DiagUsb)

import sys
if __name__ == "__main__":
	main(sys.argv)