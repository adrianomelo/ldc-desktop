# -*- coding: utf-8 -*-

def attrproperty(getter_function): 
	"""Função auxiliar utilizada por algumas classes de info_res_lib e diag_res_lib.
	Ela define uma propriedade que acessa mútiplos atributos. Por exemplo, info.name.id"""
	class _Object(object):
		def __init__(self, obj):
			self.obj = obj
		def __getattr__(self, attr):
			return getter_function(self.obj, attr)

	return property(_Object)
