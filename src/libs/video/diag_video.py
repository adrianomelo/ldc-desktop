# -*- coding: utf-8 -*-

"""
	RQF12.A : Identificar - Fabricante, produto, modelo e driver.
	RQF12.C : Diagnóstico - Verificar configuração no xorg.conf, caso este arquivo não exista, utilizar as informações do hal, hwdata e as informações obtidas com a execução do comando “mkx86config”. Para o correto funcionamento, utilizar o Librix Desktop 3.2.
"""

from libs.core.diag_dev import DiagDev
from libs.video.info_res_video import InfoResVideo
from libs.video.diag_res_video import DiagResVideo

class DiagVideo(DiagDev):
	"""Estende a classe 'DiagDev'.
	Classe que faz a linkagem da parte de diagnostico definida na bibliotecas em C com a parte de diagnostico em Python."""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do dispositivo."""
		DiagDev.__init__(self, "libldc_video.so", ctrl, InfoResVideo, DiagResVideo)

	def getInfoResults(self):
		"""
		Redefinição do médotodo de 'DiagDev'
		"""
		ret = None

		incomplete_videocard_info = None

		if (self._info_tuple):
			if (self._info_res_class):
				ret = []

				for i in self._info_tuple[1]:
					if i['libName'] == 'videocard':
						if i['info'].has_key('xf86_module_name'):
							complete_videocard = i

							if incomplete_videocard_info:
								complete_videocard['vendor'] = incomplete_videocard_info['vendor']
								complete_videocard['model'] = incomplete_videocard_info['model']
								incomplete_videocard_info = None

							ret.append(self._info_res_class(complete_videocard))
						else:
							incomplete_videocard_info = i
			else:
				print "STUB: InfoRes Class is 'None'"

		return ret

def main(argv):
	test = DiagVideo()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)
