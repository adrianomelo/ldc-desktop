# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import time

class LDC_Executor(QtCore.QThread):
    """
    Classe responsável pelo controle de execução dos plugins.
    Para cada plugin selecionado para execução, importa a classe controladora do plugin, executa os testes e emite sinal para que a interface gráfica adicione os resultados na tela de exibição de resultados.
    As funções dessa classe são executadas em thread independente da interface gráfica.
    """

    def __init__(self, parent, libraries_list):
        """
        Construtor da classe.
        """
        QtCore.QThread.__init__(self)
        self.parent = parent
        self.librariesList = libraries_list
        self.waiting = None

    def importLibraryController(self, library):
        """
        Importa o controlador do plugin/biblioteca definido em library.
        """
        importString = "from libs." + library['folder'] + "." + library['controller'] + " import " + library['ctrl_class'] + ""
        exec importString
        instString = "controller = " + library['ctrl_class'] + "(self)"
        exec instString
        return controller

    def executeLibraries(self, libraries_list):
        """
        Para cada plugin/biblioteca definido em libraries_list, importa o controlador, executa os testes e emite sinal para adicionar o resultado na interface gráfica.
        """
        #print "DEBUG:", libraries_list
        for library in libraries_list:
            #print "DEBUG:", library
            controller = self.importLibraryController(library)
            QtCore.QObject.connect(controller, QtCore.SIGNAL("showMessageBox(QString)"), self.parent.showMessageBox)
            QtCore.QObject.connect(controller, QtCore.SIGNAL("showInputDialog(QString)"), self.parent.showInputDialog)
            QtCore.QObject.connect(controller, QtCore.SIGNAL("showCustomDialog!"), self.parent.showCustomDialog)
            #print "DEBUG:", "start execution"
            controller.execute_lib()

#            try:
            reportRes = controller.getReportInfo(library['name'], library['category'], library['icon'])
#            except:
#                reportRes = None
            #print "DEBUG:", controller.infoRes
            #print "DEBUG:", controller.compatRes
            #print "DEBUG:", controller.diagRes

            category = QtGui.QApplication.translate("LDC_Info", library['category'], None, QtGui.QApplication.UnicodeUTF8)
            if controller.infoRes == []:
                if reportRes == None:
                    self.addResult(library['name'], category, controller.guiClass, library['icon'], {'info': None, 'diag': None, 'compat': None})
                else:
                    self.addResult(library['name'], category, controller.guiClass, library['icon'], {'info': None, 'diag': None, 'compat': None}, reportRes[0])

            for index in range(0, len(controller.infoRes)):
                diag = None
                if (controller.diagRes):
                    diag = controller.diagRes[index]
                if reportRes == None:
                    self.addResult(library['name'], category, controller.guiClass, library['icon'], {'info': controller.infoRes[index], 'diag':diag, 'compat':controller.compatRes[index]})
                else:
                    self.addResult(library['name'], category, controller.guiClass, library['icon'], {'info': controller.infoRes[index], 'diag':diag, 'compat':controller.compatRes[index]}, reportRes[index])

    def waitUser(self):
        """
        Define comportamento de locks e mutexes para aguardar o retorno do usuário.
        Trava o programa a espera de retorno do usuário.
        """
        wait = self.parent.getWait()
        mutex = self.parent.getWaitMutex()
        counter = self.parent.getWaitCounter()

        mutex.lock()
        wait.wait(mutex)
        counter = counter + 1
        mutex.unlock()

    def waitUserFree(self):
        """
        Define comportamento de locks e mutexes para aguardar o retorno do usuário.
        Destrava o programa após retorno do usuário.
        """
        mutex = self.parent.getWaitMutex()
        counter = self.parent.getWaitCounter()

        mutex.lock()
        counter = counter - 1
        mutex.unlock()

    def addResult(self, resultname, resultcategory, guiclass, icon, resultDict, resultReport=None):
        """
        Emite sinal para que a thread de interface gráfica monte o resultado na tela de resultados.
        Repassa nome do teste, categoria, ícone, resultados dos testes, resultados formatados para relatório pdf e classe de interface gráfica a ser montada para exibição.
        """
        self.emit(QtCore.SIGNAL("exec_addResult(PyQt_PyObject)"), [resultname, resultcategory, guiclass, icon, resultDict, resultReport])
        #TODO FIX-UGLY Eliminate this function

    def run(self):
        """
        Reimplementação da classe fundamental de threads, chamada após o comando start() ser disparado na thread pai.
        Chama a função executeLibraries, onde o comportamento da thread é de fato implementado.
        """
        self.executeLibraries(self.librariesList)