# -*- coding: utf-8 -*-

"""
	RQF06.C	: Compatibilidade - Executar teste de I/O utilizando o "memtest".
"""

from libs.core.compat_dev import CompatDev
from libs.core.commands_utils import exec_command

class CompatMemory(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade de memória.
	"""

	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)

	def compat(self, info_list):
		"""Executa o teste de compatibilidade como definido na RFQ06.C.'

		Parâmetro:
		info_list -- Lista contendo as informações detectadas para a memória (lista de 'InfoResMemory')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		result = True
		msg = u'Não foi encontrado nenhum erro na memória'

		mem_free = self.__get_free_mem("-m")
		dic_saida = {}
		output, err = self.__run_mem_tester(mem_free, '1')
		if not err:
				dic_saida = self.__format_output(output ,1)

				if not (dic_saida['RandomValue'] and dic_saida['CompareXOR'] and dic_saida['CompareSUB'] and dic_saida['CompareMUL'] and dic_saida['CompareDIV'] and dic_saida['CompareOR'] and dic_saida['CompareAND'] == "PASSOU" ):
					result = False
					msg = u"Falha no processamento de operações lógicas pela memória do sistema."

				if not (dic_saida['BitFlip'] and dic_saida['Checkerboard'] and dic_saida['WalkingOnes'] and dic_saida['BitSpread'] and dic_saida['CompareDIV'] == "PASSOU" ):
					result = False
					msg = u'Falha nos setores de fronteira da memória do sistema'

				if not (dic_saida['StuckAddress'] == "PASSOU"):
					result = False
					msg = u'Falha no setor de endereçamento da memória do sistema.'

				if not (dic_saida['BlockSequential'] and dic_saida['SolidBits'] == "PASSOU" ):
					result = False
					msg = u'Falha no setor de incremento da memória do sistema.'

		self._compat_res = [(result, msg)]

	def __get_free_mem(self, format=" "):
		"""Método que retorna o tamanho da memória livre em string"""
		i, o_str, e_str, ret_code = exec_command("/usr/bin/free "+str(format))
		lines_cmd_free = (str(o_str)).splitlines()
		line_2_elem = lines_cmd_free[1].split()
		result_list = [element for element in  line_2_elem if element != ""]
		free_mem = result_list[3]
		return free_mem

	def __run_mem_tester(self,size="",num_times=10):
		"""Método que executa o memtester com os dados passados como parâmetros.
		
		Parâmetros:
		size -- tamanho da memória livre em que será executado o teste. O default é vazio
		num_times -- números de repetições que será executado o teste, o default é 10. 
		"""
		size_int = int(size)
		if size_int > 10: #Diminuindo o tamanho para ser mais rápido o teste
			size = "10"
		i, o_str, e_str, ret_code = exec_command("memtester %s %s" % (size, num_times))
		return o_str, e_str

	def __format_output(self,s , num_times=10):
		"""Varre a string de resultado de memtester e retorna um dicionário com cada categoria do teste e uma string indicando se 'PASSOU' ou 'FALHOU'
		"""
		s = s.replace("Done.",'')
		s = s[s.index("Loop"):]
		s = s.replace("Loop 1/1:","")
		l = s.splitlines()
		l1 = [x for x in l if x!='']
		dic_saida = {'StuckAddress':'PASSOU', 'RandomValue':'PASSOU','CompareXOR':'PASSOU','CompareSUB':'PASSOU', 'CompareMUL':'PASSOU','CompareDIV':'PASSOU','CompareOR':'PASSOU','CompareAND':'PASSOU','SequentialIncrement':'PASSOU', 'SolidBits':'PASSOU', 'BlockSequential':'PASSOU', 'Checkerboard':'PASSOU', 'BitSpread':'PASSOU', 'BitFlip':'PASSOU', 'WalkingOnes':'PASSOU', 'WalkingZeroes':'PASSOU' }
		for i in range(num_times):
			z=i*16
		count = 0
		for key in dic_saida.keys():
			if "ok" not in l1[count]:
				dic_saida[key] = "FALHOU"
		count+=1
		return dic_saida

# Testing...

def main(argv):
	test = CompatMemory()
	test.runTest(libs.memory.diag_memory.DiagMemory)

import sys
if __name__ == "__main__":
	main(sys.argv)

