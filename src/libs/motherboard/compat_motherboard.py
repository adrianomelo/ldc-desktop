# -*- coding: utf-8 -*-

"""
	RQF04.B : Compatibilidade - Identificar somente os dispositivos referentes ao chipset da motherboard, utilizando o comando lspci.
"""

from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command

class CompatMotherboard(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade de placa mãe.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info):
		"""Executa o teste de compatibilidade como definido na RFQ04.B.

		Parâmetro:
		info_list -- Lista contendo as informções detectadas para a pla mãe (lista de 'InfoResMotherboard')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem
		"""
		result = True
		msg = u'Os dispositivos da placa mãe foram identificados corretamente.'
		list_classes_device = ['Host bridge', 'PCI bridge', 'ISA bridge', 'IDE interface']
		devices_names_list = self.__get_devices_names(list_classes_device)
		for device_name in devices_names_list:
			if 'UNKNOWN' in device_name.upper():
				result = False
				msg = u"Os dispositivos da placa mãe não foram identificados corretamente. Tente atualizar o arquivo de definições pciids."
		self._compat_res = [(result, msg)]

	def __get_devices_names(self, list_classes_device):
		"""Método auxiliar que retorna uma lista com os nomes dos dispositivos.
		Parâmetro:
		list_classes_device -- lista contendo os tipos de dispositivos que serão procurados.
		"""
		devices_names_list = []
		i, o_str, e_str, ret_code = exec_command("lspci -vmm")
		list_result = o_str.split('\n\n')
		for dev_result in list_result:
			if [dev_result for dev_class in list_classes_device if dev_class in dev_result]:
				list_dev = dev_result.splitlines()
				for tuple in list_dev:
					if tuple.startswith('Device:'):
						devices_names_list.append(tuple.split('\t')[1])
		return devices_names_list


def main(argv):
	"""Cria um objeto da classe e chama o 'runTest()' definido em 'CompatDev'"""
	test = CompatMotherboard()
	test.runTest(libs.motherboard.diag_motherboard.DiagMotherboard)

import sys
if __name__ == "__main__":
	main(sys.argv)
