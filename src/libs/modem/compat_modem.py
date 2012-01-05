# -*- coding: utf-8 -*-

"""
	RQF15.B : Compatibilidade - Verificar se o device “/dev/modem” foi criado, e executar comandos “AT” no dispositivo.
"""

from libs.core.commands_utils import exec_command, exec_command_parms

from libs.core.compat_dev import CompatDev
 
class CompatModem(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade do modem.
	"""
	
	def __init__(self, parent):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, parent)
	
	def compat(self, info):
		"""Executa o teste de compatibilidade como definido na RFQ15.B.'

		Parâmetro:
		info -- Lista contendo as informções detectadas para o modem (lista de 'InfoResModem')

		Retorna uma lista contendo o resultado do teste e uma string de mensagem para cada dispositivo.
		"""
		
		minicomScriptFile = "libs/modem/script.minicom"
		minicomOutputFile = "/var/tmp/ldc_minicom_output"
		
		i, o_str, e_str, retCode = exec_command('ls /dev/modem')
		
		if (retCode == 0 and o_str.__contains__('/dev/modem')):
			cmd = 'minicom /dev/modem -S %s -C %s' % (minicomScriptFile, minicomOutputFile)
			
			i, o_str, e_str, retCode = exec_command(cmd)
			
			minicomOutputList = self.__processMinicomOutput(minicomOutputFile)
			
			minicomResult = True
			
			for item in minicomOutputList:
				minicomResult = minicomResult and item['ok']
			
			if (minicomResult):
				self._compat_res = [(True, u'Seu modem é compatível com o Librix.')]
			else:
				self._compat_res = [(False, u'Seu modem foi identificado porém não responde corretamente.')]
			
			i, o_str, e_str, retCode = exec_command('rm -Rf %s' % minicomOutputFile)
		else:
			self._compat_res = [(False, u'Não foi possível encontrar o dispositivo /dev/modem.')]

	def __processMinicomOutput(self, output):
		"""Metodo auxiliar utilizado para processar o output da aplicacao minicom, verificando a resposta aos
		comantos ATI"""

		ret = None

		file = open(output)

		lines = file.readlines()

		if (len(lines)):
			ret = []

			for line in lines:			
				if (line.__contains__("ATI")):
					ret.append({'command': line.rstrip('\n'), 'ok': False})
				elif line.__contains__("OK"):
					ret[-1]['ok'] = True
				else:
					ret[-1]['result'] = line.rstrip('\n').rstrip('\r')

		return ret

# Testing...

def main(argv):
	test = CompatModem()
	test.runTest(libs.modem.diag_modem.DiagModem)

import sys
if __name__ == "__main__":
	main(sys.argv)