# -*- coding: utf-8 -*-

"""
	RQF14.B : Compatibilidade - Verificar se o dispositivo foi corretamente identificado, através do comando ifconfig.
	RQF14.C : Compatibilidade - Listar todas as redes sem fio disponíveis.
"""

from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command_parms, exec_command
from PyQt4 import QtCore

class CompatWireless(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do dispositivo.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info):
		"""Executa o teste de compatibilidade do dispositivo como definido no DTR..

		Parametro:
		info_list -- Lista contendo as informacoes detectadas para o dispositivo.
		"""

		status = -1

		if info and not (info[0].deviceFile == ""):
			device = info[0].deviceFile
			cmd = "iwlist %s scanning | grep ESSID" % device
			i, o_str, e_str, returncode = exec_command(cmd)
			iwlist = returncode
			#print "DEBUG:", 'iwlist ' + str(iwlist)

			wlan_list = []
			if iwlist == 0:
				wlan_in_range_list = o_str.split('\n')
				for wlan in wlan_in_range_list:
					wlan = wlan.strip()
					wlan = wlan.strip("ESSID:")
					wlan = wlan.strip("\"")
					wlan_list.append(wlan)

			i, o_str, e_str, returncode = exec_command("ifconfig %s" % device)
			status = returncode

			self._compat_res = []
			if (status == 0):
				self._compat_res.append((True, u"Seu adaptador wireless foi reconhecido corretamente.", wlan_list))
			else:
				self._compat_res.append((False, u"Seu adaptador wireless não foi corretamente reconhecido.", []))
		else:
			self._compat_res = []
			self._compat_res.append((False, u"Nenhum adaptador wireless foi identificado.", []))


# Testing...

def main(argv):
	test = CompatWireless()
	test.runTest(libs.wireless.diag_wireless.DiagWireless)

import sys
if __name__ == "__main__":
	main(sys.argv)