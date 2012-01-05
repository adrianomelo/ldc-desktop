# -*- coding: utf-8 -*-

"""
	RQF18.A : Identificar - Modelo, fabricante, device files, número de botões, roldana, protolo do XFree86, protocolo do GPM, tipo de conector (PS/2, serial, etc).
	RQF18.C : Diagnóstico - Verificar se o  mouse está plugado, utilizando “outb 0x64” ou “outb 0x60”. http://www.win.tue.nl/~aeb/linux/kbd/scancodes-11.html#ss11.1
"""

from libs.core.diag_dev import DiagDev

from libs.mouse.info_res_mouse import InfoResMouse
from libs.mouse.diag_res_mouse import DiagResMouse

from libs.mouse.diag_mouse_gui import DiagMouseGUI

class DiagMouse(DiagDev):

	def __init__(self, ctrl):
		DiagDev.__init__(self, "libldc_mouse.so", ctrl, InfoResMouse, DiagResMouse)

	def diag(self, info):
		"""
		Redefine o método diag, definido previamente em DiagDev, uma vez que todo o
		diagnóstico de Mouse é feito em python, não havendo biblioteca de diagnóstico
		de Mouse em C.
		"""
		
		self._diag_tuple = (None, [])
		
		infos = self.getInfoResults()
		
		for info in infos:
			wizardRes = self._ctrl.showCustomDialog(DiagMouseGUI)
				
			if (wizardRes and wizardRes['code'] == 1):
				self._diag_tuple[1].append({'actionDetected': wizardRes['result']['actionDetected']})
			else: # Cancelado
				self._diag_tuple[1].append({'actionDetected': False})

	def getInfoResults(self):
		"""
		Redefinição do método definido em DiagDev, de mesmo nome, para remover resultados indesejados
		do informativo (emuladores de botoes e simulações, neste caso).		
		"""

		ret = None

		if (self._info_tuple):
			if (self._info_res_class):
				ret = []

				for i in self._info_tuple[1]:
					if (not (i['model']['value'].__contains__("emulation") or i['model']['value'].__contains__("simulator") or i['model']['value'].__contains__("emulator") or i['model']['value'].__contains__("PS/2 Mouse"))):					
						ret.append(self._info_res_class(i))
			else:
				print "STUB: InfoRes Class is 'None'"

		return ret

def main(argv):
	test = DiagMouse()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)