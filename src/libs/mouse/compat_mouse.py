# -*- coding: utf-8 -*-

"""
	RQF18.B : Compatibilidade - Verificar se todos os botões do mouse e o wheel (se houver) funcionam corretamente.
"""

from libs.core.compat_dev import CompatDev

from libs.mouse.compat_mouse_gui import CompatMouseGUI
 
class CompatMouse(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade de mouse.
	"""
	
	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, ctrl)
	
	def compat(self, info):
		"""Executa o teste de compatibilidade de mouse como definido na RFQ18.B.
		Para isso, chama a classe 'CompatMouseGUI' que irá executar o teste de compatibilidade.
		A partir do resultado retornado pela GUI será configurado o resultado do teste de compatibilidade.

		Parâmetro:
		info_list -- Lista contendo as informações detectadas para o mouse (lista de 'InfoResMouse')
		"""
		self._compat_res = []
		
		for i in info:
			wizardRes = self.parent.showCustomDialog(CompatMouseGUI, i.model, i.numberOfButtons, i.hasWheel)

			compatible = True

			if (wizardRes and wizardRes['code'] == 1):
				if (i.numberOfButtons > 0):
					compatible = compatible and wizardRes['result']['leftClick']
				if (i.numberOfButtons > 1):
					compatible = compatible and wizardRes['result']['rightClick']
				if (i.numberOfButtons > 2):
					compatible = compatible and wizardRes['result']['middleClick']
				if (i.hasWheel):
					compatible = compatible and wizardRes['result']['wheelMove']
				
				if (compatible):
					self._compat_res.append((True, u"Seu mouse é compatível com o Librix."))
				else:
					self._compat_res.append((False, u"Seu mouse não é compatível com o Librix ou não está devidamente configurado."))
			else: # Cancelado
				self._compat_res.append((False, u"O teste foi cancelado pelo usuário."))

# Testing...

def main(argv):
	test = CompatMouse()
	test.runTest(libs.mouse.diag_mouse.DiagMouse)

import sys
if __name__ == "__main__":
	main(sys.argv)