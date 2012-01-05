# -*- coding: utf-8 -*-

import subprocess, shlex

from PyQt4 import QtCore

def exec_command(command):
	"""Funcao para executar uma aplicacao externa. O parametro 'command' e uma string, onde podem ocorrer | (pipes) mas nao aspas (simples ou duplas)
	
	ex.: command = "ls -la | grep -v foobar"
	"""
	
	commands = []

	for comm in command.split("|"):
		commands.append(prepare_command(comm))

	return exec_command_parms(commands)

import errno

def exec_command_parms(commands, stdin = None):
	"""Funcao para executar uma aplicacao externa. O parametro 'commands' e umas lista de listas. Cada elemento dessa lista representa um 
	comando a ser executado. Essa representacao e na forma de uma lista, onde cada elemento dessa lista e um parametro para a execucao da aplicacao
	
	ex.: commands = [ ['ls', '-la'], ['grep', '-v', 'foobar'] ]
	"""
	
	processes = []


	for cmd in commands:
		ps = None

		if (len(processes) == 0):
			input = None
		else:
			input = processes[-1].stdout

		done = False

		while (not done):
			try:
				ps = subprocess.Popen(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				done = True
			except OSError, e:
				if e.errno == errno.EINTR:
					continue
				else:
					raise

		processes.append(ps)

	i = processes[-1].stdin
	o = processes[-1].stdout
	e = processes[-1].stderr

	o_str = None
	e_str = None

	done = False

	while (not done):
		try:
			o_str, e_str = processes[-1].communicate() # stdout, stderr
			done = True
		except OSError, e:
			if e.errno == errno.EINTR:
				continue
			else:
				raise

	return i, o_str, e_str, ps.returncode

def prepare_command(command):
	"""Metodo auxiliar para dividir a string do command, separando a chamada da aplicacao de seus argumentos, criando uma lista"""
	
	tokens = shlex.shlex(command)

	tokens.wordchars += '.'
	tokens.wordchars += '/'
	tokens.wordchars += '\\'
	tokens.wordchars += '-'
	tokens.wordchars += '*'
	tokens.wordchars += '='
	tokens.wordchars += '$'
	tokens.wordchars += '{'
	tokens.wordchars += '}'
	tokens.wordchars += '\''
	tokens.wordchars += '+'

	result = []

	for i in tokens:
		result.append(i)

	return result


class ApplicationExecutor(QtCore.QObject):
	"""Classe para executar aplicacoes externa. Esta classe permite executar a aplicacao numa thread exclusiva, sem bloquear, por exemplo, a GUI."""
	
	def __init__(self):
		QtCore.QObject.__init__(self)

	def executeCommandAndWait(self, flat, stdin, *cmds):
		"""Executa uma aplicacao externa e espera pelo resultado
		
		flat (boolean) - indica se os parametros, em cmds, sao strings, contendo os comandos
		stdin (stream de entrada) - stream que sera utilizada como entrada para a primeira aplicacao
		cmds (strings ou lista) - strings de comando, como descrito em 'exec_command' ou lista de comandos, como em 'exec_command_parms'
		"""
		
		eventLoop = QtCore.QEventLoop()
		appThread = self.__ExternalApplicationThread(stdin, flat, *cmds)
		self.connect(appThread, QtCore.SIGNAL("finished()"), eventLoop.quit)
	
		appThread.start()
		eventLoop.exec_()
	
		return appThread.result

	class __ExternalApplicationThread(QtCore.QThread):
		"""Classe auxiliar para execucao de uma aplicacao como uma thread, herdada de QThread"""
		
		__result = None
		__pipedCmdList = None
		__stdin = None

		def __init__(self, stdin, flat, *varg_cmd):
			"""Prepara o objeto para a execucao da aplicacao externa.
		
			flat (boolean) - indica se os parametros, em cmds, sao strings, contendo os comandos
			stdin (stream de entrada) - stream que sera utilizada como entrada para a primeira aplicacao
			varg_cmd (strings ou lista) - strings de comando, como descrito em 'exec_command' ou lista de comandos, como em 'exec_command_parms'
			"""
			
			QtCore.QThread.__init__(self)
			self.__stdin = stdin

			if (flat):
				self.__pipedCmdList = []

				for arg_cmd in varg_cmd:
					for cmd in arg_cmd.split("|"):
						cmd_list = self.__prepareCommand(cmd)

						self.__pipedCmdList.append(cmd_list)

			else:
				self.__pipedCmdList = list(varg_cmd)

		def getResult(self):
			"""Retorna o resultado da execucao da aplicacao"""
			
			return self.__result

		def getPipedCmdList(self):
			"""Retorna os comandos que serao executados como uma lista de listas"""
			
			return self.__pipedCmdList

		result = property(getResult, None, None, None)
		pipedCmdList = property(getPipedCmdList, None, None, None)

		def run(self):
			"""Executa os comandos definidos na construcao do objeto"""
			
			processes = []

			for cmd in self.__pipedCmdList:
				#print "DEBUG: ", cmd

				ps = None

				if (len(processes) == 0):
					input = self.__stdin
				else:
					input = processes[-1].stdout

				done = False
				while (not done):
					try:
						ps = subprocess.Popen(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
						done = True
					except OSError, e:
						if e.errno == errno.EINTR:
							continue
						else:
							raise

				processes.append(ps)

			outputString = None
			errorString = None
			processReturnCode = None

			done = False
			while (not done):
				try:
					outputString, errorString = processes[-1].communicate() # stdout, stderr
					processReturnCode = processes[-1].returncode

					done = True
				except OSError, e:
					if e.errno == errno.EINTR:
						continue
					else:
						raise

			self.__result = (outputString, errorString, processReturnCode)
			#print "DEBUG: ", self.__result

		def __prepareCommand(self, command):
			"""Metodo auxiliar para dividir a string do command, separando a chamada da aplicacao de seus argumentos, criando uma lista"""
			
			tokens = shlex.shlex(command)

			tokens.wordchars += '.'
			tokens.wordchars += '/'
			tokens.wordchars += '\\'
			tokens.wordchars += '-'
			tokens.wordchars += '*'
			tokens.wordchars += '='
			tokens.wordchars += '$'
			tokens.wordchars += '{'
			tokens.wordchars += '}'
			tokens.wordchars += '\''
			tokens.wordchars += '+'
			tokens.wordchars += '['
			tokens.wordchars += ']'

			result = []

			for i in tokens:
				result.append(i)

			return result