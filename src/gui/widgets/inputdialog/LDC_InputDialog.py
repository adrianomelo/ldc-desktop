# -*- coding: utf-8 -*-
from gui.widgets.inputdialog.inputdialog import Ui_LDC_InputDialog
from PyQt4 import QtCore, QtGui

#QDialog::Accepted    1
#QDialog::Rejected    0

class LDC_InputDialog(QtGui.QDialog, Ui_LDC_InputDialog):
    """
    Classe responsável pela exibição padronizada de caixas de diálogo com suporte a entrada de dados do usuário para o LDC.
    """

    def __init__(self, parent):
        """ Construtor da classe. """
        QtGui.QDialog.__init__(self, parent)
        Ui_LDC_InputDialog.__init__(self)
        self.setupUi(self)
        self.ret = None

    def setMessage(self, message):
        """
        Define o parâmetro message como a mensagem a ser exibida na LDC_MessageBox.
        """
        self.message.setText(QtGui.QApplication.translate("LDC_InputDialog", message, None, QtGui.QApplication.UnicodeUTF8))