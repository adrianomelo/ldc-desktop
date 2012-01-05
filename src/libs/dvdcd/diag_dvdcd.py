# -*- coding: utf-8 -*-

"""
	RQF08.A : Identificar - Fabricante, modelo, driver, dispositivo e mídias suportadas.
	RQF08.C : Diagnostico - Através de um CD-RW de teste, efetuar a gravação e a leitura do CRC.
 	RQF08.D : Diagnostico - Através de um DVD-RW de teste, efetuar a gravação e a leitura do CRC.
"""

from libs.core.diag_dev import DiagDev
from libs.dvdcd.info_res_dvdcd import InfoResDVDCD
from libs.dvdcd.diag_res_dvdcd import DiagResDVDCD
from libs.dvdcd.diag_dvdcd_gui import DiagDVDCDGUI

from libs.core.commands_utils import exec_command_parms, prepare_command

class DiagDVDCD(DiagDev):
	"""Classe de diagnóstico e informação de DVD/CD"""

	__burnerType = None
	__mediaType = None

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca de DVD/CD."""
		DiagDev.__init__(self, "libldc_dvdcd.so", ctrl, InfoResDVDCD, DiagResDVDCD)

	def diag(self, info):
		"""
		Redefine o método diag, definido previamente em DiagDev, uma vez que todo o
		diagnóstico de DVD/CD é feito em python, não havendo biblioteca de diagnóstico
		de DVD/CD em C.
		"""
		self._diag_tuple = (None, [])

		infos = self.getInfoResults()

		for info in infos:
			expectedMedia = None

			if (not self.__checkLive()):
				devBurnerType = self.__guessBurnerType(info.deviceFile)
	
				if(devBurnerType == 'DVDRW'):
					expectedMedia = {'Type': 'DVD', 'Rewritable': False, 'Empty': False}
				elif(devBurnerType == 'CDRW'):
					expectedMedia = {'Type': 'CD', 'Rewritable': False, 'Empty': False}
				else:
					# print "SKIPPED : NOT A BURNER"
					pass

			if (expectedMedia):
				wizardRes = self._ctrl.showCustomDialog(DiagDVDCDGUI, info, expectedMedia)

				if (wizardRes and wizardRes['code'] == 1):
					self._diag_tuple[1].append({'deviceFile': info.deviceFile, 'burnerType': devBurnerType, 'testedMediaType': wizardRes['result']['currentMedia'], 'burnSuccess': wizardRes['result']['burnStatus'], 'readSuccess': wizardRes['result']['readStatus']})
				else: # Cancelado
					self._diag_tuple[1].append({'deviceFile': info.deviceFile, 'burnerType': devBurnerType, 'testedMediaType': None, 'burnSuccess': False, 'readSuccess': False})
			else:
				self._diag_tuple[1].append({'deviceFile': info.deviceFile, 'burnerType': None, 'testedMediaType': None, 'burnSuccess': False, 'readSuccess': False})

	def __guessBurnerType(self, deviceFile):
		"""
		Função que utiliza os dados fornecidos pelo teste informativo para identificar
		qual o tipo do gravador (ou se é só um leitor). Caso a informação não esteja
		disponível, a aplicação cdrecord é utilizada para tentar obtê-la.

		O retorno é a string 'DVDRW' ou 'CDRW', caso um gravador seja identificado, ou None,
		caso o dispositivo seja apenas um leitor.

		"""
		ret = None

		commands = []

		cmd_base = "cdrecord -prcap dev=%s | grep write | grep media | grep -v not" % deviceFile

		for cmd in cmd_base.split("|"):
			commands.append(prepare_command(cmd))

		cmd_awk = ['awk', '{print $3}']

		commands.append(cmd_awk)

		i, o_str, e_str, ret_code = exec_command_parms(commands)

		if(o_str.__contains__('DVD')):
			ret = 'DVDRW'
		elif(o_str.__contains__('CD')):
			ret = 'CDRW'

		return ret
	
	def __checkLive(self):
		"""Verifica se a execucao esta sendo feita a partir de um livecd, testando a existencia de alguma particao do
		tipo squashfs montada"""
		ret = False

		commands = [['mount'], ['awk', '{print $5}'], ['grep', 'squashfs']]

		i, o_str, e_str, ret_code = exec_command_parms(commands)

		if(o_str.__contains__('squashfs')):
			ret = True

		return ret

def main(argv):
	test = DiagDVDCD()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)