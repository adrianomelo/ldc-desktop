# -*- coding: utf-8 -*-

"""
	RQF17.B : Compatibilidade - Verificar se o usuario consegue escrever corretamente usando o teclado.
"""

from PyQt4 import QtCore

from libs.core.compat_dev import CompatDev

from libs.keyboard.compat_keyboard_gui import CompatKeyboardGUI
 
class CompatKeyboard(CompatDev):
	"""Estende a classe 'CompatDev'.
	Classe que implementa o teste de compatibilidade de Teclado."""
	
	#dicionaŕio indicando o panagrama que será usado para cada lingua.
	__pangrams = {
		'port': u'gazeta publica hoje no jornal uma breve nota de faxina',
		'ing': u'the quick brown fox jumps over the lazy dog',
		'french': u'portez ce whisky au vieux juge blond qui fume',
		'german': u'zwölf Boxkämpfer jagten Eva quer über den Sylter Deich',
		'danish': u'<font size="-1">quizdeltagerne spiste jordbær med fløde, mens cirkusklovnen Walther spillede på xylofon</font>',
		'esp': u'Queda gazpacho, fibra, látex, jamón, kiwi y viñas',
		'finnish': u'törkylempijä vongahdus',
		'hungarian':  u'árvízt\u0171r\u0151 tükörfúrógép',
		'icelandic':  u'kæmi ný öxi hér ykist þjófum nú bæði víl og ádrepa',
		'italian': u'ma la volpe col suo balzo ha raggiunto il quieto Fido',
		'norwegian': u'høvdingens kjære squaw får litt pizza i Mexico by',
		'romanian': u'<font size="-1">gheorghe, obezul, a reu\u015fit s\u0103 ob\u0163in\u0103 jucându-se un flux în Quebec de o mie kilowa\u0163ior\u0103</font>',
		'russian': u'<font size="+1">\u0421\u044a\u0435\u0448\u044c \u0435\u0449\u0451 \u044d\u0442\u0438\u0445 \u043c\u044f\u0433\u043a\u0438\u0445 \u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0445 \u0431\u0443\u043b\u043e\u043a, \u0434\u0430 \u0432\u044b\u043f\u0435\u0439 \u0436\u0435 \u0447\u0430\u044e</font>',
		'swedish':  u'yxskaftbud, ge vår wczonmö iqhjälp'
	}

	#dicionário indicando as configurações de cada layout
	__modelDict = {
		# * The lines commented below doesn't have keymaps for the console on our tests
		#layout              description, Layout, Model, ?(no-deadkeys), XkbOptions, Pangram
		'be-latin1'           : ['Belgian (be-latin1)', 'be', 'pc105', '', '', __pangrams['port']],
		#'bg'                 : ['Bulgarian', 'bg,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', ''],
		'br'                  : ['Brazilian', 'br', '', '', '',__pangrams['port'] ],
		'br-abnt2'            : ['Brazilian (ABNT2)', 'br', 'abnt2', '', '',__pangrams['port'] ],
		'cf'                  : ['French Canadian', 'ca_enhanced', 'pc105', '', '', __pangrams['french'] ],
		'croat'               : ['Croatian', 'hr', 'pc105', '', '', __pangrams['port'] ],
		'cz-us-qwertz'        : ['Czechoslovakian (qwertz)', 'cz,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['port'] ],
		'cz-lat2'             : ['Czechoslovakian', 'cz_qwerty','pc105','','', __pangrams['port'] ],
		'de'                  : ['German', 'de', 'pc105', '', '', __pangrams['german'] ],
		'de-latin1'           : ['German (latin1)', 'de', 'pc105', '', '',__pangrams['german'] ],
		'de-latin1-nodeadkeys': ['German (latin1 w/ no deadkeys)', 'de', 'pc105', 'nodeadkeys', '', __pangrams['german'] ],
		'dvorak'              : ['Dvorak', 'dvorak', 'pc105', '', '', __pangrams['port'] ],
		'dk'                  : ['Danish', 'dk', 'pc105', '', '', __pangrams['danish'] ],
		'dk-latin1'           : ['Danish (latin1)', 'dk', 'pc105', '', '', __pangrams['danish'] ],
		'es'                  : ['Spanish', 'es', 'pc105', '', '', __pangrams['esp'] ],
		'et'                  : ['Estonian', 'ee', 'pc105', '', '', __pangrams['port'] ],
		'fi'                  : ['Finnish', 'fi', 'pc105', '', '', __pangrams['finnish'] ],
		'fi-latin1'           : ['Finnish (latin1)', 'fi', 'pc105', '', '', __pangrams['finnish']],
		'fr'                  : ['French', 'fr', 'pc105', '', '', __pangrams['french'] ],
		#'fr-latin0'          : ['French (latin0)', 'fr', 'pc105', '', '', ''                            ],
		'fr-latin1'           : ['French (latin1)', 'fr', 'pc105', '', '',__pangrams['french'] ],
		'fr-pc'               : ['French (pc)', 'fr', 'pc105', '', '', __pangrams['french'] ],
		'fr_CH'               : ['Swiss French', 'fr_CH', 'pc105', '', '', __pangrams['french'] ],
		'fr_CH-latin1'        : ['Swiss French (latin1)', 'fr_CH', 'pc105', '', '', __pangrams['french'] ],
		'gr'                  : ['Greek', 'us,el', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['port'] ],
		'hu'                  : ['Hungarian', 'hu', 'pc105', '', '', __pangrams['hungarian'] ],
		'hu101'               : ['Hungarian (101 key)', 'hu', 'pc105', '', '', __pangrams['hungarian']],
		'is-latin1'           : ['Icelandic', 'is', 'pc105', '', '', __pangrams['icelandic'] ],
		'it'                  : ['Italian', 'it', 'pc105', '', '', __pangrams['italian'] ],
		'it-ibm'              : ['Italian (IBM)', 'it', 'pc105', '', '', __pangrams['italian'] ],
		'it2'                 : ['Italian (it2)', 'it', 'pc105', '', '', __pangrams['italian'] ],
		'jp106'               : ['Japanese', 'jp', 'jp106', '', '', __pangrams['port'] ],
		'la-latin1'           : ['Latin American', 'la', 'pc105', '', '', __pangrams['esp'] ],
		'mk-utf'              : ['Macedonian', 'mk,us', 'pc105', '','grp:shift_toggle,grp_led:scroll',  __pangrams['port'] ],
		'no'                  : ['Norwegian', 'no', 'pc105', '', '', __pangrams['norwegian'] ],
		'pl'                  : ['Polish', 'pl', 'pc105', '', '', __pangrams['port'] ],
		'pt-latin1'           : ['Portuguese', 'pt', 'pc105', '', '', __pangrams['port']],
		'ro_win'              : ['Romanian', 'ro', 'pc105', '', '', __pangrams['romanian'] ],
		'ru'                  : ['Russian', 'ru,us', 'pc105','', 'grp:shift_toggle,grp_led:scroll', __pangrams['russian'] ],
		'ru-cp1251'           : ['Russian (cp1251)', 'ru,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['russian'] ],
		'ru-ms'               : ['Russian (Microsoft)', 'ru,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll',__pangrams['russian'] ],
		'ru1'                 : ['Russian (ru1)', 'ru,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['russian'] ],
		'ru2'                 : ['Russian (ru2)', 'ru,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['russian'] ],
		'ru_win'              : ['Russian (win)', 'ru,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['russian'] ],
		#'speakup'            : ['Speakup', 'us', 'pc105', '', '', ''],
		#'speakup-lt'         : ['Speakup (laptop)', 'us', 'pc105', '', '', ''],
		'sv-latin1'           : ['Swedish', 'se', 'pc105', '', '', __pangrams['swedish'] ],
		'sg'                  : ['Swiss German', 'de_CH', 'pc105', '', '', __pangrams['german']],
		'sg-latin1'           : ['Swiss German (latin1)', 'de_CH', 'pc105', '', '', __pangrams['german']],
		'sk-qwerty'           : ['Slovakian', 'sk_qwerty', 'pc105', '', '', __pangrams['port'] ],
		'slovene'             : ['Slovenian', 'si', 'pc105', '', '', __pangrams['port'] ],
		'trq'                 : ['Turkish', 'tr', 'pc105', '', '', __pangrams['port'] ],
		'uk'                  : ['United Kingdom', 'gb', 'pc105', '', '', __pangrams['ing'] ],
		'ua'                  : ['Ukrainian', 'ua,us', 'pc105', '', 'grp:shift_toggle,grp_led:scroll', __pangrams['port'] ],
		'us-acentos'          : ['U.S. International', 'us_intl', 'pc105', '', '', __pangrams['ing'] ],
		'us'                  : ['U.S. English', 'us', 'pc105', '', '', __pangrams['ing'] ]
	}

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'CompatDev'."""
		CompatDev.__init__(self, ctrl)
	
	def compat(self, info):
		"""Executa o teste de compatibilidade de teclado como definido na RFQ17.B.
		Para isso, chama a classe 'CompatKeyboardGUI' que irá executar o teste de compatibilidade.
		A partir do resultado retornado pela GUI será configurado o resultado do teste de compatibilidade.

		Parâmetro:
		info_list -- Lista contendo as informações detectadas para o teclado (lista de 'InfoResKeyboard')
		"""
		self._compat_res = []
		
		for i in info:
			if (i.xkbLayout != "Unknown"):
				if (i.xkbModel != "Unknown"):
					model = "%s-%s" % (i.xkbLayout, i.xkbModel)
				else:
					model = i.xkbLayout
			else:
				model = "br"
			
			pangram = QtCore.QString(self.__modelDict[model][5])
			
			wizardRes = self.parent.showCustomDialog(CompatKeyboardGUI, pangram)

			if (wizardRes and wizardRes['code'] == 1):
				if (wizardRes['result']['typed'] == pangram):
					self._compat_res.append((True, u"Seu teclado é compatível com o Librix."))
				else:
					self._compat_res.append((False, u"Seu teclado não é compatível com o Librix ou não está propriamente configurado."))
			else: # Cancelado
				self._compat_res.append((False, u"O teste foi cancelado pelo usuário."))

# Testing...

def main(argv):
	test = CompatKeyboard()
	test.runTest(libs.keyboard.diag_keyboard.DiagKeyboard)

import sys
if __name__ == "__main__":
	main(sys.argv)