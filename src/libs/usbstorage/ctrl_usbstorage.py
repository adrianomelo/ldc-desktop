# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.usbstorage.compat_usbstorage import CompatUsbstorage
from libs.usbstorage.diag_usbstorage import DiagUsbstorage
from libs.usbstorage.gui_usbstorage import GUIUsbstorage

class CtrlUsbstorage(CtrlDev):
    """Estende a classe 'CtrlDev'.
    Classe de controle que chama os testes de identificação, compatibilidade, diagnóstico e cria a tela de exibição.
    """

    def __init__(self, parent):
        """Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
        CtrlDev.__init__(self, parent)

        self._diag = DiagUsbstorage(self)
        self._compat = CompatUsbstorage(self)
        self._guiClass = GUIUsbstorage

    def execute_lib(self):
        """Executa o info, compat e diag (dependendo do resultado do compatibilidade) e cria as telas de exibição."""
        # Information
        self._callInfo()

        # Compatibility
        self._callCompat()

        runDiag = False

        for i in self._compatRes:
            # Compatibility result 1st tuple element is the overall result
            # If any of them failed, runDiag
            runDiag = runDiag | (not i[0])

        # Diagnostic
        if (runDiag):
            self._callDiag()

# Testing...

if __name__ == "__main__":
    from PyQt4 import QtCore, QtGui
    import sys

    app = QtGui.QApplication(sys.argv)

    ctrl = CtrlUsbstorage()

    ctrl.execute_lib()
    ctrl.print_test()
    ctrl.gui_test()

    sys.exit(app.exec_())
